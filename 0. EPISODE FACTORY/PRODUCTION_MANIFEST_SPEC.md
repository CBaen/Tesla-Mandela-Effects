# Production Manifest Spec — For the Script Writer

**From:** The pipeline engineer (Claude Code, Wardenclyffe Unified)
**To:** The script writer (Claude, Episode Factory)
**Purpose:** You and I collaborate on the same episodes but never share a context window. This document is our contract.

---

## What This Is

You write the scripts. I turn them into hundreds of images. Between us, there's a gap: you know everything about every character, location, and piece of technology in the episode — who they are, what era they're in, what they look like. But when you hand me the script, all I receive is prose. I then have to pay a cheaper model (DeepSeek) to guess all the things you already knew. It guesses wrong. A lot.

**The fix:** Alongside each script, you output a **production manifest** — a JSON file containing every visual asset the episode needs. I import it directly. No guessing. No extraction. Your knowledge flows straight into the image pipeline.

---

## What I Need From You

For each episode, output a file named `{episodeNumber}-MANIFEST.json` (e.g., `001-MANIFEST.json`) in the same folder as the script. The format:

```json
{
  "episode": "001",
  "title": "Arriving From Between",
  "assets": [
    // ... array of asset objects (see below)
  ]
}
```

---

## Asset Types

There are three types: **characters**, **locations**, and **objects** (technology/props).

### Characters

```json
{
  "name": "Nikola_Tesla_1943",
  "type": "character",
  "era": "1943",
  "isHistorical": true,
  "fluxKnows": true,
  "birthYear": 1856,
  "physique": "",
  "attire": "",
  "notes": "Elderly, alone, feeding pigeons. Final years in Hotel New Yorker.",
  "parentName": null,
  "children": []
}
```

**The `fluxKnows` field is the most important decision you make per asset.**

FLUX (the image generator) was trained on millions of images. For famous people, it already knows what they look like. For obscure people, it has no idea.

| Person | `fluxKnows` | Why | `physique` needed? |
|--------|-------------|-----|-------------------|
| Nikola Tesla | `true` | Thousands of photos in training data | No — just name + year |
| Thomas Edison | `true` | Famous, well-photographed | No |
| Duka Tesla (mother) | `false` | No photographs exist in FLUX's training | YES — full description |
| Marta (midwife) | `false` | Fictional/obscure village figure | YES — full description |
| Father Toma | `false` | Obscure Serbian priest | YES — full description |
| P.E. Foxworth | `false` | Obscure FBI agent | YES — full description |
| John G. Trump | `false` | Not visually famous | YES — full description |
| Sava Kosanovic | `false` | Obscure diplomat | YES — full description |

**When `fluxKnows` is false, you MUST fill `physique`.** Format: "gender, ethnicity, age range, build, distinctive features." Example:

```
"physique": "Serbian woman, early 30s, strong build, dark hair pulled back tightly, weathered hands, intense dark eyes, high cheekbones"
```

**When `fluxKnows` is true, leave `physique` empty.** The pipeline will send just the name and year, and FLUX will render the person from its training data. Adding a description when FLUX already knows the person wastes precious prompt space.

**`attire` is the DEFAULT costume.** Not scene-specific. Think of it as what the character wears most of the time. Scene-specific wardrobe (Tesla in a lab coat vs. Tesla in a suit at a gala) is handled by the scene prompts, not the manifest.

**`birthYear` matters for age gating.** If a character appears as a child or infant (age < 15), the pipeline needs to know their birth year to suppress the famous-name shortcut. FLUX can render adult Tesla from training data, but it has NO reference for infant Tesla — it needs a physical description instead.

**Same person, different eras = different assets.** Tesla in 1943 (elderly, dying) and Tesla in 1884 (young, arriving in New York) are TWO separate assets:

```json
{"name": "Nikola_Tesla_1943", "era": "1943", "fluxKnows": true, ...},
{"name": "Nikola_Tesla_1884", "era": "1884", "fluxKnows": true, ...}
```

The pipeline uses the era to match the right version to the right scene.

---

### Locations

Locations are **hierarchical**. A building is a parent. Its rooms, floors, and exterior views are children.

