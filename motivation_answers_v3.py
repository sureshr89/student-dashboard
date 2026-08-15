"""Question-specific practical answers for the Motivation FAQ.
The FAQ questions remain in motivation_faq_1000_v2.py; this module gives them differentiated answers.
"""
from motivation_faq_1000_v2 import MOTIVATION

# Each family has a genuinely different workflow. Answers are then adjusted from the
# exact question (not just the category), so related questions do not receive one copy-paste answer.
FAMILIES = {
    "lazy": {
        "title": "When starting feels difficult",
        "steps": [
            "Do not set a 4-hour target. Put the required book on the desk and choose one 10-minute task.",
            "Write a visible finish line, such as 'solve questions 1-5' or 'read two NCERT pages'.",
            "Start a timer and stay with that one task until it ends; do not redesign the timetable during the block.",
            "If you continue after 10 minutes, extend the same block to 25-30 minutes. If not, take a short break and start another small block.",
        ],
        "check": "At night, count completed blocks rather than hours planned. Aim to increase completed blocks gradually."
    },
    "concentration": {
        "title": "For concentration problems",
        "steps": [
            "Choose one chapter and one task before opening the book. Remove unrelated books and tabs from the desk.",
            "Use a 30-minute focus block. Keep a scrap sheet beside you and write distracting thoughts there instead of acting on them.",
            "When attention drops, restart from the exact line/question where you stopped; do not switch subjects immediately.",
            "Take a 5-minute physical break, then begin the next block with a clearly defined question range.",
        ],
        "check": "Record how many focused blocks you completed and what usually interrupted you. Fix the biggest interruption first."
    },
    "phone": {
        "title": "For phone and social-media distraction",
        "steps": [
            "Before studying, put the phone in another room, bag or with a parent/warden whenever practical. Silent mode alone is often not enough.",
            "Turn off non-essential notifications and remove social-media shortcuts from the home screen.",
            "If the phone is needed for a lecture, download/open only the required material and use full-screen study mode where possible.",
            "Choose two planned checking times instead of checking whenever you feel bored. Return immediately after the planned check.",
        ],
        "check": "Compare your screen-time report after three days. Reduce the largest unnecessary category rather than trying to remove everything at once."
    },
    "sleep": {
        "title": "For sleep and waking problems",
        "steps": [
            "Fix the wake-up time first and keep it reasonably consistent, including weekends when possible.",
            "Finish heavy study earlier enough to allow a wind-down period; do not depend on midnight sessions every day.",
            "Keep the phone away from the bed and prepare books/clothes the night before.",
            "After waking, start with a small planned task instead of repeatedly negotiating with yourself about getting up.",
        ],
        "check": "Track bedtime, wake time and daytime sleepiness for a week. If persistent sleep problems continue, discuss them with a parent/guardian or health professional."
    },
    "timetable": {
        "title": "For realistic planning",
        "steps": [
            "First write fixed commitments: school, coaching, travel, meals and sleep. Only then plan study blocks.",
            "Give the hardest subject your best available energy period and reserve shorter periods for revision/recall.",
            "Plan 60-80% of available study time, leaving the rest as buffer for homework, doubts and delays.",
            "Set output targets instead of only hours: e.g. 20 MCQs + analysis, one derivation, or two pages of active recall.",
        ],
        "check": "At the end of the day, move unfinished tasks to a realistic slot; do not simply double tomorrow's workload."
    },
    "backlog": {
        "title": "For a large backlog",
        "steps": [
            "Make one list of pending chapters and mark prerequisites. A chapter that blocks several others gets priority.",
            "Keep the current classwork alive. Use one dedicated backlog block each day rather than abandoning current teaching.",
            "For each backlog chapter, use a three-stage cycle: learn the core idea, solve a small basic set, then test yourself.",
            "Do not spend a week making notes before solving questions. Move to practice once the basic framework is understood.",
        ],
        "check": "Measure backlog by chapters/tasks completed, not by hours spent thinking about the backlog."
    },
    "test_analysis": {
        "title": "For test analysis",
        "steps": [
            "Do not look only at the total score. Record attempted, correct, incorrect and unattempted questions.",
            "For every important wrong answer, label the cause: concept gap, wrong method, calculation, reading, time pressure or guess.",
            "Redo a sample of wrong questions without seeing the solution. If you still cannot solve them, revisit the concept.",
            "Choose the top two recurring error types and make the next practice session specifically about them.",
        ],
        "check": "Compare the same error categories in the next test. Improvement means fewer repeated errors, not just a higher raw score."
    },
    "low_marks": {
        "title": "For low marks",
        "steps": [
            "Separate the score from the diagnosis. A low score can come from weak concepts, poor selection, slow work or avoidable errors.",
            "Take one recent paper and calculate where marks were lost by chapter and error type.",
            "Pick two high-impact gaps for the next seven days instead of trying to repair the entire syllabus simultaneously.",
            "Use short timed practice followed by error correction; passive rereading alone will not show whether the gap is fixed.",
        ],
        "check": "Compare your next test with the previous one by accuracy and repeated mistakes, not only total marks."
    },
    "memory": {
        "title": "For remembering what was studied",
        "steps": [
            "After reading a section, close the book and write or say what you remember. This exposes gaps immediately.",
            "Turn important facts into small questions: definition, formula, exception, reaction, diagram label or comparison.",
            "Review difficult items after a gap rather than rereading everything every day.",
            "Mix recall with questions so you practise retrieving information in the form the exam requires.",
        ],
        "check": "Keep a small 'forgotten again' list and revisit it at the next revision rather than rewriting the entire chapter."
    },
    "revision": {
        "title": "For revision",
        "steps": [
            "First test yourself without notes. Mark what you could not recall.",
            "Review only those weak portions, then immediately close the notes and recall them again.",
            "Solve a small mixed question set so the concept is retrieved rather than merely recognised.",
            "Schedule the next recall after a gap; repeated short recalls are more useful than one long rereading session.",
        ],
        "check": "Use a simple status: secure, needs recall, or needs relearning. Revisit 'needs relearning' with examples before memorising details."
    },
    "physics": {
        "title": "For Physics",
        "steps": [
            "Write what is given, what is required and the units before choosing a formula.",
            "Draw a quick diagram for mechanics, optics, circuits, fields or geometry-based problems when it clarifies the situation.",
            "Ask which physical principle connects the given information to the unknown instead of searching your memory for any familiar formula.",
            "After solving, check dimensions, sign and approximate magnitude. Record the exact reason for important errors.",
        ],
        "check": "Once a week, redo several previously wrong Physics problems without looking at your old solution."
    },
    "chemistry": {
        "title": "For Chemistry",
        "steps": [
            "First identify the type of problem: Physical calculation, Organic transformation/mechanism, or Inorganic fact/trend.",
            "For Physical Chemistry, write units and known quantities before substitution. For Organic, write reagent and product changes. For Inorganic, verify important facts against NCERT.",
            "Keep a small error list for formulas, units, reagents, conditions and exceptions that you repeatedly confuse.",
            "Practise mixed questions after chapter-wise learning so you learn to identify the method without the chapter title being given.",
        ],
        "check": "At revision time, test yourself from the error list first; do not reread the entire chapter just because one fact was forgotten."
    },
    "maths": {
        "title": "For Maths problem solving",
        "steps": [
            "Identify the chapter, known quantities and what must be proved/found before doing algebra.",
            "Write the first useful relation, identity, diagram or substitution. Avoid staring at the complete problem waiting for an idea.",
            "If no progress occurs after a reasonable attempt, mark the question and solve another one; later study the missing idea rather than memorising the answer.",
            "After checking a solution, close it and reproduce the method from memory on a similar problem.",
        ],
        "check": "Track the types of Maths questions where you get stuck. Practise those types separately before returning to mixed tests."
    },
    "biology": {
        "title": "For Biology, Botany and Zoology",
        "steps": [
            "Use NCERT as the base for factual preparation and read the exact paragraph behind important MCQs.",
            "Convert lists, classifications and confusing facts into short recall questions rather than copying paragraphs.",
            "Draw/label important diagrams from memory and then compare them with the textbook.",
            "After studying a section, solve a small MCQ set and return to the exact NCERT lines behind mistakes.",
        ],
        "check": "Keep a short list of facts you repeatedly forget and test that list during weekly revision."
    },
    "english": {
        "title": "For English",
        "steps": [
            "For grammar, identify the exact error pattern you make instead of doing random exercises indefinitely.",
            "For writing, practise a clear structure, relevant points, correct tone and time control.",
            "For reading, identify the main idea before looking at individual details.",
            "Keep a small vocabulary/error list and use new words in your own sentences rather than only memorising meanings.",
        ],
        "check": "Compare two written answers and circle repeated grammar, structure or clarity errors; target those in the next practice."
    },
    "sanskrit": {
        "title": "For Sanskrit",
        "steps": [
            "Break a sentence into words and identify the grammatical role or form before translating.",
            "Practise a small set of forms repeatedly rather than trying to memorise a very large table in one sitting.",
            "For translation, attempt the passage yourself first and then compare word choice and sentence structure with the correct answer.",
            "Keep a personal list of recurring grammar and vocabulary mistakes for quick revision before tests.",
        ],
        "check": "Redo previously incorrect sentences after a few days without looking at the earlier correction."
    },
    "hostel": {
        "title": "For hostel students",
        "steps": [
            "Choose one reliable study location where serious work usually happens; do not depend on the room being quiet every time.",
            "Tell roommates your protected study period politely and use headphones/earplugs only when appropriate and safe.",
            "Keep the next task, books and stationery ready so a noisy environment does not create extra decisions.",
            "When the hostel is unusually noisy, switch to light recall, reading or question review and move difficult problem solving to your quiet block.",
        ],
        "check": "Identify the time and place where you consistently study best and protect that slot first."
    },
    "day_scholar": {
        "title": "For day scholars",
        "steps": [
            "Plan around actual travel, school and coaching times rather than assuming every hour at home is available.",
            "Use travel for light recall only when safe and practical; do not plan difficult numerical work while travelling.",
            "After reaching home, use a short reset and then start a fixed study block instead of waiting for a perfect mood.",
            "Prepare books and the next day's priorities before sleeping so morning decisions are minimal.",
        ],
        "check": "Protect one dependable home study block every day and treat additional time as a bonus."
    },
    "jee": {
        "title": "For JEE preparation",
        "steps": [
            "Keep current class content moving; use backlog time separately so old work does not continuously replace new learning.",
            "For each chapter, combine concept study with timed problem practice and error analysis.",
            "Use mock tests to identify weak chapters, accuracy issues and time allocation—not just to obtain a rank.",
            "For JEE Main/Advanced decisions, follow your current official syllabus/pattern and your teacher's test plan rather than random online schedules.",
        ],
        "check": "Every week, identify one concept gap, one speed/accuracy issue and one revision target."
    },
    "neet": {
        "title": "For NEET preparation",
        "steps": [
            "Build Biology around careful NCERT reading, active recall and repeated MCQ practice.",
            "For Physics and Physical Chemistry, solve questions with units and calculations written clearly instead of only watching solutions.",
            "Review incorrect and guessed questions after each test and trace factual mistakes back to the relevant text.",
            "Keep board preparation connected where topics overlap, but schedule separate written practice when boards require descriptive answers.",
        ],
        "check": "Track Biology accuracy separately from Physics/Chemistry so one strong subject does not hide another subject's weakness."
    },
    "boards": {
        "title": "For Board preparation",
        "steps": [
            "Use the current official syllabus and sample-paper pattern for your board; do not rely on an old paper pattern.",
            "Practise writing answers within time, including definitions, derivations, diagrams, steps and required terminology.",
            "After checking a paper, note presentation and step-mark losses separately from concept errors.",
            "Keep a final revision list of formulas, definitions, diagrams, reactions and commonly missed points.",
        ],
        "check": "Once a week, complete at least one timed written section and analyse where marks were lost."
    },
    "confidence": {
        "title": "For exam confidence",
        "steps": [
            "Replace vague reassurance with evidence: record chapters completed, questions solved and mistakes corrected.",
            "Take short timed tests so exam conditions become familiar rather than frightening.",
            "Before a test, decide your first-pass strategy and time checkpoints instead of predicting the result.",
            "After a bad paper, analyse it after the emotions settle and choose two repair tasks; do not change every resource at once.",
        ],
        "check": "Judge progress by controllable actions and repeated error reduction, not by one rank or one difficult paper."
    },
    "comparison": {
        "title": "For comparison with friends",
        "steps": [
            "Use a friend's performance only to identify a method you might learn—not as a verdict on your ability.",
            "Compare your current test with your previous test for accuracy, attempted questions, time use and repeated mistakes.",
            "Choose one skill to improve this week, such as Physics accuracy or Biology recall.",
            "Limit score discussions when they are making you avoid studying; return to your own error list and plan.",
        ],
        "check": "Keep a weekly personal progress record so you have a better comparison than memory or social-media posts."
    },
    "study_health": {
        "title": "For sustainable study",
        "steps": [
            "Use planned study blocks and planned breaks instead of trying to study continuously for many hours.",
            "Protect regular sleep, meals, hydration and some movement; adding hours while exhausted often reduces useful learning.",
            "Alternate demanding problem solving with lighter recall or reading when your energy drops.",
            "If tiredness, sleep problems or other health concerns persist, tell a parent/guardian and seek appropriate professional advice.",
        ],
        "check": "Track whether your study quality improves when you adjust sleep, breaks and workload rather than only increasing hours."
    },
}


