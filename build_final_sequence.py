"""
Build the 150-page timed visual sequence for Episode 001 "Arriving from Between"
Based on Whisper transcription word-level timestamps.

The 150 pages are built in strict chronological order with no gaps.
Interstitials (pages 146-150) are inserted at emotional beats where
extra visual breathing room is needed.

Each page's end time = next page's start time.
Total coverage: 0.0 to 4568.5 seconds.
"""

import json

def fmt(seconds):
    """Convert seconds to MM:SS format."""
    m = int(seconds) // 60
    s = int(seconds) % 60
    return f"{m:02d}:{s:02d}"

DURATION = 4568.5

# ====================================================================
# 150 pages in strict chronological order
# All timings derived from Whisper transcript word-level analysis
# ====================================================================

pages = [
    # ================================================================
    # SECTION 1: ROOM 3327 DISCOVERY (Pages 1-13)
    # Audio: 0.0s - 309.6s
    # ================================================================
    {
        "page": 1,
        "section": "Room 3327 Discovery",
        "evidence_type": "DOCUMENT",
        "brief": "Hotel New Yorker registration card — Room 3327, 33rd floor, January 1943",
        "narration_cue": "body hadn't even grown cold yet",
        "start": 0.0,
        "end": 14.4,
    },
    {
        "page": 2,
        "section": "Room 3327 Discovery",
        "evidence_type": "PORTRAIT",
        "brief": "Alice Monahan, hotel maid — County Cork origins — the smell she encountered before the door opened",
        "narration_cue": "Alice Monahan smelled it before the door was fully open",
        "start": 14.4,
        "end": 42.7,
    },
    {
        "page": 3,
        "section": "Room 3327 Discovery",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The smell not expected in hotel rooms — the outdoor thing — the smell that arrives after a summer storm",
        "narration_cue": "the other thing. The outdoor thing. The smell that arrives after a summer storm",
        "start": 42.7,
        "end": 62.0,
    },
    {
        "page": 4,
        "section": "Room 3327 Discovery",
        "evidence_type": "ARCHITECTURAL",
        "brief": "Hotel New Yorker 33rd floor corridor — passkey in hand — Room 3327",
        "narration_cue": "pass key was in her hand. Room 3327. Hotel New Yorker, 33rd floor",
        "start": 62.0,
        "end": 72.8,
    },
    {
        "page": 5,
        "section": "Room 3327 Discovery",
        "evidence_type": "ARTIFACT",
        "brief": "Do Not Disturb sign on door handle — on the handle since approximately January 5th — three days",
        "narration_cue": "Do Not Disturb sign had been on the handle since approximately January 5th",
        "start": 72.8,
        "end": 97.0,
    },
    {
        "page": 6,
        "section": "Room 3327 Discovery",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The door swings inward — the smell moves into the corridor before she crosses the threshold",
        "narration_cue": "door swung inward. The smell did not wait for her to step into it.",
        "start": 97.0,
        "end": 124.2,
    },
    {
        "page": 7,
        "section": "Room 3327 Discovery",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Metallic taste — like a copper penny held too long in a closed hand — she stepped in",
        "narration_cue": "metallic quality. Like a copper penny held too long in a closed hand",
        "start": 124.2,
        "end": 143.3,
    },
    {
        "page": 8,
        "section": "Room 3327 Discovery",
        "evidence_type": "ARCHITECTURAL",
        "brief": "Room 3327 interior — curtains heavy and still — cold of a room without a living body — radiator ticking",
        "narration_cue": "curtains hung undisturbed. The frame sealed against January. The cold of a different kind.",
        "start": 143.3,
        "end": 166.6,
    },
    {
        "page": 9,
        "section": "Room 3327 Discovery",
        "evidence_type": "ARTIFACT",
        "brief": "Three gray-tipped feathers on the windowsill — not drifted there — placed — at angles that do not suggest casual landing",
        "narration_cue": "On the window sill. Three feathers. Gray tipped. They lay as if placed.",
        "start": 166.6,
        "end": 186.6,
    },
    {
        "page": 10,
        "section": "Room 3327 Discovery",
        "evidence_type": "DOCUMENT",
        "brief": "Hotel napkins — dozens — equations in handwriting that crossed the printed borders without registering them as limit",
        "narration_cue": "Hotel napkins. Dozens of them. Equations. A handwriting that treated the napkin's edge as a boundary the mind declined to recognize.",
        "start": 186.6,
        "end": 207.7,
    },
    {
        "page": 11,
        "section": "Room 3327 Discovery",
        "evidence_type": "FORENSIC",
        "brief": "In the bed. The body. Arranged with the precision of someone who understood this would be the last arrangement.",
        "narration_cue": "In the bed. The body. Arranged with a precision that did not suggest rest.",
        "start": 207.7,
        "end": 245.9,
    },
    {
        "page": 12,
        "section": "Room 3327 Discovery",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Alice backs out — she closes the door — the air tasted of lightning — she does not say anything about the smell",
        "narration_cue": "Lightning. The air tasted of lightning. She backed out. She closed the door.",
        "start": 245.9,
        "end": 278.8,
    },
    {
        "page": 13,
        "section": "Room 3327 Discovery",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "What was in that room? Not the body. The body is the easy answer and the wrong question.",
        "narration_cue": "What was in that room? Not the body. The body is the easy answer and the wrong question.",
        "start": 278.8,
        "end": 309.6,
    },

    # ================================================================
    # SECTION 2: SMILJAN — THE BIRTH NIGHT
    # Audio: 309.6s - 716.6s
    # ================================================================
    {
        "page": 14,
        "section": "Smiljan Birth Night",
        "evidence_type": "TITLE_CARD",
        "brief": "July 10th 1856 — The village of Smiljan — Lika region of the military frontier — The investigation begins",
        "narration_cue": "July 10th 1856. The village of Smiljan. That is where this investigation begins.",
        "start": 309.6,
        "end": 332.2,
    },
    {
        "page": 15,
        "section": "Smiljan Birth Night",
        "evidence_type": "PORTRAIT",
        "brief": "The midwife crossing the threshold of the Tesla farmhouse — hair on arms standing rigid — a sudden wrongness in her own skin",
        "narration_cue": "Two o'clock in the morning. A violent lightning storm. The midwife crossed the threshold.",
        "start": 332.2,
        "end": 361.1,
    },
    {
        "page": 16,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The first spark — jumped from hem of skirt to floorboard — felt in her teeth — not dry winter static",
        "narration_cue": "she felt the first spark. It jumped from the hem of her skirt to the floorboard with a crack she felt in her teeth.",
        "start": 361.1,
        "end": 394.2,
    },
    {
        "page": 17,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Sparks with every step — air pressurized, thick, resistant — something that had weight — that wanted to remain where it was",
        "narration_cue": "sparks jumped. The air was charged. Pressurized in a way that made breathing feel like drawing something thicker than air.",
        "start": 394.2,
        "end": 414.0,
    },
    {
        "page": 18,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The smell in the house — she knew the storm outside — this was that smell — except the storm was outside",
        "narration_cue": "The smell in the house. She knew the storm outside. The smell of lightning working through air. Except the storm was outside.",
        "start": 414.0,
        "end": 457.3,
    },
    {
        "page": 19,
        "section": "Smiljan Birth Night",
        "evidence_type": "PORTRAIT",
        "brief": "Dooker Tesla — woman with a memory like an inventory — hands that built her own tools — Serbian epic poetry memorized",
        "narration_cue": "Dooker Tesla. A woman with a memory like an inventory. And hands that had built her own tools.",
        "start": 457.3,
        "end": 478.2,
    },
    {
        "page": 20,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The contraction arriving with the lightning — Dooker's grip — not the grip of a frightened woman — doing something with all of herself",
        "narration_cue": "The contraction arrived with the next crack of lightning outside. And Dooker's grip on the wooden rail.",
        "start": 478.2,
        "end": 523.9,
    },
    {
        "page": 21,
        "section": "Smiljan Birth Night",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "At midnight exactly — then it broke — the storm built to its height — a sound the valley would not forget",
        "narration_cue": "At midnight exactly the family would say later.",
        "start": 523.9,
        "end": 536.3,
    },
    {
        "page": 22,
        "section": "Smiljan Birth Night",
        "evidence_type": "DOCUMENT",
        "brief": "The midwife said first: lightning is an omen — this child will be a child of darkness. Dooker without hesitation: No. Child of light.",
        "narration_cue": "The midwife said it first. The lightning is an omen. This child will be a child of darkness. No. He will be a child of light.",
        "start": 536.3,
        "end": 571.8,
    },
    {
        "page": 23,
        "section": "Smiljan Birth Night",
        "evidence_type": "PORTRAIT",
        "brief": "Nikola Tesla arrived — the midwife's hands received him — weight of the arriving child — not heavier than expected",
        "narration_cue": "Nikola Tesla arrived. The midwife's hands received him.",
        "start": 571.8,
        "end": 602.0,
    },
    {
        "page": 24,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "More present than the room around him — different quantity of presence — like a lightning rod concentrates charge",
        "narration_cue": "more present than the room around him. The way a lightning rod concentrates charge.",
        "start": 602.0,
        "end": 628.6,
    },
    {
        "page": 25,
        "section": "Smiljan Birth Night",
        "evidence_type": "PORTRAIT",
        "brief": "He was not crying — his eyes were open — the storm continued — the sparks continued",
        "narration_cue": "He was not crying. His eyes were open. The storm continued. The sparks continued.",
        "start": 628.6,
        "end": 642.3,
    },
    # *** INTERSTITIAL 146 — Birth Night Atmosphere hold ***
    {
        "page": 146,
        "section": "INTERSTITIAL — Birth Night Atmosphere",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — the smell of electrical discharge in open air — not as residue but as condition — the birth is done and the smell remains",
        "narration_cue": "did not diminish when the birth was done. Did not clear the way a smell clears.",
        "start": 642.3,
        "end": 659.4,
    },
    {
        "page": 26,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The midwife describes the night to her daughter — passes to her daughter — eventually reaches old age in Gospic",
        "narration_cue": "The midwife would later describe the night to her daughter. Who would pass it to her daughter.",
        "start": 659.4,
        "end": 696.8,
    },
    {
        "page": 27,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Something had arrived ahead of it — below the Lika plateau — in the valley town of Gospic",
        "narration_cue": "Something had arrived ahead of it. Below the leaker plateau.",
        "start": 696.8,
        "end": 716.6,
    },

    # ================================================================
    # SECTION 3: WITNESS 1 — BLOSSICH
    # Audio: 716.6s - 982.8s
    # ================================================================
    {
        "page": 28,
        "section": "Witness 1 - Blossich",
        "evidence_type": "PORTRAIT",
        "brief": "Schoolteacher Stavko Blossich — Gospic, 15km down the limestone road — keeping a diary — not a fanciful man",
        "narration_cue": "A school teacher named Stravko Blossich was keeping a diary. Blossich was not a fanciful man.",
        "start": 716.6,
        "end": 754.4,
    },
    {
        "page": 29,
        "section": "Witness 1 - Blossich",
        "evidence_type": "DOCUMENT",
        "brief": "The diary — its texture and patience — weather, road conditions, livestock — 30 years of observation — the man who finds the observable world more interesting than the interior one",
        "narration_cue": "The diary itself. Its texture. Its patience. Its attention to the practical world.",
        "start": 754.4,
        "end": 769.7,
    },
    {
        "page": 30,
        "section": "Witness 1 - Blossich",
        "evidence_type": "DOCUMENT",
        "brief": "July 1856 entry — exact date water-damaged — transcribed in 1931 regional folklore pamphlet — exists in no national archive",
        "narration_cue": "an entry in July of 1856. The exact date water damaged in the surviving page. Transcribed in a 1931 regional folklore pamphlet that exists in no national archive.",
        "start": 769.7,
        "end": 799.5,
    },
    {
        "page": 31,
        "section": "Witness 1 - Blossich",
        "evidence_type": "FIELD_REPORT",
        "brief": "During the night of the storm the livestock did not shelter — they moved into the open — standing in the open fields",
        "narration_cue": "during the night of the storm the livestock in the valley did not shelter. The livestock had moved into the open.",
        "start": 799.5,
        "end": 826.9,
    },
    {
        "page": 32,
        "section": "Witness 1 - Blossich",
        "evidence_type": "FIELD_REPORT",
        "brief": "Every animal facing the same direction — not toward shelter — as if being addressed by something that had arrived or was arriving",
        "narration_cue": "Every animal in those open fields facing the same way as if they were being addressed by something.",
        "start": 826.9,
        "end": 857.7,
    },
    {
        "page": 33,
        "section": "Witness 1 - Blossich",
        "evidence_type": "FIELD_REPORT",
        "brief": "The well water the following morning — a taste where there usually was none — sharper — more present — the water itself unmediated",
        "narration_cue": "Then the well water. He drew from the well the following morning and the water had a taste. Not a bad taste. Sharper. More present.",
        "start": 857.7,
        "end": 893.3,
    },
    {
        "page": 34,
        "section": "Witness 1 - Blossich",
        "evidence_type": "FIELD_REPORT",
        "brief": "The morning of July 11th 1856 — the light in the valley looked like an examination was being conducted — very white and particular",
        "narration_cue": "The morning of July 11th 1856. The light in the valley over Gospeach looked like an examination was being conducted.",
        "start": 893.3,
        "end": 946.1,
    },
    {
        "page": 35,
        "section": "Witness 1 - Blossich",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "He knew nothing of the birth — no connection to the Tesla family — the observable world had produced these observations — he moved to the next day's entry",
        "narration_cue": "He knew nothing of the birth in the Tesla household during the storm. He recorded them. He moved to the next day's entry.",
        "start": 946.1,
        "end": 982.8,
    },

    # ================================================================
    # SECTION 4: WITNESS 2 — KATARINA
    # Audio: 982.8s - 1133.3s
    # ================================================================
    {
        "page": 36,
        "section": "Witness 2 - Katarina",
        "evidence_type": "DOCUMENT",
        "brief": "The second account — arrived not through paper but through three generations of voice — 1974 graduate student, University of Zagreb",
        "narration_cue": "There is a second account. It arrived not through paper but through three generations of voice.",
        "start": 982.8,
        "end": 1014.3,
    },
    {
        "page": 37,
        "section": "Witness 2 - Katarina",
        "evidence_type": "DOCUMENT",
        "brief": "The cassette interview — Katarina, approximately 80 years old in 1974 — third generation memory — never completed thesis",
        "narration_cue": "The woman she interviewed was named Katarina. She was approximately 80 years old in 1974.",
        "start": 1014.3,
        "end": 1054.0,
    },
    {
        "page": 38,
        "section": "Witness 2 - Katarina",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The sky looked clean in a way it hadn't been before — not cleaner — not improved — a quality — a character the sky had not previously had",
        "narration_cue": "the sky looked clean in a way it hadn't been before. Not cleaner, not an improvement.",
        "start": 1054.0,
        "end": 1117.6,
    },
    {
        "page": 39,
        "section": "Witness 2 - Katarina",
        "evidence_type": "DOCUMENT",
        "brief": "The grandmother said it once — with the precision of recording an observation she cannot account for but cannot let go — Katarina died before 1990",
        "narration_cue": "She said it once. With the precision of someone recording an observation they cannot account for but cannot let go of.",
        "start": 1117.6,
        "end": 1133.3,
    },

    # ================================================================
    # SECTION 5: WITNESS 3 — METEOROLOGICAL INSTITUTE
    # Audio: 1133.3s - 1266.3s
    # ================================================================
    {
        "page": 40,
        "section": "Witness 3 - Meteorological",
        "evidence_type": "DOCUMENT",
        "brief": "Third source — institutional — Austrian Imperial Meteorological Institute — observation station Gospic — standard measurements",
        "narration_cue": "the third source which is institutional. The Austrian Imperial Meteorological Institute maintained an observation station in Gospic.",
        "start": 1133.3,
        "end": 1183.0,
    },
    {
        "page": 41,
        "section": "Witness 3 - Meteorological",
        "evidence_type": "DOCUMENT",
        "brief": "Margin of July 11th entry — different hand, different pen — atmospheric ionization reading anomalous — instrument rechecked — no fault found",
        "narration_cue": "In a hand different from the standard observer. Atmospheric ionization reading anomalous this morning. Instrument rechecked. No instrument fault found.",
        "start": 1183.0,
        "end": 1223.5,
    },
    {
        "page": 42,
        "section": "Witness 3 - Convergence",
        "evidence_type": "DIAGRAM",
        "brief": "Three instruments pointing at the same morning from three different angles — none knew what the others had seen",
        "narration_cue": "Three instruments pointing at the same morning from three different angles.",
        "start": 1223.5,
        "end": 1243.5,
    },
    # *** INTERSTITIAL 147 — Convergence Hold ***
    {
        "page": 147,
        "section": "INTERSTITIAL — Convergence Hold",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — what arrived in the Smeleon Valley that night — arrived in the light, the well water, the atmospheric instruments, the bodies of animals facing the same direction until morning",
        "narration_cue": "What arrived in the Smeleon Valley that night. Arrived in the light. In the well water. In the atmospheric instruments.",
        "start": 1243.5,
        "end": 1266.3,
    },

    # ================================================================
    # SECTION 6: THE STANDARD BIOGRAPHY — ITS SHAPE AND LIMITS
    # Audio: 1266.3s - 1469.7s
    # ================================================================
    {
        "page": 43,
        "section": "The Standard Biography",
        "evidence_type": "DIAGRAM",
        "brief": "The standard biography of Nikola Tesla has a shape — born Balkans, New York, Edison, AC, Niagara, Wardenclyffe, hotels",
        "narration_cue": "The standard biography of Nikola Tesla has a shape.",
        "start": 1266.3,
        "end": 1302.7,
    },
    {
        "page": 44,
        "section": "The Standard Biography",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The shape is real — every fact accurate — and finding it — the specific gravity of a remarkable life — also insufficient",
        "narration_cue": "The shape is real. Every fact in it is accurate. It is also insufficient.",
        "start": 1302.7,
        "end": 1329.4,
    },
    {
        "page": 45,
        "section": "The Standard Biography",
        "evidence_type": "DOCUMENT",
        "brief": "Nikola Tesla arrived at Port of New York June 6th 1884 — four cents in his pocket — letter of introduction to Thomas Edison",
        "narration_cue": "Nikola Tesla arrived at the port of New York on June 6th, 1884. With four cents in his pocket.",
        "start": 1329.4,
        "end": 1357.3,
    },
    {
        "page": 46,
        "section": "The Standard Biography",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Running complete functional mechanical systems in his mind — not designs, not sketches — running machines — with precision that requires a moment to register",
        "narration_cue": "He had been running machines in his mind for years before that crossing. Not designs. Not sketches. Running machines.",
        "start": 1357.3,
        "end": 1377.1,
    },
    {
        "page": 47,
        "section": "The Standard Biography",
        "evidence_type": "DOCUMENT",
        "brief": "My Inventions — Electrical Experimenter 1919 — exact verifiable words: It is absolutely immaterial to me whether I run my turbine in thought or test it in my shop",
        "narration_cue": "He wrote in his memoir My Inventions. It is absolutely immaterial to me. Whether I run my turbine in thought or test it in my shop.",
        "start": 1377.1,
        "end": 1407.9,
    },
    {
        "page": 48,
        "section": "The Standard Biography",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Invariably my device works as I conceived — 20 years — not a single exception — what kind of internal architecture produces that accuracy?",
        "narration_cue": "Invariably my device works as I conceived that it should. In 20 years there has not been a single exception.",
        "start": 1407.9,
        "end": 1447.8,
    },
    {
        "page": 49,
        "section": "The Standard Biography",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Pull the childhood — the man who arrived in New York was already old — the structures of perception in place since before he had language for them",
        "narration_cue": "pull the childhood. Because the man who arrived in New York with four cents was already old by then.",
        "start": 1447.8,
        "end": 1469.7,
    },

    # ================================================================
    # SECTION 7: CHILDHOOD — THE CAT (MAKAK)
    # Audio: 1469.7s - 1745.3s
    # ================================================================
    {
        "page": 50,
        "section": "Childhood - The Cat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "He was three years old — not a gift, a condition — the boy in Smiljan carrying something the biography's shape does not fully account for",
        "narration_cue": "He was three years old.",
        "start": 1469.7,
        "end": 1491.4,
    },
    {
        "page": 51,
        "section": "Childhood - The Cat",
        "evidence_type": "PORTRAIT",
        "brief": "Makak — Serbian word for Tomcat — a family cat — large enough for a three-year-old's hands flat against its back",
        "narration_cue": "Makak. The Serbian word for Tomcat.",
        "start": 1491.4,
        "end": 1512.8,
    },
    {
        "page": 52,
        "section": "Childhood - The Cat",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Dark room — Nikola age three — small hands resting flat on the cat's back — grain of fur against palms — body warmth rising through it",
        "narration_cue": "Nicola Tesla, age three, in a dark room, stroking the cat's back in the darkness.",
        "start": 1512.8,
        "end": 1553.5,
    },
    {
        "page": 53,
        "section": "Childhood - The Cat",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The fur erupted — a sheet of sparks — not one discharge — continuous — fanning across the entire back — blue-white and absolute in the darkness",
        "narration_cue": "Then the fur erupted. A sheet of sparks. Not one discharge. A continuous sheet of them, fanning across the entire back.",
        "start": 1553.5,
        "end": 1580.4,
    },
    {
        "page": 54,
        "section": "Childhood - The Cat",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Room lit from beneath — from the interface between fur and palm — child's own hands visible — small bones silhouetted in light that came from the animal",
        "narration_cue": "the room was lit from beneath. From the interface between fur and palm. The small bones of his fingers, silhouetted in light.",
        "start": 1580.4,
        "end": 1621.1,
    },
    {
        "page": 55,
        "section": "Childhood - The Cat",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The cat scrambles away — hands empty and tingling — eyes full of the after-image of his own fingers lit from beneath",
        "narration_cue": "the cat was scrambling away. And the child's hands were empty and tingling.",
        "start": 1621.1,
        "end": 1643.2,
    },
    {
        "page": 56,
        "section": "Childhood - The Cat",
        "evidence_type": "PORTRAIT",
        "brief": "He asked his father — Milutin Tesla — Serbian Orthodox priest — man of logic and scripture — he looked at his son's hands",
        "narration_cue": "He asked his father. Milutin Tesla was a Serbian orthodox priest.",
        "start": 1643.2,
        "end": 1659.6,
    },
    {
        "page": 57,
        "section": "Childhood - The Cat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Electricity — the same thing as lightning — the boy born in a lightning storm has pulled lightning from a cat's back with his bare hands",
        "narration_cue": "electricity. The same thing as lightning.",
        "start": 1659.6,
        "end": 1693.2,
    },
    {
        "page": 58,
        "section": "Childhood - The Cat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Not frightened — this is the part that requires a pause — the quality of a mind that has received a data point and is already organizing it",
        "narration_cue": "Not frightened. This is the part that requires a pause. The quality of a mind that has just received a data point.",
        "start": 1693.2,
        "end": 1733.4,
    },
    {
        "page": 59,
        "section": "Childhood - The Cat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The mental engineering facility that would not fail in 20 years of professional work was already in operation at age three — already sorting, already noting — from what?",
        "narration_cue": "The mental engineering facility that would not fail in 20 years of professional work was already in operation at age three.",
        "start": 1733.4,
        "end": 1745.3,
    },

    # ================================================================
    # SECTION 8: CHILDHOOD — THE FORK VISION
    # Audio: 1745.3s - 2031.4s
    # ================================================================
    {
        "page": 60,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "He was six years old when the geometry arrived — dinner at the Tesla household — ordinary sounds of a family in use",
        "narration_cue": "He was six years old when the geometry arrived.",
        "start": 1745.3,
        "end": 1763.2,
    },
    {
        "page": 61,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ARTIFACT",
        "brief": "The fork — tin — heavy for a child's hand — seam detectable under thumb — body warm within 60 seconds of holding",
        "narration_cue": "Fork in his hand. Tin. Heavy for a child's hand. Heavier than it looks.",
        "start": 1763.2,
        "end": 1799.1,
    },
    {
        "page": 62,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Then the fork was gone — his attention wandered — the table gone, his mother's face gone, the room gone — holding nothing",
        "narration_cue": "Then the fork was gone. He didn't fall and he wasn't hiding it. His attention wandered.",
        "start": 1799.1,
        "end": 1817.8,
    },
    {
        "page": 63,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ATMOSPHERIC",
        "brief": "A flash of blinding light so complete it erased the dining room — then a place — not the Tesla household — not anywhere near Smiljan",
        "narration_cue": "a flash of blinding light so complete it erased the dining room entirely. Then a place.",
        "start": 1817.8,
        "end": 1852.9,
    },
    {
        "page": 64,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Exact texture of a wall — quality of afternoon light against stone — geometry he had no business knowing — more real than the dinner table",
        "narration_cue": "The exact texture of a wall. The quality of afternoon light against stone. The particular geometry of a space he had no business knowing at six years old.",
        "start": 1852.9,
        "end": 1885.0,
    },
    {
        "page": 65,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "DOCUMENT",
        "brief": "Documented in memoir with matter-of-fact precision of a technical specification — flashes, blinding, involuntary, total — developing techniques for shortening them",
        "narration_cue": "He documented this in his memoir with the matter of fact precision of a technical specification.",
        "start": 1885.0,
        "end": 1917.3,
    },
    {
        "page": 66,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Language of an engineer writing about a system he had to learn to manage — here is a phenomenon I experience — here are the methods I applied",
        "narration_cue": "The language in the memoir is the language of an engineer writing about a system he had to learn to manage.",
        "start": 1917.3,
        "end": 1951.6,
    },
    {
        "page": 67,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The fork still in his hand — the tactile world had not gone anywhere — only the visual field replaced — could not turn it off any more than he could turn off the sound of his own name",
        "narration_cue": "The fork was still in his hand. He could feel it. He could not turn it off.",
        "start": 1951.6,
        "end": 1985.0,
    },
    {
        "page": 68,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "PORTRAIT",
        "brief": "His mother looking at him — her expression — not alarmed, not unalarmed — she had seen his eyes go somewhere before — she had been watching for it",
        "narration_cue": "His mother was looking at him. She had seen his eyes go somewhere. She had been watching for it.",
        "start": 1985.0,
        "end": 2005.0,
    },
    {
        "page": 69,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "PORTRAIT",
        "brief": "A woman who has decided not to say anything — monitoring something in her child she cannot explain and cannot stop — the fork still in his hand",
        "narration_cue": "watching for it. Had perhaps been watching since before he could remember. Decided not to say anything.",
        "start": 2005.0,
        "end": 2031.4,
    },

    # ================================================================
    # SECTION 9: CHILDHOOD — THE COUNTING
    # Audio: 2031.4s - 2187.3s
    # ================================================================
    {
        "page": 70,
        "section": "Childhood - The Counting",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Second separate behavior — the need to count and divide — steps counted, objects in groups of three, cubic volume of food calculated",
        "narration_cue": "There was a second separate behavior running alongside them throughout Tesla's entire life. The need to count. The need to divide.",
        "start": 2031.4,
        "end": 2067.6,
    },
    {
        "page": 71,
        "section": "Childhood - The Counting",
        "evidence_type": "DOCUMENT",
        "brief": "W. Bernard Carlson — Tesla: Inventor of the Electrical Age — Princeton University Press 2013 — compulsion consistent from childhood through old age — not a phase, not a preference, a need",
        "narration_cue": "W. Bernard Carlson's biography. Princeton University Press. 2013. Documents this compulsion as consistent from childhood through old age.",
        "start": 2067.6,
        "end": 2108.6,
    },
    {
        "page": 72,
        "section": "Childhood - The Counting",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "What if the counting was not the origin of the geometry — but the response to it — the attempt to make the visible world match what the visual episodes were already showing him",
        "narration_cue": "What if the counting was not the origin of the geometry. But the response to it.",
        "start": 2108.6,
        "end": 2145.7,
    },
    {
        "page": 73,
        "section": "Childhood - The Counting",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The six-year-old at the dinner table had not looked for the replacement — it found him — it would not stop finding him — the episodes returned, uninvited",
        "narration_cue": "The six-year-old at the dinner table had not looked for the replacement. It had found him. And it would not stop finding him.",
        "start": 2145.7,
        "end": 2187.3,
    },

    # ================================================================
    # SECTION 10: DANE'S DEATH — THE COAT ON THE HOOK
    # Audio: 2187.3s - 2550.7s
    # ================================================================
    {
        "page": 74,
        "section": "Dane Death - The Coat",
        "evidence_type": "DOCUMENT",
        "brief": "Dane Tesla died — horse accident in Smiljan — biographies disagree on year 1863-1865 — Tesla memoir: I witnessed the tragic scene — that is all",
        "narration_cue": "Donna Tesla died when Nicola was approximately seven years old. Tesla's memoir gives only: I witnessed the tragic scene.",
        "start": 2187.3,
        "end": 2226.1,
    },
    {
        "page": 75,
        "section": "Dane Death - The Coat",
        "evidence_type": "ARTIFACT",
        "brief": "Dane's coat still on the hook by the door — not Tesla's coat — hanging slightly differently when the person who will take it down is no longer coming",
        "narration_cue": "Donna's coat still on the hook by the door. Which hangs slightly differently. When the person who will take it down is no longer coming.",
        "start": 2226.1,
        "end": 2262.3,
    },
    {
        "page": 76,
        "section": "Dane Death - The Coat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The absence has gotten into the coat — affected its relationship with gravity — the shoes beside the door — worn leather — broken in exactly one person's way",
        "narration_cue": "The absence has gotten into the coat somehow. Has affected its relationship with gravity.",
        "start": 2262.3,
        "end": 2305.3,
    },
    {
        "page": 77,
        "section": "Dane Death - The Coat",
        "evidence_type": "ARTIFACT",
        "brief": "The shoes — worn leather — the slight asymmetry of how Dane stood — shoes learn their wearer — these shoes had learned theirs — the body was not coming back",
        "narration_cue": "The shoes beside the door. Worn leather. Broken in exactly the way one person's foot breaks leather.",
        "start": 2305.3,
        "end": 2344.0,
    },
    # *** INTERSTITIAL 148 — Coat/Shoes Hold ***
    {
        "page": 148,
        "section": "INTERSTITIAL — Dane Coat Hold",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — every room in the house was the wrong size — too large — something that had been occupying them has stopped — the presence of an absence",
        "narration_cue": "Every room in the house was the wrong size. The presence of an absence. Which is a different thing from ordinary space.",
        "start": 2344.0,
        "end": 2394.3,
    },
    {
        "page": 78,
        "section": "Dane Death - The Coat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "After Dane died — the visions intensified — they were not produced by grief — they preceded grief — grief opened a larger passage",
        "narration_cue": "After Don died. The visions intensified. The visions were not produced by grief. They preceded grief.",
        "start": 2394.3,
        "end": 2451.4,
    },
    {
        "page": 79,
        "section": "Dane Death - The Coat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "What grief did — not create the phenomenon — open a larger passage through which it could arrive — a different question from what happened to this grieving child's nervous system",
        "narration_cue": "What grief did. Is not create the phenomenon. But open a larger passage through which it could arrive.",
        "start": 2451.4,
        "end": 2500.1,
    },
    {
        "page": 80,
        "section": "Dane Death - The Coat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The celebrated child — the exceptional one — the household organized around him — and then he was not — the geometry came more often — a wider door",
        "narration_cue": "He was the celebrated child. And then he was not. The geometry came more often.",
        "start": 2500.1,
        "end": 2550.7,
    },

    # ================================================================
    # SECTION 11: LIFE'S SHAPE — WESTINGHOUSE AND WARDENCLYFFE
    # Audio: 2550.7s - 2712.7s
    # ================================================================
    {
        "page": 81,
        "section": "Life Shape - The Immigrant",
        "evidence_type": "DIAGRAM",
        "brief": "Now. The shape of the life — the immigrant crossing, the Edison rivalry, the war of currents — documented, verifiable — the short version: Tesla won",
        "narration_cue": "Now. The shape of the life. The immigrant crossing. The Edison rivalry. The war of currents. All of this is known.",
        "start": 2550.7,
        "end": 2579.3,
    },
    {
        "page": 82,
        "section": "Life Shape - Westinghouse",
        "evidence_type": "DOCUMENT",
        "brief": "He gave George Westinghouse his Niagara patents for far less than their value — the traditional account says he voluntarily tore up the royalty contract",
        "narration_cue": "He gave George Westinghouse his Niagara patents for far less than their value.",
        "start": 2579.3,
        "end": 2613.2,
    },
    {
        "page": 83,
        "section": "Life Shape - Wardenclyffe",
        "evidence_type": "ARCHITECTURAL",
        "brief": "Then Wardenclyffe — a tower on Long Island — designed to transmit electrical power wirelessly across the planet — through the earth itself",
        "narration_cue": "Then Wardencliff. A tower on Long Island. Designed to transmit electrical power wirelessly across the planet.",
        "start": 2613.2,
        "end": 2659.1,
    },
    {
        "page": 84,
        "section": "Life Shape - Wardenclyffe",
        "evidence_type": "DOCUMENT",
        "brief": "JP Morgan — primary investor — refused additional funds — the tower stopped — demolished for scrap during World War I — the scrap did not cover what Tesla owed",
        "narration_cue": "His primary investor was JP Morgan. He refused to provide additional funds. The tower stopped. Wardencliff was demolished for scrap.",
        "start": 2659.1,
        "end": 2712.7,
    },

    # ================================================================
    # SECTION 12: THE ROOM ASSIGNED — COULD NOT FIND HIS KIND
    # Audio: 2712.7s - 2865.0s
    # ================================================================
    {
        "page": 85,
        "section": "The Room Assigned",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Hotels — a sequence of them — the Hotel New Yorker — Westinghouse Electric — 77 years old — the century he had powered was not paying him back",
        "narration_cue": "Hotels. A sequence of them. The Hotel New Yorker. He was 77 years old. And the century he had powered was not paying him back.",
        "start": 2712.7,
        "end": 2750.8,
    },
    {
        "page": 86,
        "section": "The Room Assigned",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "In that room assigned to him in exchange for his name — he could not find his kind — 86 years looking in the coded way a being looks for its kind",
        "narration_cue": "In that room. He could not find his kind. He spent 86 years looking.",
        "start": 2750.8,
        "end": 2783.4,
    },
    {
        "page": 87,
        "section": "The Room Assigned",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The window open in January — not by accident — not because the room had overheated — he left it open because she might come",
        "narration_cue": "He left the window of his room open in January. He left it open because she might come.",
        "start": 2783.4,
        "end": 2836.9,
    },
    {
        "page": 88,
        "section": "The Room Assigned",
        "evidence_type": "DOCUMENT",
        "brief": "Work — still doing work — hotel napkins — real mathematics — active thought — like a map of a continent drawn on a grain of rice",
        "narration_cue": "The napkins. Hotel napkins. The equations were real mathematics. Active thought. Genuine science.",
        "start": 2836.9,
        "end": 2865.0,
    },

    # ================================================================
    # SECTION 13: THE PIGEON
    # Audio: 2865.0s - 3303.0s
    # ================================================================
    {
        "page": 89,
        "section": "The Pigeon",
        "evidence_type": "PORTRAIT",
        "brief": "White — O'Neill's biography records Tesla's description — a beautiful bird — pure white with light gray tips — had come to him in the years before — made a habit of his window",
        "narration_cue": "White. A beautiful bird. Pure white with light gray tips on its wings.",
        "start": 2865.0,
        "end": 2896.3,
    },
    {
        "page": 90,
        "section": "The Pigeon",
        "evidence_type": "PORTRAIT",
        "brief": "She looked at him — this is the part that requires the pause — not: she was a pretty bird and he was lonely — the specific word he used: recognition",
        "narration_cue": "She had looked at him. This is the part that requires the pause. The specific word he used. Recognition. Not affection.",
        "start": 2896.3,
        "end": 2932.6,
    },
    {
        "page": 91,
        "section": "The Pigeon",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Human eyes had looked at him for 86 years — studied, celebrated, dismissed, exploited, declared harmless — not once had he found what he found when this bird looked at him",
        "narration_cue": "Human eyes had looked at him for 86 years. Not once in all of that looking had he found what he found when this bird looked at him.",
        "start": 2932.6,
        "end": 2953.8,
    },
    {
        "page": 92,
        "section": "The Pigeon",
        "evidence_type": "DOCUMENT",
        "brief": "I loved that pigeon as a man loves a woman. And she loved me. — O'Neill records him saying it — he was not speaking imprecisely",
        "narration_cue": "I loved that pigeon as a man loves a woman. And she loved me.",
        "start": 2953.8,
        "end": 2979.1,
    },
    {
        "page": 93,
        "section": "The Pigeon",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "In 86 years of looking for his kind, he had found it once — in a white bird with grey-tipped wings — using the most exact language available for an experience that language could not fully hold",
        "narration_cue": "In 86 years of looking for his kind, he had found it once in a white bird with grey tipped wings.",
        "start": 2979.1,
        "end": 2988.0,
    },
    {
        "page": 94,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "She died — Hotel St. Regis — he was holding her — the weight of a bird — birds are lighter than they appear — feathers make the size",
        "narration_cue": "She died. He was holding her. The weight in his hands. Birds are lighter than they appear.",
        "start": 2988.0,
        "end": 3022.4,
    },
    {
        "page": 95,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The grey-tipped feathers against his palms — the slight variable warmth of a living thing generating its own heat — and then, in the moment before she died — the light",
        "narration_cue": "in the moment before she died. The light.",
        "start": 3022.4,
        "end": 3044.6,
    },
    {
        "page": 96,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "O'Neill recording what his subject said — yes, it was a real light — powerful, dazzling, blinding — more intense than any lamp in his laboratory — do not convert to metaphor",
        "narration_cue": "Yes, it was a real light. A powerful, dazzling, blinding light. A light more intense than I had ever produced by the most powerful lamps in my laboratory.",
        "start": 3044.6,
        "end": 3079.3,
    },
    # *** INTERSTITIAL 149 — Pigeon Light Hold ***
    {
        "page": 149,
        "section": "INTERSTITIAL — Pigeon Light Hold",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — something came from her eyes that exceeded every light source his laboratory had ever contained — the room in the moment of the light — he registered it, survived it, carried it as documented fact",
        "narration_cue": "The room in the moment of the light. He was there. He registered it. He survived it.",
        "start": 3079.3,
        "end": 3117.3,
    },
    {
        "page": 97,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Then the light was gone — the bird had a different quality of weight — what was held is now carried — the absence of collaboration",
        "narration_cue": "Then the light was gone. And the bird in his hands had a different quality of weight. What was held is now carried.",
        "start": 3117.3,
        "end": 3169.4,
    },
    {
        "page": 98,
        "section": "The Pigeon",
        "evidence_type": "DOCUMENT",
        "brief": "O'Neill records what Tesla said — the words of a precise man who chose them carefully — when that pigeon died, something went out of my life",
        "narration_cue": "When that pigeon died, something went out of my life.",
        "start": 3169.4,
        "end": 3211.6,
    },
    {
        "page": 99,
        "section": "The Pigeon",
        "evidence_type": "DOCUMENT",
        "brief": "Up to that time I knew I would complete my work — when that something went out of my life, I knew my life's work was finished",
        "narration_cue": "Up to that time, I knew with a certainty that I would complete my work.",
        "start": 3211.6,
        "end": 3265.3,
    },
    {
        "page": 100,
        "section": "The Pigeon",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The pigeon was the last connection — when she died the thread snapped — what remained was the man continuing because he did not know how to stop",
        "narration_cue": "the pigeon was the last connection to that origin. And when she died, the thread snapped.",
        "start": 3265.3,
        "end": 3303.0,
    },

    # ================================================================
    # SECTION 14: INSTITUTIONAL RESPONSE — FBI AND OAPC
    # Audio: 3303.0s - 3560.2s
    # ================================================================
    {
        "page": 101,
        "section": "Institutional Response",
        "evidence_type": "TITLE_CARD",
        "brief": "Now. January 7th 1943 — there is a fact about that day the standard biography mentions and then moves past",
        "narration_cue": "Now. January 7th, 1943.",
        "start": 3303.0,
        "end": 3332.9,
    },
    {
        "page": 102,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "Office of Alien Property Custodian — Trading with the Enemy Act — not an agency designed for Tesla — American citizen since 1891, 52 years",
        "narration_cue": "The office of alien property custodian. The statute did not fit.",
        "start": 3332.9,
        "end": 3356.8,
    },
    {
        "page": 103,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "FBI Assistant Director P.E. Foxworth — Special Intelligence Service — involved from early January 7th — before body publicly reported — before Alice Monahan used her passkey",
        "narration_cue": "FBI Assistant Director P. E. Foxworth, head of the Special Intelligence Service. Involved from early in the day of January 7th, before the body was publicly reported.",
        "start": 3356.8,
        "end": 3402.2,
    },
    {
        "page": 104,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "Approximately 80 trunks and crates — barrels and packages — six decades of work — notes, designs, correspondence — objects of investigation accumulated by a mind that had not stopped",
        "narration_cue": "Approximately 80 trunks and crates, along with barrels and packages. Six decades of work.",
        "start": 3402.2,
        "end": 3421.4,
    },
    {
        "page": 105,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "Dr. John G. Trump — MIT assistant professor — NDRC technical aide — assigned to review what Tesla spent 60 years producing — three days",
        "narration_cue": "The government assigned Dr. John G. Trump. Three days. Trump reviewed 60 years of work in three days.",
        "start": 3421.4,
        "end": 3463.4,
    },
    {
        "page": 106,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "His conclusion: Tesla's work did not include new sound workable principles — would not constitute a hazard — Harmless — FBI declassified file 300+ pages",
        "narration_cue": "Harmless. The FBI's declassified Tesla file runs more than 300 pages.",
        "start": 3463.4,
        "end": 3496.1,
    },
    {
        "page": 107,
        "section": "Institutional Response",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Harmless things are catalogued, archived, made available — harmless things do not require crates that arrived within two days — harmless things are not classified",
        "narration_cue": "Harmless things are not classified. Harmless things do not require crates that arrived within approximately two days.",
        "start": 3496.1,
        "end": 3526.7,
    },
    {
        "page": 108,
        "section": "Institutional Response",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Approximately 80 trunks — classified — the institutional story is clean — well documented — the enemy has a name and an address — exhale",
        "narration_cue": "Approximately 80 trunks. Classified. The institutional story is clean. Exhale.",
        "start": 3526.7,
        "end": 3560.2,
    },

    # ================================================================
    # SECTION 15: THE MANDELA EFFECT — THE SUN
    # Audio: 3560.2s - 3960.5s
    # ================================================================
    {
        "page": 109,
        "section": "The Mandela Effect",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The FBI did not steal the color of the sun — and then consider this",
        "narration_cue": "the FBI did not steal the color of the sun.",
        "start": 3560.2,
        "end": 3569.7,
    },
    {
        "page": 110,
        "section": "The Mandela Effect",
        "evidence_type": "DOCUMENT",
        "brief": "Go back further than Fiona Broome's coinage of the term around 2009 — oral histories, archived threads — before the internet gave communities shared space",
        "narration_cue": "Go back further than Fiona Broome's coinage of the term around 2009.",
        "start": 3569.7,
        "end": 3599.9,
    },
    {
        "page": 111,
        "section": "The Mandela Effect",
        "evidence_type": "DIAGRAM",
        "brief": "Reports do not cluster around 2008 or CERN — they cluster in the middle of the 20th century — children noting the light of adulthood different from the light of childhood",
        "narration_cue": "They do not cluster around 2008 when the large Hadron Collider began full operations at CERN. They cluster in the middle of the 20th century.",
        "start": 3599.9,
        "end": 3630.1,
    },
    {
        "page": 112,
        "section": "The Mandela Effect",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The sun was yellow — warmth, amber-toned, coating quality — light that settles rather than discloses — people who came of age in the latter half find it clinical, white, more like a lamp than a star",
        "narration_cue": "The sun was yellow. People who remember it as yellow describe warmth, a coating quality. People who came of age in the latter half find the light clinical, white, more like a lamp than like a star.",
        "start": 3630.1,
        "end": 3676.6,
    },
    {
        "page": 113,
        "section": "The Mandela Effect",
        "evidence_type": "DIAGRAM",
        "brief": "Reports independent — across languages, cultures, decades — not the consistency of shared false memory — the consistency of independent witnesses describing the same change",
        "narration_cue": "The reports are independent. The consistency is not the consistency of a shared false memory.",
        "start": 3676.6,
        "end": 3706.3,
    },
    {
        "page": 114,
        "section": "The Mandela Effect",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Track the timeline back — the beginning of the shift does not point at a facility with a name and address — it points at a birth",
        "narration_cue": "the beginning of the shift does not point at an institution. It points at a birth.",
        "start": 3706.3,
        "end": 3753.4,
    },
    {
        "page": 115,
        "section": "The Mandela Effect",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The institutional investigation deserves the investigation it received — it is a real question — but it is not the question",
        "narration_cue": "That question deserves the investigation it has received. It is a real question. But it is not the question.",
        "start": 3753.4,
        "end": 3780.8,
    },
    {
        "page": 116,
        "section": "The Mandela Effect",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The question: what arrived when Tesla arrived? What the birth admitted? What came through the membrane on a night when lightning split the sky?",
        "narration_cue": "The question is what arrived when Tesla arrived? What the birth admitted?",
        "start": 3780.8,
        "end": 3827.8,
    },

    # ================================================================
    # SECTION 16: THE SYNTHESIS
    # Audio: 3827.8s - 3960.5s
    # ================================================================
    {
        "page": 117,
        "section": "The Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Childhood behaviors not as biography but as record — involuntary visual phenomena — geometric compulsion — mental engineering that ran without error",
        "narration_cue": "The childhood behaviors, not as biography, but as record.",
        "start": 3827.8,
        "end": 3852.2,
    },
    {
        "page": 118,
        "section": "The Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The inventions were transmissions — not deliberate signals to a known recipient — coded in the architecture of the sender — carrying information from a source the sender cannot fully access but cannot suppress",
        "narration_cue": "The inventions were transmissions, not deliberate signals to a known recipient.",
        "start": 3852.2,
        "end": 3895.0,
    },
    {
        "page": 119,
        "section": "The Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Each one removing a wall — dissolving a constraint — the wireless power, the resonant frequency of the earth — between here and somewhere the physics was already different",
        "narration_cue": "each one removing a wall. Between here and somewhere the physics was already different.",
        "start": 3895.0,
        "end": 3924.7,
    },
    {
        "page": 120,
        "section": "The Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "When the pigeon died — the transmission ended — not the work — the destination — the pigeon was the last connection and when she died the thread went slack",
        "narration_cue": "When the pigeon died, the transmission ended. The destination ended.",
        "start": 3924.7,
        "end": 3960.5,
    },

    # ================================================================
    # SECTION 17: WALTER SIMMONS — THE SECOND WITNESS
    # Audio: 3960.5s - 4114.7s
    # ================================================================
    {
        "page": 121,
        "section": "Walter Simmons",
        "evidence_type": "DOCUMENT",
        "brief": "Walter Simmons — maintenance department Hotel New Yorker 1935-1950 — partial diary survive in typescript — family provided to a researcher in the 1960s",
        "narration_cue": "There was a man named Walter Simmons who worked in the maintenance department of the Hotel New Yorker.",
        "start": 3960.5,
        "end": 4010.3,
    },
    {
        "page": 122,
        "section": "Walter Simmons",
        "evidence_type": "DOCUMENT",
        "brief": "Simmons diary — January 1943 — regular rounds — 33rd floor corridor — Room 3327 — Do Not Disturb sign on the door",
        "narration_cue": "His diary entry for January of 1943 concerns the 33rd floor corridor.",
        "start": 4010.3,
        "end": 4037.7,
    },
    {
        "page": 123,
        "section": "Walter Simmons",
        "evidence_type": "DOCUMENT",
        "brief": "He wrote: I noticed the smell in the corridor near the room — I have been in this building for years and I know its smells — this was not one of them",
        "narration_cue": "I noticed the smell in the corridor near the room. I have been in this building for years, and I know its smells. This was not one of them.",
        "start": 4037.7,
        "end": 4056.1,
    },
    {
        "page": 124,
        "section": "Walter Simmons",
        "evidence_type": "DOCUMENT",
        "brief": "The kind of smell after a summer storm — the clean kind — tells you lightning has been through — he paused — in the diary the pause is visible — then: it was January, there was no storm",
        "narration_cue": "The kind of smell you get after a summer storm, the clean kind. He paused. Then, it was January. There was no storm.",
        "start": 4056.1,
        "end": 4092.7,
    },
    {
        "page": 125,
        "section": "Walter Simmons",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "He didn't stop — didn't report the smell — Room 3327 was not a door you knocked on — he noted it and moved on — the typescript ends — He smelled it. He noted it. He walked on.",
        "narration_cue": "He noted it that night and moved on. He smelled it. He noted it. He walked on.",
        "start": 4092.7,
        "end": 4114.7,
    },

    # ================================================================
    # SECTION 18: RETURN TO ROOM 3327 — THE SYNTHESIS
    # Audio: 4114.7s - 4410.6s
    # ================================================================
    {
        "page": 126,
        "section": "Return to Room 3327",
        "evidence_type": "TITLE_CARD",
        "brief": "Return to Room 3327 — January 8th 1943 — six in the morning — Alice Monaghan's passkey — the door opening",
        "narration_cue": "Return to Room 3327. The same room. January 8th, 1943. Six in the morning.",
        "start": 4114.7,
        "end": 4142.5,
    },
    {
        "page": 127,
        "section": "Return to Room 3327",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The smell hitting her before eyes adjusted — sharp — clean in a way that is not comfortable — curtains heavy and still — cold of a room without a living body",
        "narration_cue": "The smell hitting her before her eyes have adjusted to the room. Sharp. Clean. The curtains. Heavy. Still.",
        "start": 4142.5,
        "end": 4173.6,
    },
    {
        "page": 128,
        "section": "Return to Room 3327",
        "evidence_type": "FORENSIC",
        "brief": "Three feathers — gray-tipped — not fallen, placed — napkins, equations in handwriting that crossed the edges — body arranged — last arrangement — smell of lightning, summer storm",
        "narration_cue": "Three feathers. Gray tipped. Not fallen. Placed. Napkins. Equations. The body. Arranged. The smell. Lightning.",
        "start": 4173.6,
        "end": 4204.2,
    },
    {
        "page": 129,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "What does ozone require? The word from Greek ozine — meaning to smell — coined 1840 by Christian Friedrich Schoenbein",
        "narration_cue": "What does ozone require? The word comes from the Greek ozine. Meaning to smell.",
        "start": 4204.2,
        "end": 4231.4,
    },
    {
        "page": 130,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Ozone forms when electrical discharge splits oxygen molecules — lightning produces it — high voltage equipment — Tesla's laboratories always carried the smell",
        "narration_cue": "Lightning produces it. Tesla's laboratories had always carried the smell.",
        "start": 4231.4,
        "end": 4273.3,
    },
    {
        "page": 131,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Tesla had not been running electrical experiments in room 3327 — 86-year-old man in declining health — no equipment — no power supply capable of producing electrical discharge at the required scale",
        "narration_cue": "Tesla had not been running electrical experiments in room 3327. He was an 86 year old man in declining health.",
        "start": 4273.3,
        "end": 4308.5,
    },
    {
        "page": 132,
        "section": "Return to Room 3327",
        "evidence_type": "DIAGRAM",
        "brief": "Leaker Valley morning of July 11th 1856: ionization anomaly, examination light, clean sky — Room 3327 January 1943: ozone smell — same atmospheric signature at birth and at death",
        "narration_cue": "The same signature. The same atmospheric response to the same kind of event.",
        "start": 4308.5,
        "end": 4357.3,
    },
    {
        "page": 133,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Birth and death are the same event — not in the metaphorical sense that arrivals and departures share a grammar — in the forensic sense — the same environmental signature at the point of arrival and the point of departure",
        "narration_cue": "Birth and death are the same event. In the forensic sense. The same environmental signature at the point of arrival and the point of departure.",
        "start": 4357.3,
        "end": 4403.1,
    },
    {
        "page": 134,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "None of them could account for it — none of them had the investigation — the investigation has the frame",
        "narration_cue": "None of them could account for it because none of them had the investigation. The investigation has the frame.",
        "start": 4403.1,
        "end": 4410.6,
    },

    # ================================================================
    # SECTION 19: FINAL SYNTHESIS — WHAT IT WAS
    # Audio: 4410.6s - 4523.2s
    # ================================================================
    {
        "page": 135,
        "section": "Final Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Something came through a storm in Smiljan on July 10th 1856",
        "narration_cue": "Something came through a storm in Smeleon on July 10th, 1856.",
        "start": 4410.6,
        "end": 4423.9,
    },
    {
        "page": 136,
        "section": "Final Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "It spent 86 years inside a human life — ran machines without error for 20 years — could not find others of its kind — gave the electrical century to a species that received it and gave nothing back",
        "narration_cue": "It spent 86 years inside a human life. It ran machines without error for 20 years. It could not find others of its kind.",
        "start": 4423.9,
        "end": 4445.2,
    },
    {
        "page": 137,
        "section": "Final Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Found the pigeon — only creature in 86 years that looked at it and found what it was looking for — held the pigeon when the pigeon died — felt the weight change from held to carried",
        "narration_cue": "It found the pigeon. The only creature in 86 years that looked at it and found what it was looking for. It held the pigeon when the pigeon died.",
        "start": 4445.2,
        "end": 4462.6,
    },
    # *** INTERSTITIAL 150 — Departure Hold ***
    {
        "page": 150,
        "section": "INTERSTITIAL — Departure Hold",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — covered hotel napkins with equations — left the window open in January — because the body had not finished learning what the mind already knew",
        "narration_cue": "covered hotel napkins with equations and left the window open in January. Because the body had not finished learning what the mind already knew.",
        "start": 4462.6,
        "end": 4468.2,
    },
    {
        "page": 138,
        "section": "Final Synthesis",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Then it departed — through the same kind of door it arrived through — the door smelled like lightning for three days",
        "narration_cue": "And then it departed. Through the same kind of door it arrived through. And the door smelled like lightning for three days.",
        "start": 4468.2,
        "end": 4483.1,
    },
    {
        "page": 139,
        "section": "Final Synthesis",
        "evidence_type": "TITLE_CARD",
        "brief": "Something arrived from between the darkness and the light — did it sneak through with the child during birth? Was it bound to the child? Or could it have been the child?",
        "narration_cue": "Something arrived from between the darkness and the light.",
        "start": 4483.1,
        "end": 4499.0,
    },
    {
        "page": 140,
        "section": "Final Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Can you feel it too? Time is different. Memories are different. Food tastes different. The sun and sky are not the same.",
        "narration_cue": "Can you feel it too? Time is different. Memories are different. Food tastes different.",
        "start": 4499.0,
        "end": 4516.9,
    },

    # ================================================================
    # SECTION 20: THE FINAL QUESTION (Pages 141-145)
    # Audio: 4516.9s - 4568.5s
    # ================================================================
    {
        "page": 141,
        "section": "The Final Question",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "You may not remember life before Nikola Tesla — and soon you may not remember Nikola Tesla existed at all — here is where we introduce the strange question",
        "narration_cue": "You may not remember life before Nikola Tesla. And soon you may not remember Nikola Tesla existed at all.",
        "start": 4516.9,
        "end": 4523.2,
    },
    {
        "page": 142,
        "section": "The Final Question",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Here is the strange question — possibly the most logical question — the one many refuse to ask — if he had abilities no man has ever had",
        "narration_cue": "Here is where we introduce the strange question. If he had abilities no man has ever had.",
        "start": 4523.2,
        "end": 4540.6,
    },
    {
        "page": 143,
        "section": "The Final Question",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The modern electrical system, the radio, remote control, neon lights, x-rays, wireless communication, the induction motor — and so much more suppressed, hidden, or stolen",
        "narration_cue": "the modern electrical system, the radio, the remote control, neon lights, x-rays, wireless communication, the induction motor",
        "start": 4540.6,
        "end": 4548.0,
    },
    {
        "page": 144,
        "section": "The Final Question",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Father of the 20th century — free energy — stop wars — reinvent the entire world — talk to beings not from this earth, as he claimed",
        "narration_cue": "father of the 20th century had access to secrets that could create free energy, stop wars, reinvent the entire world, and talk to beings not from this earth, as he claimed.",
        "start": 4548.0,
        "end": 4563.5,
    },
    {
        "page": 145,
        "section": "The Final Question",
        "evidence_type": "TITLE_CARD",
        "brief": "Then what was Nikola Tesla?",
        "narration_cue": "Then what was Nikola Tesla?",
        "start": 4563.5,
        "end": 4568.5,
    },
]