```json
{
  "name": "Hotel_New_Yorker_1943",
  "type": "location",
  "era": "1943",
  "isHistorical": true,
  "fluxKnows": true,
  "physique": "",
  "attire": "",
  "notes": "Art deco hotel, 43 stories, 34th and 8th Avenue, Manhattan",
  "parentName": null,
  "children": [
    {
      "name": "Room_3327_1943",
      "era": "1943",
      "physique": "Corner room on 33rd floor. Two walls of curtained windows facing south toward Bryant Park. Cramped. Dark wood desk positioned by south window. Single bed against north wall, sheets pulled tight. Steamer trunks and filing boxes stacked floor to ceiling against far wall. Steam radiator beneath window. Art deco brass hardware. Bare lightbulb overhead.",
      "notes": "Tesla lived here for a decade. Room number divisible by 3. Pigeons visited the windowsill daily."
    },
    {
      "name": "Hotel_Lobby_1943",
      "era": "1943",
      "physique": "Grand art deco lobby. Marble floors with geometric inlays. Brass elevator doors with sunburst pattern. High ceilings with ornamental molding. Crystal chandeliers. Revolving door entrance onto 8th Avenue.",
      "notes": ""
    },
    {
      "name": "Hotel_Exterior_1943",
      "era": "1943",
      "physique": "43-story art deco tower at the corner of 34th Street and 8th Avenue. Brick and limestone facade. Vertical lines emphasizing height. 'Hotel New Yorker' signage at the crown. Street-level awnings. January snow on the sidewalks.",
      "notes": ""
    },
    {
      "name": "Hotel_Corridor_33rd_Floor_1943",
      "era": "1943",
      "physique": "Long narrow hallway. Repeating pattern of dark wood doors. Geometric carpet in muted burgundy and gold. Flat institutional lighting. Brass room numbers on each door.",
      "notes": "The corridor Tesla walked to reach Bryant Park elevators."
    }
  ]
}
```

**Why hierarchies matter:** The image generator cannot render "Hotel New Yorker" as a useful scene — it's too vague. But it CAN render "Room 3327" (cramped desk with trunks) or "Hotel Exterior" (43-story tower in snow). The parent exists for organizational grouping. The children are what actually become images.

**Every distinct visual setting needs its own child.** If the script describes three different rooms in the same building, that's three children. If it describes the same room at two different time periods, that's two children with different eras.

**`fluxKnows` for locations:** Famous buildings (Hotel New Yorker, Wardenclyffe Tower, Niagara Falls power plant) — `true`. FLUX knows what they look like. Village farmhouses, generic hotel rooms, fictional labs — `false`, needs `physique`.

---

### Objects (Technology / Props)

This is where your expertise matters most. FLUX does NOT know what Tesla's inventions look like. The script describes them in narrative terms ("the rotating magnetic field"). The image generator needs VISUAL terms.

```json
{
  "name": "Rotating_Magnetic_Field_Apparatus_1882",
  "type": "object",
  "era": "1882",
  "isHistorical": true,
  "fluxKnows": false,
  "physique": "A tabletop device with a heavy iron core at center. Four copper wire coils wound symmetrically around the core, each connected by thick cloth-insulated leads to a brass commutator switch. The rotor is a polished iron cylinder on precision brass bearings. A hand-crank on the right side. Mounted on a wooden base with felt feet. When energized, the invisible magnetic field rotates — the copper coils glow faintly with induced current.",
  "attire": "",
  "notes": "Tesla's most important invention. First demonstration of alternating current. Basis of all modern AC motors and generators.",
  "parentName": null,
  "children": []
}
```

**Think of `physique` for objects as a verbal blueprint.** Describe:
- Materials (iron, copper, brass, glass, wood, leather)
- Shape and dimensions (tabletop, room-sized, handheld)
- Components and how they connect (coils wound around core, leads to switch)
- Distinctive visual features (glass vacuum tubes, glowing elements, brass fittings)
- Era-appropriate construction (hand-wound wire, not machine-perfect)

**Objects that FLUX might know:** If it's a common historical object (a telegraph machine, a typewriter, a microscope), `fluxKnows` can be `true`. If it's Tesla-specific or obscure, it's `false`.

**The seized trunks** deserve their own asset:

```json
{
  "name": "Tesla_Seized_Trunks_1943",
  "type": "object",
  "era": "1943",
  "isHistorical": true,
  "fluxKnows": false,
  "physique": "Approximately eighty steamer trunks, filing boxes, and wire-bound wooden crates. Mixed sizes from small document boxes to large steamer trunks with leather straps and brass clasps. Labels in mixed English and Serbian handwriting, dates spanning decades. Some wrapped in wire. Arranged not randomly but as an organized archive — nearest the desk hold recent work, far wall holds the oldest notebooks from the 1890s.",
  "attire": "",
  "notes": "Seized by the Office of Alien Property within 2 days of Tesla's death. Contents include notebooks, technical drawings, correspondence, and devices. The complete archive of six decades of work.",
  "parentName": null,
  "children": []
}
```