def choose_family(q):
    q = q.lower()
    # Specific topics first, broad words later.
    if "hostel" in q or "roommate" in q or "homesick" in q: return "hostel"
    if "day scholar" in q or "travel" in q or "reach home" in q: return "day_scholar"
    if "jee" in q: return "jee"
    if "neet" in q: return "neet"
    if "board" in q: return "boards"
    if any(x in q for x in ("physics",)): return "physics"
    if any(x in q for x in ("chemistry", "organic", "inorganic", "physical chemistry")): return "chemistry"
    if any(x in q for x in ("math", "calculus", "algebra", "trigonometry")): return "maths"
    if any(x in q for x in ("biology", "botany", "zoology", "ncert biology")): return "biology"
    if "english" in q: return "english"
    if "sanskrit" in q: return "sanskrit"
    if any(x in q for x in ("burnout", "exhausted", "study breaks", "balance study and rest")): return "study_health"
    if any(x in q for x in ("compare", "comparison", "friend scores", "friend")): return "comparison"
    if any(x in q for x in ("confidence", "scared", "worrying about my rank", "bad test")): return "confidence"
    if any(x in q for x in ("test", "mock", "analyse", "analyze", "accuracy", "silly mistake")): return "test_analysis"
    if any(x in q for x in ("low marks", "marks are low", "score", "score not improving")): return "low_marks"
    if any(x in q for x in ("backlog", "pending", "falling behind", "fallen behind")): return "backlog"
    if any(x in q for x in ("sleep", "wake up", "snooze", "sleepy", "morning")): return "sleep"
    if any(x in q for x in ("phone", "youtube", "social media", "gaming", "notification")): return "phone"
    if any(x in q for x in ("timetable", "schedule", "time management", "divide time", "daily target", "week")): return "timetable"
    if any(x in q for x in ("concentr", "focus", "daydream", "noise", "mind wandering")): return "concentration"
    if any(x in q for x in ("memory", "remember", "forget")): return "memory"
    if any(x in q for x in ("revision", "revise")): return "revision"
    if any(x in q for x in ("lazy", "motivation", "procrastin", "start studying", "excuses", "habit")): return "lazy"
    return "timetable"


