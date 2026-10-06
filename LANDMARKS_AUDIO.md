# THRESHOLD — landmarks and acoustic design

The generator now separates its connected navigation graph from the room geometry. Six shuffled, four-cell landmarks sit within a seeded maze of differently proportioned offices and narrow covered walkways. Landmark interiors open across their internal cell boundaries. Ceilings range from 3.2 to 6.8 metres. Every combat sector contains all six landmarks, with relays distributed among three of them and weapon caches at their anchors.

| Landmark | Architecture and oddities | Acoustics |
| --- | --- | --- |
| The Showroom | Upholstered sofas, desks, chairs and partitions intersecting furniture | Short, damped furnished-room reflections |
| Stillwater Atrium | Tall tiled hall, shallow pools, columns and stairs terminating in a sealed wall | Long, bright tiled decay and local water sounds |
| The Column Hall | Repeating columns, raised false doorway and furniture stranded on a low suspended ceiling | Broad hall reflections |
| Records Without Names | Filing cabinets, shelves and a desk crossing a partition | Absorbent archive response |
| Service Gallery | Overhead pipes, railings, drainage channels and industrial columns | Metallic ambience and long industrial decay |
| The Last Party | Empty tables, paper decorations, repeated chairs and a sofa penetrating the perimeter | Damped room response with ventilation |

The distorted architecture is visual and physical; this version does not warp space or teleport the player between overlapping rooms. Clear central routes and 2.8 m wide by 3 m tall connecting apertures support combat and the largest entity. Hidden loot annexes retain their player-only membrane collision.

The safehouse entrance uses three uneven, matte blue tape strips over continuous wallpaper, based on the supplied reference. There is no emissive portal surface or blue light. Crossing the bounded taped area starts the run; the surrounding wall remains solid.

## Audio implementation

`ABRAudioDirector` owns five Unreal reverb presets: storage (0.38 s decay), furnished rooms (0.88 s), tiled atrium (3.7 s), industrial halls (2.25 s), and narrow passages (1.45 s). The listener's generated room selects the preset, with 1.25 s DSP transitions. Sources use spatialization, distance filtering, reverb sends, and visibility traces that attenuate and low-pass sounds behind walls. This is a designed room-profile system, not geometric acoustic ray tracing or measured impulse responses.

A quiet stereo bed combines with local ventilation, water, or metal emitters. Room emitters crossfade on traversal. Player and audible pursuing entities use surface-dependent footsteps; Smilers remain silent. Weapon transients briefly duck the ambience. Separate concurrency limits constrain weapon/general voices, and a linked master limiter reserves output headroom. Original ElevenLabs files remain unchanged; the preparation script removes DC offset, trims dry foley onset, crossfades loop seams, and reserves source headroom before import.

New ElevenLabs sources: ventilation, pool water, loose industrial metal, carpet/tile/metal footsteps, and a dry rifle shot. Existing ElevenLabs horror and safehouse sources are retained. Prompts and provenance are saved in `SourceAssets/ElevenLabs/manifest.json`.

The arsenal update replaces all player weapon firing/reload/handling cues with 23 dedicated ElevenLabs sources. Player weapon audio has its own full-band direct path, bypassing environmental occlusion and distance filtering, while retaining a manual send into the room reverb. This prevents a nearby wall from muffling the player's own shot. Environmental audio still uses occlusion and air absorption. See `ARSENAL.md` and `SourceAssets/ArsenalAudio/manifest.json`.

Gunfire uses the Core Bodycam Niagara effect, a camera-facing procedural flame core, and a 55 ms warm light pulse, sized by weapon type. The flame follows the actual weapon muzzle during the pulse.

## References and original content

- [A24's Backrooms](https://a24films.com/films/backrooms): furniture-showroom setting; the taped-wall entrance follows the user's supplied film reference.
- [POOLS](https://store.steampowered.com/app/2663530/POOLS/): tiled liminal spaces and room-dependent sound/echo informed the atrium and acoustic contrast.
- [Backrooms: Escape Together](https://store.steampowered.com/app/2141730/Backrooms_Escape_Together/): procedurally generated Backrooms exploration informed the connected landmark structure.

Layouts, beveled furniture meshes, tape geometry and flame material are original project content. No film frames, game levels or game audio were imported. Rebuild furniture with `Tools/create_liminal_furniture.py` in Blender; prepare audio with `Tools/prepare_liminal_audio.py`; import with `Tools/create_liminal_content.py` in Unreal's Python commandlet using `-AllowCommandletAudio` and `-DisablePlugins=Fab`.

`Tools/CaptureLandmarks.ps1` captures all six rooms, a firing frame, and a seven-second rendered audio sample for each. Add `-AudioQA` to isolate the shot and reverb tail; add `-Packaged` to verify the distributed build. Validation results are recorded in `QA_RESULTS.md`.