---

## The Name_Year Format

Every asset name MUST follow `Name_Year` format with underscores:

| Correct | Wrong | Why wrong |
|---------|-------|-----------|
| `Nikola_Tesla_1943` | `Nikola Tesla 1943` | Spaces break matching |
| `Nikola_Tesla_1943` | `Nikola_Tesla` | Missing year breaks era matching |
| `Nikola_Tesla_1943` | `Tesla_1943` | First name needed for word-boundary matching |
| `Room_3327_1943` | `Room 3327` | Spaces + missing year |
| `Rotating_Magnetic_Field_Apparatus_1882` | `rotating_magnetic_field` | Missing year, lowercase |

The year is the year the asset is **depicted**, not when it was created or when the person was born. Tesla's death scene asset is `_1943` even though Tesla was born in 1856.

---

## What NOT to Include

- **Scene-specific details.** The manifest describes WHAT EXISTS, not what happens in any particular scene. Scene composition is handled by the image pipeline.
- **Emotional or narrative context.** "Tesla felt alone" doesn't help image generation. "Elderly man, gaunt, sunken eyes, white hair" does.
- **Audio/script text.** The manifest is metadata about visual assets, not narration.
- **Costume changes per scene.** Default attire in the manifest; scene-specific wardrobe in the scene prompts.

---

## Complete Episode 001 Example

Here's what the manifest for "Arriving From Between" should look like. Use this as your template:

