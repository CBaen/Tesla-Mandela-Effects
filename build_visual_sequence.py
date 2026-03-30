import json
import math

def fmt(seconds):
    m = int(seconds) // 60
    s = int(seconds) % 60
    return f"{m:02d}:{s:02d}"

# 150-page visual sequence for Episode 001 "Arriving from Between"
# Each page has: page number, section, evidence_type, brief description, narration_cue, start, end
# Timings are based on Whisper transcript word-level analysis

DURATION = 4568.5

pages_raw = [
    # ============================================================
    # SECTION 1: ROOM 3327 DISCOVERY (Pages 1-14) — 0s to ~310s
    # ============================================================
    # Page 1: Hotel registration card - Room 3327
    {
        "page": 1,
        "section": "Room 3327 Discovery",
        "evidence_type": "DOCUMENT",
        "brief": "Hotel New Yorker registration card, Room 3327, January 1943",
        "narration_cue": "body hadn't even grown cold yet",
        "start": 0.0,
        "end": 14.4,
    },
    # Page 2: Alice Monahan - County Cork origin
    {
        "page": 2,
        "section": "Room 3327 Discovery",
        "evidence_type": "PORTRAIT",
        "brief": "Alice Monahan, hotel maid, County Cork origins — period photograph style",
        "narration_cue": "Alice Monahan smelled it before the door was fully open",
        "start": 14.4,
        "end": 42.7,
    },
    # Page 3: Hotel corridor, 33rd floor - the passkey
    {
        "page": 3,
        "section": "Room 3327 Discovery",
        "evidence_type": "ARCHITECTURAL",
        "brief": "Hotel New Yorker 33rd floor corridor, room 3327 door, passkey in hand",
        "narration_cue": "pass key was in her hand",
        "start": 42.7,
        "end": 72.8,
    },
    # Page 4: Do Not Disturb sign, 3 days on the handle
    {
        "page": 4,
        "section": "Room 3327 Discovery",
        "evidence_type": "ARTIFACT",
        "brief": "Do Not Disturb sign on door handle — guest management record notation",
        "narration_cue": "Do Not Disturb sign had been on the handle since approximately January 5th",
        "start": 72.8,
        "end": 97.0,
    },
    # Page 5: The door swings inward — smell hits
    {
        "page": 5,
        "section": "Room 3327 Discovery",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Door swinging inward — the smell fills the corridor before she crosses threshold",
        "narration_cue": "door swung inward. The smell did not wait",
        "start": 97.0,
        "end": 124.2,
    },
    # Page 6: Copper/metallic taste — sensory detail
    {
        "page": 6,
        "section": "Room 3327 Discovery",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Metallic taste — like a copper penny held too long in a closed hand",
        "narration_cue": "metallic quality. Like a copper penny held too long",
        "start": 124.2,
        "end": 143.3,
    },
    # Page 7: Room interior — curtains still, cold without window open
    {
        "page": 7,
        "section": "Room 3327 Discovery",
        "evidence_type": "ARCHITECTURAL",
        "brief": "Room 3327 interior — curtains still, sealed against January, cold of absence",
        "narration_cue": "curtains hung undisturbed. The frame sealed against January",
        "start": 143.3,
        "end": 166.6,
    },
    # Page 8: Three feathers on the windowsill
    {
        "page": 8,
        "section": "Room 3327 Discovery",
        "evidence_type": "ARTIFACT",
        "brief": "Three gray-tipped feathers on the windowsill — placed, not fallen",
        "narration_cue": "On the window sill. Three feathers. Gray tipped.",
        "start": 166.6,
        "end": 186.6,
    },
    # Page 9: Hotel napkins with equations
    {
        "page": 9,
        "section": "Room 3327 Discovery",
        "evidence_type": "DOCUMENT",
        "brief": "Hotel napkins — dozens of them — equations crossing printed borders without registering edges",
        "narration_cue": "Hotel napkins. Dozens of them. Equations.",
        "start": 186.6,
        "end": 207.7,
    },
    # Page 10: The body — arranged with precision
    {
        "page": 10,
        "section": "Room 3327 Discovery",
        "evidence_type": "FORENSIC",
        "brief": "The body in the bed — arranged with precision of someone who understood this was the last arrangement",
        "narration_cue": "In the bed. The body. Arranged with a precision that did not suggest rest.",
        "start": 207.7,
        "end": 245.9,
    },
    # Page 11: Alice backs out — the smell — lightning in January
    {
        "page": 11,
        "section": "Room 3327 Discovery",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Alice Monahan backs out of the room — air tastes of lightning — she closes the door",
        "narration_cue": "Lightning. The air tasted of lightning. She backed out.",
        "start": 245.9,
        "end": 278.8,
    },
    # Page 12: What was in that room?
    {
        "page": 12,
        "section": "Room 3327 Discovery",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Investigative question — not the body. The wrong question. What was in that room?",
        "narration_cue": "What was in that room? Not the body.",
        "start": 278.8,
        "end": 302.7,
    },
    # Page 13: Investigation begins — transition card
    {
        "page": 13,
        "section": "Room 3327 Discovery",
        "evidence_type": "TITLE_CARD",
        "brief": "Title card: ARRIVING FROM BETWEEN — investigation begins — January 8th 1943",
        "narration_cue": "That is where this investigation begins. That is what we are going to find.",
        "start": 302.7,
        "end": 309.6,
    },
    # Page 14: Interstitial — Room 3327 to Smiljan transition
    {
        "page": 14,
        "section": "Room 3327 Discovery",
        "evidence_type": "INTERSTITIAL",
        "brief": "Map transition: Hotel New Yorker Manhattan 1943 → Smiljan village 1856",
        "narration_cue": "July 10th 1856. The village of Smiljan.",
        "start": 309.6,
        "end": 332.2,
    },

    # ============================================================
    # SECTION 2: SMILJAN BIRTH NIGHT — THREE WITNESSES (Pages 15-36)
    # ~332s to ~990s
    # ============================================================
    # Page 15: The midwife crosses the threshold
    {
        "page": 15,
        "section": "Smiljan Birth Night",
        "evidence_type": "PORTRAIT",
        "brief": "The midwife crossing the Tesla farmhouse threshold — hair standing on arms, violent lightning storm",
        "narration_cue": "midwife crossed the threshold of the Tesla farmhouse",
        "start": 332.2,
        "end": 354.2,
    },
    # Page 16: The first spark — wrongness in her skin
    {
        "page": 16,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The first spark — jumped from hem of skirt to floorboard — felt in her teeth",
        "narration_cue": "she felt the first spark. It jumped from the hem of her skirt",
        "start": 354.2,
        "end": 394.2,
    },
    # Page 17: Sparks jumping with every step — pressurized air
    {
        "page": 17,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Sparks with every step — air pressurized, thick, resistant — the smell of storm already inside",
        "narration_cue": "sparks jumped. The air was charged.",
        "start": 394.2,
        "end": 449.6,
    },
    # Page 18: Dooker Tesla — the mother
    {
        "page": 18,
        "section": "Smiljan Birth Night",
        "evidence_type": "PORTRAIT",
        "brief": "Dooker Tesla — memory like an inventory, hands that built her own tools, memorized Serbian epic poetry",
        "narration_cue": "Dooker Tesla. A woman with a memory like an inventory.",
        "start": 449.6,
        "end": 478.2,
    },
    # Page 19: The contraction arrives with the lightning
    {
        "page": 19,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Contraction arriving with the lightning outside — the grip of someone doing something with all of themselves",
        "narration_cue": "contraction arrived with the next crack of lightning",
        "start": 478.2,
        "end": 523.9,
    },
    # Page 20: At midnight exactly — the exchange
    {
        "page": 20,
        "section": "Smiljan Birth Night",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "At midnight exactly — the lightning at its height — oral tradition record",
        "narration_cue": "at midnight exactly the family would say later",
        "start": 523.9,
        "end": 536.3,
    },
    # Page 21: The omen — child of darkness / child of light
    {
        "page": 21,
        "section": "Smiljan Birth Night",
        "evidence_type": "DOCUMENT",
        "brief": "The midwife: lightning is an omen — this child will be a child of darkness. Dooker: No. Child of light.",
        "narration_cue": "The midwife said it first. The lightning is an omen.",
        "start": 536.3,
        "end": 571.8,
    },
    # Page 22: Nikola Tesla arrives — weight in the midwife's hands
    {
        "page": 22,
        "section": "Smiljan Birth Night",
        "evidence_type": "PORTRAIT",
        "brief": "The moment of birth — Nikola Tesla arrives — weight in the midwife's hands",
        "narration_cue": "Nikola Tesla arrived. The midwife's hands received him.",
        "start": 571.8,
        "end": 602.0,
    },
    # Page 23: More present than the room — lightning rod
    {
        "page": 23,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The infant — more present than the room — different concentration — like a lightning rod",
        "narration_cue": "more present than the room around him. More there.",
        "start": 602.0,
        "end": 628.6,
    },
    # Page 24: Not crying — eyes open — the storm continues
    {
        "page": 24,
        "section": "Smiljan Birth Night",
        "evidence_type": "PORTRAIT",
        "brief": "The newborn — not crying — eyes open — sparks continue — storm smell does not diminish",
        "narration_cue": "He was not crying. His eyes were open.",
        "start": 628.6,
        "end": 696.8,
    },
    # Page 25: The smell remains — not residue but condition
    {
        "page": 25,
        "section": "Smiljan Birth Night",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The storm smell occupying the room — not as residue but as condition — something had arrived ahead",
        "narration_cue": "smell of lightning that had already struck. And the lightning was still in the sky.",
        "start": 696.8,
        "end": 722.1,
    },

    # === WITNESS 1: BLOSSICH ===
    # Page 26: Gossip from the valley — school teacher Blossich
    {
        "page": 26,
        "section": "Smiljan Birth Night - Witness Blossich",
        "evidence_type": "PORTRAIT",
        "brief": "Schoolteacher Stavko Blossich — Gospic, 15km down the limestone road — keeping a diary",
        "narration_cue": "A school teacher named Stravko Blossich was keeping a diary.",
        "start": 722.1,
        "end": 754.4,
    },
    # Page 27: The diary itself — texture, patience
    {
        "page": 27,
        "section": "Smiljan Birth Night - Witness Blossich",
        "evidence_type": "DOCUMENT",
        "brief": "The diary — its texture, patience, attention to practical world — weather, road conditions, livestock",
        "narration_cue": "diary itself. Its texture. Its patience.",
        "start": 754.4,
        "end": 776.8,
    },
    # Page 28: The 1931 regional folklore pamphlet
    {
        "page": 28,
        "section": "Smiljan Birth Night - Witness Blossich",
        "evidence_type": "DOCUMENT",
        "brief": "July 1856 diary entry — transcribed in 1931 regional folklore pamphlet — no national archive",
        "narration_cue": "1931 regional folklore pamphlet that exists in no national archive",
        "start": 776.8,
        "end": 799.5,
    },
    # Page 29: Livestock in the open — facing same direction
    {
        "page": 29,
        "section": "Smiljan Birth Night - Witness Blossich",
        "evidence_type": "FIELD_REPORT",
        "brief": "Livestock moved into open fields — standing facing same direction — not toward shelter",
        "narration_cue": "The livestock had moved into the open. Standing in open fields. Facing same direction.",
        "start": 799.5,
        "end": 839.4,
    },
    # Page 30: Recorded at dawn — before explanation could smooth
    {
        "page": 30,
        "section": "Smiljan Birth Night - Witness Blossich",
        "evidence_type": "DOCUMENT",
        "brief": "Blossich recorded at dawn — writing quickly before mind's need for explanation could smooth the image",
        "narration_cue": "recorded this at dawn walking out to assess the valley",
        "start": 839.4,
        "end": 857.7,
    },
    # Page 31: The well water — a taste where there was none
    {
        "page": 31,
        "section": "Smiljan Birth Night - Witness Blossich",
        "evidence_type": "FIELD_REPORT",
        "brief": "The well water — a taste where there usually was none — sharper, more present — the water itself unmediated",
        "narration_cue": "Then the well water. He drew from the well the following morning.",
        "start": 857.7,
        "end": 893.3,
    },
    # Page 32: The morning light — examination being conducted
    {
        "page": 32,
        "section": "Smiljan Birth Night - Witness Blossich",
        "evidence_type": "FIELD_REPORT",
        "brief": "Morning of July 11th 1856 — light in the valley — like an examination being conducted",
        "narration_cue": "The light in the valley over Gospeach looked like an examination was being conducted.",
        "start": 893.3,
        "end": 946.1,
    },
    # Page 33: He knew nothing of the birth — no connection
    {
        "page": 33,
        "section": "Smiljan Birth Night - Witness Blossich",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Blossich — no connection to Tesla family — recording the observable world — moved to next day's entry",
        "narration_cue": "He knew nothing of the birth in the Tesla household during the storm.",
        "start": 946.1,
        "end": 982.8,
    },

    # === WITNESS 2: KATARINA ===
    # Page 34: The second account — three generations of voice
    {
        "page": 34,
        "section": "Smiljan Birth Night - Witness Katarina",
        "evidence_type": "DOCUMENT",
        "brief": "Second account — arrived through three generations of voice — 1974 graduate student, University of Zagreb",
        "narration_cue": "There is a second account. It arrived not through paper but through three generations of voice.",
        "start": 982.8,
        "end": 1014.3,
    },
    # Page 35: The cassette interview — Katarina, age 80
    {
        "page": 35,
        "section": "Smiljan Birth Night - Witness Katarina",
        "evidence_type": "DOCUMENT",
        "brief": "The cassette interview — Katarina, approximately 80 years old in 1974 — third generation memory",
        "narration_cue": "The woman she interviewed was named Katarina.",
        "start": 1014.3,
        "end": 1054.0,
    },
    # Page 36: The sky looked clean — in a way it hadn't been before
    {
        "page": 36,
        "section": "Smiljan Birth Night - Witness Katarina",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The sky looked clean in a way it hadn't been before — not improved — a new character it had not previously had",
        "narration_cue": "the sky looked clean in a way it hadn't been before",
        "start": 1054.0,
        "end": 1133.3,
    },

    # === WITNESS 3: AUSTRIAN METEOROLOGICAL INSTITUTE ===
    # Page 37: Third source — institutional — Austrian Imperial Meteorological Institute
    {
        "page": 37,
        "section": "Smiljan Birth Night - Witness Meteorological",
        "evidence_type": "DOCUMENT",
        "brief": "Austrian Imperial Meteorological Institute — observation station Gospic — standard measurements",
        "narration_cue": "the third source which is institutional. The Austrian Imperial Meteorological Institute",
        "start": 1133.3,
        "end": 1183.0,
    },
    # Page 38: The anomalous ionization margin notation
    {
        "page": 38,
        "section": "Smiljan Birth Night - Witness Meteorological",
        "evidence_type": "DOCUMENT",
        "brief": "Margin notation — July 11th — different hand, different pen — atmospheric ionization reading anomalous",
        "narration_cue": "Atmospheric ionization reading anomalous this morning. Instrument rechecked. No instrument fault found.",
        "start": 1183.0,
        "end": 1223.5,
    },
    # Page 39: Three instruments pointing at the same morning
    {
        "page": 39,
        "section": "Smiljan Birth Night - Convergence",
        "evidence_type": "DIAGRAM",
        "brief": "Convergence — three instruments: schoolteacher, grandmother, meteorological instrument — same morning, three different angles",
        "narration_cue": "Three instruments pointing at the same morning from three different angles.",
        "start": 1223.5,
        "end": 1256.9,
    },
    # Page 40: None of them knew what the others had seen
    {
        "page": 40,
        "section": "Smiljan Birth Night - Convergence",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "None of them knew what the others had seen — none knew a child was born — the valley noticed",
        "narration_cue": "None of them knew what the others had seen. None of them knew that a child had been born.",
        "start": 1256.9,
        "end": 1266.3,
    },

    # ============================================================
    # SECTION 3: THE STANDARD BIOGRAPHY — ITS SHAPE AND LIMITS
    # Pages 41-60 — ~1266s to ~1745s
    # ============================================================
    # Page 41: The standard biography — its shape
    {
        "page": 41,
        "section": "The Standard Biography",
        "evidence_type": "DIAGRAM",
        "brief": "Standard biography shape — born Balkans, New York, Edison, AC, Niagara, Wardenclyffe, hotels, death",
        "narration_cue": "The standard biography of Nikola Tesla has a shape.",
        "start": 1266.3,
        "end": 1302.7,
    },
    # Page 42: The shape is real — but insufficient
    {
        "page": 42,
        "section": "The Standard Biography",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The shape is real. Every fact checkable. But it describes surface without accounting for what produced it.",
        "narration_cue": "The shape is real. Every fact in it is accurate. And finding it — also insufficient.",
        "start": 1302.7,
        "end": 1329.4,
    },
    # Page 43: Arrival at port of New York — June 6th 1884
    {
        "page": 43,
        "section": "The Standard Biography",
        "evidence_type": "DOCUMENT",
        "brief": "Tesla arrives Port of New York June 6th 1884 — four cents — letter of introduction to Edison",
        "narration_cue": "Nikola Tesla arrived at the port of New York on June 6th, 1884. With four cents in his pocket.",
        "start": 1329.4,
        "end": 1357.3,
    },
    # Page 44: Running machines in his mind — before the crossing
    {
        "page": 44,
        "section": "The Standard Biography",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Running complete functional mechanical systems in mind for years — not designs, not sketches — running machines",
        "narration_cue": "He had been running machines in his mind for years before that crossing.",
        "start": 1357.3,
        "end": 1377.1,
    },
    # Page 45: My Inventions — 1919 — absolutely immaterial to me
    {
        "page": 45,
        "section": "The Standard Biography",
        "evidence_type": "DOCUMENT",
        "brief": "Tesla's memoir My Inventions, Electrical Experimenter 1919 — exact verifiable words — absolutely immaterial to me",
        "narration_cue": "It is absolutely immaterial to me. Whether I run my turbine in thought or test it in my shop.",
        "start": 1377.1,
        "end": 1407.9,
    },
    # Page 46: 20 years — not a single exception
    {
        "page": 46,
        "section": "The Standard Biography",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Invariably my device works as I conceived — 20 years, not a single exception — zero error",
        "narration_cue": "20 years. Not a single exception.",
        "start": 1407.9,
        "end": 1447.8,
    },
    # Page 47: Pull the childhood — the man old before arrival
    {
        "page": 47,
        "section": "The Standard Biography",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Pull the childhood — the man who arrived in New York was already old — structures of perception in place since before language",
        "narration_cue": "pull the childhood. Because the man who arrived in New York with four cents was already old by then.",
        "start": 1447.8,
        "end": 1469.7,
    },

    # ============================================================
    # SECTION 4: CHILDHOOD PHENOMENA — THE CAT
    # Pages 48-60 — ~1469s to ~1745s
    # ============================================================
    # Page 48: He was three years old
    {
        "page": 48,
        "section": "Childhood - The Cat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "He was three years old — not a gift, a condition — the boy carrying something the biography doesn't account for",
        "narration_cue": "He was three years old.",
        "start": 1469.7,
        "end": 1491.4,
    },
    # Page 49: Makak — the family cat
    {
        "page": 49,
        "section": "Childhood - The Cat",
        "evidence_type": "PORTRAIT",
        "brief": "Makak — Serbian word for Tomcat — large enough for a three-year-old's hands flat against back",
        "narration_cue": "Makak. The Serbian word for Tomcat.",
        "start": 1491.4,
        "end": 1512.8,
    },
    # Page 50: Dark room — small hands — warmth of living animal
    {
        "page": 50,
        "section": "Childhood - The Cat",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Dark room — Nikola age three — hands resting on cat's back — grain of fur against palms — body warmth rising",
        "narration_cue": "Nicola Tesla, age three, in a dark room, stroking the cat's back in the darkness.",
        "start": 1512.8,
        "end": 1553.5,
    },
    # Page 51: The sheet of sparks — fur erupted
    {
        "page": 51,
        "section": "Childhood - The Cat",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The fur erupted — a sheet of sparks — continuous — fanning across the cat's back — blue-white and absolute",
        "narration_cue": "Then the fur erupted. A sheet of sparks.",
        "start": 1553.5,
        "end": 1580.4,
    },
    # Page 52: Room lit from beneath — small bones silhouetted
    {
        "page": 52,
        "section": "Childhood - The Cat",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Room lit from beneath — child's own hands visible from inside — small bones silhouetted in discharge light",
        "narration_cue": "the room was lit from beneath. From the interface between fur and palm.",
        "start": 1580.4,
        "end": 1621.1,
    },
    # Page 53: Cat scrambles away — hands empty — eyes full of after-image
    {
        "page": 53,
        "section": "Childhood - The Cat",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Cat scrambling away — hands empty and tingling — eyes full of after-image of own fingers lit from beneath",
        "narration_cue": "the cat was scrambling away. And the child's hands were empty and tingling.",
        "start": 1621.1,
        "end": 1643.2,
    },
    # Page 54: He asked his father — Milutin Tesla
    {
        "page": 54,
        "section": "Childhood - The Cat",
        "evidence_type": "PORTRAIT",
        "brief": "He asked his father — Milutin Tesla, Serbian Orthodox priest, man of logic and scripture",
        "narration_cue": "He asked his father. Milutin Tesla was a Serbian orthodox priest",
        "start": 1643.2,
        "end": 1659.6,
    },
    # Page 55: The answer — electricity — same thing as lightning
    {
        "page": 55,
        "section": "Childhood - The Cat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Milutin: electricity — same thing as lightning — the boy born in a lightning storm has pulled lightning from a cat's back",
        "narration_cue": "electricity. The same thing as lightning.",
        "start": 1659.6,
        "end": 1693.2,
    },
    # Page 56: Not frightened — the quality of a mind receiving a data point
    {
        "page": 56,
        "section": "Childhood - The Cat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Not frightened — this is the part that requires a pause — quality of a mind that has received a data point and is organizing it",
        "narration_cue": "Not frightened. This is the part that requires a pause.",
        "start": 1693.2,
        "end": 1733.4,
    },
    # Page 57: Mental engineering facility already in operation at age three
    {
        "page": 57,
        "section": "Childhood - The Cat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Mental engineering facility already operating at age three — already sorting, already noting — from what?",
        "narration_cue": "The mental engineering facility that would not fail in 20 years was already in operation at age three.",
        "start": 1733.4,
        "end": 1745.3,
    },

    # ============================================================
    # SECTION 5: CHILDHOOD PHENOMENA — THE FORK VISION
    # Pages 58-70 — ~1745s to ~2031s
    # ============================================================
    # Page 58: He was six years old — the geometry arrived
    {
        "page": 58,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "He was six years old when the geometry arrived — dinner at the Tesla household",
        "narration_cue": "He was six years old when the geometry arrived.",
        "start": 1745.3,
        "end": 1763.2,
    },
    # Page 59: The fork in his hand — tin, heavy, warm
    {
        "page": 59,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ARTIFACT",
        "brief": "The fork — tin, heavy for a child's hand — seam detectable under thumb — body warm within 60 seconds",
        "narration_cue": "Fork in his hand. Tin. Heavy for a child's hand.",
        "start": 1763.2,
        "end": 1799.1,
    },
    # Page 60: The fork was gone — attention wandered
    {
        "page": 60,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The fork was gone — the table gone — his mother's face gone — the room gone — holding nothing",
        "narration_cue": "Then the fork was gone. He didn't fall and he wasn't hiding it.",
        "start": 1799.1,
        "end": 1817.8,
    },
    # Page 61: Flash of blinding light — dining room erased
    {
        "page": 61,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Flash of blinding light so complete it erased the dining room entirely — then a place",
        "narration_cue": "a flash of blinding light so complete it erased the dining room entirely.",
        "start": 1817.8,
        "end": 1852.9,
    },
    # Page 62: A place — exact texture of a wall — geometry he had no business knowing
    {
        "page": 62,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ATMOSPHERIC",
        "brief": "A place — exact texture of a wall — quality of afternoon light against stone — geometry he had no business knowing at six",
        "narration_cue": "The exact texture of a wall. The quality of afternoon light against stone.",
        "start": 1852.9,
        "end": 1885.0,
    },
    # Page 63: Documented in his memoir — matter of fact precision
    {
        "page": 63,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "DOCUMENT",
        "brief": "Documented in memoir with matter-of-fact precision of technical specification — flashes, blinding, involuntary, total",
        "narration_cue": "He documented this in his memoir with the matter of fact precision of a technical specification.",
        "start": 1885.0,
        "end": 1917.3,
    },
    # Page 64: Language of an engineer — developing techniques
    {
        "page": 64,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Language of an engineer — a phenomenon I experience, methods I applied — developing techniques to shorten episodes",
        "narration_cue": "The language in the memoir is the language of an engineer writing about a system he had to learn to manage.",
        "start": 1917.3,
        "end": 1951.6,
    },
    # Page 65: The fork still in his hand — could not turn it off
    {
        "page": 65,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The fork still in his hand — tactile world intact — only visual field replaced — could not turn it off",
        "narration_cue": "The fork was still in his hand. He could feel it. He could not turn it off.",
        "start": 1951.6,
        "end": 1985.0,
    },
    # Page 66: His mother was looking at him
    {
        "page": 66,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "PORTRAIT",
        "brief": "His mother looking at him — specific expression — not alarmed, not unalarmed — she had seen his eyes go somewhere before",
        "narration_cue": "His mother was looking at him. Her expression. She had seen his eyes go somewhere.",
        "start": 1985.0,
        "end": 2005.0,
    },
    # Page 67: A woman who has decided not to say anything
    {
        "page": 67,
        "section": "Childhood - The Fork Vision",
        "evidence_type": "PORTRAIT",
        "brief": "The mother — watching since before he could remember — monitoring something she cannot explain or stop — not saying anything",
        "narration_cue": "watching for it. Had perhaps been watching since before he could remember.",
        "start": 2005.0,
        "end": 2031.4,
    },

    # ============================================================
    # SECTION 6: CHILDHOOD PHENOMENA — THE COUNTING
    # Pages 68-74 — ~2031s to ~2187s
    # ============================================================
    # Page 68: The second separate behavior — the counting
    {
        "page": 68,
        "section": "Childhood - The Counting",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Second separate behavior — the need to count, divide — steps counted, objects in groups of three",
        "narration_cue": "There was a second separate behavior running alongside them throughout Tesla's entire life.",
        "start": 2031.4,
        "end": 2067.6,
    },
    # Page 69: W. Bernard Carlson biography — consistent across entire life
    {
        "page": 69,
        "section": "Childhood - The Counting",
        "evidence_type": "DOCUMENT",
        "brief": "W. Bernard Carlson — Tesla, Inventor of the Electrical Age — Princeton UP 2013 — compulsion consistent from childhood through old age",
        "narration_cue": "W. Bernard Carlson's biography. Tesla. Inventor of the electrical age. Documents this compulsion as consistent.",
        "start": 2067.6,
        "end": 2108.6,
    },
    # Page 70: What if the counting was not the origin but the response?
    {
        "page": 70,
        "section": "Childhood - The Counting",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Two phenomena — what if the counting was not the origin of the geometry, but the response to it?",
        "narration_cue": "What if the counting was not the origin of the geometry. But the response to it.",
        "start": 2108.6,
        "end": 2145.7,
    },
    # Page 71: The six-year-old at the dinner table
    {
        "page": 71,
        "section": "Childhood - The Counting",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The six-year-old had not looked for the replacement — it found him — and would not stop finding him",
        "narration_cue": "The six-year-old at the dinner table had not looked for the replacement. It had found him.",
        "start": 2145.7,
        "end": 2187.3,
    },

    # ============================================================
    # SECTION 7: DANE'S DEATH — THE COAT ON THE HOOK
    # Pages 72-82 — ~2187s to ~2550s
    # ============================================================
    # Page 72: Donna Tesla died — horse accident — Tesla's silence
    {
        "page": 72,
        "section": "Dane Death - The Coat",
        "evidence_type": "DOCUMENT",
        "brief": "Dane Tesla died — horse accident in Smiljan — biographies disagree on year — Tesla memoir: I witnessed the tragic scene",
        "narration_cue": "Donna Tesla died when Nicola was approximately seven years old.",
        "start": 2187.3,
        "end": 2226.1,
    },
    # Page 73: Donya's coat still on the hook
    {
        "page": 73,
        "section": "Dane Death - The Coat",
        "evidence_type": "ARTIFACT",
        "brief": "Donya's coat still on the hook by the door — not Tesla's coat — hanging differently when the person won't take it down",
        "narration_cue": "Donna's coat still on the hook by the door.",
        "start": 2226.1,
        "end": 2262.3,
    },
    # Page 74: The absence has gotten into the coat
    {
        "page": 74,
        "section": "Dane Death - The Coat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The absence has gotten into the coat — affected its relationship with gravity — the shoes beside the door",
        "narration_cue": "The absence has gotten into the coat somehow.",
        "start": 2262.3,
        "end": 2305.3,
    },
    # Page 75: The shoes — worn leather — learned their wearer
    {
        "page": 75,
        "section": "Dane Death - The Coat",
        "evidence_type": "ARTIFACT",
        "brief": "The shoes — worn leather — broken in exactly one person's way — the shape of Dane's foot pressed in over years",
        "narration_cue": "The shoes beside the door. Worn leather. Broken in exactly the way one person's foot breaks leather.",
        "start": 2305.3,
        "end": 2344.0,
    },
    # Page 76: Every room the wrong size — presence of an absence
    {
        "page": 76,
        "section": "Dane Death - The Coat",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Every room in the house the wrong size — too large — the presence of an absence — a different thing from ordinary space",
        "narration_cue": "Every room in the house was the wrong size.",
        "start": 2344.0,
        "end": 2394.3,
    },
    # Page 77: After Dane died — visions intensified
    {
        "page": 77,
        "section": "Dane Death - The Coat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "After Dane died — the visions intensified — not created by grief — grief opened a wider passage",
        "narration_cue": "After Don died. The visions intensified.",
        "start": 2394.3,
        "end": 2451.4,
    },
    # Page 78: A wider door — grief's work
    {
        "page": 78,
        "section": "Dane Death - The Coat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "What grief did — not create the phenomenon — open a larger passage through which it could arrive",
        "narration_cue": "What grief did. Is not create the phenomenon. But open a larger passage through which it could arrive.",
        "start": 2451.4,
        "end": 2500.1,
    },
    # Page 79: The celebrated child — he was no longer
    {
        "page": 79,
        "section": "Dane Death - The Coat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The celebrated child — the exceptional one — the household organized around him — and then he was not",
        "narration_cue": "He was the celebrated child. The exceptional one.",
        "start": 2500.1,
        "end": 2538.5,
    },
    # Page 80: The geometry came more often — a wider door
    {
        "page": 80,
        "section": "Dane Death - The Coat",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "In the wrongly proportioned house, with the coat and shoes — the geometry came more often — a wider door",
        "narration_cue": "the geometry came more often. As if whatever was already present had found a wider door.",
        "start": 2538.5,
        "end": 2550.7,
    },

    # ============================================================
    # SECTION 8: LIFE'S SHAPE — WESTINGHOUSE AND WARDENCLYFFE
    # Pages 81-95 — ~2550s to ~2700s
    # ============================================================
    # Page 81: Now. The shape of the life.
    {
        "page": 81,
        "section": "Life Shape - Westinghouse",
        "evidence_type": "DIAGRAM",
        "brief": "Now. The shape of the life — immigrant crossing, Edison rivalry, war of currents — short version: Tesla won",
        "narration_cue": "Now. The shape of the life.",
        "start": 2550.7,
        "end": 2579.3,
    },
    # Page 82: He gave Westinghouse his Niagara patents
    {
        "page": 82,
        "section": "Life Shape - Westinghouse",
        "evidence_type": "DOCUMENT",
        "brief": "He gave George Westinghouse his Niagara patents — far less than their value — the company would not survive otherwise",
        "narration_cue": "He gave George Westinghouse his Niagara patents for far less than their value.",
        "start": 2579.3,
        "end": 2613.2,
    },
    # Page 83: Wardenclyffe — tower on Long Island
    {
        "page": 83,
        "section": "Life Shape - Wardenclyffe",
        "evidence_type": "ARCHITECTURAL",
        "brief": "Wardenclyffe — tower on Long Island — transmit electrical power wirelessly — through the earth itself",
        "narration_cue": "Then Wardencliff. A tower on Long Island.",
        "start": 2613.2,
        "end": 2633.4,
    },
    # Page 84: JP Morgan — refused additional funds — the tower stopped
    {
        "page": 84,
        "section": "Life Shape - Wardenclyffe",
        "evidence_type": "DOCUMENT",
        "brief": "JP Morgan — primary investor — expanded scope — refused additional funds — the tower stopped — demolished for scrap",
        "narration_cue": "His primary investor was JP Morgan. He refused to provide additional funds. The tower stopped.",
        "start": 2633.4,
        "end": 2677.8,
    },
    # Page 85: Hotels. A sequence of them. The Hotel New Yorker.
    {
        "page": 85,
        "section": "Life Shape - Wardenclyffe",
        "evidence_type": "ARCHITECTURAL",
        "brief": "Hotels — a sequence of them — Hotel New Yorker — Westinghouse Electric — 77 years old — century not paying him back",
        "narration_cue": "Hotels. A sequence of them. Westinghouse Electric Company. Arranged him a room.",
        "start": 2677.8,
        "end": 2712.7,
    },

    # ============================================================
    # SECTION 9: THE ROOM ASSIGNED — COULD NOT FIND HIS KIND
    # Pages 86-94 — ~2712s to ~2865s
    # ============================================================
    # Page 86: In that room. He could not find his kind.
    {
        "page": 86,
        "section": "The Room Assigned",
        "evidence_type": "ATMOSPHERIC",
        "brief": "In that room assigned to him — in exchange for his name — he could not find his kind",
        "narration_cue": "In that room. He could not find his kind.",
        "start": 2712.7,
        "end": 2750.8,
    },
    # Page 87: 86 years looking for his kind
    {
        "page": 87,
        "section": "The Room Assigned",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "86 years looking in the coded way — a being looks for its kind when it has no certainty its kind exists on this side",
        "narration_cue": "He spent 86 years looking in the coded way that a being looks for its kind.",
        "start": 2750.8,
        "end": 2783.4,
    },
    # Page 88: The window open in January — she might come
    {
        "page": 88,
        "section": "The Room Assigned",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The window open in January — not by accident — not overheated — he left it open because she might come",
        "narration_cue": "He left the window of his room open in January. He left it open because she might come.",
        "start": 2783.4,
        "end": 2836.9,
    },
    # Page 89: Work. Hotel napkins. Equations on a grain of rice.
    {
        "page": 89,
        "section": "The Room Assigned",
        "evidence_type": "DOCUMENT",
        "brief": "Work — still doing work — hotel napkins — real mathematics — map of a continent on a grain of rice",
        "narration_cue": "The napkins. Hotel napkins. The only surface available in quantity. Real mathematics.",
        "start": 2836.9,
        "end": 2865.0,
    },

    # ============================================================
    # SECTION 10: THE PIGEON
    # Pages 90-105 — ~2865s to ~3303s
    # ============================================================
    # Page 90: White. Pure white with light gray tips.
    {
        "page": 90,
        "section": "The Pigeon",
        "evidence_type": "PORTRAIT",
        "brief": "White — O'Neill's biography — a beautiful bird — pure white with light gray tips — made a habit of his window",
        "narration_cue": "White. A beautiful bird. Pure white with light gray tips on its wings.",
        "start": 2865.0,
        "end": 2896.3,
    },
    # Page 91: She looked at him — recognition
    {
        "page": 91,
        "section": "The Pigeon",
        "evidence_type": "PORTRAIT",
        "brief": "She looked at him — this is the part that requires the pause — the specific word he used: recognition",
        "narration_cue": "She had looked at him. This is the part that requires the pause.",
        "start": 2896.3,
        "end": 2927.8,
    },
    # Page 92: Human eyes had looked at him for 86 years — no recognition
    {
        "page": 92,
        "section": "The Pigeon",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Human eyes for 86 years — studied, celebrated, dismissed, exploited, declared harmless — no recognition until this bird",
        "narration_cue": "Human eyes had looked at him for 86 years. Not once had he found what he found when this bird looked at him.",
        "start": 2927.8,
        "end": 2953.8,
    },
    # Page 93: I loved that pigeon as a man loves a woman
    {
        "page": 93,
        "section": "The Pigeon",
        "evidence_type": "DOCUMENT",
        "brief": "I loved that pigeon as a man loves a woman. And she loved me. — exact language, most precise available",
        "narration_cue": "I loved that pigeon as a man loves a woman. And she loved me.",
        "start": 2953.8,
        "end": 2988.0,
    },
    # Page 94: She died — Hotel St. Regis — weight in his hands
    {
        "page": 94,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "She died — Hotel St. Regis — he was holding her — weight of a bird — feathers make the size",
        "narration_cue": "She died. He was living then at the Hotel St. Regis. He was holding her.",
        "start": 2988.0,
        "end": 3022.4,
    },
    # Page 95: In the moment before she died — the light
    {
        "page": 95,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "In the moment before she died — the light — O'Neill records Tesla's account — the words",
        "narration_cue": "in the moment before she died. The light.",
        "start": 3022.4,
        "end": 3044.6,
    },
    # Page 96: Powerful, dazzling, blinding light
    {
        "page": 96,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "A powerful, dazzling, blinding light — more intense than any lamp in his laboratory — do not convert to metaphor",
        "narration_cue": "Yes, it was a real light. A powerful, dazzling, blinding light. A light more intense than I had ever produced.",
        "start": 3044.6,
        "end": 3079.3,
    },
    # Page 97: Something came from her eyes
    {
        "page": 97,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Something came from her eyes — exceeded every light source his laboratory had ever contained — he registered it",
        "narration_cue": "something came from her eyes that exceeded by his own account every light source his laboratory had ever contained.",
        "start": 3079.3,
        "end": 3117.3,
    },
    # Page 98: Then the light was gone — the weight changed
    {
        "page": 98,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Then the light was gone — the weight changed — what was held is now carried — absence of collaboration",
        "narration_cue": "Then the light was gone. And the bird in his hands had a different quality of weight.",
        "start": 3117.3,
        "end": 3156.2,
    },
    # Page 99: O'Neill records — when that pigeon died, something went out of my life
    {
        "page": 99,
        "section": "The Pigeon",
        "evidence_type": "DOCUMENT",
        "brief": "O'Neill records what Tesla said — when that pigeon died, something went out of my life — not: I was sad",
        "narration_cue": "When that pigeon died, something went out of my life.",
        "start": 3156.2,
        "end": 3211.6,
    },
    # Page 100: Up to that time I knew I would complete my work
    {
        "page": 100,
        "section": "The Pigeon",
        "evidence_type": "DOCUMENT",
        "brief": "Up to that time I knew I would complete my work — when that something went out, I knew my life's work was finished",
        "narration_cue": "Up to that time, I knew with a certainty that I would complete my work.",
        "start": 3211.6,
        "end": 3265.3,
    },
    # Page 101: The thread snapped — the window open in January
    {
        "page": 101,
        "section": "The Pigeon",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The pigeon was the last connection — when she died the thread snapped — the window left open — not expectation",
        "narration_cue": "the pigeon was the last connection to that origin. And when she died, the thread snapped.",
        "start": 3265.3,
        "end": 3303.0,
    },

    # ============================================================
    # SECTION 11: INSTITUTIONAL RESPONSE — FBI AND OAPC
    # Pages 102-115 — ~3303s to ~3560s
    # ============================================================
    # Page 102: Now. January 7th 1943.
    {
        "page": 102,
        "section": "Institutional Response",
        "evidence_type": "TITLE_CARD",
        "brief": "Now. January 7th 1943 — the day the standard biography mentions and moves past",
        "narration_cue": "Now. January 7th, 1943.",
        "start": 3303.0,
        "end": 3332.9,
    },
    # Page 103: Office of Alien Property Custodian
    {
        "page": 103,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "Office of Alien Property Custodian — Trading with Enemy Act — not designed for Tesla — American citizen 52 years",
        "narration_cue": "The office of alien property custodian — established under the Trading with the Enemy Act.",
        "start": 3332.9,
        "end": 3356.8,
    },
    # Page 104: FBI — Foxworth — involved before the body was publicly reported
    {
        "page": 104,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "FBI Assistant Director P.E. Foxworth — Special Intelligence Service — involved before body publicly reported — before passkey used",
        "narration_cue": "FBI Assistant Director P. E. Foxworth, head of the Special Intelligence Service",
        "start": 3356.8,
        "end": 3402.2,
    },
    # Page 105: 80 trunks and crates — six decades of work
    {
        "page": 105,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "Approximately 80 trunks and crates — barrels and packages — six decades of work — notes, designs, correspondence",
        "narration_cue": "Approximately 80 trunks and crates. Six decades of work.",
        "start": 3402.2,
        "end": 3421.4,
    },
    # Page 106: Dr. John G. Trump — three days
    {
        "page": 106,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "Dr. John G. Trump — MIT assistant professor — technical aide NDRC — reviewed 60 years of work in three days",
        "narration_cue": "The government assigned Dr. John G. Trump. Three days.",
        "start": 3421.4,
        "end": 3463.4,
    },
    # Page 107: Harmless — 300 pages declassified FBI file
    {
        "page": 107,
        "section": "Institutional Response",
        "evidence_type": "DOCUMENT",
        "brief": "Harmless — FBI declassified Tesla file 300+ pages — publicly available — but contents classified for decades",
        "narration_cue": "Harmless. The FBI's declassified Tesla file runs more than 300 pages.",
        "start": 3463.4,
        "end": 3496.1,
    },
    # Page 108: Harmless things are not classified
    {
        "page": 108,
        "section": "Institutional Response",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Harmless things are catalogued, archived, made available — harmless things do not require 80 trunks arriving within 2 days",
        "narration_cue": "Harmless things are not classified. Harmless things are catalogued, archived.",
        "start": 3496.1,
        "end": 3526.7,
    },
    # Page 109: 80 trunks. Classified. The institutional story is clean.
    {
        "page": 109,
        "section": "Institutional Response",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "80 trunks. Classified. Institutional story is clean — well documented — the enemy has a name and address",
        "narration_cue": "Approximately 80 trunks. Classified. The institutional story is clean.",
        "start": 3526.7,
        "end": 3560.2,
    },
    # Page 110: The FBI did not steal the color of the sun
    {
        "page": 110,
        "section": "Institutional Response",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "But — the FBI did not steal the color of the sun — exhale — and then consider this",
        "narration_cue": "The FBI did not steal the color of the sun.",
        "start": 3560.2,
        "end": 3569.7,
    },

    # ============================================================
    # SECTION 12: THE MANDELA EFFECT — THE SUN
    # Pages 111-127 — ~3569s to ~3960s
    # ============================================================
    # Page 111: Fiona Broome — coinage of the term around 2009
    {
        "page": 111,
        "section": "The Mandela Effect",
        "evidence_type": "DOCUMENT",
        "brief": "Go back further than Fiona Broome's coinage around 2009 — oral histories, archived threads — before the internet gave communities shared space",
        "narration_cue": "Go back further than Fiona Broome's coinage of the term around 2009.",
        "start": 3569.7,
        "end": 3599.9,
    },
    # Page 112: Not CERN — not 2008 — middle of the 20th century
    {
        "page": 112,
        "section": "The Mandela Effect",
        "evidence_type": "DIAGRAM",
        "brief": "Reports do not cluster around 2008 / CERN — they cluster in middle of the 20th century — children noting the light different",
        "narration_cue": "They do not cluster around 2008 when the large Hadron Collider began full operations at CERN.",
        "start": 3599.9,
        "end": 3630.1,
    },
    # Page 113: The sun was yellow — warmth, amber, coating quality
    {
        "page": 113,
        "section": "The Mandela Effect",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The sun was yellow — warmth, amber-toned, coating quality, settling on surfaces — the old light",
        "narration_cue": "The sun was yellow. People who remember it as yellow describe warmth, a coating quality to the light.",
        "start": 3630.1,
        "end": 3658.4,
    },
    # Page 114: Reports independent — across languages, cultures, decades
    {
        "page": 114,
        "section": "The Mandela Effect",
        "evidence_type": "DIAGRAM",
        "brief": "Reports independent — across languages, cultures, decades — not a shared false memory — independent witnesses describing the same change",
        "narration_cue": "The reports are independent. They are across languages and cultures and decades.",
        "start": 3658.4,
        "end": 3706.3,
    },
    # Page 115: The beginning of the shift points at a birth
    {
        "page": 115,
        "section": "The Mandela Effect",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Track back — beginning of the shift does not point at an institution — it points at a birth",
        "narration_cue": "the beginning of the shift does not point at an institution. It points at a birth.",
        "start": 3706.3,
        "end": 3753.4,
    },
    # Page 116: The institutional investigation is real — but not the question
    {
        "page": 116,
        "section": "The Mandela Effect",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The institutional investigation deserves the investigation it received — real question — but it is not the question",
        "narration_cue": "That question deserves the investigation it has received. But it is not the question.",
        "start": 3753.4,
        "end": 3780.8,
    },
    # Page 117: What arrived when Tesla arrived — what came through the membrane
    {
        "page": 117,
        "section": "The Mandela Effect",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The question: what arrived when Tesla arrived? What the birth admitted? What came through the membrane?",
        "narration_cue": "The question is what arrived when Tesla arrived?",
        "start": 3780.8,
        "end": 3827.8,
    },
    # Page 118: Childhood behaviors as record — not biography
    {
        "page": 118,
        "section": "The Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Childhood behaviors not as biography — as record — involuntary visual phenomena, geometric compulsion",
        "narration_cue": "The childhood behaviors, not as biography, but as record.",
        "start": 3827.8,
        "end": 3852.2,
    },
    # Page 119: Inventions were transmissions — not deliberate signals
    {
        "page": 119,
        "section": "The Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "The inventions were transmissions — not deliberate signals to known recipient — coded in architecture of sender",
        "narration_cue": "The inventions were transmissions, not deliberate signals to a known recipient.",
        "start": 3852.2,
        "end": 3895.0,
    },
    # Page 120: Each one removing a wall — between here and somewhere
    {
        "page": 120,
        "section": "The Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Each invention removing a wall — between here and somewhere the physics was already different",
        "narration_cue": "each one removing a wall. The walls between this reality and somewhere he could not locate.",
        "start": 3895.0,
        "end": 3924.7,
    },
    # Page 121: When the pigeon died — the transmission ended
    {
        "page": 121,
        "section": "The Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "When the pigeon died — transmission ended — not the work — the destination — the pigeon was the last connection",
        "narration_cue": "When the pigeon died, the transmission ended.",
        "start": 3924.7,
        "end": 3960.5,
    },

    # ============================================================
    # SECTION 13: WALTER SIMMONS — THE SECOND WITNESS TO THE SMELL
    # Pages 122-125 — ~3960s to ~4114s
    # ============================================================
    # Page 122: Walter Simmons — maintenance — Hotel New Yorker 1935-1950
    {
        "page": 122,
        "section": "Walter Simmons",
        "evidence_type": "DOCUMENT",
        "brief": "Walter Simmons — maintenance department Hotel New Yorker 1935-1950 — partial diary — typescripted by family",
        "narration_cue": "There was a man named Walter Simmons who worked in the maintenance department of the Hotel New Yorker.",
        "start": 3960.5,
        "end": 4010.3,
    },
    # Page 123: His diary entry for January 1943 — 33rd floor corridor
    {
        "page": 123,
        "section": "Walter Simmons",
        "evidence_type": "DOCUMENT",
        "brief": "Simmons diary entry January 1943 — regular rounds — 33rd floor — Room 3327 — Do Not Disturb sign",
        "narration_cue": "His diary entry for January of 1943 concerns the 33rd floor corridor.",
        "start": 4010.3,
        "end": 4037.7,
    },
    # Page 124: I noticed the smell — the kind you get after a summer storm
    {
        "page": 124,
        "section": "Walter Simmons",
        "evidence_type": "DOCUMENT",
        "brief": "He wrote: I noticed the smell. The kind after a summer storm. The clean kind that tells you lightning has been through.",
        "narration_cue": "I noticed the smell in the corridor near the room. This was not one of the building's smells.",
        "start": 4037.7,
        "end": 4079.3,
    },
    # Page 125: It was January. There was no storm. He walked on.
    {
        "page": 125,
        "section": "Walter Simmons",
        "evidence_type": "DOCUMENT",
        "brief": "It was January. There was no storm. Room 3327 not a door you knocked on. He noted it. He walked on. Typescript ends.",
        "narration_cue": "It was January. There was no storm. He noted it that night and moved on.",
        "start": 4079.3,
        "end": 4114.7,
    },

    # ============================================================
    # SECTION 14: RETURN TO ROOM 3327 — THE SYNTHESIS
    # Pages 126-140 — ~4114s to ~4410s
    # ============================================================
    # Page 126: Return to Room 3327 — January 8th
    {
        "page": 126,
        "section": "Return to Room 3327",
        "evidence_type": "TITLE_CARD",
        "brief": "Return to Room 3327 — January 8th 1943 — six in the morning — Alice Monaghan's passkey",
        "narration_cue": "Return to Room 3327. January 8th, 1943.",
        "start": 4114.7,
        "end": 4142.5,
    },
    # Page 127: The same scene — revisited
    {
        "page": 127,
        "section": "Return to Room 3327",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Same room revisited — smell before eyes adjusted — sharp, clean — curtains heavy still — cold of absence",
        "narration_cue": "The smell hitting her before her eyes have adjusted. Sharp. Clean.",
        "start": 4142.5,
        "end": 4173.6,
    },
    # Page 128: The feathers again. The napkins. The body.
    {
        "page": 128,
        "section": "Return to Room 3327",
        "evidence_type": "FORENSIC",
        "brief": "Three feathers — placed — napkins, equations crossing edges — body arranged with tightness of last arrangement",
        "narration_cue": "Three feathers. Gray tipped. Not fallen. Placed. Napkins. Equations.",
        "start": 4173.6,
        "end": 4204.2,
    },
    # Page 129: What does ozone require?
    {
        "page": 129,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "What does ozone require? The word from Greek ozine — meaning to smell — coined 1840 by Schoenbein",
        "narration_cue": "What does ozone require? The word comes from the Greek ozine. Meaning to smell.",
        "start": 4204.2,
        "end": 4231.4,
    },
    # Page 130: Lightning produces it — high voltage equipment — Tesla's laboratories
    {
        "page": 130,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Lightning produces it — high voltage electrical equipment — Tesla's laboratories always carried the smell — decades of work",
        "narration_cue": "Lightning produces it. Tesla's laboratories had always carried the smell.",
        "start": 4231.4,
        "end": 4273.3,
    },
    # Page 131: But Tesla had not been running experiments in room 3327
    {
        "page": 131,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Tesla had not been running electrical experiments in room 3327 — 86 year old man — declining health — no equipment",
        "narration_cue": "Tesla had not been running electrical experiments in room 3327.",
        "start": 4273.3,
        "end": 4308.5,
    },
    # Page 132: Same atmospheric signature — birth morning, death morning
    {
        "page": 132,
        "section": "Return to Room 3327",
        "evidence_type": "DIAGRAM",
        "brief": "Leaker Valley July 11th 1856 — ionization, examination light, clean sky — Room 3327 January 1943 — same signature",
        "narration_cue": "The same signature. The same atmospheric response to the same kind of event.",
        "start": 4308.5,
        "end": 4357.3,
    },
    # Page 133: Birth and death are the same event
    {
        "page": 133,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Birth and death are the same event — not in metaphorical sense — in the forensic sense — same environmental signature",
        "narration_cue": "Birth and death are the same event. In the forensic sense.",
        "start": 4357.3,
        "end": 4403.1,
    },
    # Page 134: None of them had the investigation — the investigation has the frame
    {
        "page": 134,
        "section": "Return to Room 3327",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "None of them could account for it — none had the investigation — the investigation has the frame",
        "narration_cue": "None of them could account for it because none of them had the investigation. The investigation has the frame.",
        "start": 4403.1,
        "end": 4410.6,
    },

    # ============================================================
    # SECTION 15: FINAL SYNTHESIS — WHAT IT WAS
    # Pages 135-145 — ~4410s to ~4516s
    # ============================================================
    # Page 135: Something came through a storm in Smiljan
    {
        "page": 135,
        "section": "Final Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Something came through a storm in Smiljan on July 10th 1856",
        "narration_cue": "Something came through a storm in Smeleon on July 10th, 1856.",
        "start": 4410.6,
        "end": 4423.9,
    },
    # Page 136: 86 years inside a human life — could not find its kind
    {
        "page": 136,
        "section": "Final Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Spent 86 years inside a human life — ran machines without error — could not find others of its kind",
        "narration_cue": "It spent 86 years inside a human life. It ran machines without error for 20 years.",
        "start": 4423.9,
        "end": 4445.2,
    },
    # Page 137: Found the pigeon — held it when it died
    {
        "page": 137,
        "section": "Final Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Found the pigeon — only creature in 86 years that looked at it and found what it was looking for — held it when it died",
        "narration_cue": "It found the pigeon. The only creature in 86 years that looked at it and found what it was looking for.",
        "start": 4445.2,
        "end": 4462.6,
    },
    # Page 138: Then it departed — through the same kind of door it arrived through
    {
        "page": 138,
        "section": "Final Synthesis",
        "evidence_type": "ATMOSPHERIC",
        "brief": "Then it departed — through the same kind of door it arrived through — the door smelled like lightning for three days",
        "narration_cue": "And then it departed. Through the same kind of door it arrived through.",
        "start": 4462.6,
        "end": 4483.1,
    },
    # Page 139: Something arrived from between the darkness and the light
    {
        "page": 139,
        "section": "Final Synthesis",
        "evidence_type": "TITLE_CARD",
        "brief": "Something arrived from between the darkness and the light — did it sneak through with the child? Or could it have been the child?",
        "narration_cue": "Something arrived from between the darkness and the light.",
        "start": 4483.1,
        "end": 4499.0,
    },
    # Page 140: Can you feel it too?
    {
        "page": 140,
        "section": "Final Synthesis",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Can you feel it too? Time is different. Memories are different. Food tastes different.",
        "narration_cue": "Can you feel it too? Time is different. Memories are different.",
        "start": 4499.0,
        "end": 4512.1,
    },
    # Page 141: The sun and sky are not the same
    {
        "page": 141,
        "section": "Final Synthesis",
        "evidence_type": "ATMOSPHERIC",
        "brief": "The sun and sky are not the same — you may not remember life before Nikola Tesla — soon you may not remember he existed",
        "narration_cue": "The sun and sky are not the same. You may not remember life before Nikola Tesla.",
        "start": 4512.1,
        "end": 4523.2,
    },

    # ============================================================
    # SECTION 16: THE FINAL QUESTION (Pages 142-150)
    # ~4523s to 4568.5s
    # ============================================================
    # Page 142: Here is where we introduce the strange question
    {
        "page": 142,
        "section": "The Final Question",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Here is where we introduce the strange question — the most logical question — the one many refuse to ask",
        "narration_cue": "Here is where we introduce the strange question.",
        "start": 4523.2,
        "end": 4533.2,
    },
    # Page 143: Abilities no man has ever had
    {
        "page": 143,
        "section": "The Final Question",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "If he had abilities no man has ever had — engineer technology in his mind alone — the modern electrical system",
        "narration_cue": "If he had abilities no man has ever had.",
        "start": 4533.2,
        "end": 4548.0,
    },
    # Page 144: Father of the 20th century — free energy — talk to beings not from this earth
    {
        "page": 144,
        "section": "The Final Question",
        "evidence_type": "TEXT_OVERLAY",
        "brief": "Father of the 20th century — free energy — stop wars — talk to beings not from this earth, as he claimed",
        "narration_cue": "father of the 20th century had access to secrets that could create free energy",
        "start": 4548.0,
        "end": 4563.5,
    },
    # Page 145: Then what was Nikola Tesla?
    {
        "page": 145,
        "section": "The Final Question",
        "evidence_type": "TITLE_CARD",
        "brief": "Then what was Nikola Tesla? — the question that holds — the investigation that does not resolve",
        "narration_cue": "Then what was Nikola Tesla?",
        "start": 4563.5,
        "end": 4568.5,
    },

    # ============================================================
    # INTERSTITIAL / DEPTH PAGES (Pages 146-150)
    # Inserted within sections for pacing — use during pauses, transitions
    # These cover portions already covered above — they serve as
    # visual atmosphere holds or section title cards
    # We need to ensure full coverage of 4568.5 seconds
    # These 5 pages are placed as holds within longer segments
    # ============================================================
]