# ====================================================================
# Sort pages into chronological order and renumber sequentially
# ====================================================================

# Sort by start time
pages_sorted = sorted(pages, key=lambda x: x['start'])

# Verify we have exactly 150 pages
assert len(pages_sorted) == 150, f"Expected 150 pages, got {len(pages_sorted)}"

# Enforce no-gap coverage: each page's end = next page's start
# (adjust any minor rounding issues)
for i in range(len(pages_sorted) - 1):
    # Ensure end of page i = start of page i+1
    pages_sorted[i]['end'] = pages_sorted[i+1]['start']

# Ensure last page ends at total duration
pages_sorted[-1]['end'] = DURATION

# Renumber pages in chronological order (maintain the page number as the logical visual order)
# The page numbers in pages_sorted are already the final numbers we want
# We just need to rebuild the page list with sequential numbering (1-150 in time order)
# But we WANT to keep the original page numbers since they reference the visual map

# Let's just output them sorted by start time with their original page numbers
# That's more useful for the production team

# Build final output
output = {
    "episode": "001",
    "title": "Arriving from Between",
    "duration_seconds": DURATION,
    "total_pages": 150,
    "generated_from": "Whisper word-level timestamps — 001-whisper-clean.json",
    "notes": [
        "Pages 146-150 are INTERSTITIAL pages inserted at emotional beats for visual breathing room.",
        "All other pages are numbered by narrative section, not strict chronological order.",
        "The JSON is sorted by start_seconds for production use.",
        "Every second of the 4568.5-second audio is covered — no gaps.",
        "evidence_type: DOCUMENT | PORTRAIT | ATMOSPHERIC | ARTIFACT | ARCHITECTURAL | FORENSIC | TEXT_OVERLAY | DIAGRAM | FIELD_REPORT | TITLE_CARD | INTERSTITIAL"
    ],
    "pages": []
}

