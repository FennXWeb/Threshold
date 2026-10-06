"""Package an existing cooked Unreal Windows build for SMOG.

Usage: python scripts/package_release.py --build PATH --crt PATH --output PATH
PATH for --crt is the installed x64/Microsoft.VC143.CRT redistributable folder.
The output directory must be new: existing artifacts are never removed.
"""
import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SMOG = ["smog_icon.ico", "smog_logo.png", "smog_header.png", "smog_meta.xml", "smog_launch.bat"]
DOCS = ["PLAY.md", "CREDITS.md", "CHANGELOG.md", "LANDMARKS_AUDIO.md"]

def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", type=Path, required=True)
    parser.add_argument("--crt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    version = ET.parse(ROOT / "smog_meta.xml").getroot().findtext("version")
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    stage = out / "Windows"
    stage.mkdir()
    copied = 0
    for source in sorted(args.build.rglob("*")):
        relative = source.relative_to(args.build)
        if source.is_symlink():
            raise ValueError(f"Symlink in build: {relative}")
        if not source.is_file() or "Saved" in relative.parts or source.suffix.lower() == ".pdb":
            continue
        if len(relative.parts) == 1 and source.name != "BackroomsGame.exe":
            continue
        destination = stage / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied += 1
    assert copied >= 28, "Compiled runtime incomplete"
    crt_files = list(args.crt.glob("*.dll"))
    assert {"msvcp140.dll", "vcruntime140.dll", "vcruntime140_1.dll"} <= {p.name.lower() for p in crt_files}
    for source in crt_files:
        shutil.copy2(source, stage / "BackroomsGame/Binaries/Win64" / source.name)
    for name in SMOG + DOCS:
        shutil.copy2(ROOT / name, stage / name)
    shutil.copy2(ROOT / "PLAY.md", stage / "README.md")
    files = []
    for path in sorted(stage.rglob("*")):
        if path.is_file():
            files.append({"path": path.relative_to(stage).as_posix(),
                          "bytes": path.stat().st_size, "sha256": sha256(path)})
    manifest = {
        "title": "THRESHOLD", "version": version,
        "release_tag": f"v{version}", "platform": "windows-x64",
        "engine": "Unreal Engine 5.7.4", "configuration": "Development",
        "game_compiled_date": "2026-09-30", "distribution_date": "2026-10-06",
        "asset": f"threshold-{version}-windows-x64.zip",
        "save_directory": "%LOCALAPPDATA%/ThresholdProtocol/THRESHOLD/Saved/SaveGames",
        "uncompressed_payload_bytes": sum(f["bytes"] for f in files),
        "manifest_scope": "All archive files except release-manifest.json itself",
        "files": files,
    }
    manifest_text = json.dumps(manifest, indent=2) + "\n"
    (stage / "release-manifest.json").write_text(manifest_text, encoding="utf-8")
    (ROOT / "release-manifest.json").write_text(manifest_text, encoding="utf-8")
    archive = out / manifest["asset"]
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as bundle:
        for path in sorted(stage.rglob("*")):
            if path.is_file():
                bundle.write(path, path.relative_to(stage).as_posix())
    checksum = f"{sha256(archive)}  {archive.name}\n"
    (out / "SHA256SUMS.txt").write_text(checksum, encoding="ascii")
    (ROOT / "SHA256SUMS.txt").write_text(checksum, encoding="ascii")
    print(json.dumps({"archive": str(archive), "bytes": archive.stat().st_size,
                      "sha256": checksum.split()[0], "runtime_files_copied": copied,
                      "app_local_crt_files": len(crt_files)}, indent=2))

if __name__ == "__main__":
    main()
