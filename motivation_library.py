"""Student-safe Motivation & Study Help library for Classes 11-12 JEE/NEET/Boards."""

SUBJECTS = ["Physics", "Chemistry", "Maths", "Biology", "Botany", "Zoology", "English", "Sanskrit"]
CONTEXTS = [
    "JEE preparation", "NEET preparation", "board exam preparation", "hostel life", "day-scholar routine",
    "coaching homework", "school and coaching balance", "revision time", "mock-test preparation", "daily study routine"
]
TOPICS = [
    "motivation and procrastination", "concentration", "time management", "sleep and waking up",
    "phone and social-media distractions", "reading and learning speed", "notes", "memory and recall",
    "revision", "backlog", "test preparation", "test analysis", "low marks", "exam confidence",
    "goals and progress", "discipline and habits", "weak subjects", "strong subjects", "doubt clearing",
    "question practice", "mock tests", "study breaks and energy", "family expectations", "friend comparison",
    "JEE and boards together", "NEET and boards together", "hostel study routine", "day-scholar study routine",
    "Physics numericals", "Chemistry Physical", "Chemistry Organic", "Chemistry Inorganic", "Maths problem solving",
    "Biology NCERT", "Botany diagrams and terms", "Zoology concepts", "English grammar and writing",
    "English reading and vocabulary", "Sanskrit grammar and translation", "Sanskrit vocabulary", "exam-day strategy"
]
FORMS = [
    "How can I improve {topic} for {context}?", "What should I do if I struggle with {topic} during {context}?",
    "How can I manage {topic} when I have school and coaching?", "How can I handle {topic} when I am staying in a hostel?",
    "How can I handle {topic} as a day scholar?", "How can I make a simple daily plan for {topic}?",
    "How can I stop wasting time on {topic}?", "How can I become consistent with {topic}?",
    "What is a practical way to practise {topic} every day?", "How can I improve {topic} before my next test?",
    "How can I improve {topic} without studying late every night?", "What should I do when {topic} feels difficult?",
    "How can I track my progress in {topic}?", "How can I balance {topic} with other subjects?",
    "How can I recover if I have fallen behind in {topic}?", "How can I avoid common mistakes in {topic}?",
    "How can I use my test results to improve {topic}?", "How can I make {topic} easier to revise?",
    "What can I do today to make progress in {topic}?", "How can I stay calm and practical while working on {topic}?"
]


def build_questions():
    out, seen = [], set()
    for topic in TOPICS:
        for context in CONTEXTS:
            q = FORMS[len(out) % len(FORMS)].format(topic=topic, context=context)
            if q.lower() not in seen:
                seen.add(q.lower())
                out.append({"Category": topic.title(), "Question": q, "Keywords": f"{topic} {context}"})
            if len(out) >= 800:
                return out
    return out

MOTIVATION = build_questions()


def _context_bits(q):
    bits = []
    if "hostel" in q:
        bits.append("Hostel plan: use a library/quiet room for one protected block, keep essentials ready before the block, and agree on quiet time with roommates.")
    elif "day scholar" in q or "day-scholar" in q:
        bits.append("Day-scholar plan: include travel and home duties in the timetable and protect one fixed study block after reaching home.")
    elif "school" in q or "coaching" in q:
        bits.append("School/coaching plan: finish urgent classwork first, then reserve a short daily block for revision and backlog instead of mixing everything together.")
    if any(x in q for x in ("jee", "neet", "board", "exam", "test")):
        bits.append("Exam rule: keep current lessons moving, practise timed questions regularly, and use mistakes to decide what to revise next.")
    return bits