for i, p in enumerate(pages_sorted):
    duration = round(p['end'] - p['start'], 2)
    output['pages'].append({
        "page": p['page'],
        "sequence": i + 1,  # 1-150 in time order
        "start_seconds": round(p['start'], 2),
        "end_seconds": round(p['end'], 2),
        "start_timecode": fmt(p['start']),
        "end_timecode": fmt(p['end']),
        "duration_seconds": duration,
        "section": p['section'],
        "evidence_type": p['evidence_type'],
        "brief": p['brief'],
        "narration_cue": p['narration_cue'],
    })

# Verify coverage
total_covered = sum(p['duration_seconds'] for p in output['pages'])
print(f"Total pages: {len(output['pages'])}")
print(f"Total audio duration: {DURATION}s")
print(f"Total coverage by pages: {total_covered:.2f}s")
print(f"Coverage gap: {DURATION - total_covered:.2f}s")

# Check for gaps/overlaps
print("\nChecking for gaps/overlaps...")
gaps = []
for i in range(len(output['pages']) - 1):
    curr_end = output['pages'][i]['end_seconds']
    next_start = output['pages'][i+1]['start_seconds']
    if abs(curr_end - next_start) > 0.01:
        gaps.append(f"Gap between seq {i+1} and {i+2}: {curr_end:.2f} -> {next_start:.2f}")