# Now we need exactly 150 pages. Let's check and then add the remaining 5 interstitials
# Currently we have 145 pages. Need 5 more.
# We'll insert interstitials at major section transitions

# The 5 interstitial pages (146-150) are depth/atmosphere pages
# that can be inserted as visual holds. We'll place them at key emotional beats
# that need extra visual air:
# - During the Smiljan birth night atmosphere
# - After the three instruments convergence
# - During Dane's coat/shoes
# - During the pigeon death light
# - During the final synthesis

# But to keep page count exact, we add 5 interstitials that
# take time from existing long segments

# Let me add the 5 interstitial pages and adjust surrounding timings
extra_pages = [
    {
        "page": 146,
        "section": "INTERSTITIAL — Birth Night Atmosphere",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — the Smiljan plateau at night — lightning still in the sky — 1856",
        "narration_cue": "did not diminish when the birth was done",
        "start": 642.3,
        "end": 659.4,
    },
    {
        "page": 147,
        "section": "INTERSTITIAL — Convergence Hold",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — three independent witnesses, none knowing the others — July 11th 1856 morning light",
        "narration_cue": "Until morning. The valley noticed.",
        "start": 1243.5,
        "end": 1256.9,
    },
    {
        "page": 148,
        "section": "INTERSTITIAL — Dane Coat Hold",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — the coat on the hook — the shoes by the door — the house wrong in a way with no visible cause",
        "narration_cue": "every room in the house was the wrong size",
        "start": 2318.5,
        "end": 2344.0,
    },
    {
        "page": 149,
        "section": "INTERSTITIAL — Pigeon Light Hold",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — the moment of light — the room in the moment — he registered it — he survived it",
        "narration_cue": "The room in the moment of the light.",
        "start": 3085.7,
        "end": 3102.9,
    },
    {
        "page": 150,
        "section": "INTERSTITIAL — Departure Hold",
        "evidence_type": "INTERSTITIAL",
        "brief": "Atmospheric hold — the body not making a living body's adjustments — the difference between held and carried",
        "narration_cue": "covered hotel napkins with equations and left the window open in January",
        "start": 4452.7,
        "end": 4462.6,
    },
]

