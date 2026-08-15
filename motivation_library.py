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
    """Return a practical, student-safe answer targeted to roughly 200-300 words."""
    q = question.lower()
    subject = next((s for s in SUBJECTS if s.lower() in q), None)
    hostel = "hostel" in q
    day = "day scholar" in q or "day-scholar" in q
    exam = any(x in q for x in ("jee", "neet", "board", "exam", "test"))

    if any(x in q for x in ("phone", "social", "distraction")):
        focus = "controlling phone and other distractions"
        actions = "Keep the phone outside your immediate study reach, turn off non-essential notifications and use a fixed check window during breaks. If it is needed for a lecture, open only that material and close other apps."
    elif "backlog" in q or "fallen behind" in q:
        focus = "recovering a study backlog"
        actions = "List pending chapters, mark prerequisites and choose one small backlog block each day while continuing current classwork. Do not try to clear everything in one night."
    elif any(x in q for x in ("sleep", "waking", "hostel")):
        focus = "building a sustainable routine"
        actions = "Keep a regular sleep and wake window, prepare books before sleeping and make the first study task small. In a hostel, use a library or quiet study area when the room is noisy; as a day scholar, use travel time only for light review."
    elif any(x in q for x in ("low marks", "marks", "test", "mock", "exam")):
        focus = "improving test performance"
        actions = "After every test, classify mistakes as concept, calculation, reading, time-management or guessing errors. Pick the two biggest categories and practise them before the next test."
    elif any(x in q for x in ("memory", "recall", "revision")):
        focus = "active recall and revision"
        actions = "Close the book and reproduce formulas, definitions, diagrams or solution steps from memory. Check immediately, correct gaps and revisit after a spaced interval instead of only rereading."
    elif any(x in q for x in ("read", "speed", "english", "sanskrit")):
        focus = "efficient reading and language learning"
        actions = "Preview headings, read for meaning, underline only essential information and then explain the main idea without looking. For language subjects, add a short daily vocabulary or grammar block."
    elif subject:
        focus = f"improving {subject}"
        actions = f"For {subject}, select a small concept set, learn the core idea, solve basic questions and then move to mixed exam-level questions. Keep a doubt list and analyse mistakes."
    elif any(x in q for x in ("motivation", "procrast", "lazy")):
        focus = "starting when motivation is low"
        actions = "Choose a task that can be completed in 10 minutes, such as five questions, one example or one page of revision. Put the phone away, start a timer and begin before deciding whether you feel motivated."
    else:
        focus = "steady academic progress"
        actions = "Choose one measurable target, divide it into small tasks, work in a focused block, take a planned short break and record what was completed."

    if hostel:
        context_line = "In a hostel, protect one quiet study block in the library or designated study area and tell roommates when you need uninterrupted time. "
    elif day:
        context_line = "As a day scholar, include travel and home responsibilities in the plan and protect a fixed study block after returning home. "
    else:
        context_line = "Build the routine around your real school, coaching, travel and family timetable rather than copying another student's schedule. "

    exam_line = (
        "For JEE/NEET and boards, keep current lessons moving while reserving a smaller block for backlog and revision; do not sacrifice regular sleep for a temporary burst of study. "
        if exam else
        "When an exam approaches, gradually increase timed practice and revision while still fixing genuine concept gaps. "
    )
    subject_line = (
        f"For {subject}, keep an error notebook showing why each question was missed and revisit those errors after a few days. "
        if subject else
        "Keep a small error-and-doubt notebook so your effort is guided by actual gaps rather than hours spent sitting with a book. "
    )

    return (
        f"The practical goal is {focus}. You do not need a perfect routine; you need one you can repeat. "
        "Start by writing one measurable target for the next study block instead of a vague target such as ‘study more’. "
        f"{actions} {context_line}{exam_line}{subject_line}"
        "Use a simple cycle: plan for a few minutes, study with one task only, check your work and record the result. "
        "If you miss a day, restart with the next planned block instead of trying to compensate with an exhausting session. "
        "For a difficult chapter, write the exact doubt and ask a teacher or mentor rather than repeatedly rereading it. "
        "After a test, spend time analysing mistakes and convert the two most important mistakes into practice tasks. "
        "For motivation, remember that consistency is built by repeated small actions, not by waiting to feel inspired. "
        "A useful daily structure is one block for current lessons, one block for questions and a short revision block. "
        "At the end of the day, record what you completed, what remains and the first task for tomorrow. "
        "This makes the next start easier and prevents the plan from becoming overwhelming. "
        "If prolonged stress, tiredness or pressure is making normal study difficult, speak to a parent, teacher, mentor or another trusted adult and ask for practical support."
    )


def advice(question):
    return practical_advice(question)
