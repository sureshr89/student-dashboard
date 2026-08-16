"""Question-specific practical answers for the 1,000 Motivation FAQs.

Answers are generated from the exact question, subject/context signals and a
rotating response structure. The rotation prevents the library from showing
one generic paragraph for every question while keeping the answers practical,
student-safe and suitable for JEE/NEET/Board preparation.
"""
from hashlib import sha256

from motivation_faq_1000_v2 import MOTIVATION


def _subject(q):
    ql = q.lower()
    for name in ("Physics", "Chemistry", "Maths", "Biology", "Botany", "Zoology", "English", "Sanskrit"):
        if name.lower() in ql:
            return name
    if "jee" in ql:
        return "JEE preparation"
    if "neet" in ql:
        return "NEET preparation"
    if "board" in ql:
        return "Board preparation"
    return "your current subjects"


def _context(q):
    ql = q.lower()
    if "hostel" in ql or "roommate" in ql:
        return "hostel student"
    if "day scholar" in ql or "travel" in ql or "reach home" in ql:
        return "day-scholar routine"
    if "school" in ql and "coaching" in ql:
        return "school-and-coaching routine"
    return "normal home study routine"


def _focus(q):
    ql = q.lower()
    rules = [
        (("lazy", "motivation", "procrastin", "excuse", "start studying"), "starting quickly with a small target"),
        (("concentr", "focus", "attention", "daydream", "noise", "lecture"), "protecting one uninterrupted study block"),
        (("timetable", "schedule", "divide time", "daily target", "plan study"), "planning around actual available hours"),
        (("sleep", "wake up", "snooze", "sleepy", "morning"), "fixing the sleep-to-study transition"),
        (("phone", "youtube", "social media", "gaming", "notification", "short-video"), "removing the easiest distraction before studying"),
        (("backlog", "pending", "falling behind", "unfinished"), "clearing priority work without creating fresh backlog"),
        (("test", "mock", "accuracy", "silly mistake", "attempt", "skip"), "turning test mistakes into specific corrections"),
        (("low marks", "score", "marks not improving", "result"), "finding exactly where marks are being lost"),
        (("confidence", "scared", "worry", "compare", "friend"), "measuring progress by controllable actions"),
        (("remember", "memory", "forget", "facts", "formula"), "using retrieval instead of repeated rereading"),
        (("revision", "revise"), "using active recall followed by targeted practice"),
        (("numerical", "problem", "solve", "speed", "calculation"), "following a repeatable problem-solving process"),
    ]
    for words, focus in rules:
        if any(w in ql for w in words):
            return focus
    return "turning the exact problem into one measurable study action"


def _action(q, subject):
    ql = q.lower()
    if "ncert" in ql:
        return f"For {subject}, read the relevant NCERT section, close the book, recall the key facts or steps, then reopen it only to correct what you missed."
    if "formula" in ql:
        return f"For {subject}, keep a one-page formula sheet with one example beside each important formula and practise choosing the correct formula before substituting numbers."
    if "chapter" in ql:
        return "Break the chapter into sections. Finish one section, recall it without notes, and solve a short question set before moving to the next section."
    if "test" in ql or "mock" in ql:
        return "After every test, separate wrong, guessed and slow questions. Give each group a different correction instead of simply rereading the whole chapter."
    if "hostel" in ql:
        return "Keep two study locations and two types of tasks ready: difficult problem solving for quiet periods and recall/reading for unavoidable noisy periods."
    if "school" in ql and "coaching" in ql:
        return "Combine overlapping work. If school and coaching teach the same concept, use school homework as a second practice round instead of creating duplicate notes."
    if "day scholar" in ql or "travel" in ql or "reach home" in ql:
        return "Protect one dependable study block after you reach home. Use travel only for safe, light recall rather than difficult numerical work."
    if "phone" in ql or "youtube" in ql or "social media" in ql:
        return "Put the phone outside arm's reach, switch off non-essential notifications and decide the exact task before starting the timer."
    if "sleep" in ql:
        return "Choose a fixed sleep and wake window, keep the phone away from the bed, and start the first study task immediately after the morning routine."
    if "timetable" in ql or "schedule" in ql:
        return "List your fixed commitments first, then place only two or three important study blocks around them. Leave a small buffer for unfinished work."
    if "backlog" in ql:
        return "Rank pending chapters as urgent, important or later. Clear one high-value unfinished section each day while continuing a small amount of current syllabus work."
    if "focus" in ql or "concentr" in ql or "attention" in ql:
        return "Use a 35-45 minute single-task block. Keep one sheet beside you for distracting thoughts; write them down and return to the question instead of following them."
    if "memory" in ql or "remember" in ql or "forget" in ql:
        return "Study a short section, close the material and reproduce the important points from memory. Check only after the attempt and repeat the missed items later."
    return f"Write one concrete target for {subject}: a fixed question set, a recalled section, a derivation, a diagram, a grammar exercise or a timed written answer. Finish that output before adding another task."


