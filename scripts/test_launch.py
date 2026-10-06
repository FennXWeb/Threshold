"""Exercise the packaged BAT, process lifetime, saves and an update relocation.

Requires Windows. Supply the already-validated ZIP and a NEW test directory.
The isolated LocalAppData override leaves the real player's profile untouched.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import zipfile
from pathlib import Path

archive = Path(sys.argv[1]).resolve()
test_root = Path(sys.argv[2]).resolve()
test_root.mkdir(parents=True, exist_ok=False)
install = test_root / "SMOG Install Version 1"
with zipfile.ZipFile(archive) as bundle:
    bundle.extractall(install)
local_data = test_root / "Local AppData"
local_data.mkdir()
environment = dict(os.environ, LOCALAPPDATA=str(local_data))
profile = local_data / "ThresholdProtocol/THRESHOLD/Saved/SaveGames/Threshold_Profile_v1.sav"
binary_name = "BackroomsGame.exe"

def run_bat(folder, arguments, name):
    log = test_root / f"{name}.log"
    command = f'"{os.environ["COMSPEC"]}" /d /s /c ""{folder / "smog_launch.bat"}" {arguments} -unattended -nosplash "-abslog={log}""'
    started = time.monotonic()
    with (test_root / f"{name}-console.txt").open("w", encoding="utf-8") as output:
        process = subprocess.Popen(command, cwd=test_root, env=environment,
                                   stdout=output, stderr=subprocess.STDOUT,
                                   creationflags=subprocess.CREATE_NO_WINDOW)
        exit_code = process.wait(timeout=240)
    assert exit_code == 0, f"{name}: launcher failed with {exit_code}; see {log}"
    text = log.read_text(encoding="utf-8", errors="replace")
    assert "LogExit: Exiting." in text, f"{name}: BAT returned before normal engine shutdown"
    assert not re.search(r"Fatal error:|Unhandled Exception:|Assertion failed:", text)
    assert not list(folder.rglob("*.sav")), "Save was written into versioned install"
    return {"exit_code": exit_code, "seconds": round(time.monotonic()-started, 2)}, text

smoke, smoke_text = run_bat(install, "-BRSmoke -BRSeed=74104 -nullrhi -nosound", "smoke")
assert "BR_SMOKE PASS" in smoke_text
smoke["pass_lines"] = len(re.findall(r"BR_CHECK PASS", smoke_text))
assert smoke["pass_lines"] == 226, smoke
assert not profile.exists(), "Smoke mode leaked a real save"
first, _ = run_bat(install, '-nullrhi -nosound -ExecCmds="quit"', "first-launch")
assert profile.exists(), "Normal launch did not create an external profile"
before = hashlib.sha256(profile.read_bytes()).hexdigest()
mtime = profile.stat().st_mtime_ns
relocated = test_root / "SMOG Install Version 2"
install.rename(relocated)
second, _ = run_bat(relocated, '-nullrhi -nosound -ExecCmds="quit"', "after-update")
assert profile.exists() and hashlib.sha256(profile.read_bytes()).hexdigest() == before
assert profile.stat().st_mtime_ns == mtime, "Profile was regenerated rather than loaded"
report = {"status": "PASS", "smoke": smoke, "first_launch": first,
          "after_update": second, "external_profile_created": True,
          "profile_reused_after_install_relocation": True,
          "install_path_with_spaces": True, "unrelated_working_directory": True,
          "batch_waited_for_engine_shutdown": True,
          "real_user_profile_accessed": False}
(test_root / "launch-report.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps(report, indent=2))
