import json, os

ANCHOR = "Extreme close-up of a single aged journal page filling the entire frame edge to edge. Yellowed paper with faint blue ruled lines, slight foxing spots, tea stains at corners, a partial coffee ring. Warm overhead lighting, paper texture visible. Hyper-realistic photograph. "

src = os.path.join(os.path.dirname(__file__), "001-VISUAL-TIMED-SEQUENCE.json")
dst = os.path.join(os.path.dirname(__file__), "001-VISUAL-TIMED-SEQUENCE-v2.json")

with open(src, encoding="utf-8") as f:
    entries = json.load(f)

PROMPTS = {
1: "A faded hotel registration card taped to the page with yellowing adhesive tape. The card shows a large room number '3327' printed in bold type at the top, with printed form fields partially filled in with black typewriter ink. Cobalt blue handwritten annotation beneath: 'January 7, 1943 — never checked out.' Red marker circle around the floor number. A brass pushpin holds the upper corner.",

2: "A black-and-white portrait photograph paper-clipped to the upper left of the page — a middle-aged woman in maid's uniform, dark apron, face turned slightly away from camera, expression unreadable. Cobalt blue ink annotation beside her shoulder: 'A. Monahan — County Cork — 11 yrs service.' Red arrow drawn pointing to her right hand, which is slightly raised. The photo has a white border and small crease at one corner.",

3: "Dense annotation page. The top half filled with cobalt blue handwriting in tight looping script covering the ruled lines completely, words pressed together with urgency. A rough pencil sketch in the lower half showing a storm cloud with radiating lines beneath it — not lightning, more like a diffusion pattern spreading downward. Red marker underlines two words near the center. A water stain blooms at the lower right corner.",

4: "A faded color Polaroid photograph taped at an angle with yellowing adhesive tape showing a long hotel corridor — dark carpet runner, identical doors receding into distance, a single hanging lamp casting amber light. The far end of the corridor is slightly overexposed, almost white. Below the Polaroid, cobalt blue ink annotation: 'Floor 33 — north wing — Room 3327 fourth from end.' Red arrow pointing toward the brightest door.",

5: "A physical object on the page: a small rectangular cardboard door hanger sign, 'DO NOT DISTURB' printed in faded red serif type, pinned flat with two brass pushpins. The hanger is slightly yellowed, its wire loop bent. Cobalt blue annotation beside it: 'On handle approx. Jan 5 — 3 days.' Red marker circle around the date. The hanger's shadow falls across the ruled lines beneath it.",

6: "A faded color Polaroid taped at a slight angle showing a hotel room doorway from the corridor — door swung inward, a rectangle of dim room visible beyond. The air at the threshold appears slightly hazy, as if something in the exposure shifted. Cobalt blue annotation below: 'The smell moved first — before she crossed.' Red arrow pointing into the dark rectangle of the open door.",

7: "A small swatch of dark copper-colored fabric pinned to the page with a brass pin — rough texture, tightly woven. Beside it, a flat copper penny taped down with transparent yellowing tape, its surface dull and warm-toned. Cobalt blue annotation: 'Metallic — penny held too long — her words exactly.' Red underline beneath the penny. A pencil sketch of an open hand beside the objects, fingers curled.",

8: "A wide-angle Polaroid photograph taped to the page showing a hotel room interior — heavy curtains, a single chair, a radiator along the far wall. The room is very still. A lamp is on but gives dim amber light. Cobalt blue annotation in the lower margin: 'Cold — wrong kind of cold — no living body.' Red marker circle around the radiator. A small foxing spot near the upper left corner of the photo.",

9: "Three actual gray-tipped feathers taped to the page in a triangular arrangement, each secured with a thin strip of yellowing transparent tape. The feathers are white shafts with pale gray tips — dove or pigeon. Beside them, cobalt blue annotation in careful script: 'Not fallen — placed — angles deliberate.' A small red arrow pointing to the angle of the middle feather. The page shows slight indentation where the feathers rest.",

10: "A fragment of hotel napkin — white paper, slightly yellowed — taped to the page. The napkin surface is covered edge to edge in dense pencil equation marks, mathematical notation crossing the printed border of the napkin without pause. Cobalt blue annotation beside it: 'Equations cross the border — do not register it as limit.' Red marker circles the point where writing crosses the napkin edge.",

11: "A sketch drawn directly on the journal page in precise pencil lines showing a narrow bed from above — mattress, pillow, folded hands. The figure in the bed is suggested by outline only, very still, almost geometric in its stillness. Cobalt blue annotation in the margin: 'Arranged — last arrangement — deliberate.' Red arrows pointing to the position of the hands. Emerald green line drawn along the body's central axis.",

12: "Dense annotation page. Cobalt blue handwriting filling the entire ruled surface, words at varying pressures — some lines pressed hard, others light. In the center, a large red question mark drawn in marker, surrounded by smaller pencil question marks radiating outward. At the bottom margin, a single underlined phrase in red. Old tea stain in the upper right quadrant.",

13: "A torn fragment of a map — yellowed paper with printed topographic lines, Cyrillic place names in faded black type — taped to the page. A red marker circle around a village name in the center. Cobalt blue annotation beside it: 'Smiljan — Lika region — July 10, 1856.' An emerald green line drawn from the village circle toward the page margin with an arrow.",

14: "A faded black-and-white photograph taped at an angle showing a stone farmhouse exterior — thick walls, small windows, a wooden door slightly ajar. A dirt path leads to the entrance. Cobalt blue annotation below: 'Tesla farmhouse — Smiljan — midwife crossed this threshold.' Red arrow pointing to the doorway. The photo has a white border, foxing spots, and one corner is dog-eared.",

15: "A pencil sketch on the journal page showing the hem of a long skirt above a wooden floorboard, with small radiating spark lines drawn between fabric and wood. The lines are drawn with care — not chaotic, deliberate. Cobalt blue annotation: 'First spark — felt in teeth — not static.' Red arrows pointing to three separate spark lines. The sketch has a slightly technical quality, like an engineering observation.",

16: "Dense annotation page. The upper half filled with cobalt blue handwriting, the ink slightly heavier on certain words. In the lower half, a rough pencil diagram showing a human figure standing, with radiating lines extending from the feet outward and upward. The lines thicken toward the top. Red marker underlines a line of text near the middle. Emerald green connecting arrows link two separate annotations.",

17: "A wide-format sketch drawn directly on the journal page showing the interior of a farmhouse room — low ceiling beams, a figure standing near the center, radiating lines spreading from the figure's feet through the floor and walls. The lines suggest pressure, density, something that wanted to stay. Cobalt blue annotation in the upper margin: 'Weight — it had weight — wanted to remain.' Red marker encircles the figure's feet.",

18: "A faded sepia portrait photograph paper-clipped to the upper right corner — a strong-faced woman with dark hair pulled back, hands visible at the frame edge, expression composed and formidable. Cobalt blue annotation beside her: 'Dooker Tesla — inventory memory — built her own tools.' Red underline beneath the word 'tools.' A small emerald green asterisk in the margin.",

19: "A pencil sketch drawn on the journal page showing two hands gripping something — knuckles defined, tendons visible, a quality of enormous contained force. Below the hands, cobalt blue annotation: 'Not the grip of a frightened woman — doing something with all of herself.' Red arrows point to each set of knuckles. The sketch is technically precise, almost anatomical.",

20: "A torn scrap of paper — rough edges, pale yellow — taped to the center of the page. On it, written in cobalt blue ink in large careful letters: 'Midnight exactly.' Below it in the same hand, smaller: 'Then it broke.' The scrap is pinned at one corner with a brass pushpin. Red marker underlines 'midnight exactly.' The page beneath shows a faint ring from a glass or cup.",

21: "A densely packed page with two evidence items side by side: left side has a handwritten note card in cobalt blue ink with two short lines of text in a dialogue format, taped flat; right side has a small pencil sketch of a woman's face in profile, expression fierce and certain. Red string connects the note card to the sketch. Margin filled with cobalt blue annotations and a single red circle.",

22: "A faded Polaroid photograph taped to the center of the page showing a pair of weathered hands — a midwife's hands, large, capable, slightly curled as if receiving weight. The hands are empty in the photograph but the gesture is one of receiving. Cobalt blue annotation below: 'Weight of the arriving child — not heavier than expected.' Red arrow pointing to the cupped shape of the hands.",

23: "A pencil sketch on the journal page showing a lightning rod mounted on a roofline — the rod rising to a sharp point, with fine radiating lines concentrating toward the tip. Around the tip, the lines are densest. Cobalt blue annotation beside the drawing: 'More present than the room — different quantity of presence.' Red arrows point to the convergence point at the rod's tip.",

24: "Dense annotation page. Cobalt blue handwriting in very careful script, each letter distinct, covering the upper two-thirds of the page. In the lower third, a pencil sketch of a pair of open eyes — irises detailed, pupils dilated, the surrounding whites clean and alert. Red marker circles both pupils. Cobalt blue annotation beneath: 'Eyes open — storm continued — sparks continued.'",

25: "A folded note — pale cream paper, fold lines visible — taped open to the page. Inside, cobalt blue ink writing in a compact hand. The note's edges are slightly foxed. Beside it, a rough pencil sketch of a room outline with a single figure standing in the center, storm lines visible through a sketched window. Red underline through a single phrase. Emerald green arrow pointing from the note to the sketch.",

26: "A handwritten letter fragment — torn from a larger page, edges ragged — taped at an angle. The fragment is covered in dense cobalt blue script, the handwriting slightly aged. Below the fragment, a second smaller note in different handwriting — lighter ink, more careful letters. Red paper clip holds both to the page. Cobalt blue annotation in the margin: '3 generations — voice to voice.'",

27: "A torn piece of a geological survey map — printed topographic lines, elevation numbers in small serif type, a valley feature marked in faded red — taped to the page. A cobalt blue circle drawn around a valley depression. Annotation beside: 'Something arrived below the plateau — in the valley — before.' Red arrows pointing downward toward the circled valley. Water stain along the right edge.",

28: "A faded black-and-white photograph taped to the upper half of the page showing a village road — cobblestones, low stone buildings, a single figure walking away in the middle distance. The figure is small and slightly blurred. Cobalt blue annotation below: 'Gospic — 15km — limestone road — not a fanciful man.' Red arrow pointing to the walking figure.",

29: "A physical object: a small hardbound journal — just the cover visible — taped flat with wide yellowing tape, its cloth cover dark green, slightly worn at the spine corners. Beside it, cobalt blue annotation: 'Diary — 30 years — the man who finds the observable world more interesting.' Red underline beneath 'observable world.' A brass pushpin at the upper right corner of the journal cover.",

30: "A fragment of a printed pamphlet page — pale gray paper, small serif type visible — taped to the center of the page. One line of text circled in red marker. Cobalt blue annotation beside it: '1931 regional folklore pamphlet — no national archive.' A second annotation below in smaller script: 'July 1856 entry — date water-damaged.' The pamphlet fragment has a torn right edge and a foxing spot.",

31: "A pencil sketch on the journal page showing an open field at night — flat horizon, a few crude fence posts, and multiple small animal shapes standing in the field, all oriented in the same direction. The alignment is the striking visual element. Cobalt blue annotation: 'Every animal facing the same direction — not toward shelter.' Red arrows indicating the direction all figures face.",

32: "A sketch on the journal page showing twelve small animal silhouettes arranged in a grid, all facing the same direction — left to right. The uniformity is eerie. Cobalt blue annotation beside the grid: 'As if being addressed by something — arriving or arrived.' Red marker draws a single direction arrow across all figures. Emerald green lines connect them in rows.",

33: "A small glass vial — capped, empty now — taped to the page with a strip of yellowing tape, labeled in cobalt blue ink: 'Well — Gospic — July 11 sample?' The vial is clear glass, slightly dusty. Beside it, a handwritten note: 'Taste where there usually was none — sharper — more present.' Red marker circle around the vial cap. A pencil sketch of a well beside it.",

34: "Dense annotation page. The page is nearly covered in cobalt blue handwriting, but in the center, a rough pencil sketch of a valley landscape seen from above — flat fields, a road, a river line, all bathed in white light suggested by the blank page itself. The light is the absence of pencil marks. Cobalt blue annotation in the margins: 'White — particular — like an examination.' Red underlines on two phrases.",

35: "A faded Polaroid photograph taped at a slight angle showing farmland in early morning — fields, a fence line, muted sky. The image is slightly overexposed, washed out at the horizon. Cobalt blue annotation below: 'The light looked like an examination was being conducted.' Red marker circle on the brightest area of sky in the photo.",

36: "A torn cassette tape insert card — the kind from an audio cassette, printed text on cream paper, slightly yellowed — taped to the page. Handwriting in cobalt blue over the printed text. Below it, a small sticky note in pale yellow with cobalt ink: '1974 — Zagreb — oral history project.' Red paper clip holds both pieces. A coffee ring partially overlaps the cassette card.",

37: "A photograph of an old audio cassette tape — the cassette itself photographed lying flat, the tape reels visible through the clear window, a white label with typed text. Taped to the page with two strips of yellowing tape. Cobalt blue annotation beside it: 'Katarina — approx. 80 yrs — 1974 — 3rd generation memory.' Red arrow pointing to the label area. The cassette label shows faint typed text.",

38: "A pencil sketch drawn directly on the journal page showing a wide open sky — horizon line low, large expanse of sky above, a single small figure standing in a field below, head tilted back, looking up. The sky is rendered with very light pencil strokes — not clouds, a quality of light. Cobalt blue annotation: 'Clean in a way it hadn't been before — a character the sky hadn't previously had.' Red underline.",

39: "A small handwritten index card — aged cream stock, cobalt blue ink in a precise careful hand — a single sentence covering the card, taped flat to the page with transparent tape. Beside it, a second smaller card in different handwriting beneath the first. Cobalt blue marginal annotation: 'Said once — precision of recording what cannot be accounted for.' Red marker underlines one word on the first card.",

40: "A printed form fragment — institutional header visible at top, columns of printed fields — taped to the lower half of the page. The form has handwritten entries in black ink filling certain fields. Cobalt blue annotation beside it: 'Austrian Imperial Meteorological Institute — Gospic station — standard.' Red paper clip at the top corner. An emerald green circle around the date column.",

41: "A torn margin strip from a ledger page — pale yellow ruled paper, printed columns, a neat row of numbers in black ink — taped to the page. In the margin of the strip, handwriting in a different pen and hand, cobalt blue ink, pressed harder. Red marker circles the marginal note. Cobalt annotation: 'Different hand — different pen — anomalous.' Emerald green arrow pointing from the main column to the marginal note.",

42: "A dense page with three evidence items arranged in a triangle: upper left — a map fragment; upper right — a pamphlet clipping; bottom center — a form fragment. Red string connects all three. In the center between them, cobalt blue ink handwriting: 'None knew what the others saw.' Red marker circles the connecting node point. Margins filled with cobalt annotations and question marks.",

43: "A pencil sketch filling the journal page showing three separate instrument faces — compass, barometer, thermometer — arranged in a row, all slightly tilted as if laid on a table. Each has cobalt blue annotation in small script beside it. Red arrows pointing to the needle of each instrument, which all deflect in the same direction. Emerald green lines connecting all three needles.",

44: "A printed book page fragment — small serif type, two columns — taped to the center of the page. The fragment shows a timeline entry. Cobalt blue annotation around it: 'The standard shape — every fact accurate — also insufficient.' Red marker strikes a diagonal line through the biography text. A pen circle in red around the word 'insufficient' written in cobalt in the margin.",

45: "A faded black-and-white photograph taped at an angle showing the New York City harbor — ships, water, distant skyline — the image slightly aged and silvery. Cobalt blue annotation below: 'Port of New York — June 6 1884 — four cents.' Red arrow pointing toward the gangway of the nearest ship. A small torn corner of the photograph is held down with a separate strip of tape.",

46: "A mechanical engineering blueprint fragment — torn, thin translucent paper, blue ink lines showing a turbine cross-section — taped to the page. The technical drawing is detailed. Cobalt blue annotation beside it: 'Running complete functional machines in his mind — not designs — running.' Red marker circles the turbine's central shaft. An emerald green annotation traces one component with a question mark.",

47: "A handwritten quotation on a torn strip of cream paper — a single sentence in cobalt blue ink, the handwriting careful and deliberate — taped to the upper center of the page. Below it, cobalt blue annotation: 'My Inventions — 1919 — exact and verifiable.' Red underline beneath the word 'absolutely' in the quotation strip. A small red marker arrow points from the annotation to the strip.",

48: "Dense annotation page. Cobalt blue handwriting covers the full page in tight rows, the pressure varying — some words almost carved into the paper. In the bottom right corner, a small red question mark and a cobalt blue sketch of a gear, two cogs meshed. Emerald green arrows radiate from the gear outward. A coffee ring overlaps the upper left quadrant.",

49: "A faded Polaroid photograph taped to the page showing a small boy's shoes — leather, slightly scuffed, toes pointing toward the camera — on a wooden floor. The shoes are too small to belong to the adult who wore them in the room. Cobalt blue annotation below: 'The structures of perception — in place before he had language for them.' Red arrow pointing at the worn toe of the left shoe.",

50: "A pencil sketch on the journal page showing a child's hand — small fingers, detailed palm lines — resting flat on a flat surface. Around the hand, radiating pencil lines suggest energy or attention flowing from the point of contact outward. Cobalt blue annotation: 'Not a gift — a condition — carrying something.' Red arrows along the radiating lines. Emerald green circle drawn around the point of palm contact.",

51: "A physical object: a tuft of cat fur — gray-brown — pinned to a small white backing card with a red ink catalog label beneath: 'Specimen — domestic feline — Smiljan.' The card is taped to the page. Beside it, cobalt blue annotation in small careful script. Red marker circle around the catalog label. The fur is slightly matted, pinned flat with a single brass pin.",

52: "A dark room sketch drawn on the journal page — minimal pencil marks suggest walls, floor, a window outline letting in almost no light. In the center, two small shapes: a child seated, a larger cat form beside it. The sketch is done with very little line — mostly suggested by what isn't drawn. Cobalt blue annotation: 'Grain of fur against palms — body warmth rising through it.' Red circle at the contact point.",

53: "A pencil and cobalt blue ink sketch on the journal page showing a cat's back — fur rendered in careful parallel strokes — with spark lines radiating across the entire dorsal surface, edge to edge, in blue ink. The sparks are drawn with precision: short arcs, evenly distributed, continuous. Red annotation: 'Sheet — not one discharge — continuous.' Cobalt blue: 'Blue-white and absolute.' A foxing spot at upper right.",

54: "Dense annotation page. The entire page covered in cobalt blue handwriting that gradually increases in density from top to bottom, words pressing closer together near the bottom margin. In the center, a pencil sketch of two hands — small, child-sized — fingers spread, rendered in faint lines as if lit from beneath. Red marker circles the space between the fingers. Emerald green hatching fills the palm area.",

55: "A physical object: a single white feather — slightly curved, with a pale gray tip — pinned flat to a white backing card with a red label. The card is taped to the page. Beside it, cobalt blue annotation: 'After-image — own fingers lit from beneath.' Red arrow pointing to the gray tip. A pencil sketch beside the feather shows a child's hand in silhouette, finger bones suggested by thin lines.",

56: "A faded black-and-white photograph taped to the page showing a bearded man in a clerical collar — strong jaw, direct gaze, a book partially visible in his hands. Cobalt blue annotation beside him: 'Milutin Tesla — Serbian Orthodox — man of logic and scripture.' Red underline under 'logic and scripture.' A small emerald green asterisk in the upper margin.",

57: "A physical object: a thin tin fork — the actual utensil or a close photograph of one — taped flat to the page. It is plain, slightly bent, its tines slightly spread. Beside it, cobalt blue annotation: 'Tin — heavy for a child — body warm within 60 seconds.' Red marker traces the fork's outline. An emerald green arrow points from the fork toward the center of the page.",

58: "A sketch on the journal page showing a dining table from above — plates, cups, seated figures as simple outlines — and one chair at the table's corner that is empty, the figure at it absent, an empty space in the sketch. Cobalt blue annotation: 'Then the table gone — the room gone — holding nothing.' Red marker fills the empty chair outline. Emerald green lines radiate from the empty seat outward.",

59: "A Polaroid photograph taped at a sharp angle showing a stone wall exterior in afternoon light — the light is low and amber-toned, the texture of the stone very specific and three-dimensional. The wall is not any identifiable place. Cobalt blue annotation below: 'Exact texture — quality of afternoon light — geometry he had no business knowing.' Red circle around the most detailed section of stonework.",

60: "Dense annotation page covered in cobalt blue handwriting in two styles — one careful and measured in the upper half, one faster and looser in the lower half, as if two states of mind. In the center of the page, a horizontal red line separates them. Emerald green circles around three individual words in the lower section. A water stain at the lower right corner.",

61: "A sketch directly on the journal page showing a fork being held by a small hand — the grip is uncertain, the fork slightly tilted — and beside it, the same fork in the same hand but the hand is now transparent, suggested only by outline, and the dining room behind it has been replaced with white space. Cobalt blue annotation beside the second image: 'Total — visual field replaced — involuntary.' Red underline.",

62: "A faded Polaroid taped at a slight angle showing a dining room interior — table set, chairs, a window with light coming through. The image is slightly blurred, as if taken quickly, or as if the room itself was slightly unstable. Cobalt blue annotation: 'More real than the dinner table.' Red arrows pointing to the blurred edges. Emerald green annotation tracing the window light.",

63: "A physical object: a small brass key — old, simple design — taped flat to the page beside a short printed excerpt from a book, the book page cut and taped. The excerpt is three lines, centered. Cobalt blue annotation beside the key: 'Documented — memoir — matter-of-fact precision of a technical specification.' Red marker circle around the key's bow.",

64: "A torn page from a printed book — small serif type, one column, slightly yellowed — taped to the upper center. Several lines are underlined in red marker. Cobalt blue annotations fill the margin beside the passage. Red paper clip at the corner. A coffee ring overlaps the lower portion of the book fragment.",

65: "A pencil sketch on the journal page showing a human figure — adult, seen from the side — with an overlay of dashed lines suggesting a different space imposed over the figure's visual field: a different room, different walls, a different geometry of light. The two spaces overlap at the figure's eyes. Cobalt blue annotation: 'Could not turn it off — no more than the sound of his own name.' Red underline.",

66: "Dense annotation page. Cobalt blue handwriting in careful measured rows — the handwriting of someone transcribing something important — covering most of the page. In the lower left, a small pencil sketch of a woman's face in profile, expression attentive and slightly withdrawn, as if watching. Red marker underlines a phrase in the upper half. Emerald green arrow pointing from the sketch to the phrase.",

67: "A physical object: a plain tin fork — photographed or taped flat — beside a woman's hand in a separate sketch, drawn in pencil, the hand hovering near the fork, not touching it, expression of the hand watchful. Cobalt blue annotation: 'Her expression — not alarmed, not unalarmed — watching for it.' Red arrow from the hand sketch to the fork. An emerald green bracket around the space between them.",

68: "A handwritten note on a small index card — aged cream stock — taped flat, a single sentence in cobalt blue ink, the writing very deliberate, each word placed with care. Below it, a smaller note in the same hand: 'She had decided not to say anything — monitoring something she cannot explain and cannot stop.' Red underline beneath 'monitoring.' Brass pushpin at one corner.",

69: "Dense annotation page. The page has two zones: upper half covered in cobalt blue handwriting discussing counting behavior; lower half has a pencil sketch showing a row of objects — cups, books, shoes — arranged in groups of three, clearly organized. Red circles around each group of three. Cobalt blue: 'Not a phase — not a preference — a need.' Emerald green connecting arrows between groups.",

70: "A printed book cover fragment — just the title area — cut and taped: dark binding, gold-embossed type, slightly worn. Beside it, cobalt blue annotation: 'Carlson — Princeton 2013 — consistent from childhood through old age.' Red underline under the word 'consistent.' A small emerald green arrow pointing from the book fragment toward a pencil sketch of a counting sequence beside it.",

71: "A pencil sketch on the journal page showing a child at a dinner table seen from slightly above — the child's gaze aimed not at the table but at something in the middle distance, expression concentrating. Around the child's head, very faint pencil lines suggest a different environment overlaid — barely there, almost erasure. Cobalt blue annotation: 'The visible world — attempt to match what episodes were already showing.' Red arrow.",

72: "Dense annotation page. Cobalt blue handwriting filling two-thirds of the page, the ink slightly varied in tone suggesting the writing was done over multiple sessions. In the bottom third, a pencil sketch of a timeline — horizontal line, two points marked with cobalt blue circles, an arrow extending rightward beyond the page edge. Red marker fills both circle points. Emerald green annotation between them.",

73: "A physical object: a small boy's leather shoe — worn, the toe slightly scuffed, the sole edge cracked — taped flat to the page. Beside it, a man's dress shoe also taped flat, much larger. Cobalt blue annotation between them: 'Dane Tesla — before and after — horse accident — biographies disagree on year.' Red marker draws a line between the two shoes. A foxing spot at the upper corner.",

74: "A faded Polaroid taped at an angle showing a wooden coat hook on a plaster wall — a single coat hanging on it, the coat slightly heavy, slightly wrong in the way it hangs, as if the person who shaped it is no longer coming back. Cobalt blue annotation below: 'Hanging slightly differently — when the person who will take it down is no longer coming.' Red arrow pointing to the empty space below the coat's hem.",

75: "A pencil sketch on the journal page showing a pair of leather shoes seen from slightly above — placed side by side, slightly asymmetric, the right heel more worn than the left. The shoes are empty. Around them, cobalt blue annotation in careful script, the writing circling the shoes: 'Shoes learn their wearer — these had learned theirs — the body was not coming back.' Red marker traces the asymmetric wear.",

76: "Dense annotation page. The page is almost entirely covered in cobalt blue handwriting, but the text is arranged around a large empty rectangle left blank in the center of the page — a deliberate negative space. Red marker traces the border of the empty rectangle. Cobalt blue annotation at the border: 'Presence of an absence — every room the wrong size.' Emerald green hatching in two corners.",

77: "A faded Polaroid taped at a slight angle showing a child's bedroom — narrow bed, single window, a chair, objects on a shelf — everything slightly too still. The room is empty of people. Cobalt blue annotation below: 'After Dane died — visions intensified — not produced by grief — preceded grief.' Red circle around the empty chair. Emerald green arrow pointing toward the window.",

78: "Dense annotation page. Cobalt blue handwriting in two columns — left column in careful measured script, right column faster and looser. In the upper center, a small rough pencil sketch of an open door — light pouring through it, wide. Red marker underlines a phrase in the left column. Cobalt blue: 'Grief opened a larger passage.' Emerald green circle around the door sketch.",

79: "A dense page with multiple evidence items: a small photograph of a Niagara Falls postcard taped upper left; a torn newspaper clipping taped lower right; a rough pencil sketch of a transmission tower in the center; and a printed timeline fragment at the bottom. Red string connects all four. Margins filled with cobalt blue notes. Red marker circles the transmission tower sketch. The page has a tea stain at the lower left.",

80: "A blueprint fragment — thin translucent drafting paper, blue ink lines showing a simplified Niagara turbine plan — taped at an angle. Several lines struck through in red marker. Cobalt blue annotation: 'Patents torn up — far less than value — traditional account says voluntarily.' Red marker X through the royalty clause section of the blueprint.",

81: "A technical sketch on the journal page showing a tall wireless tower — Wardenclyffe proportions — with transmission lines radiating downward through the ground, not upward through the air. The ground lines are emphasized in cobalt blue. Annotation: 'Through the earth itself — not through air.' Red arrow pointing downward through the ground section. Emerald green marks the earth layer.",

82: "A physical object: a crumpled receipt or promissory note — pale yellow paper, faint printed lines — taped flat, heavily annotated in cobalt blue around its edges. The central figures on the document are circled in red. Cobalt blue annotation: 'JP Morgan — refused — tower stopped — scrap did not cover the debt.' Red underline beneath a number visible on the document.",

83: "A faded Polaroid taped at a slight angle showing a hotel room interior — a single bed, a window with a view of city lights at night, a writing desk with papers on it. The room is sparse and lived-in rather than appointed. Cobalt blue annotation below: 'Hotel New Yorker — 77 years old — the century he had powered was not paying him back.' Red circle around the writing desk.",

84: "Dense annotation page. Cobalt blue handwriting covers the page with increasing density from top to bottom. In the lower third, a rough pencil sketch of a window frame — open, a cold empty rectangle — with fine lines suggesting wind or air movement through it. Red underline on a phrase in the upper section. Cobalt blue: '86 years looking — coded way a being looks for its kind.' Emerald green around the window sketch.",

85: "A faded Polaroid taped at a slight angle showing a hotel window — open, curtains slightly moving, city skyline visible beyond, winter light. The window is open despite the cold. Cobalt blue annotation below: 'Open in January — not by accident — he left it open because she might come.' Red arrow pointing through the open window toward the sky. A foxing spot near the lower corner.",

86: "A physical object: a fragment of a hotel napkin — white, slightly yellowed, printed border visible — with dense pencil and pen mathematical notation covering every available surface. The equations run to the edge. Taped flat. Cobalt blue annotation: 'Still doing work — active thought — map of a continent on a grain of rice.' Red marker traces the edge of the notation area.",

87: "A faded black-and-white photograph paper-clipped to the page showing a white pigeon standing on a window ledge — the bird's posture upright, slightly turned to face the camera, light gray wing-tips visible. Below, cobalt blue annotation: 'White — pure white — light gray tips — made a habit of his window.' Red arrow pointing to the wing tips. A small emerald green circle around the bird's eye.",

88: "A pencil sketch on the journal page showing a close-up of two eyes — human on the left, bird on the right — both drawn with careful iris detail. A horizontal cobalt blue line connects the two gazes. Annotation: 'The specific word he used: recognition.' Red circle around the iris of the bird's eye. Emerald green traces the line connecting the two gazes.",

89: "Dense annotation page. The handwriting fills the entire page but slows near the bottom — the letters becoming larger, more deliberate. In the center, a single phrase is written in slightly larger cobalt blue script, then underlined twice in red marker. The page shows a tea stain in the upper right and a foxing spot near the left margin. No sketch — only the weight of the writing itself.",

90: "A physical object: three small gray-tipped feathers pinned to a white backing card — arranged in a fan shape, their quills touching at the center pin point. A red ink catalog label: 'Hotel St. Regis — date est. 1939.' The card is taped to the page. Cobalt blue annotation: 'She died — he was holding her — weight of a bird — lighter than they appear.' Red circle around the catalog label.",

91: "A pencil sketch on the journal page showing two open hands, palms up, in close-up — the fingers slightly curved in the posture of holding something small. Between the hands, the space is empty but the sketch has an intensity around the empty space — fine pencil lines radiating from the absence. Cobalt blue annotation: 'The weight of a bird — and then, in the moment before she died — the light.' Red marker fills the empty center.",

92: "A torn page from a printed biography — small serif type, slightly yellowed — taped to the upper half of the page. Two sentences are circled in red marker. Cobalt blue annotation fills the margin beside the circled sentences: 'O'Neill recording — yes it was a real light — dazzling blinding — do NOT convert to metaphor.' Red underline beneath 'do not convert to metaphor' written in the margin.",

93: "Dense annotation page. Cobalt blue handwriting at maximum density — the page almost entirely blue with ink. In the center, a rough pencil sketch of a room interior with a single bright point of light at the center — all pencil lines radiating away from it, the room organized around that central point of light. Red marker traces the outermost ring of radiating lines. Emerald green fills the light source point.",

94: "A physical object: a single white feather — pale, nearly weightless — pinned flat to a white card. The card has a red ink label. Beside it, a torn strip with a printed quotation taped flat, the text barely visible. Cobalt blue annotation: 'Something went out of my life — his words — chosen carefully by a precise man.' Red underline beneath the printed text strip. A coffee ring overlaps one corner of the card.",

95: "A pencil sketch on the journal page showing a hand holding a feather — the grip gentle, the feather lying across the palm. Beside it, the same hand drawn empty — the feather gone, the hand now slightly different in posture, carrying the absence. Cobalt blue annotation between the two sketches: 'What was held is now carried.' Red marker dividing line between the two sketches. Emerald green connecting arrow.",

96: "A newspaper clipping — aged, gray newsprint, headline type visible — taped to the upper portion of the page. The headline and first paragraph are circled in red. Cobalt blue annotation beside the clipping: 'January 7 1943 — fact the standard biography mentions and then moves past.' Red underline beneath one line of the clipping text. A foxing spot overlaps the lower corner of the clipping.",

97: "A physical object: a government form — pale cream institutional paper, printed header 'Office of Alien Property Custodian' visible in small type — taped flat. Several fields circled in red marker. Cobalt blue annotation: 'Trading with the Enemy Act — not designed for Tesla — American citizen 52 years.' Red arrow pointing to the citizenship-related field area. An emerald green circle around the agency header.",

98: "A faded black-and-white photograph paper-clipped to the page showing a row of wooden packing crates and trunks in a storage room — stacked, labeled, a dim overhead light casting shadows between them. The quantity is striking. Cobalt blue annotation below: 'Approximately 80 trunks — 6 decades of work.' Red arrows pointing to three separate crates. A foxing spot at the upper left.",

99: "A physical object: a small academic identity card or faculty card — printed form, typed name, institutional affiliation — taped flat. Beside it, a torn newspaper clipping with a name circled in red. Cobalt blue annotation: 'John G. Trump — MIT — NDRC — three days — to review what 60 years produced.' Red underline beneath 'three days.' Emerald green circle around the institutional affiliation on the card.",

100: "A densely packed page with multiple items: a government document fragment upper left, a short printed excerpt lower right, a rubber stamp impression in red ink ('CLASSIFIED') in the center. Red string connecting the document to the excerpt. Cobalt blue annotation: 'Harmless things do not require crates — do not get classified.' Red marker underlines the stamp. Emerald green brackets around the 'harmless' annotation.",

101: "Dense annotation page. Cobalt blue handwriting fills the page in careful rows, but every other line has been struck through with a single red marker line — the kind of crossing-out that means revision, not erasure. In the lower quarter, the strike-throughs stop and the handwriting is clean. Red marker underlines the clean section. Cobalt blue annotation in margin: 'The institutional story is clean — well documented — exhale.'",

102: "A pencil sketch on the journal page showing a timeline — horizontal line with dates marked — but at one point the line branches into two parallel lines that continue separately. One branch is labeled in cobalt blue, the other in red. The two lines do not rejoin. Emerald green annotation at the branch point. Cobalt blue: 'Consider this.' Red underline.",

103: "A physical object: a printed index card — typed text, archival quality — taped flat. The card has a handwritten annotation in cobalt blue ink in the margin. Beside it, a second card with a different piece of typed information. Red string connecting the two cards. Cobalt blue: 'Reports cluster — middle of 20th century — not 2008 — not CERN.' Red circle at the connection point.",

104: "A Polaroid photograph taped at an angle showing a suburban street in late afternoon light — the light is warm and amber-toned, slightly hazy, coating the surfaces. Cobalt blue annotation: 'Yellow — warmth — amber-toned — coating quality — light that settles rather than discloses.' Red arrow pointing toward the sky area. A foxing spot in the lower left corner.",

105: "A Polaroid photograph taped beside the first showing the same type of street scene — but the light is different: white, sharp, clinical, more like a lamp than a star. The surfaces look disclosed rather than coated. Cobalt blue annotation: 'Clinical — white — more like a lamp than a star.' Red arrows comparing both photos. Emerald green bracket connecting the two Polaroids.",

106: "Dense annotation page. Cobalt blue handwriting covers the full page but the ink color shifts slightly partway through — same hand, different pen, as if resumed at a different time. In the center, a rough pencil sketch of a sun circle with two versions: one with warm radiating lines, one with sharper, straighter lines. Red marker divides them. Cobalt blue: 'Independent — across languages — not shared false memory.'",

107: "A pencil sketch on the journal page showing two parallel timeline lines — one labeled 'birth' at the left with a date circle, one labeled 'shift' at the right with an arrow. The distance between them is annotated in cobalt blue. Red marker fills the birth date circle. Emerald green annotation: 'The beginning of the shift does not point at a facility — it points at a birth.' Red underline.",

108: "Dense annotation page. Cobalt blue handwriting in tight careful rows filling the entire page. At the bottom margin, three large cobalt blue question marks drawn carefully — the kind someone writes when they have organized everything they know and it still doesn't answer the question. Red underline beneath the phrase above the question marks. Emerald green circles around the question marks.",

109: "A pencil sketch on the journal page showing a human infant — rendered simply, curled, newborn — with a surrounding field of faint geometric lines extending beyond the body, as if the infant is the center of a larger structure that arrived with it. The geometric lines are precise and non-biological. Cobalt blue annotation: 'What arrived when Tesla arrived — what the birth admitted.' Red arrows tracing the outermost geometric lines.",

110: "A page covered in cobalt blue annotations radiating from a central pencil sketch of an AC motor — technical cross-section, clearly drawn — with multiple arrows pointing outward toward marginal notes. The notes use words like 'transmission' and 'signal' rather than 'invention.' Red marker circles the central rotor. Emerald green lines trace the radiating annotation paths.",

111: "A pencil sketch on the journal page showing a transmission tower on a landscape — but the signals it emits are drawn downward through the earth, not upward through the air. The downward lines continue off the page edge. Cobalt blue annotation: 'Not signals to known recipient — carrying information from source the sender cannot fully access.' Red arrows point downward. Emerald green traces the earth layer.",

112: "A faded Polaroid taped at a slight angle showing a hotel room window from inside — curtains slightly open, winter city visible outside, the glass slightly fogged. In the foreground, out of focus, a shape on the windowsill suggesting something light was there and is no longer. Cobalt blue annotation: 'When the pigeon died — the transmission ended — not the work — the destination.' Red arrow toward the empty windowsill.",

113: "A physical object: a maintenance worker's handwritten daily log sheet — printed form with ruled lines, official header — taped flat. Several lines of handwriting visible. Cobalt blue annotation beside it: 'Walter Simmons — maintenance — Hotel New Yorker 1935-1950.' Red marker circles one line of the handwritten text. A coffee ring in the upper corner of the form.",

114: "A physical object: a typescript page — typewritten text, slightly yellowed — taped to the page. The typescript has a handwritten correction in cobalt blue ink in the margin. At the bottom, a note in cobalt blue: 'January 1943 — 33rd floor — Do Not Disturb on the door.' Red marker underlines one sentence in the typescript. Emerald green annotation beside the circled passage.",

115: "Dense annotation page. The page has two zones of handwriting separated by a horizontal red marker line. Above the line: dense cobalt blue text. Below the line: sparser cobalt blue text — a pause visible in the spacing. Red underline at the bottom: 'He smelled it. He noted it. He walked on.' Cobalt blue annotation fills the left margin. A foxing spot at the upper right.",

116: "A faded Polaroid taped at a slight angle showing a hotel corridor — the perspective long, a door in the distance visible with a white door hanger on the handle, the light at that end of the corridor slightly different in quality. Cobalt blue annotation: 'Return — January 8 1943 — six in the morning — passkey.' Red arrow pointing to the distant door. Emerald green traces the light difference.",

117: "A pencil sketch on the journal page showing a doorway from the threshold perspective — the door just opened, the room dark beyond, curtains drawn, the quality of cold and stillness suggested by the minimal pencil marks. Cobalt blue annotation: 'Smell hitting before eyes adjusted — curtains heavy — cold of a room without a living body.' Red marker traces the doorway outline.",

118: "A dense page with multiple evidence items arranged on the page: three gray-tipped feathers pinned in a triangle, a hotel napkin fragment with equation notation, a small sketch of a prone figure — all within a red marker border. Red string connecting all three. Cobalt blue annotation at each item. The page feels like a reconstruction of the room.",

119: "A torn dictionary page — small type, slightly yellowed — showing a single word entry, taped to the center of the page. The word and etymology are circled in red. Cobalt blue annotation: 'Ozone — Greek ozine — meaning to smell — coined 1840 — Schoenbein.' Red underline beneath the etymology line. An emerald green circle around the date.",

120: "A sketch on the journal page showing a molecular diagram — oxygen molecules splitting, recombining in a different configuration — drawn in pencil and cobalt blue ink with the precision of someone who has studied chemistry. Red marker circles the transformation point. Cobalt blue annotation: 'Electrical discharge splits oxygen — lightning produces it — Tesla's labs always carried the smell.'",

121: "A faded black-and-white photograph taped to the page showing the exterior of a hotel — imposing stone facade, windows in rows, a street level view. Cobalt blue annotation: 'No equipment — no power supply — 86-year-old man in declining health.' Red marker strikes through the building facade, as if crossing out an explanation. Emerald green annotation in the lower margin.",

122: "A dense page comparing two evidence columns: left column has a diagram of the Lika valley dated July 1856 with cobalt blue annotations for 'ionization anomaly' and 'examination light'; right column has a diagram of hotel room 3327 dated January 1943 with cobalt blue annotations for 'ozone smell' and 'gray feathers.' Red string connecting the matching items across both columns. Cobalt blue: 'Same atmospheric signature — birth and death.'",

123: "A pencil sketch on the journal page showing two identical door shapes side by side — one labeled in cobalt blue as 'birth' and one as 'death.' Both have the same architectural proportions, the same quality of threshold. Between them, a red horizontal equals sign. Cobalt blue annotation: 'Same event — not metaphorical — forensic.' Emerald green connecting line between the doors.",

124: "Dense annotation page. The handwriting is deliberate and measured — the kind of writing done when summarizing everything gathered. In the lower half, a single sentence is written in larger cobalt blue script, then surrounded by a red marker border. Emerald green circles three words within the bordered sentence. A coffee ring overlaps the upper margin.",

125: "A pencil sketch on the journal page showing a simple figure — a human silhouette — standing in an empty landscape, looking upward. Around the figure, very faint lines suggest a different kind of space overlapping the landscape — not threatening, but different. The figure's posture is that of someone who has spent 86 years searching. Cobalt blue annotation: 'Looking — coded way — for its kind.' Red circle around the figure's head.",

126: "A faded Polaroid taped at an angle showing the facade of the Hotel St. Regis — stone exterior, a row of windows, winter light on the building face. Cobalt blue annotation below: 'Found the pigeon — only creature in 86 years.' Red arrow pointing to one upper window. A foxing spot at the lower left of the Polaroid.",

127: "A sketch on the journal page showing two hands — an adult's hands — cupped together, palms up, holding something that is not visible. The hands are drawn with care — the weight in the posture is of something light but important. Cobalt blue annotation: 'Held the pigeon — felt the weight change — from held to carried.' Red marker traces the curved line of the cupped palms.",

128: "Dense annotation page. The page has a sketched spiral in pencil at its center — loose, hand-drawn — and the cobalt blue handwriting orbits the spiral outward, wrapping around it in decreasing density. At the spiral's center, the annotation reads simply: 'the body had not finished learning.' Red underline at the center. Emerald green traces the outermost orbit line.",

129: "A physical object: a small fragment of window glass — or a photograph of one — mounted on the page, the glass slightly fogged, slight condensation pattern at the edge. Beside it, cobalt blue annotation: 'Left the window open — because the body had not finished learning what the mind already knew.' Red arrow from the glass toward the open space beside it. A brass pushpin holds the mount.",

130: "A pencil sketch on the journal page showing a stylized door outline — not a hotel door, more archetypal — with fine lines radiating outward from the doorway in all directions, suggesting something passing through it. The lines continue past the page edges. Cobalt blue annotation: 'Departed — through the same kind of door it arrived through.' Red marker traces the doorway outline. Emerald green fills the interior of the door shape.",

131: "Dense annotation page. The handwriting slows and becomes more careful near the bottom — the letters larger, the spacing wider, as if the writer is arriving at something. The final lines are written in a slightly different, more deliberate hand. Red underline at the very bottom line. Cobalt blue annotation in the margin: 'The door smelled like lightning for three days.' An emerald green circle at the end.",

132: "A pencil sketch on the journal page showing a stylized storm cloud over a landscape — inside the cloud, a small geometric shape that does not belong in clouds, angular and precise, as if something is arriving through the storm. Below the landscape, a faint outline of the same geometric shape. Cobalt blue annotation: 'Arrived from between the darkness and the light.' Red arrows pointing to both shapes. Emerald green connecting line.",

133: "Dense annotation page. The cobalt blue handwriting is large and spaced — the kind of writing that happens when questions are being asked rather than answered. Three distinct question-shaped sentences visible by their punctuation and spacing, each on its own line with white space above and below. Red marker underlines the middle question. Emerald green circles the last word of the page.",

134: "A Polaroid photograph taped at a slight angle showing a crowd street scene — people walking, ordinary urban life — taken perhaps in the 1960s based on the clothing. The people are looking in different directions, none at each other. Cobalt blue annotation below: 'Time is different — memories are different — food tastes different.' Red arrows pointing at three separate figures in the crowd.",

135: "Dense annotation page with a comparison grid drawn in pencil — two columns, multiple rows — listing observable differences in cobalt blue ink. The grid is organized like scientific field notes. Red marker fills three cells in the right column. Emerald green draws a diagonal across the full grid. Cobalt blue annotation in the margin: 'The sun and sky are not the same — here is the documentation.'",

136: "A dense page with multiple evidence items: a faded Polaroid of a yellow-toned sunrise taped upper left; a faded Polaroid of a white-toned sky taped upper right; a newspaper clipping lower center; printed text annotations in cobalt blue filling the spaces between. Red string connecting the two Polaroids. Cobalt blue: 'You may not remember Nikola Tesla existed at all.' Red underline at the bottom.",

137: "A pencil sketch on the journal page showing a large question mark drawn carefully in the center of the page — the curve precise, the dot below it a filled circle. Around the question mark, cobalt blue annotations spiral outward: partial sentences, fragments, the words 'abilities,' 'suppressed,' 'stolen,' 'claimed.' Red marker traces the outer edge of the question mark. Emerald green fills the dot.",

138: "A dense page with multiple evidence items packed closely: a blueprint fragment of an electrical motor, a newspaper photograph of a wireless transmission tower, a short printed text block about free energy, and a hand-drawn diagram of a radio wave. Red string connecting all four. Cobalt blue annotations fill every margin. The page has a coffee ring and a water stain. Red marker underlines a single phrase: 'so much more.'",

139: "A final page — the paper slightly different, heavier, as if it is a different document altogether. A single large question written in cobalt blue ink covers the full page, the letters large and deliberate, each word on its own line. Red marker underlines the final word. The page is otherwise clear — no annotations, no clutter. Just the question. A single foxing spot at the upper right corner."
}

output = []
for i, e in enumerate(entries):
    page_num = e.get('page', i+1)
    p = PROMPTS.get(page_num)
    if p:
        full_prompt = ANCHOR + p
    else:
        full_prompt = ANCHOR + f"Dense handwritten notes in cobalt blue ink covering the page, annotations, red underlines, emerald green arrows. Coffee ring stain at corner."

    new_entry = dict(e)
    new_entry['prompt'] = full_prompt
    # Keep brief as well for reference
    output.append(new_entry)

print(f"Built {len(output)} entries")
print(f"Sample prompt length for page 1: {len(output[0]['prompt'])} chars")
print(f"Sample prompt length for page 50: {len(output[49]['prompt'])} chars")
print(f"Longest prompt: {max(len(x['prompt']) for x in output)} chars")

# Write output
with open(dst, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Written to: {dst}")
