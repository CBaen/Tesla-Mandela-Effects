# Location & Prop Design Guide — For the Script Writer

**From:** The pipeline engineer (Claude Code, Wardenclyffe Unified)
**To:** The script writer (Claude, Episode Factory)
**Date:** 2026-03-20
**Re:** Locations are characters now. Here's how to design them.

---

## The Big Change

We can now generate images where a character stands in a specific location with specific props — and everything looks consistent across the entire episode. The Hotel New Yorker front desk looks like the SAME front desk in every scene. Edwin Park looks like the SAME Edwin Park. This works because we send up to 7 reference images to the image generator simultaneously.

**This means locations matter more than ever.** A well-designed location that appears in 15 scenes carries 15 scenes of visual consistency. A character who appears in 3 scenes carries 3. Locations are the backbone.

---

## The Three Categories

### 1. LOCATION (a place with its set dressing built in)

Everything fixed in the room is part of the location's physique description. The trunks against the wall, the desk by the window, the napkins, the radiator — these are SET DRESSING. They appear in the location's reference image. They do not get their own asset entries.

**The physique description IS the set design.** Describe it like a set designer would: what's on every surface, where the light comes from, what's on the walls, what's on the floor. The more specific, the more consistent every scene in this location will be.

**Physique can be as long as you need** — it's used to generate ONE reference image. It doesn't go directly into scene prompts.

Example:
```json
{
  "name": "Room_3327_1943",
  "type": "location",
  "physique": "Corner room on the 33rd floor. Two walls of curtained windows, south-facing toward Bryant Park. Dark wood desk at the south window with a small stack of hotel napkins covered in pencil equations and two pencil stubs. Single iron bed against the north wall, sheets with military precision. Sixty steamer trunks, wooden crates, and filing boxes stacked floor to ceiling against the far wall, labeled in mixed English and Serbian. Steam radiator beneath south window. Art deco brass hardware. Bakelite desk lamp. Rotary telephone on nightstand. Dried pigeon droppings and three grey feathers on the south windowsill."
}
```

All of those objects (napkins, trunks, telephone, lamp, feathers) are SET DRESSING. They live in this room. They are not separate props.

### 2. PROP (an object that MOVES between locations)

A prop gets its own asset entry ONLY when it appears OUTSIDE its home location. If the trunks never leave Room 3327, they're set dressing. If the trunks are loaded into a government vehicle on the street, NOW they need their own reference image.

**The test:** Does this object appear in a scene where its home location is NOT the setting? If yes → prop. If no → set dressing.

Examples of PROPS:
- `Tesla_Trunks_And_Archive_1943` — only needed for scenes of trunks being carried down the corridor, loaded into vehicle, or sitting in a government warehouse
- `Hotel_Napkin_Behind_Radiator_1943` — only needed for the close-up evidence examination scene (the napkin isolated from its room)
- `Office_Of_Alien_Property_Crates_1943` — these arrive from outside the hotel, so they need their own reference

Examples of SET DRESSING (not props):
- The clock on the front desk wall → part of `Hotel_Front_Desk_1943`
- The carpet pattern in the corridor → part of `Hotel_Corridor_33rd_Floor_1943`
- The brass key hooks → part of `Hotel_Front_Desk_1943`
- Tesla's desk lamp → part of `Room_3327_1943`

### 3. SET DETAIL (mentioned in physique but not visually critical)

Objects that add atmosphere but don't need to be recognizable across scenes. These are described in the physique but the image generator won't necessarily render them precisely. Things like "period-appropriate wall sconces" or "marble floors."

---

## Designing Locations as Characters

Each major location should be designed like a character — with a consistent visual identity, recognizable features, and emotional purpose.

**Ask yourself for each location:**
1. What does this room FEEL like? (Cramped and desperate? Grand and institutional? Cold and forensic?)
2. What are the 3-5 objects a viewer would recognize if they saw this room again? (The trunks, the desk, the windowsill with feathers)
3. What is the LIGHT like? (Winter light through two windows? Single desk lamp? Fluorescent institutional?)
4. What era details ground it? (Art deco hardware? Rotary phone? Brass fittings?)
5. What would a detective notice first? (This is a mystery — the location is evidence)

---

## What NOT to Include in Location Physique

- **Narrative context:** "This is where Tesla died" → notes field, not physique
- **Emotional description:** "The room felt heavy with absence" → not renderable
- **Action/staging:** "Alice stood in the doorway" → scene prompt, not location design
- **Historical facts:** "Tesla lived here for a decade" → notes field

The physique is ONLY what the camera sees. Materials, objects, light, spatial arrangement.

---

## Props That Need Their Own Reference

Only create a separate prop asset when ALL of these are true:
1. The object appears OUTSIDE its home location
2. The object needs to be visually recognizable as the SAME object in both contexts
3. The object appears in 2+ scenes independently

If any of these are false, it's set dressing. Bake it into the location physique.

---

## Why This Matters for Cost

Each scene can use up to 7 reference images. If the trunks are baked into Room 3327's reference, a scene of "Room 3327 with Tesla's trunks" uses 1 reference slot. If the trunks are a separate prop, the same scene uses 2 slots. Across 600 scenes, unnecessary props waste reference slots that could be used for characters or additional locations.

Every reference slot is a chance to make something consistent. Don't waste them on objects that are already in the room.
