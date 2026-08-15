"""Clean 1000-question Motivation & Study FAQ for Class 11-12 JEE/NEET/Boards students."""

SUBJECTS = ["Physics", "Chemistry", "Maths", "Biology", "Botany", "Zoology", "English", "Sanskrit"]
CONTEXTS = ["JEE", "NEET", "Boards", "hostel", "day scholar", "school + coaching"]

# Curated, natural student questions. Each entry is an independent FAQ; no chapter-style merging.
BASE_FAQS = [
    ("Motivation", "How can I study when I feel lazy?"),
    ("Motivation", "How can I start studying immediately instead of waiting for motivation?"),
    ("Motivation", "What should I do when I have no motivation to study?"),
    ("Motivation", "How can I stop procrastinating before I start studying?"),
    ("Motivation", "How can I study every day even when I do not feel motivated?"),
    ("Motivation", "How can I make studying a daily habit?"),
    ("Motivation", "How can I study when the chapter feels boring?"),
    ("Motivation", "How can I restart my preparation after wasting many days?"),
    ("Motivation", "How can I stop making excuses for not studying?"),
    ("Motivation", "How can I make myself begin a difficult chapter?"),
    ("Concentration", "How can I concentrate while studying?"),
    ("Concentration", "Why do I lose concentration after a few minutes?"),
    ("Concentration", "How can I focus for one hour without checking my phone?"),
    ("Concentration", "How can I stop my mind from wandering while studying?"),
    ("Concentration", "How can I avoid daydreaming during study time?"),
    ("Concentration", "How can I focus on a difficult topic?"),
    ("Concentration", "How can I improve my attention span for lectures?"),
    ("Concentration", "How can I study when there is noise around me?"),
    ("Time Management", "How can I make a realistic study timetable?"),
    ("Time Management", "How should I divide my time between Physics, Chemistry and Maths?"),
    ("Time Management", "How should I divide my time between Physics, Chemistry and Biology?"),
    ("Time Management", "How can I manage school and coaching together?"),
    ("Time Management", "How can I finish my daily study targets?"),
    ("Time Management", "How can I stop wasting time between study sessions?"),
    ("Time Management", "How can I plan my week for JEE preparation?"),
    ("Time Management", "How can I plan my week for NEET preparation?"),
    ("Time Management", "How can I balance new chapters and revision?"),
    ("Time Management", "How can I study effectively when I have very little time?"),
    ("Sleep", "How can I wake up early to study?"),
    ("Sleep", "How can I stop pressing snooze in the morning?"),
    ("Sleep", "How can I sleep on time during exam preparation?"),
    ("Sleep", "How can I stop feeling sleepy while studying?"),
    ("Sleep", "How many hours should I sleep during JEE or NEET preparation?"),
    ("Sleep", "How can I maintain a regular sleep schedule in a hostel?"),
    ("Phone", "How can I reduce my phone usage while studying?"),
    ("Phone", "How can I stop checking my phone every few minutes?"),
    ("Phone", "How can I control YouTube while preparing for exams?"),
    ("Phone", "How can I stop social media from disturbing my studies?"),
    ("Phone", "How can I reduce gaming during exam preparation?"),
    ("Phone", "How can I study without checking notifications?"),
    ("Reading", "How can I read faster without losing understanding?"),
    ("Reading", "How can I understand a chapter quickly?"),
    ("Reading", "How can I stop reading the same line repeatedly?"),
    ("Reading", "How can I remember what I read?"),
    ("Reading", "How should I read NCERT effectively?"),
    ("Notes", "How should I make short notes?"),
    ("Notes", "How can I make useful revision notes?"),
    ("Notes", "What should I include in my formula notebook?"),
    ("Notes", "How can I make one-page notes for a chapter?"),
    ("Memory", "Why do I forget what I studied yesterday?"),
    ("Memory", "How can I improve my memory for exams?"),
    ("Memory", "How can I remember formulas?"),
    ("Memory", "How can I remember Biology facts?"),
    ("Memory", "How can I use active recall correctly?"),
    ("Revision", "How should I revise a chapter?"),
    ("Revision", "How often should I revise a chapter?"),
    ("Revision", "How can I revise a large syllabus?"),
    ("Revision", "How can I revise weak topics first?"),
    ("Revision", "How can I revise without simply rereading?"),
    ("Backlog", "How can I clear a large study backlog?"),
    ("Backlog", "What should I do when many chapters are pending?"),
    ("Backlog", "How can I balance backlog with current classes?"),
    ("Backlog", "How can I stop creating new backlog?"),
    ("Backlog", "How can I recover after falling behind in preparation?"),
    ("Tests", "How should I prepare for a mock test?"),
    ("Tests", "What should I do one day before a test?"),
    ("Tests", "How should I prepare for a full syllabus test?"),
    ("Tests", "How can I stay calm before a test?"),
    ("Test Analysis", "How should I analyse my test after it is over?"),
    ("Test Analysis", "How can I identify my repeated mistakes?"),
    ("Test Analysis", "How can I reduce silly mistakes?"),
    ("Test Analysis", "How can I improve my accuracy?"),
    ("Test Analysis", "How can I use my test mistakes to improve?"),
    ("Low Marks", "My marks are low. What should I do?"),
    ("Low Marks", "I studied but still got low marks. What went wrong?"),
    ("Low Marks", "Why are my marks not improving?"),
    ("Low Marks", "How can I increase my score gradually?"),
    ("Confidence", "How can I improve my confidence before exams?"),
    ("Confidence", "I feel scared before exams. What should I do?"),
    ("Confidence", "How can I stop worrying about my rank?"),
    ("Confidence", "How can I recover confidence after a bad test?"),
    ("Comparison", "How can I stop comparing my marks with my friends?"),
    ("Comparison", "My friend scores more than me. What should I do?"),
    ("Comparison", "How can I focus on my own progress?"),
    ("Discipline", "How can I become more disciplined in studies?"),
    ("Discipline", "How can I stay consistent with my timetable?"),
    ("Discipline", "What should I do after missing a study day?"),
    ("Goals", "How can I set realistic study goals?"),
    ("Goals", "How can I set weekly academic targets?"),
    ("Goals", "How can I track my study progress?"),
    ("Problem Solving", "What should I do when I cannot solve a question?"),
    ("Problem Solving", "How can I solve questions faster?"),
    ("Problem Solving", "How can I improve my problem-solving approach?"),
    ("Problem Solving", "How can I avoid calculation mistakes?"),
    ("JEE", "How should I prepare for JEE while attending school?"),
    ("JEE", "How should I balance JEE Main and Advanced preparation?"),
    ("JEE", "How many questions should I solve every day for JEE?"),
    ("JEE", "What should I do if my JEE mock score is not improving?"),
    ("JEE", "How should I analyse a JEE mock test?"),
    ("JEE", "How can I reduce silly mistakes in JEE?"),
    ("JEE", "How should I prepare JEE and Board exams together?"),
    ("JEE", "What should I do if I have only a few months left for JEE?"),
    ("NEET", "How should I study NCERT Biology for NEET?"),
    ("NEET", "How many Biology MCQs should I practise?"),
    ("NEET", "How should I revise Biology repeatedly?"),
    ("NEET", "What should I do when I forget Biology facts?"),
    ("NEET", "How should I balance Physics, Chemistry and Biology for NEET?"),
    ("NEET", "How can I improve NEET mock-test accuracy?"),
    ("NEET", "How should I analyse a NEET test?"),
    ("NEET", "How should I prepare NEET and Board exams together?"),
    ("Boards", "How should I prepare for Board exams with JEE preparation?"),
    ("Boards", "How should I prepare for Board exams with NEET preparation?"),
    ("Boards", "How can I improve my Board answer presentation?"),
    ("Boards", "How should I practise long-answer questions?"),
    ("Boards", "How can I remember definitions and derivations?"),
    ("Boards", "How should I revise before a Board exam?"),
    ("Hostel", "How can I study effectively in a hostel?"),
    ("Hostel", "My roommates disturb me while studying. What can I do?"),
    ("Hostel", "How can I maintain a study routine in a hostel?"),
    ("Hostel", "How can I handle homesickness during exam preparation?"),
    ("Day Scholar", "How can I study effectively after travelling to coaching?"),
    ("Day Scholar", "How can I manage travel, school and coaching?"),
    ("Day Scholar", "How can I study when I reach home tired?"),
    ("Physics", "How can I improve Physics numericals?"),
    ("Physics", "I know Physics formulas but cannot solve questions. What should I do?"),
    ("Physics", "How can I improve my Physics concepts?"),
    ("Physics", "How should I maintain a Physics mistake notebook?"),
    ("Chemistry", "How can I improve Physical Chemistry numericals?"),
    ("Chemistry", "How should I study Organic Chemistry?"),
    ("Chemistry", "How should I revise Inorganic Chemistry from NCERT?"),
    ("Maths", "How can I improve Maths problem solving?"),
    ("Maths", "What should I do when I cannot start a Maths problem?"),
    ("Maths", "How can I improve Maths speed and accuracy?"),
    ("Biology", "How should I study Biology from NCERT?"),
    ("Biology", "How can I remember Biology diagrams and terms?"),
    ("Botany", "How can I revise Botany diagrams?"),
    ("Zoology", "How can I remember Zoology classifications and examples?"),
    ("English", "How can I improve English grammar for Boards?"),
    ("English", "How can I improve English writing answers?"),
    ("English", "How can I improve English vocabulary?"),
    ("Sanskrit", "How can I improve Sanskrit grammar?"),
    ("Sanskrit", "How can I improve Sanskrit translation?"),
    ("Sanskrit", "How can I remember Sanskrit vocabulary?"),
    ("Health & Study", "How can I avoid burnout during exam preparation?"),
    ("Health & Study", "How can I take effective study breaks?"),
    ("Health & Study", "How can I balance study and rest?"),
    ("Health & Study", "How can I avoid feeling exhausted after long study sessions?"),
]

