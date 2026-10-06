# Distribution validation — 1.0.0

Checked October 6, 2026 against the actual portable ZIP, extracted into a fresh directory.

| Check | Result |
| --- | --- |
| Compiled build integrity | 28 binaries/content containers match the Unreal staged build |
| Latest executable | September 30, 2026 build; newer than all current source, content and configuration changes |
| Packaged gameplay suite | 226 checks passed; process exit 0 |
| SMOG contract | All five files at repository and ZIP root; byte-identical copies |
| Metadata | UTF-8 XML, smog root, supported fields, no DTD/entities, matching release asset pattern |
| Header | 2400 x 1000 PNG; 3,135,482 bytes |
| Logo | 1200 x 400 PNG with actual alpha transparency; 452,176 bytes |
| Icon | ICO with 16, 32, 48, 64, 128 and 256 px images; 143,948 bytes |
| Archive | 64 files; 629,381,128 bytes compressed; every file verified against the SHA-256 manifest |
| Runtime | Windows x64 PE executable, cooked containers, engine support files and 10 app-local Visual C++ CRT DLLs |
| ZIP safety | No symlinks, traversal, alternate data streams or reserved Windows names; within SMOG limits |
| Clean distribution | No test profiles, logs, PDB symbols or editable Unreal assets |
| Launch behavior | Actual BAT executed from an unrelated working directory, with spaces in installation and user-data paths |
| Play-time tracking | BAT remained running until normal engine shutdown |
| Save persistence | Fresh normal launch created a profile outside the installation; a second launch after relocating the installation reused the same file without rewriting it |
| Profile isolation | Verification used a temporary LocalAppData override; the player's real profile was untouched |
| Graphics launch | DirectX 12 offscreen run on RTX 5070 completed normally, with zero Error/Warning log entries; safehouse, debrief and upgrade screens captured |

The public [launch-validation.json](launch-validation.json) records launcher test results. The current [safehouse capture](screenshots/safehouse.png) is an actual game render. Header/logo/icon files are separately generated promotional art; their originals and exact prompts are in [artwork](artwork).

The compiled executable SHA-256 is `ed37e4a5235eb0c73ba69ef85daeba48f7918b8224258dd96908373c433581fc`. The downloadable ZIP's SHA-256 is recorded in [SHA256SUMS.txt](SHA256SUMS.txt); all payload hashes are in [release-manifest.json](release-manifest.json).

These checks cover distribution integrity, functional gameplay, rendering startup and save-location behavior. They are not a performance benchmark, a fresh Windows installation test or an end-to-end SMOG UI test. Audio/voice asset and audible playback checks from the latest game build were retained; the game binaries and cooked content were not changed for this publication.
