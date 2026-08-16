"""Question-specific practical answers for the 1,000 Motivation FAQs.

This file deliberately replaces the old category-only answer system. Each
answer is built from the exact question, its category, subject and context so
students do not receive one generic answer for many different questions.
"""
from motivation_faq_1000_v2 import MOTIVATION


def _subject(q):
    ql = q.lower()
    for name in ("Physics", "Chemistry", "Maths", "Biology", "Botany", "Zoology", "English", "Sanskrit"):
        if name.lower() in ql:
            return name
    if "jee" in ql: return "JEE"
    if "neet" in ql: return "NEET"
    if "board" in ql: return "Board exams"
    return "your preparation"


def _context(q):
    ql = q.lower()
    if "hostel" in ql or "roommate" in ql: return "hostel"
    if "day scholar" in ql or "travel" in ql or "reach home" in ql: return "day scholar"
    if "school" in ql and "coaching" in ql: return "school + coaching"
    return "your normal study routine"


def _focus(q, category):
    ql = q.lower()
    rules = [
        (("lazy", "motivation", "procrastin", "excuse", "start studying", "perfect mood"), "starting with a small, measurable task"),
        (("concentr", "focus", "attention", "daydream", "noise", "mind wandering", "lecture"), "protecting one uninterrupted study block"),
        (("timetable", "schedule", "divide time", "daily target", "week", "plan study"), "planning around your real available hours"),
        (("sleep", "wake up", "snooze", "sleepy", "morning"), "building a repeatable sleep-and-study routine"),
        (("phone", "youtube", "social media", "gaming", "notification", "short-video"), "removing the easiest route to distraction"),
        (("backlog", "pending", "falling behind", "unfinished"), "clearing priority chapters without creating fresh backlog"),
        (("test", "mock", "analyse", "analyze", "accuracy", "silly mistake", "attempt or skip"), "turning test data into one or two specific corrections"),
        (("low marks", "score", "marks not improving", "result"), "diagnosing exactly where marks are being lost"),
        (("confidence", "scared", "worry", "compare", "friend"), "measuring progress through controllable actions"),
        (("remember", "memory", "forget", "facts", "formula"), "retrieving information instead of repeatedly rereading it"),
        (("revision", "revise"), "using active recall followed by targeted practice"),
        (("numerical", "problem", "solve", "speed", "calculation"), "using a repeatable problem-solving process"),
    ]
    for words, focus in rules:
        if any(w in ql for w in words): return focus
    return f"making a practical plan for {category.lower()}"


def _specific_action(q, category):
    ql = q.lower()
    subject = _subject(q)
    if "how many" in ql:
        return f"Start with a quantity you can complete accurately, such as 20 focused questions for {subject}, then increase it only when accuracy and review quality remain stable."
    if "ncert" in ql:
        return f"For {subject}, keep the relevant NCERT section open while reviewing mistakes and mark the exact line, table or figure that answers the question."
    if "formula" in ql:
        return f"For {subject}, write each important formula beside one example showing when it applies and one common mistake; test yourself without looking at the example later."
    if "chapter" in ql:
        return "Choose one chapter connected to the question, divide it into small sections, and finish one section with a short recall or question set before moving on."
    if "question" in ql and ("cannot" in ql or "difficult" in ql or "solve" in ql):
        return "Before checking a solution, write the given data, the required quantity and the first principle or relation you think may connect them. This makes the exact gap visible."
    if "speed" in ql:
        return f"Use a small timed set in {subject}, record where each minute was lost, and work on that bottleneck before trying to increase the overall question count."
    if "school" in ql and "coaching" in ql:
        return "Combine overlapping work whenever possible: use school homework as revision of the same concept instead of creating a second completely separate task."
    if "hostel" in ql:
        return "Keep a backup study location and a lighter task ready. If the room becomes noisy, move difficult problem solving to the quiet slot and use the noisy period for recall or reading."
    if "day scholar" in ql or "reach home tired" in ql:
        return "Protect one dependable study block after your routine settles. Use travel only for light recall when safe and practical, rather than expecting difficult numerical work during a commute."
    return f"Write one concrete target for {subject}: a chapter section, a fixed number of questions, a recall list, a diagram reproduced from memory, or a timed written answer. Finish that target before adding another task."


def _category_step(q, category):
    subject = _subject(q)
    ql = q.lower()
    if category in ("Physics", "Chemistry", "Maths") or any(x in ql for x in ("numerical", "calculation", "problem")):
        return f"For {subject}, after the first attempt, classify the mistake as concept, method, calculation, reading or time pressure. Practise the same error type again rather than simply reading the solution."
    if category in ("Biology", "Botany", "Zoology") or any(x in ql for x in ("biology", "botany", "zoology", "ncert")):
        return "After reading, close the book and recall the facts, sequence, classification or diagram. Then check the text and mark only what you missed."
    if category in ("English", "Sanskrit") or any(x in ql for x in ("english", "sanskrit", "grammar", "translation", "writing")):
        return f"For {subject}, practise one small written task and check it against the required format. Keep a short list of recurring grammar, vocabulary or presentation errors."
    if "test" in ql or "mock" in ql:
        return "After the session, separate wrong answers, guessed answers and slow answers. Each group needs a different correction, so do not treat every lost mark as a knowledge problem."
    return "Use a short timed block, finish the chosen output, and spend the final few minutes checking what was actually completed. If the plan was too large, reduce tomorrow's target rather than abandoning the routine."


def practical_advice(question):
    q = str(question).strip()
    category = next((str(x.get("Category", "Study Help")) for x in MOTIVATION if str(x.get("Question", "")).strip() == q), "Study Help")
    subject, context = _subject(q), _context(q)
    focus = _focus(q, category)
    action = _specific_action(q, category)
    second = _category_step(q, category)
    return f"""### Practical answer

**Your question:** {q}

The best way to handle this is to focus on **{focus}**, rather than trying to change your whole routine at once. For **{subject}**, the plan should fit your **{context}** situation.

**1. Start with one clear action.** {action}

**2. Make the practice measurable.** {second} Do not count only study hours. Count an output: questions solved, a section recalled, a derivation written, a diagram reproduced, or mistakes corrected.

**3. Use a realistic example.** Suppose you have a 60-minute slot. Spend about 5 minutes deciding the exact target, 40-45 minutes doing the work without switching tasks, and the final 10-15 minutes checking or recalling. If the target is too large, reduce it instead of extending the session endlessly.

**4. Review the actual obstacle.** At the end, write one sentence: *What stopped me, or what helped me today?* If the same obstacle appears for three days, change one variable—task size, location, timing, phone access or study method—instead of simply blaming yourself.

**5. Prepare the next start.** Before leaving the desk, write the first question, page, formula, diagram, paragraph or exercise you will begin next time. This removes the starting decision and makes the following session easier.

The goal is not a perfect timetable. It is a repeatable process that produces visible progress. Use your recent tests, mistakes and unfinished work as evidence for what to do next. If the difficulty is conceptual, ask a teacher or mentor one specific doubt and then retry the same type of problem without looking at the solution. This turns the question into an action plan rather than a general motivational message."""


def advice(question):
    return practical_advice(question)

assert len(MOTIVATION) == 1000, f"Expected 1000 questions, got {len(MOTIVATION)}"
_answers = [practical_advice(str(x.get("Question", ""))) for x in MOTIVATION]
assert all(len(a.split()) >= 100 for a in _answers), "Every motivation answer must contain at least 100 words"
assert len(set(_answers)) == len(_answers), "Motivation answers must not be exact duplicates"