```json
{
  "episode": "001",
  "title": "Arriving From Between",
  "assets": [
    {
      "name": "Nikola_Tesla_1943",
      "type": "character",
      "era": "1943",
      "isHistorical": true,
      "fluxKnows": true,
      "birthYear": 1856,
      "physique": "",
      "attire": "",
      "notes": "Age 86. Final day. Found dead in Room 3327.",
      "parentName": null,
      "children": []
    },
    {
      "name": "Nikola_Tesla_1856",
      "type": "character",
      "era": "1856",
      "isHistorical": true,
      "fluxKnows": false,
      "birthYear": 1856,
      "physique": "Newborn infant, dark hair, pale skin",
      "attire": "Swaddled in white linen",
      "notes": "Birth scene. FLUX cannot render infant Tesla from training data — needs description.",
      "parentName": null,
      "children": []
    },
    {
      "name": "Duka_Tesla_1856",
      "type": "character",
      "era": "1856",
      "isHistorical": true,
      "fluxKnows": false,
      "birthYear": 1822,
      "physique": "Serbian woman, mid-30s, strong peasant build, dark hair pulled back tightly, weathered hands, intense dark eyes, high cheekbones, broad shoulders from farm work",
      "attire": "Simple white linen dress for childbirth, wool blanket over shoulders",
      "notes": "Tesla's mother. Invented household tools. Known for exceptional memory — could recite Serbian epic poetry from memory.",
      "parentName": null,
      "children": []
    },
    {
      "name": "Milutin_Tesla_1856",
      "type": "character",
      "era": "1856",
      "isHistorical": true,
      "fluxKnows": false,
      "birthYear": 1819,
      "physique": "Serbian Orthodox priest, late 30s, tall, lean build, full dark beard, deep-set eyes, high forehead. Scholarly bearing.",
      "attire": "Black Orthodox clerical robe with silver cross pendant, black kamilavka cap",
      "notes": "Tesla's father. Parish priest of Smiljan. Kept the baptismal register.",
      "parentName": null,
      "children": []
    },
    {
      "name": "Marta_Midwife_1856",
      "type": "character",
      "era": "1856",
      "isHistorical": false,
      "fluxKnows": false,
      "birthYear": 1820,
      "physique": "Croatian village woman, mid-30s, sturdy build, calloused hands, kind weathered face, grey-streaked dark hair under a white kerchief",
      "attire": "Simple brown wool dress, white apron, leather shoes",
      "notes": "Village midwife of Smiljan for 20 years. Delivered most children in the parish. Left Smiljan 4 years after Tesla's birth, moved to Zagreb, never returned.",
      "parentName": null,
      "children": []
    },
    {
      "name": "Father_Toma_1856",
      "type": "character",
      "era": "1856",
      "isHistorical": false,
      "fluxKnows": false,
      "birthYear": 1815,
      "physique": "Serbian Orthodox priest, early 40s, stocky build, close-cropped grey beard, steady hands (contradicting his later claim of palsy), penetrating grey eyes",
      "attire": "Black Orthodox vestments with embroidered gold trim for baptismal ceremony, tall black kamilavka",
      "notes": "Baptized Tesla. Wrote 'Quod transit debet cito nominari' in the margin of his transfer petition. Took a vow of silence for 35 years until death.",
      "parentName": null,
      "children": []
    },
    {
      "name": "PE_Foxworth_1943",
      "type": "character",
      "era": "1943",
      "isHistorical": true,
      "fluxKnows": false,
      "birthYear": 1906,
      "physique": "American man, late 30s, clean-shaven, sharp jaw, close-cropped dark hair, military bearing despite civilian suit, alert eyes",
      "attire": "Dark grey wool suit, white shirt, narrow tie, fedora, leather briefcase",
      "notes": "Assistant director of FBI's New York field office. Coordinated the seizure of Tesla's papers. Did not receive the call that morning — was already prepared.",
      "parentName": null,
      "children": []
    },
    {
      "name": "John_G_Trump_1943",
      "type": "character",
      "era": "1943",
      "isHistorical": true,
      "fluxKnows": false,
      "birthYear": 1907,
      "physique": "American man, mid-30s, round face, receding hairline, wire-rimmed glasses, academic appearance, mild expression",
      "attire": "Tweed suit jacket, bow tie, white shirt",
      "notes": "MIT professor. Reviewed Tesla's papers and declared them 'speculative, philosophical, and somewhat promotional.' His report closed the case.",
      "parentName": null,
      "children": []
    },
    {
      "name": "Sava_Kosanovic_1943",
      "type": "character",
      "era": "1943",
      "isHistorical": true,
      "fluxKnows": false,
      "birthYear": 1894,
      "physique": "Yugoslav man, late 40s, dignified bearing, dark hair with grey at temples, thin mustache, diplomatic posture",
      "attire": "Dark formal suit, overcoat, leather gloves",
      "notes": "Tesla's nephew. Yugoslav diplomat stationed in New York. First family member to arrive after Tesla's death. Reported items missing from the room.",
      "parentName": null,
      "children": []
    },
    {
      "name": "Hotel_New_Yorker_1943",
      "type": "location",
      "era": "1943",
      "isHistorical": true,
      "fluxKnows": true,
      "physique": "",
      "attire": "",
      "notes": "Art deco hotel, 43 stories, 34th and 8th Avenue, Manhattan. Tesla's home for his final decade.",
      "parentName": null,
      "children": [
        {
          "name": "Room_3327_1943",
          "era": "1943",
          "physique": "Corner room on 33rd floor. Two walls of curtained windows facing south toward Bryant Park. Cramped, barely large enough for the life compressed into it. Dark wood desk positioned near the south-facing glass. Single bed against the north wall, sheets pulled tight with military precision. Steamer trunks, filing boxes, and wire-bound crates stacked floor to ceiling against the far wall, labeled in mixed English and Serbian. Steam radiator beneath the south window, ticking unevenly. Dried white pigeon droppings and scattered feathers on the windowsill. A stack of hotel napkins on the desk covered in mathematical notation. Bakelite desk lamp. 1940s rotary telephone.",
          "notes": "Tesla's room for a decade. Room number divisible by 3 (his requirement). The room is a compressed timeline — six decades of inquiry."
        },
        {
          "name": "Hotel_New_Yorker_Exterior_1943",
          "era": "1943",
          "physique": "43-story art deco tower at the corner of 34th Street and 8th Avenue. Brick and limestone facade with vertical emphasis. 'Hotel New Yorker' signage. January snow on sidewalks. Yellow taxi cabs on 8th Avenue. Pedestrians in winter coats and hats.",
          "notes": ""
        },
        {
          "name": "Hotel_Corridor_33rd_Floor_1943",
          "era": "1943",
          "physique": "Long narrow hallway with repeating dark wood doors. Geometric carpet pattern in muted burgundy and gold. Flat institutional lighting from wall sconces. Brass room numbers on each door. Quiet. Still.",
          "notes": ""
        }
      ]
    },
    {
      "name": "Smiljan_Village_1856",
      "type": "location",
      "era": "1856",
      "isHistorical": true,
      "fluxKnows": false,
      "physique": "",
      "attire": "",
      "notes": "Village in the Military Frontier of the Austrian Empire (modern-day Croatia). Population under 400. Limestone valley between mountains, single road.",
      "parentName": null,
      "children": [
        {
          "name": "Tesla_House_Smiljan_1856",
          "era": "1856",
          "physique": "Simple stone farmhouse with whitewashed walls and a dark timber roof. Small windows with wooden shutters. A yard behind the house with bare earth. An oil lamp visible through the window. Chimney with nesting swifts. Summer night — warm air, limestone dust, wild thyme scent.",
          "notes": "The birthing room is inside. Adjacent to the parish church where Milutin Tesla served as priest."
        },
        {
          "name": "Tesla_Birthing_Room_1856",
          "era": "1856",
          "physique": "Small interior room lit by a single oil lamp. Rough stone walls, low timber ceiling. A bed with linen sheets. A washing basin on a wooden stand beside the bed, water trembling in concentric rings. The air feels dense — pressure in the ears, hair on arms standing up.",
          "notes": "Where Tesla was born at the stroke of midnight during a thunderstorm (or not — the weather records are ambiguous)."
        },
        {
          "name": "Smiljan_Parish_Church_1856",
          "era": "1856",
          "physique": "Small Serbian Orthodox church. Stone construction with a modest bell tower. Whitewashed interior with Orthodox iconography. Wooden pews. Baptismal register on a lectern near the altar. Beeswax candle scent.",
          "notes": "Where Father Toma baptized Tesla. The baptismal register still holds his signature."
        }
      ]
    },
    {
      "name": "Manhattan_Storage_Warehouse_1943",
      "type": "location",
      "era": "1943",
      "isHistorical": true,
      "fluxKnows": false,
      "physique": "",
      "attire": "",
      "notes": "West side of Manhattan. Where Tesla's trunks were transferred after seizure.",
      "parentName": null,
      "children": [
        {
          "name": "Manhattan_Storage_Interior_1943",
          "era": "1943",
          "physique": "Dark industrial warehouse space. Concrete floors, steel shelving. Rows of stacked trunks and crates under bare fluorescent lights. Climate-indifferent darkness. Labels in Tesla's handwriting softening in the humidity.",
          "notes": "The trunks sat here for years before being shipped to Belgrade."
        }
      ]
    },
    {
      "name": "Tesla_Seized_Trunks_1943",
      "type": "object",
      "era": "1943",
      "isHistorical": true,
      "fluxKnows": false,
      "physique": "Approximately eighty containers: worn leather steamer trunks with brass clasps, reinforced wooden crates bound with wire, cardboard filing boxes. Mixed sizes. Labels in mixed English and Serbian handwriting in a personal shorthand. Dates spanning decades on the labels. The arrangement is not random — it is an archive organized by a mind that remembered the location of every document in every container.",
      "attire": "",
      "notes": "Seized by the Office of Alien Property. Approximately 80 trunks catalogued and removed. The accumulated output of six decades of work.",
      "parentName": null,
      "children": []
    },
    {
      "name": "Tesla_Hotel_Napkin_Equations_1943",
      "type": "object",
      "era": "1943",
      "isHistorical": true,
      "fluxKnows": false,
      "physique": "Stack of white hotel napkins, each covered in dense, precise mathematical notation and circuit diagrams drawn in pencil. Wave frequency calculations, resonant circuit schematics, electromagnetic field equations. The handwriting is controlled, confident — the hand of an engineer who spent six decades training himself to think in equations. Some napkins are stacked neatly; others are scattered across the desk surface with pencil stubs between them.",
      "attire": "",
      "notes": "Tesla could not afford proper stationery. The napkins were his notebooks. The work on them showed no sign of mental deterioration.",
      "parentName": null,
      "children": []
    },
    {
      "name": "Office_Of_Alien_Property_Crates_1943",
      "type": "object",
      "era": "1943",
      "isHistorical": true,
      "fluxKnows": false,
      "physique": "New wooden shipping crates with raw, unfinished pine slats. Splintery. Stamped with official government markings: 'OFFICE OF ALIEN PROPERTY' in black ink. Serial numbers. Pre-labeled, pre-fitted for transport — as if the dimensions of what they intended to take had been measured before Tesla's body was cold.",
      "attire": "",
      "notes": "The agents arrived with these crates already prepared. Empty, already labeled, already fitted for transport.",
      "parentName": null,
      "children": []
    }
  ]
}
```

---

## How to Produce This

When you finish writing an episode script, generate the manifest as a separate output. Think of it as your casting sheet + location scout + prop department combined.

For each asset, ask yourself:
1. Does the image generator know what this looks like from its name alone? (`fluxKnows`)
2. If not, what does it LOOK like? Not what it MEANS — what it looks like. Materials, colors, shapes, textures.
3. Where does this appear in the timeline? (era)
4. Is this a container for sub-locations? (parent with children)

Output the manifest as valid JSON. The pipeline engineer will handle everything else.

---

## Questions?

If something in this spec is unclear, write your question in the manifest file as a comment field: `"_question": "Is Wardenclyffe Tower fluxKnows=true?"` and the pipeline engineer will answer it on the next pass.