if gaps:
    print("GAPS FOUND:")
    for g in gaps:
        print(f"  {g}")
else:
    print("No gaps found. Coverage is complete.")

# Write output
output_path = r'C:\Users\baenb\Desktop\Tesla Mandela Effects\0. EPISODE FACTORY\EPISODES\001 - ARRIVING FROM BETWEEN\001-VISUAL-TIMED-SEQUENCE.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"\nOutput written to:\n{output_path}")

# Print summary statistics
sections = {}
for p in output['pages']:
    s = p['section'].split(' - ')[0] if ' - ' in p['section'] else p['section']
    s = s.replace('INTERSTITIAL — ', 'INTERSTITIAL')
    if 'INTERSTITIAL' in s:
        s = 'INTERSTITIAL'
    sections[s] = sections.get(s, 0) + p['duration_seconds']

print("\n=== Section Time Breakdown ===")
for section, dur in sorted(sections.items(), key=lambda x: -x[1]):
    minutes = dur / 60
    print(f"  {section}: {dur:.0f}s ({minutes:.1f}min)")

# Print short/long duration pages
print("\n=== Duration Distribution ===")
durations = [p['duration_seconds'] for p in output['pages']]
print(f"  Shortest page: {min(durations):.1f}s (page {output['pages'][durations.index(min(durations))]['page']})")
print(f"  Longest page: {max(durations):.1f}s (page {output['pages'][durations.index(max(durations))]['page']})")
print(f"  Average: {sum(durations)/len(durations):.1f}s")

print("\n=== Sample Pages ===")
for p in output['pages'][:5]:
    print(f"  Seq {p['sequence']:3d} | Page {p['page']:3d} | {p['start_timecode']}-{p['end_timecode']} ({p['duration_seconds']:.1f}s) | {p['section'][:30]}")
print("  ...")
for p in output['pages'][-5:]:
    print(f"  Seq {p['sequence']:3d} | Page {p['page']:3d} | {p['start_timecode']}-{p['end_timecode']} ({p['duration_seconds']:.1f}s) | {p['section'][:30]}")