def _review(q, subject):
    ql = q.lower()
    if any(x in ql for x in ("numerical", "problem", "calculation", "solve", "speed")):
        return f"During review, classify each {subject} mistake as concept, equation choice, calculation, reading or time pressure. Re-solve one similar question without looking at the solution."
    if any(x in ql for x in ("biology", "botany", "zoology", "ncert", "fact", "memory")):
        return "For memory-heavy work, use blank-page recall: write the headings, sequence, classification or diagram from memory and compare it with the text afterward."
    if any(x in ql for x in ("english", "sanskrit", "grammar", "writing", "translation")):
        return f"For {subject}, check one written response against the required format and keep a short list of recurring grammar, vocabulary or presentation errors."
    if "motivation" in ql or "lazy" in ql or "procrastin" in ql:
        return "Record the start time and the finished output, not your mood. This gives you evidence that action can happen even when motivation is low."
    return "Before stopping, write two lines: what was completed and what should begin next time. That makes the next session easier to start and prevents vague plans."


def _mode(q):
    return int(sha256(q.casefold().encode("utf-8")).hexdigest()[:8], 16) % 8


def practical_advice(question):
    q = str(question).strip()
    if not q:
        return "### Practical answer\nPlease enter a specific study question so a useful action plan can be given."
    category = next((str(x.get("Category", "Study Help")) for x in MOTIVATION if str(x.get("Question", "")).strip() == q), "Study Help")
    subject = _subject(q)
    context = _context(q)
    focus = _focus(q)
    action = _action(q, subject)
    review = _review(q, subject)
    mode = _mode(q)

    common = [
        f"**Question:** {q}\n\nThe practical target is **{focus}**. Do not try to repair your entire preparation in one day. For a {context}, the plan must fit the time, energy and study environment you actually have.",
        f"**Question:** {q}\n\nTreat this as a study-method problem, not a character problem. Your immediate goal is to make the next session easier to execute for {subject}. A small completed task is more useful than a large plan that remains unfinished.",
        f"**Question:** {q}\n\nUse evidence from your recent study sessions or tests. Identify the one behaviour connected to this problem, change that behaviour for three sessions, and judge the result from completed work rather than from how motivated you felt.",
        f"**Question:** {q}\n\nKeep the solution simple enough to use on an ordinary school day. For {subject}, choose one output you can verify and protect the time needed to finish it. If your environment changes, change the task type rather than abandoning the session.",
        f"**Question:** {q}\n\nA realistic approach is to reduce friction before increasing effort. Prepare the material, decide the first task, remove one distraction and begin with a short block. Once you are working, continue only as long as the quality remains useful.",
        f"**Question:** {q}\n\nThink in terms of the next 60 minutes, not the entire exam. For {subject}, decide what you will produce, how you will check it and what you will do if you get stuck. This keeps preparation practical and measurable.",
        f"**Question:** {q}\n\nThe solution should work even on a low-energy day. Keep a minimum version of the task ready, complete it, then extend the session if your concentration is good. Consistency is built by making the starting requirement small.",
        f"**Question:** {q}\n\nInstead of searching for another motivational trick, test one concrete change. Apply it during the next study block, record the result and keep it only if it improves your output. This makes your preparation a process you can adjust logically.",
    ]

    endings = [
        f"\n\n**Practical steps**\n- {action}\n- Work for 35-50 minutes without switching subjects unnecessarily.\n- Spend 10-15 minutes checking the output and correcting mistakes.\n- {review}\n- Before leaving, write the first task for the next session.\n\n**Example:** If you have one hour tonight, spend 5 minutes selecting the exact task, 40 minutes doing it, and 15 minutes reviewing. Stop judging the session by hours alone; judge it by what you can now solve, recall or write that you could not do before.",
        f"\n\n**Try this today**\n1. Choose one specific chapter section or skill related to the question.\n2. {action}\n3. Put a tick beside each completed output rather than counting passive reading time.\n4. {review}\n5. Set tomorrow's first task before you finish today.\n\n**Example:** A 60-minute block can be 5 minutes planning, 45 minutes active work and 10 minutes correction. If you cannot finish the planned amount, reduce the quantity next time while keeping the review step.",
        f"\n\n**A realistic routine**\n- First 5 minutes: decide exactly what success will look like.\n- Next 40 minutes: {action}\n- Final 15 minutes: {review}\n\nIf you are in a {context}, use your best environment for the hardest task and reserve interruptions for lighter work. Repeat this for three sessions before changing the plan. If the same conceptual doubt remains, ask a teacher one precise question and then retry the problem yourself. The goal is not perfection; it is a visible improvement in the next attempt.",
        f"\n\n**Make it measurable**\n- Target: one clearly defined output in the next study block.\n- Practice: {action}\n- Check: {review}\n- Record: write the number of questions attempted, correct, guessed and left unfinished.\n\n**Example:** If you plan 20 questions, finishing 14 carefully with a clear mistake analysis can be more valuable than rushing through 30. Increase volume only when accuracy and review are stable. Use the same method for three days and compare the results.",
        f"\n\n**When the problem appears again**\n- Do not restart the whole timetable.\n- Return to the smallest action that addresses it: {action}\n- Use a timer and keep distractions outside the study area.\n- {review}\n- Ask for help when you can name the exact step where you are stuck.\n\nFor a {context}, keep a backup task ready so an unexpected interruption does not turn into a completely lost day. A good backup might be formula recall, NCERT revision, vocabulary, diagrams or previously marked mistakes. Resume the main task at the next reliable slot.",
        f"\n\n**Use your next test or assignment as feedback**\n- Before starting: predict the one difficulty you want to improve.\n- During practice: {action}\n- Afterward: {review}\n- Keep only one or two corrections for the next session instead of making a huge error list.\n\n**Example:** If calculation errors are common, solve a short set slowly with deliberate checking first. Once accuracy improves, add a timer. If the problem is recall, use closed-book retrieval before doing more questions. Change the method according to the evidence.",
        f"\n\n**Low-energy version**\n- Start with 10 minutes rather than waiting for motivation.\n- If you continue, use the full block for: {action}\n- Finish with: {review}\n- Mark the session as successful if you completed the agreed minimum.\n\nThis is especially useful during heavy JEE/NEET/Board periods when school, coaching or hostel routines make every day different. The minimum task protects continuity; the longer block is optional. Over several weeks, a repeatable minimum is easier to maintain than a demanding timetable that repeatedly fails.",
        f"\n\n**Three-day experiment**\nDay 1: {action}\nDay 2: repeat it with one small improvement.\nDay 3: repeat it and compare the output with Day 1.\n\nEach day, spend a few minutes on {review.lower()} If the result improves, keep the change. If it does not, identify whether the issue was time, environment, understanding, practice quality or fatigue and adjust only that variable. This prevents random changes to your entire preparation and gives you a practical method you can keep using.",
    ]

    answer = f"### Practical answer\n\n{common[mode]}{endings[mode]}"
    return answer


def advice(question):
    return practical_advice(question)


# Safety checks: exactly 1,000 unique questions, every answer is substantial,
# and no two generated answers are exact duplicates.
assert len(MOTIVATION) == 1000, f"Expected 1000 questions, got {len(MOTIVATION)}"
assert len({str(x.get('Question', '')).strip().casefold() for x in MOTIVATION}) == 1000, "Motivation questions must be unique"
_answers = [practical_advice(str(x.get("Question", ""))) for x in MOTIVATION]
assert all(len(a.split()) >= 100 for a in _answers), "Every motivation answer must contain at least 100 words"
assert len(set(_answers)) == len(_answers), "Motivation answers must not be exact duplicates"