def _question_specific_additions(q, family):
    """One or two actions based on the exact wording make each FAQ more useful."""
    extras = []
    if "how many" in q:
        extras.append("Do not choose a fixed number just because someone online recommends it; start with a manageable quantity and increase it when accuracy stays stable.")
    if "one day before" in q or "tomorrow" in q:
        extras.append("The day before, prioritise recall and targeted practice; avoid opening several completely new resources late at night.")
    if "few months" in q or "only a few" in q or "last" in q:
        extras.append("With limited time, rank topics by syllabus importance, prerequisite value and your current weakness; do not try to complete every resource.")
    if "school and coaching" in q or "school" in q and "coaching" in q:
        extras.append("Use school/coaching overlap where possible: turn class homework and revision into one planned task instead of duplicating it.")
    if "formula" in q:
        extras.append("Keep formulas beside one representative solved problem; knowing a formula is not enough if you cannot identify when it applies.")
    if "nc​ert" in q or "ncert" in q:
        extras.append("When an MCQ exposes a factual gap, return to the exact NCERT paragraph/figure instead of relying only on a coaching summary.")
    if "question" in q and "cannot" in q:
        extras.append("Before seeing a solution, write what is known, what is required and one possible principle. This turns 'I cannot solve it' into a specific obstacle.")
    if "fast" in q or "speed" in q:
        extras.append("Increase speed only after accuracy is stable. Use a timer on a small set and review why time was lost.")
    if "hostel" in q:
        extras.append("If the environment changes daily, keep a backup plan: library/study hall for hard work and the room for lighter revision.")
    if "day scholar" in q or "reach home tired" in q:
        extras.append("Do not schedule your hardest work immediately after a long commute if that is consistently your lowest-energy period; place it earlier when possible.")
    return extras[:2]


def practical_advice(question):
    q = str(question).strip()
    key = choose_family(q)
    data = FAMILIES[key]
    extras = _question_specific_additions(q.lower(), key)
    steps = list(data["steps"])
    if extras:
        steps[-1] = extras[0]
        if len(extras) > 1:
            steps.insert(2, extras[1])
    # Keep every answer readable and practical, but not artificially identical in structure.
    lines = [f"### {data['title']}"]
    lines.append("- **What to do:** " + steps[0])
    for i, step in enumerate(steps[1:], 2):
        lines.append(f"- **Step {i}:** {step}")
    lines.append(f"- **Daily check:** {data['check']}")
    lines.append("- **If you get stuck:** Write the exact obstacle in one sentence and ask your teacher/mentor a specific question. Then retry the same type of task without looking at the solution.")
    lines.append("- **Remember:** A practical plan should fit your actual school/coaching/hostel schedule. Do not copy another student's timetable blindly.")
    return "\n".join(lines)


def advice(question):
    return practical_advice(question)