def practical_advice(question):
    """Generate a different, practical, bullet-based answer of about 150-200 words."""
    q = question.lower()
    topic = next((t for t in TOPICS if t.lower() in q), "study routine")
    subject = next((s for s in SUBJECTS if s.lower() in q), None)

    # Topic-specific plans. The selected plan plus the question form/context makes answers meaningfully different.
    plans = {
        "motivation and procrastination": [
            "Start with a 10-minute task instead of waiting to feel motivated.",
            "Write one measurable target: 5 questions, 2 pages, or one worked example.",
            "Keep the phone away until the block ends.",
            "After finishing, mark the task complete and choose the next small task."
        ],
        "concentration": [
            "Choose one subject and one chapter before starting.",
            "Study for 25-40 minutes without switching apps or subjects.",
            "Keep a scrap page for distracting thoughts and return to the question.",
            "Take a 5-10 minute planned break, then restart with the next target."
        ],
        "time management": [
            "List today's fixed commitments first: school, coaching, meals and travel.",
            "Place the hardest subject in your best available energy period.",
            "Use short blocks for revision and longer blocks for problem solving.",
            "Leave a small buffer so one delayed task does not destroy the whole plan."
        ],
        "sleep and waking up": [
            "Set a consistent bedtime and wake time instead of changing it every day.",
            "Pack books and clothes before sleeping so the morning has fewer decisions.",
            "Keep the phone away from the bed when possible.",
            "Do a simple first task after waking: formula recall, NCERT reading, or five questions."
        ],
        "phone and social-media distractions": [
            "Put the phone outside arm's reach during focused study.",
            "Turn off non-essential notifications and remove distracting shortcuts.",
            "Use the phone only during planned breaks or for the required lecture/test.",
            "If you repeatedly check it, write the urge down and continue for five more minutes."
        ],
        "reading and learning speed": [
            "Preview headings and questions before reading a chapter.",
            "Read for meaning rather than trying to pronounce every word slowly.",
            "After a page, close the book and say the main idea from memory.",
            "Increase speed only after understanding becomes reliable."
        ],
        "notes": [
            "Do not copy the entire textbook or lecture.",
            "Write definitions, formulas, key exceptions, diagrams and mistakes in your own words.",
            "Keep one small revision page for each chapter.",
            "Review the page after solving questions and add only genuinely useful points."
        ],
        "memory and recall": [
            "Close the book and recall the concept before checking the answer.",
            "Use short self-tests for formulas, definitions, reactions, diagrams or vocabulary.",
            "Repeat difficult items after one day, three days and about a week.",
            "Explain one concept aloud as if teaching a friend."
        ],
        "revision": [
            "Use active recall instead of reading the same page repeatedly.",
            "Mark chapters as strong, medium or weak.",
            "Revise weak topics first with a small set of questions.",
            "End each revision block with a quick self-test."
        ],
        "backlog": [
            "Make one list of pending chapters and mark the prerequisite chapters.",
            "Choose only one backlog target per day while continuing current classes.",
            "Start with high-value or prerequisite topics rather than the easiest topic.",
            "Do not sacrifice every sleep hour to clear the backlog."
        ],
        "test preparation": [
            "Check the syllabus and divide it into completed, partly completed and untouched topics.",
            "Solve timed questions before the test instead of only rereading notes.",
            "Keep the last revision focused on formulas, reactions, diagrams and common errors.",
            "Prepare your stationery, admit-card requirements and sleep schedule in advance."
        ],
        "test analysis": [
            "Separate mistakes into concept, calculation, reading, time and guessing errors.",
            "Write the exact reason beside every important wrong answer.",
            "Choose the two largest error types for the next practice session.",
            "Redo selected wrong questions without looking at the solution."
        ],
        "low marks": [
            "Do not judge the whole subject from one score.",
            "Compare attempted, correct, incorrect and unattempted questions.",
            "Find the three chapters producing the most lost marks.",
            "Make the next week's practice directly target those gaps."
        ],
        "exam confidence": [
            "Build confidence from completed tasks rather than predictions about the result.",
            "Take short timed tests and record what improved.",
            "Prepare a one-page last-minute revision sheet for each major subject.",
            "Avoid comparing your daily progress with another student's timetable."
        ],
        "goals and progress": [
            "Set a weekly target that can be measured.",
            "Track chapters completed, questions solved and tests analysed.",
            "Review the numbers once a week and change the plan based on evidence.",
            "Keep the next target small enough that you can start immediately."
        ],
        "discipline and habits": [
            "Attach study to a fixed time or event each day.",
            "Prepare the desk and books before the study block.",
            "Use the same starting routine every day for less decision-making.",
            "If you miss a day, restart the next block instead of abandoning the week."
        ],
        "weak subjects": [
            "Identify whether the weakness is concept knowledge, practice or exam speed.",
            "Start with prerequisite concepts instead of jumping directly to difficult problems.",
            "Solve a small set of basic questions and then increase difficulty.",
            "Keep a doubt list for the teacher rather than collecting vague doubts."
        ],
        "strong subjects": [
            "Maintain the subject with regular mixed practice instead of ignoring it.",
            "Use harder questions to improve accuracy and speed.",
            "Track careless mistakes even when the score is high.",
            "Do not spend all study time on the strongest subject."
        ],
        "doubt clearing": [
            "Write the exact step where you became confused.",
            "Try the problem once more without immediately checking the solution.",
            "Ask the teacher a specific question and note the corrected method.",
            "Redo the same type of question later without help."
        ],
        "question practice": [
            "Begin with a small set of questions from one concept.",
            "Mark questions as easy, uncertain or wrong.",
            "Analyse why uncertain questions took time.",
            "Repeat a mixed set later so the method is not dependent on question order."
        ],
        "mock tests": [
            "Take the mock under realistic timing and avoid checking answers midway.",
            "Record score, attempted questions, accuracy and time lost.",
            "Review mistakes before taking another full mock.",
            "Practise the weakest error category between two mocks."
        ],
        "study breaks and energy": [
            "Use short planned breaks instead of unplanned phone scrolling.",
            "Stand, walk, drink water and return on time.",
            "Place difficult work in your higher-energy period.",
            "If you are consistently exhausted, review sleep and workload rather than simply adding hours."
        ],
        "family expectations": [
            "Convert pressure into a specific academic target you can control.",
            "Show parents a simple weekly plan and progress record.",
            "Discuss one concrete difficulty instead of saying only that studies are stressful.",
            "Keep your daily routine based on your actual learning needs."
        ],
        "friend comparison": [
            "Compare your current score with your previous score first.",
            "Borrow useful study methods from friends without copying their entire schedule.",
            "Track your own accuracy, speed and chapter completion.",
            "Use comparison only to identify a skill you can practise."
        ],
        "JEE and boards together": [
            "Map overlapping chapters so one study block serves both goals.",
            "Use NCERT and board-style writing for board preparation.",
            "Use timed objective and numerical practice for JEE.",
            "Keep a weekly slot for board answer writing instead of leaving it to the final weeks."
        ],
        "NEET and boards together": [
            "Use NCERT as the common base for Biology and relevant Chemistry topics.",
            "Practise NEET-style MCQs after concept study.",
            "Schedule board-style written answers separately for descriptive subjects.",
            "Review diagrams, definitions and terminology regularly."
        ],
        "hostel study routine": [
            "Identify one reliable quiet place for serious study.",
            "Keep books and stationery ready before leaving the room.",
            "Agree on a simple quiet period with roommates.",
            "Use short revision tasks when the hostel environment is noisy."
        ],
        "day-scholar study routine": [
            "Build the plan around actual travel and home timings.",
            "Use travel for light recall when safe and practical, not difficult problem solving.",
            "Keep a fixed study start time after reaching home.",
            "Prepare the next day's books before sleeping."
        ],
        "Physics numericals": [
            "Write the given values and units before using a formula.",
            "Draw a small diagram when the problem involves motion, force, fields or circuits.",
            "Estimate the answer before calculating so unreasonable results are noticed.",
            "Record the reason for each wrong numerical in an error notebook."
        ],
        "Chemistry Physical": [
            "Write the known quantities and required quantity first.",
            "Check units before substitution.",
            "Keep a small formula sheet and practise one representative problem for each formula.",
            "Redo calculations where the error came from conversion or arithmetic."
        ],
        "Chemistry Organic": [
            "Organise reactions by functional group and reaction type.",
            "Learn why a reagent produces a transformation instead of memorising isolated equations.",
            "Practise conversion chains from starting material to product.",
            "Keep a reaction-error list for reagents and conditions you confuse."
        ],
        "Chemistry Inorganic": [
            "Use NCERT as the primary reading source for important facts.",
            "Create compact comparison tables for trends and exceptions.",
            "Recall facts without looking before checking the book.",
            "Revise difficult exceptions repeatedly rather than rereading the whole chapter."
        ],
        "Maths problem solving": [
            "Identify the chapter and type of problem before calculating.",
            "Write the first useful relation instead of staring at the whole question.",
            "If stuck for several minutes, mark the question and move on.",
            "After checking a solution, close it and reproduce the key steps yourself."
        ],
        "Biology NCERT": [
            "Read the NCERT paragraph carefully and mark only high-value terms.",
            "Convert important lists into short recall questions.",
            "Use diagrams and labelled structures for visual recall.",
            "Practise MCQs only after understanding the text behind the answer."
        ],
        "Botany diagrams and terms": [
            "Draw important diagrams from memory rather than tracing them.",
            "Label each structure without looking, then check spelling and position.",
            "Make a one-page comparison of similar terms.",
            "Re-draw weak diagrams after a few days."
        ],
        "Zoology concepts": [
            "Make short comparisons between groups instead of memorising isolated facts.",
            "Use tables for classification, structures and functions.",
            "Recall examples without looking at the notes.",
            "Use NCERT wording for important factual questions."
        ],
        "English grammar and writing": [
            "Keep a list of grammar errors you repeatedly make.",
            "Practise one small grammar topic each day.",
            "For writing tasks, use a fixed structure and check tense, spelling and clarity.",
            "Read a model answer and then write your own version without copying it."
        ],
        "English reading and vocabulary": [
            "Read a short passage daily and identify the main idea.",
            "Record only useful unfamiliar words with meaning and an example sentence.",
            "Use the new words in your own sentences.",
            "Review the vocabulary after a few days instead of collecting a huge list."
        ],
        "Sanskrit grammar and translation": [
            "Break the sentence into words and identify the grammatical role of each.",
            "Practise a small set of forms repeatedly.",
            "Translate short passages and compare with the correct meaning.",
            "Keep a list of recurring grammar mistakes and revise it before tests."
        ],
        "Sanskrit vocabulary": [
            "Learn a small group of words with meaning each day.",
            "Write the word, meaning and one simple usage together.",
            "Test yourself without looking at the meaning.",
            "Mix old and new words during revision."
        ],
        "exam-day strategy": [
            "Prepare stationery, required documents and travel arrangements the previous day.",
            "Avoid learning large new topics immediately before the exam.",
            "Read instructions carefully and use a time checkpoint during the paper.",
            "If one question consumes too much time, mark it and move forward."
        ],
    }

    # Pick a rotating micro-variation from the exact question so the 800 entries do not return one identical answer.
    import hashlib
    variant = int(hashlib.sha256(q.encode()).hexdigest()[:8], 16) % 4
    actions = plans.get(topic, plans["motivation and procrastination"])
    if variant == 1:
        actions = actions[1:] + actions[:1]
    elif variant == 2:
        actions = [actions[2], actions[0], actions[3], actions[1]]
    elif variant == 3:
        actions = [actions[3], actions[1], actions[0], actions[2]]

    subject_note = ""
    if subject and subject.lower() not in topic.lower():
        subject_note = f"\n- **Subject connection:** For {subject}, apply the same idea to one specific chapter this week rather than trying to change every subject at once."

    context_notes = _context_bits(q)
    context_text = "\n".join(f"- {x}" for x in context_notes)
    if context_text:
        context_text = "\n" + context_text

    # Add a question-specific first step based on the exact wording.
    if "today" in q:
        first = "Today, choose one small task related to this question and finish it before starting another task."
    elif "before my next test" in q or "test" in q:
        first = "Before the next test, use the last test's mistakes to choose the first two practice tasks."
    elif "every day" in q or "daily" in q:
        first = "For the next 7 days, repeat one small action from the list at the same time each day."
    elif "how can i" in q or "what should i" in q:
        first = "Start with the first action today; do not wait until you have designed a perfect timetable."
    else:
        first = "Choose one action from this list and practise it in your next study block."

    return (
        f"### Practical plan\n{first}\n\n"
        + "\n".join(f"- **Step {i+1}:** {a}" for i, a in enumerate(actions))
        + context_text
        + subject_note
        + "\n- **Daily check:** At the end of the block, record what you completed, one mistake or difficulty, and the first task for the next session."
        + "\n- **If it does not work:** Change one part of the method and test it for a week instead of changing the entire routine every day."
        + "\n\nThe aim is steady improvement, not a perfect study day. For JEE, NEET and board preparation, protect regular sleep and keep current lessons moving while using small targeted blocks for weak areas."
    )


def advice(question):
    return practical_advice(question)
