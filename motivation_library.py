"""Large, student-safe Motivation & Study Help library for Classes 11-12 JEE/NEET/Boards."""

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
    "What can I do today to make progress in {topic}?", "How can I stay calm and practical while working on {topic}?",
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


def practical_advice(question):
    """Return a simple, practical, student-safe bullet guide of about 150-200 words."""
    q = question.lower()
    subject = next((s for s in SUBJECTS if s.lower() in q), None)
    hostel = "hostel" in q
    day = "day scholar" in q or "day-scholar" in q
    exam = any(x in q for x in ("jee", "neet", "board", "exam", "test"))

    if any(x in q for x in ("phone", "social", "distraction")):
        title = "Control distractions"
        steps = [
            "Keep the phone outside your study reach and switch off unnecessary notifications.",
            "If you need the phone for a lecture, open only that app and close everything else.",
            "Use a fixed 10-minute phone-check window during a planned break.",
            "Study with one book or one question set open at a time."
        ]
    elif "backlog" in q or "fallen behind" in q:
        title = "Clear the backlog without panic"
        steps = [
            "Write every pending chapter on one page and mark the chapters needed for current classes.",
            "Choose one small backlog task each day—do not try to finish everything in one night.",
            "Use active questions after learning a chapter instead of only watching lectures.",
            "Continue current school/coaching work while gradually reducing the backlog."
        ]
    elif any(x in q for x in ("sleep", "waking", "hostel")):
        title = "Build a routine you can repeat"
        steps = [
            "Keep a reasonably fixed sleep and wake time instead of changing it every day.",
            "Prepare books and the first task before sleeping so starting is easy.",
            "In a hostel, use a library or quiet study area when the room is noisy.",
            "As a day scholar, protect a fixed study block after reaching home."
        ]
    elif any(x in q for x in ("marks", "test", "mock", "exam")):
        title = "Turn marks into an improvement plan"
        steps = [
            "After the test, classify each mistake: concept, calculation, reading, time or guessing.",
            "Pick the two biggest mistake types and practise those first.",
            "Redo wrong questions without looking at the solution, then compare your method.",
            "Keep an error notebook and check the same mistakes again before the next test."
        ]
    elif any(x in q for x in ("memory", "recall", "revision")):
        title = "Make revision active"
        steps = [
            "Close the book and recall formulas, definitions, diagrams or steps from memory.",
            "Check immediately and mark only the points you forgot.",
            "Revisit those points after a gap instead of rereading the whole chapter.",
            "Use short mixed question sets to check whether you can actually apply the idea."
        ]
    elif any(x in q for x in ("read", "speed", "english", "sanskrit")):
        title = "Improve reading and language practice"
        steps = [
            "Preview headings first, then read for meaning rather than trying to memorise every line.",
            "After a section, close the book and explain the main idea in your own words.",
            "For English or Sanskrit, keep a small daily vocabulary and grammar practice block.",
            "Use writing practice regularly for board-style answers."
        ]
    elif subject:
        title = f"Practise {subject} effectively"
        steps = [
            f"Choose one small {subject} concept and understand the basic idea before solving difficult questions.",
            "Solve a few basic questions first, then move to mixed JEE/NEET/board-level questions.",
            "Write down every important doubt instead of repeatedly rereading the same page.",
            "Keep an error notebook and revisit missed questions after a few days."
        ]
    elif any(x in q for x in ("motivation", "procrast", "lazy")):
        title = "Start before waiting for motivation"
        steps = [
            "Choose one task that takes about 10 minutes: five questions, one example or one page.",
            "Put the phone away, start a timer and begin immediately.",
            "After 10 minutes, continue if you can; otherwise take a short planned break.",
            "Repeat small study blocks daily—the goal is consistency, not a perfect day."
        ]
    else:
        title = "Make steady progress"
        steps = [
            "Choose one measurable target for the next study block.",
            "Work on only that task and remove obvious distractions.",
            "Take a short planned break, then start the next block.",
            "Record what you completed and choose tomorrow's first task before stopping."
        ]

    context = []
    if hostel:
        context.append("For hostel students: protect one quiet library/study-room block and tell roommates when you need uninterrupted time.")
    elif day:
        context.append("For day scholars: include travel and home responsibilities when planning your realistic study time.")
    else:
        context.append("Fit the plan around your real school, coaching, travel and family timetable rather than copying another student's routine.")
    if exam:
        context.append("For JEE/NEET/boards: keep current lessons moving, reserve a smaller block for backlog and revision, and avoid sacrificing regular sleep.")
    if subject:
        context.append(f"For {subject}: spend more time analysing wrong questions than simply counting how many questions you attempted.")

    bullets = "\n".join(f"- {x}" for x in steps)
    ending = (
        "\n\n**Simple daily check:** Write down (1) what I completed, (2) what I got wrong, and (3) the first task for tomorrow. "
        "If you miss a day, simply restart with the next planned block instead of trying to compensate with an exhausting session. "
        "Small repeated actions are more useful than waiting for a perfect mood or a perfect timetable."
    )
    return f"### {title}\n\n{bullets}\n\n" + " ".join(context) + ending


def advice(question):
    return practical_advice(question)
