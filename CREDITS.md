# THRESHOLD asset credits

Source paths below identify development provenance. Editable source assets and the Unreal project are not included in this distribution. Film/game reference notes are in [LANDMARKS_AUDIO.md](LANDMARKS_AUDIO.md) in the repository.

# Included Epic Games content

`Content/Weapons/Rifle` and `Content/Weapons/GrenadeLauncher` were copied from the installed Unreal Engine 5.7.4 template resources under `Templates/TemplateResources/Standard/Weapons/Content`.

These Epic Games template meshes, skeletons, textures, materials, physics assets, and example audio remain governed by the applicable Unreal Engine license. No ownership or separate permissive license is claimed for them.

The game also references the installed Engine basic shapes and default fonts. The game code, procedural surface definitions, environment layouts, and synthesized files in `SourceAssets/Audio` were created for this project.

## ElevenLabs sound effects

Eight WAV files in `SourceAssets/ElevenLabs`, imported as `/Game/Audio/EL_*`, were generated for this project with the configured ElevenLabs account using `eleven_text_to_sound_v2`. They were requested through the [Sound Effects API](https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert). The manifest records the prompts, durations and file hashes. Usage and distribution remain subject to the generating account's applicable ElevenLabs terms. These files are not described as original procedural synthesis or as independently licensed third-party recordings.

No API key or network dependency is included in the runtime game. Audio generation is an offline development step; playback uses cooked Unreal SoundWave assets.

## Core Bodycam FPS System