# Additional common-question patterns create useful, clearly worded FAQs without repeating the exact same question.
PATTERNS = [
    ("How can I improve {subject} when I am weak in it?", "Subject Improvement"),
    ("How should I revise {subject} before my next test?", "Revision"),
    ("How can I reduce mistakes in {subject}?", "Test Analysis"),
    ("How can I practise {subject} every day without getting bored?", "Subject Practice"),
    ("How can I remember important {subject} formulas or facts?", "Memory"),
    ("How can I manage {subject} with my other subjects?", "Time Management"),
    ("What should I do when I cannot understand a {subject} chapter?", "Doubt Clearing"),
    ("How can I improve my score in {subject}?", "Marks Improvement"),
]

CONTEXT_PATTERNS = [
    ("How can I handle {base} during JEE preparation?", "JEE"),
    ("How can I handle {base} during NEET preparation?", "NEET"),
    ("How can I handle {base} during Board exam preparation?", "Boards"),
    ("How can I handle {base} while staying in a hostel?", "Hostel"),
    ("How can I handle {base} as a day scholar?", "Day Scholar"),
]


def build_faqs():
    out = []
    seen = set()
    def add(cat, q):
        key = q.strip().lower()
        if key and key not in seen and len(out) < 1000:
            seen.add(key)
            out.append({"Category": cat, "Question": q.strip(), "Keywords": q.lower()})
    for cat, q in BASE_FAQS:
        add(cat, q)
    for subject in SUBJECTS:
        for template, cat in PATTERNS:
            add(cat, template.format(subject=subject))
    # Turn important existing questions into context-specific questions only when the wording remains natural.
    bases = [q for _, q in BASE_FAQS]
    for base in bases:
        for template, cat in CONTEXT_PATTERNS:
            if len(out) >= 1000:
                break
            add(cat, template.format(base=base[:-1].lower()))
        if len(out) >= 1000:
            break
    return out[:1000]