# Note: Pages 146-150 overlap with existing pages
# Their timings are ALREADY embedded within the main pages (24, 39, 76, 97, 137)
# We treat them as sub-pages within those segments

# For the final JSON, we need a clean sequential structure
# Let's re-examine: the task says 150 PAGES that cover the full 4568.5 seconds
# The interstitials are described as "inserted at transitions"
# So the total pages including interstitials = 150

# Current main pages: 145
# Interstitials: 5
# Total: 150

# The interstitials should REPLACE portions of existing pages to maintain no-gap coverage
# Let me restructure pages 24, 39, 76, 97, 137 to split around the interstitials

# PAGE 24 (628.6 - 696.8) splits around interstitial 146 (642.3 - 659.4)
# PAGE 39 (1223.5 - 1256.9) splits around interstitial 147 (1243.5 - 1256.9)
# PAGE 76 (2344.0 - 2394.3) — interstitial 148 precedes it (2318.5 - 2344.0) — already covered by page 75
# PAGE 97 (3079.3 - 3117.3) splits around interstitial 149 (3085.7 - 3102.9)
# PAGE 137 (4445.2 - 4462.6) splits around interstitial 150 (4452.7 - 4462.6)

# REVISED APPROACH: Build 150 pages in strict chronological order
# Some existing pages will be shortened, interstitials inserted as distinct pages

# The cleanest solution: rework the page list to exactly 150 sequential pages
# with no overlaps and no gaps. Let me consolidate.

all_pages = pages_raw + extra_pages

# Sort by start time for verification
sorted_pages = sorted(all_pages, key=lambda x: x['start'])

print(f"Total pages defined: {len(all_pages)}")
print(f"First page start: {all_pages[0]['start']}")
print(f"Last page end: {sorted(all_pages, key=lambda x: x['end'])[-1]['end']}")
print("Done")
