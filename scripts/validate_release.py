"""Verify the actual downloadable ZIP and its SMOG contract before publication."""
import fnmatch
import hashlib
import json
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
archive = Path(sys.argv[1])
smog = ["smog_icon.ico", "smog_logo.png", "smog_header.png", "smog_meta.xml", "smog_launch.bat"]
xml_bytes = (ROOT / "smog_meta.xml").read_bytes()
assert b"<!DOCTYPE" not in xml_bytes.upper() and b"<!ENTITY" not in xml_bytes.upper()
xml = ET.fromstring(xml_bytes)
assert xml.tag == "smog"
assert re.fullmatch(r"#?[0-9a-fA-F]{6}", xml.findtext("accent"))
assert fnmatch.fnmatch(archive.name, xml.findtext("release/asset"))
for field in ("title", "description", "developer", "genre", "version"):
    assert xml.findtext(field), field
for name, dimensions in (("smog_header.png", (2400, 1000)), ("smog_logo.png", (1200, 400))):
    with Image.open(ROOT / name) as image:
        image.load()
        assert image.size == dimensions
        if "logo" in name:
            assert image.mode == "RGBA" and image.getextrema()[3][0] == 0
with Image.open(ROOT / "smog_icon.ico") as icon:
    assert {(16, 16), (32, 32), (48, 48), (256, 256)} <= icon.ico.sizes()
for name in smog[:3]:
    assert (ROOT / name).stat().st_size < 8_000_000
with zipfile.ZipFile(archive) as bundle:
    infos = bundle.infolist()
    names = {i.filename for i in infos}
    assert len(names) == len(infos) < 100_000
    assert archive.stat().st_size < 10_000_000_000
    assert sum(i.file_size for i in infos) < 30_000_000_000
    reserved = re.compile(r"^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)", re.I)
    for item in infos:
        path = PurePosixPath(item.filename)
        assert not path.is_absolute() and ".." not in path.parts
        assert ":" not in item.filename and "\\" not in item.filename
        assert not stat.S_ISLNK(item.external_attr >> 16)
        assert all(not reserved.match(p) and p.rstrip(" .") == p for p in path.parts)
        assert "saved" not in [p.lower() for p in path.parts]
        assert path.suffix.lower() not in (".pdb", ".sav", ".log", ".uasset", ".uproject")
    for name in smog:
        assert bundle.read(name) == (ROOT / name).read_bytes(), f"SMOG mismatch: {name}"
    manifest = json.loads(bundle.read("release-manifest.json"))
    assert manifest == json.loads((ROOT / "release-manifest.json").read_text())
    assert names == {f["path"] for f in manifest["files"]} | {"release-manifest.json"}
    for file in manifest["files"]:
        with bundle.open(file["path"]) as stream:
            assert hashlib.file_digest(stream, "sha256").hexdigest() == file["sha256"], file["path"]
        assert bundle.getinfo(file["path"]).file_size == file["bytes"]
    executable = "BackroomsGame/Binaries/Win64/BackroomsGame.exe"
    with bundle.open(executable) as stream:
        header = stream.read(4096)
    assert header[:2] == b"MZ"
    pe_offset = int.from_bytes(header[60:64], "little")
    assert header[pe_offset:pe_offset+6] == b"PE\x00\x00\x64\x86"
    launcher = bundle.read("smog_launch.bat").decode("ascii")
    assert "-UserDir=%THRESHOLD_USER_DIR%" in launcher and "%LOCALAPPDATA%" in launcher
    assert not re.search(r"^\s*start\b", launcher, re.M | re.I)
    for dll in ("msvcp140.dll", "vcruntime140.dll", "vcruntime140_1.dll"):
        assert f"BackroomsGame/Binaries/Win64/{dll}" in names
with archive.open("rb") as stream:
    digest = hashlib.file_digest(stream, "sha256").hexdigest()
assert (ROOT / "SHA256SUMS.txt").read_text().split()[0] == digest
print(json.dumps({"status": "PASS", "files": len(infos), "bytes": archive.stat().st_size,
                  "sha256": digest, "smog_files_identical": 5,
                  "icon_sizes": [16, 32, 48, 64, 128, 256],
                  "header": [2400, 1000], "transparent_logo": [1200, 400]}, indent=2))
