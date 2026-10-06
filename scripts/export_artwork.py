"""Export the three generated originals to the SMOG publishing dimensions.

Requires Pillow. This only resizes/encodes original imagegen outputs; it does
not synthesize, paint, remove backgrounds, or alter the generated artwork.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
for name, size in (("header", (2400, 1000)), ("logo", (1200, 400))):
    with Image.open(ROOT / "artwork" / f"{name}-source.png") as source:
        source.resize(size, Image.Resampling.LANCZOS).save(
            ROOT / f"smog_{name}.png", optimize=True)
with Image.open(ROOT / "artwork/icon-source.png") as source:
    source.save(ROOT / "smog_icon.ico", format="ICO",
                sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
with Image.open(ROOT / "smog_logo.png") as logo:
    assert logo.mode == "RGBA" and logo.getextrema()[3][0] == 0
for name in ("smog_header.png", "smog_logo.png", "smog_icon.ico"):
    assert (ROOT / name).stat().st_size < 8_000_000
    print(f"{name}: {(ROOT / name).stat().st_size:,} bytes")
