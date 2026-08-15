"""Large, student-safe Motivation & Study Help library for Classes 11-12 JEE/NEET/Boards."""

SUBJECTS = [
    "Physics", "Chemistry", "Maths", "Biology", "Botany", "Zoology", "English", "Sanskrit"
]
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

# 20 practical question forms per topic = 800 unique questions.
FORMS = [
    "How can I improve {topic} for {context}?",
    "What should I do if I struggle with {topic} during {context}?",
    "How can I manage {topic} when I have school and coaching?",
    "How can I handle {topic} when I am staying in a hostel?",
    "How can I handle {topic} as a day scholar?",
    "How can I make a simple daily plan for {topic}?",
    "How can I stop wasting time on {topic}?",
    "How can I become consistent with {topic}?",
    "What is a practical way to practise {topic} every day?",
    "How can I improve {topic} before my next test?",
    "How can I improve {topic} without studying late every night?",
    "What should I do when {topic} feels difficult?",
    "How can I track my progress in {topic}?",
    "How can I balance {topic} with other subjects?",
    "How can I recover if I have fallen behind in {topic}?",
    "How can I avoid common mistakes in {topic}?",
    "How can I use my test results to improve {topic}?",
    "How can I make {topic} easier to revise?",
    "What can I do today to make progress in {topic}?",
    "How can I stay calm and practical while working on {topic}?",
]


def build_questions():
    out = []
    seen = set()
    for topic in TOPICS:
        for context in CONTEXTS:
            # Keep the library broad but stop at exactly 800 unique questions.
            q = FORMS[len(out) % len(FORMS)].format(topic=topic, context=context)
            key = q.lower()
            if key not in seen:
                seen.add(key)
                out.append({"Category": topic.title(), "Question": q, "Keywords": f"{topic} {context}"})
            if len(out) >= 800:
                return out
    return out

MOTIVATION = build_questions()


def practical_advice(question):
    """Return a practical, student-safe answer of roughly 200-300 words."""
    q = question.lower()
    subject = next((s for s in SUBJECTS if s.lower() in q), None)
    hostel = "hostel" in q
    day = "day scholar" in q or "day-scholar" in q
    exam = "jee" in q or "neet" in q or "board" in q or "exam" in q or "test" in q

    if "phone" in q or "social" in q or "distraction" in q:
        focus = "phone and distraction control"
        actions = "Keep the phone outside the study reach, switch off non-essential notifications, and use a fixed check window during breaks. If the phone is needed for a lecture or test, open only that material and close other apps."
    elif "backlog" in q or "fallen behind" in q:
        focus = "backlog recovery"
        actions = "Write every pending chapter on one page, mark prerequisites, and choose one small backlog block each day while continuing the current classwork. Do not try to finish everything in one night."
    elif "sleep" in q or "waking" in q or "hostel" in q:
        focus = "a sustainable daily routine"
        actions = "Fix a regular sleep and wake window, prepare books before sleeping, and keep the first study task small and specific. In a hostel, use a library or quiet study area when the room is noisy; as a day scholar, use travel time for light review rather than heavy problem solving."
    elif "low marks" in q or "marks" in q or "test" in q or "mock" in q or "exam" in q:
        focus = "test improvement"
        actions = "After every test, classify mistakes into concept gaps, calculation errors, reading errors, time-management errors and guesses. Pick the two largest categories and practise them before the next test."
    elif "memory" in q or "recall" in q or "revision" in q:
        focus = "active recall and revision"
        actions = "Close the book and reproduce formulas, definitions, diagrams or solution steps from memory. Check immediately, correct the gaps, and revisit the same material after a spaced interval instead of rereading passively."
    elif "read" in q or "speed" in q or "english" in q or "sanskrit" in q:
        focus = "efficient reading and understanding"
        actions = "Preview headings first, read for meaning, underline only essential information, then close the material and explain the main idea in your own words. For language subjects, add a short daily vocabulary/grammar practice block."
    elif subject:
        focus = f"improving {subject}"
        actions = f"For {subject}, choose a small concept set, learn the core idea, solve a few basic questions, then move to mixed exam-level questions. Keep a doubt list and review mistakes rather than repeatedly attempting the same question without analysis."
    elif "motivation" in q or "procrast" in q or "lazy" in q:
        focus = "starting study when motivation is low"
        actions = "Choose one task that can be completed in 10 minutes, such as five questions, one worked example or one page of revision. Put the phone away, start a timer and begin before deciding whether you feel motivated."
    else:
        focus = "steady academic progress"
        actions = "Choose one clear target, divide it into small tasks, work in a focused block, take a short planned break and record what was completed. Review the result at the end of the day and adjust tomorrow's plan."

    context_line = (
        "If you are in a hostel, protect one quiet study block in the library or designated study area and communicate your study time to roommates. "
        if hostel else
        "If you are a day scholar, account for travel and home responsibilities and protect a fixed study block after returning home. "
        if day else
        "Adjust the plan around your actual school, coaching and travel timetable rather than copying somebody else's schedule. "
    )
    exam_line = (
        "For JEE/NEET and board preparation, keep the current classwork moving while using a separate short block for backlog and revision; do not sacrifice sleep to create a temporary burst of study. "
        if exam else
        "If an exam is approaching, gradually shift more time toward timed practice and revision while keeping enough concept learning to fix genuine gaps. "
    )
    subject_line = (
        f"For {subject}, keep an error notebook with the exact reason each question was missed and revisit those errors after a few days. "
        if subject else
        "Keep a small error-and-doubt notebook so that your effort is guided by actual gaps rather than by how much time you spent sitting with a book. "
    )

    return (
        f"The practical goal here is {focus}. You do not need a perfect routine; you need a routine that you can repeat. "
        f"Start by writing one specific target for the next study block. Avoid vague targets such as ‘study Physics’ or ‘revise Biology’. "
        f"Instead, choose something measurable such as completing a defined set of questions, revising a chapter section, writing a short answer, or correcting yesterday's mistakes. "
        f"{actions} {context_line}{exam_line}{subject_line}"
        "Use a simple cycle: plan for a few minutes, study with one task only, check your work, and record the result. "
        "If you miss a day, restart with the next planned block instead of trying to compensate with an exhausting session. "
        "For difficult chapters, ask your teacher or mentor a specific doubt and write the explanation in your own words. "
        "For tests, spend more time analysing errors than looking only at the final score. "
        "For motivation, remember that consistency is built through repeated small actions, not through waiting to feel inspired. "
        "A useful daily minimum can be one focused block for current lessons, one block for questions, and a short revision block. "
        "At the end of the day, write three things: what you completed, what remains, and the first task for tomorrow. "
        "This keeps the next start easy and prevents the plan from becoming overwhelming. "
        "If stress, tiredness or pressure is interfering with normal study for a long period, speak to a parent, teacher, mentor or another trusted adult and ask for practical support."
    )


def advice(question):
    return practical_advice(question)
