# THRESHOLD

Launch **smog_launch.bat**, or press Play in SMOG. Keep this entire Windows folder together.

You begin in a safehouse. Choose one Common starter with **E** at the armory (also available from the safehouse pause menu). Use **E** at the archive terminal for permanent upgrades, then walk through the **blue tape outline on the wallpaper** to start a run. Activate three relays, collect weapons and upgrades, and choose to descend or extract. Death/extraction awards memories for your next rebirth.

| Input | Action |
| --- | --- |
| WASD / mouse | Move / look |
| Left / right mouse | Fire / aim |
| Shift | Sprint |
| Ctrl / C | Crouch; slide while sprinting |
| Z | Prone |
| Space | Jump / vault / mantle |
| R | Reload |
| Q / wheel | Switch between two carried slots |
| 1 / 2 | Select weapon slot |
| 1 / 2 / 3 in upgrade menu | Choose upgrade |
| E / F | Interact / flashlight |
| X / B, held | Lean left / right |
| G / V | Grenade / melee |
| T | Equipped active ability |
| Tab, held | Map |
| Escape | Pause, sensitivity, reduced motion, body censorship, voice settings |

Some walls conceal loot rooms. Enemies cannot follow through them. Rare Observation Wings replace combat with an anomaly puzzle.

The archive has **96 connected skills and 403 ranks across eight branches**. Select a branch and node to see prerequisites, price and effects. Unlock and equip one of eight active abilities, then press **T** during combat. Refund All Ranks offers a full memory refund after an in-game confirmation. Original perk saves migrate automatically.

The survivor has 110 ElevenLabs recordings selected dynamically for combat, discoveries and objectives. Pause settings control **Off / Restrained / Frequent**, voice volume and subtitles. Speech playback works offline.

Synchronizing all three relays unlocks the **refuge door**. Follow the objective marker, enter the protected room, and use its console with **E** to spend credits, rearm, descend or extract. Enemies cannot follow or damage you inside. Leaving the room resumes danger. Entity deaths now use ragdolls. Menus include animated feedback and ElevenLabs interface sounds; Reduced Motion also simplifies UI animation.

This is a solo Development build. First launch may briefly stutter while driver pipelines compile. Saves retain permanent progression and settings; a running expedition is not saved when the application closes.

See [CREDITS.md](CREDITS.md) for third-party asset attribution. The project uses five animated community entity models and the supplied Core Bodycam FPS System; the arm animation set is shared across weapon archetypes.

Six landmarks are joined by changing rooms and walkways. Listen for room-dependent echoes and footsteps through walls. Each landmark contains a weapon case; three contain your relay objectives. Furniture and architecture are intentionally misplaced.

Weapon cases, enemies and procurement can drop actual guns on the floor. Look at a gun and press **E**. An empty slot fills first; with both full, your equipped gun drops with its exact remaining ammo and rarity. Every fresh run resets to your chosen Common starter.

## Saves and updates

The SMOG launcher writes permanent progression and settings to:

`%LOCALAPPDATA%\ThresholdProtocol\THRESHOLD\Saved\SaveGames\Threshold_Profile_v1.sav`

Logs and engine settings are in the neighboring `Saved` subfolders. SMOG updates and uninstalling game versions do not delete this external profile. Always launch through `smog_launch.bat` (SMOG does this automatically) to use this persistent location.

To bring a profile from an earlier standalone development build, close the game, back up both profiles, and copy your old `Threshold_Profile_v1.sav` from that build's `BackroomsGame\Saved\SaveGames` into the path above. Replace an existing profile only if you intend to use the older progress. No developer profile is shipped in this release.

## Runtime

Windows x64 with DirectX 12 graphics support. Microsoft Visual C++ redistributable runtime DLLs are included beside the executable; no Unreal Editor installation is required. Keep `Engine`, `BackroomsGame` and the five SMOG files together after extraction.