MOTIVATION = build_faqs()

PLANS = {
    "motivation": ["Choose one task that takes 10-15 minutes.", "Write a measurable target such as 5 questions or 2 pages.", "Put the phone away until the block ends.", "Start before you feel ready; motivation often follows action."],
    "concentration": ["Choose one subject and one task before starting.", "Use a 25-40 minute focused block.", "Keep distracting thoughts on a scrap page instead of following them.", "Take a short planned break and return on time."],
    "time management": ["List fixed commitments first.", "Put difficult work in your best energy period.", "Use shorter blocks for revision and longer blocks for problem solving.", "Keep a small buffer for delays."],
    "sleep": ["Keep a consistent bedtime and wake time.", "Prepare books and clothes before sleeping.", "Keep the phone away from the bed when possible.", "Start the morning with one small planned study task."],
    "phone": ["Keep the phone outside arm's reach during study.", "Turn off non-essential notifications.", "Use the phone only for planned breaks or required learning.", "If you feel the urge to check it, finish five more minutes first."],
    "backlog": ["List pending chapters and prerequisites.", "Choose one realistic backlog target per day.", "Keep current classes moving while clearing old work.", "Do not sacrifice regular sleep to chase the backlog."],
    "test": ["Analyse every important wrong answer.", "Classify mistakes as concept, calculation, reading, time or guessing.", "Redo selected wrong questions without the solution.", "Use the two biggest error patterns to plan the next practice block."],
    "marks": ["Look at attempted, correct, incorrect and unattempted questions.", "Find the chapters causing the largest mark loss.", "Choose two gaps to work on this week.", "Compare the next test with your previous performance, not only with others."],
    "physics": ["Write given values and units.", "Draw a diagram when useful.", "Estimate the answer before calculation.", "Record the reason for every important numerical mistake."],
    "chemistry": ["Identify whether the question is Physical, Organic or Inorganic.", "Check units or reaction conditions before solving.", "Use NCERT carefully for Inorganic facts.", "Keep a small error list for formulas, reagents and exceptions."],
    "maths": ["Identify the chapter and problem type.", "Write the first useful relation instead of staring at the whole problem.", "If stuck, mark it and move to the next question.", "After checking a solution, close it and reproduce the key steps."],
    "biology": ["Read NCERT carefully.", "Turn lists and facts into recall questions.", "Use labelled diagrams for visual memory.", "Practise MCQs after understanding the underlying text."],
    "hostel": ["Choose one reliable quiet place.", "Keep books and stationery ready.", "Agree on a simple quiet period with roommates.", "Use short revision tasks when the room is noisy."],
    "day scholar": ["Build the timetable around actual travel time.", "Use travel only for light recall when safe and practical.", "Set a fixed study start time after reaching home.", "Prepare the next day's materials before sleeping."],
}