The user supplied [Core Bodycam FPS System by Bogdan Pirvulescu](https://www.fab.com/listings/ab6677d3-1d7e-42f8-80ed-50c9aa5d8697). Retained assets remain in `Content/Basic_Bodycam`; the replaced Makarov mesh is archived in `Backups/OriginalWeaponAssets`. Their use remains subject to the license under which the user acquired the pack.

The integrated first-person arms are [First Person arms by DJMaesen / bumstrum](https://sketchfab.com/3d-models/first-person-arms-e3c42c05b22944e5839deb8e003f0987), licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), as credited by the pack author. THRESHOLD adapts the animation Blueprint to its native character and scales animation playback to weapon reload times. The pack author credits Pixabay for included sounds. No ownership of the pack models, animations, effects or sounds is claimed.

## Backrooms entity models and animations

Downloaded through Sketchfab's official free download controls on 28 September 2026.

| Runtime entity | Asset and attribution | Listed license |
| --- | --- | --- |
| Smiler | [Smiler (Backrooms)](https://sketchfab.com/3d-models/smiler-backrooms-ea10d7f4750341f0ada6a12a6530014a), Edward Johnson 3 / sirenhead1929; original model credited to lucaarcadu | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Captain Clark | [Pirate clark](https://sketchfab.com/3d-models/pirate-clark-794037e2316a43c190345d3e5ba5c033), photon (that one larry) / Professor_E12; credits norpa | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| The Lifeform | [Accurate Backrooms Bacteria v2 with Animations](https://sketchfab.com/3d-models/accurate-backrooms-bacteria-v2-with-animations-c067bae794c14fc1969fe22605cdd837), Unschooling with Fin; inspired by Kane Pixels | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Skin Stealer | [The Backrooms - Skin Stealer w/ animations](https://sketchfab.com/3d-models/the-backrooms-skin-stealer-w-animations-68d78f780d67410ead0b62fe6d069b33), jake25916 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Partygoer | [Rigged Partygoer](https://sketchfab.com/3d-models/rigged-partygoer-5dc69f96b93346c595335d5e501ab792), taggedk; [original model linked by uploader](https://skfb.ly/oyUDq) | [Sketchfab Free Standard](https://sketchfab.com/licenses) |

Changes: combined mesh parts, removed viewer helpers, extracted textures, adapted materials and scale, constrained cinematic root motion, generated LODs, and added missing idle, locomotion, attack and death clips. Authored source animations are retained where available. These are independent community assets; attribution does not imply creator endorsement or rights to underlying film/game branding. Partygoer source files must not be redistributed as a standalone asset. The Windows game includes cooked content only.


## Liminal environment and expanded sound design

The four beveled furniture meshes (sofa, chair, desk, cabinet), the landmark generator, tape outline and procedural muzzle-flame material are original project content. Their generation/import scripts and source FBX files are included in the project.

Seven additional sounds were generated through the user's authorized ElevenLabs account: `EL_VentLoop`, `EL_WaterLoop`, `EL_MetalLoop`, `EL_StepCarpet`, `EL_StepTile`, `EL_StepMetal`, and `EL_DryRifle`. Exact prompts and source hashes are retained in `SourceAssets/ElevenLabs/manifest.json`. Runtime copies are DC-corrected, trimmed and crossfaded where appropriate; source recordings remain intact. Room acoustics use Unreal Engine's built-in reverb and Audio Mixer.

Film/game references are documented in [LANDMARKS_AUDIO.md](LANDMARKS_AUDIO.md). No film images, game rooms or game audio are redistributed.

## Selected weapon models (arsenal update)

The six models below were selected and downloaded by the user from Sketchfab. Original GLBs and embedded provenance are retained in `SourceAssets/Arsenal`. Modifications: normalized units and grip origins, gameplay mesh reduction where needed, PBR material conversion, muzzle/sight sockets, and functional rear/front iron sights for rail-only models.

- [Desert Eagle Gun](https://sketchfab.com/3d-models/desert-eagle-gun-1605b6c38826433fb3fe564e1d043199) — attix84work (https://sketchfab.com/attix84work). Embedded asset license: CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/).
- [LMG](https://sketchfab.com/3d-models/lmg-8c24d7374ea64bdab1c30f49c69d5ed8) — DJMaesen (https://sketchfab.com/bumstrum). Embedded asset license: CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/).
- [M4 Carbine Rifle](https://sketchfab.com/3d-models/m4-carbine-rifle-3d028a9e936e4f58a5f10e2339ed7f88) — UmangRank (https://sketchfab.com/UmangRank). Embedded asset license: SKETCHFAB Standard (https://sketchfab.com/licenses).
- [Origin-12 SD Black - COD:MW2019 (PBR)](https://sketchfab.com/3d-models/origin-12-sd-black-codmw2019-pbr-6955618c434a44cfa4168a595e9be4c3) — Wicked_Vixx (https://sketchfab.com/tylukex). Embedded asset license: CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/).
- [AR SLR](https://sketchfab.com/3d-models/ar-slr-bf6a5fb58a484f60b302adecb8bf0aec) — luapqq (https://sketchfab.com/luapqq). Embedded asset license: CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/).
- [Vektor](https://sketchfab.com/3d-models/vektor-e8937e301f2b481b981b6b1b86accb70) — ErhanMatur (https://sketchfab.com/erhanmatur). Embedded asset license: CC-BY-4.0 (http://creativecommons.org/licenses/by/4.0/).

The Origin-12 listing identifies the model as Call of Duty: Modern Warfare (2019) content uploaded by Wicked_Vixx. The attribution above records the source listing and does not expand the rights supplied with the download.

All current weapon firing, reload, equip, aim-in, aim-out, empty-trigger and ground-drop sounds were generated through the configured ElevenLabs account (`eleven_text_to_sound_v2`). Original files, prompts and hashes: `SourceAssets/ArsenalAudio/manifest.json`. The prepared sources retain dry attacks; Unreal supplies the live room reverb.

## Refuge and interface update

Nine additional interface/relay/refuge cues were generated with ElevenLabs `eleven_text_to_sound_v2` through the user's configured account. Prompts, original hashes and runtime processing levels are retained in `SourceAssets/UIAudio/manifest.json`. Refuge geometry, interface animation code and ragdoll configuration are original project work. Entity mesh attribution above also applies to their generated physics assets.

## Player voice and archive update

110 original fictional survivor lines were generated through the user's configured ElevenLabs account using the premade Callum voice (N2lVS1w4EtoT3dr4eOWO) and eleven_v3. This uses a stock provider voice, not a cloned actor or a film recording. Exact text, delivery tags, voice/model and hashes for original/prepared PCM files are retained in SourceAssets/Voice/manifest.json. Playback is local and requires no provider account. The skill catalog, branching interface, ability implementation and contextual dialogue director are original project work.

## Microsoft runtime

App-local x64 Visual C++ runtime DLLs are redistributed from the installed Microsoft Visual Studio 2022 Microsoft.VC143.CRT redistributable directory. Copyright Microsoft Corporation; the runtime retains its Microsoft license. These files are supplied solely to run the compiled game.

## SMOG artwork

The THRESHOLD header, transparent wordmark and blue-tape icon were generated for this release with OpenAI image generation on October 6, 2026. They are promotional artwork rather than gameplay captures. Original outputs and prompts are included in the repository.