def practical_advice(question):
    q = question.lower()
    if "hostel" in q: key = "hostel"
    elif "day scholar" in q or "day-scholar" in q: key = "day scholar"
    elif "physics" in q: key = "physics"
    elif "chemistry" in q: key = "chemistry"
    elif any(x in q for x in ("maths", "math")): key = "maths"
    elif any(x in q for x in ("biology", "botany", "zoology")): key = "biology"
    elif any(x in q for x in ("backlog", "pending", "behind")): key = "backlog"
    elif any(x in q for x in ("test", "mock", "exam")): key = "test"
    elif any(x in q for x in ("marks", "score", "rank")): key = "marks"
    elif any(x in q for x in ("phone", "youtube", "social media", "gaming", "screen")): key = "phone"
    elif any(x in q for x in ("sleep", "wake", "morning")): key = "sleep"
    elif any(x in q for x in ("time", "timetable", "schedule")): key = "time management"
    elif any(x in q for x in ("focus", "concentr", "distract")): key = "concentration"
    else: key = "motivation"
    steps = PLANS[key]
    if "jee" in q or "neet" in q or "board" in q:
        exam = "\n- **Exam connection:** Keep current lessons moving, practise timed questions regularly, and let test mistakes decide what you revise next."
    else:
        exam = ""
    return "### Practical plan\n" + "\n".join(f"- **Step {i+1}:** {s}" for i, s in enumerate(steps)) + exam + "\n- **Daily check:** Write what you completed, one difficulty you found, and the first task for the next session.\n- **If it does not work:** Change one part of the method and test it for a week rather than changing everything every day."


def advice(question):
    return practical_advice(question)
