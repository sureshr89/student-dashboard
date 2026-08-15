"""Clean, searchable 1000-question Motivation FAQ for Class 11-12 JEE/NEET/Boards."""

SUBJECTS = ["Physics", "Chemistry", "Maths", "Biology", "Botany", "Zoology", "English", "Sanskrit"]
CONTEXTS = ["JEE preparation", "NEET preparation", "Board exam preparation", "hostel study", "day-scholar study", "school and coaching"]

# Natural, commonly asked student questions. Each is an independent FAQ entry.
BASE = [
("Motivation", "How can I study when I feel lazy?"),
("Motivation", "How can I start studying immediately?"),
("Motivation", "What should I do when I have no motivation to study?"),
("Motivation", "How can I stop procrastinating?"),
("Motivation", "How can I study every day without waiting for motivation?"),
("Motivation", "How can I make studying a daily habit?"),
("Motivation", "How can I study when the chapter feels boring?"),
("Motivation", "How can I restart after wasting many days?"),
("Motivation", "How can I stop making excuses for not studying?"),
("Concentration", "How can I concentrate while studying?"),
("Concentration", "Why do I lose concentration quickly?"),
("Concentration", "How can I focus for one hour?"),
("Concentration", "How can I stop my mind from wandering?"),
("Concentration", "How can I avoid daydreaming while studying?"),
("Concentration", "How can I focus on difficult chapters?"),
("Concentration", "How can I study when there is noise around me?"),
("Time Management", "How can I make a realistic study timetable?"),
("Time Management", "How should I divide time between subjects?"),
("Time Management", "How can I manage school and coaching together?"),
("Time Management", "How can I finish my daily targets?"),
("Time Management", "How can I stop wasting time between study sessions?"),
("Time Management", "How can I plan my study week?"),
("Time Management", "How can I balance new chapters and revision?"),
("Sleep", "How can I wake up early to study?"),
("Sleep", "How can I stop pressing snooze?"),
("Sleep", "How can I sleep on time during exam preparation?"),
("Sleep", "How can I stop feeling sleepy while studying?"),
("Sleep", "How can I maintain a regular sleep schedule in a hostel?"),
("Phone", "How can I reduce my phone usage?"),
("Phone", "How can I stop checking my phone while studying?"),
("Phone", "How can I control YouTube during exam preparation?"),
("Phone", "How can I stop social media from disturbing my studies?"),
("Phone", "How can I reduce gaming during study hours?"),
("Phone", "How can I study without checking notifications?"),
("Reading", "How can I read faster without losing understanding?"),
("Reading", "How can I understand a chapter quickly?"),
("Reading", "How can I stop reading the same line repeatedly?"),
("Reading", "How can I remember what I read?"),
("Reading", "How should I read NCERT effectively?"),
("Notes", "How should I make short notes?"),
("Notes", "How can I make useful revision notes?"),
("Notes", "What should I include in my formula notebook?"),
("Notes", "How can I make one-page notes?"),
("Memory", "Why do I forget what I studied?"),
("Memory", "How can I improve my memory for exams?"),
("Memory", "How can I remember formulas?"),
("Memory", "How can I remember Biology facts?"),
("Memory", "How can I use active recall?"),
("Revision", "How should I revise a chapter?"),
("Revision", "How often should I revise?"),
("Revision", "How can I revise a large syllabus?"),
("Revision", "How can I revise weak topics first?"),
("Revision", "How can I revise without simply rereading?"),
("Backlog", "How can I clear a large study backlog?"),
("Backlog", "What should I do when many chapters are pending?"),
("Backlog", "How can I balance backlog with current classes?"),
("Backlog", "How can I stop creating new backlog?"),
("Backlog", "How can I recover after falling behind?"),
("Tests", "How should I prepare for a mock test?"),
("Tests", "What should I do one day before a test?"),
("Tests", "How should I prepare for a full syllabus test?"),
("Tests", "How can I stay calm before a test?"),
("Test Analysis", "How should I analyse my test?"),
("Test Analysis", "How can I identify my repeated mistakes?"),
("Test Analysis", "How can I reduce silly mistakes?"),
("Test Analysis", "How can I improve my accuracy?"),
("Test Analysis", "How can I use test mistakes to improve?"),
("Low Marks", "My marks are low. What should I do?"),
("Low Marks", "I studied but still got low marks. What went wrong?"),
("Low Marks", "Why are my marks not improving?"),
("Low Marks", "How can I increase my score gradually?"),
("Confidence", "How can I improve my confidence before exams?"),
("Confidence", "I feel scared before exams. What should I do?"),
("Confidence", "How can I stop worrying about my rank?"),
("Confidence", "How can I recover confidence after a bad test?"),
("Comparison", "How can I stop comparing my marks with friends?"),
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
("Study Health", "How can I avoid burnout during exam preparation?"),
("Study Health", "How can I take effective study breaks?"),
("Study Health", "How can I balance study and rest?"),
("Study Health", "How can I avoid feeling exhausted after long study sessions?"),
]

# High-value topic phrases used to create clear, non-duplicated context FAQs.
TOPICS = [
"starting studies", "procrastination", "concentration", "phone distraction", "sleep routine", "morning routine",
"time management", "study timetable", "revision", "active recall", "memory", "short notes", "backlog",
"test preparation", "test analysis", "silly mistakes", "accuracy", "low marks", "exam confidence", "rank pressure",
"question practice", "problem solving", "school and coaching", "JEE and Boards", "NEET and Boards", "hostel routine",
"day-scholar routine", "Physics numericals", "Chemistry numericals", "Organic Chemistry reactions", "Inorganic Chemistry NCERT",
"Maths problem solving", "Biology NCERT", "Botany diagrams", "Zoology facts", "English writing", "English vocabulary",
"Sanskrit grammar", "Sanskrit translation", "exam-day preparation", "mock-test strategy", "syllabus completion", "weak subjects",
"strong subjects", "doubt clearing", "study breaks", "comparison with friends", "family expectations", "resource selection",
]


def build_faqs():
    out, seen = [], set()
    def add(category, question):
        q = question.strip()
        if q and q.lower() not in seen and len(out) < 1000:
            seen.add(q.lower())
            out.append({"Category": category, "Question": q, "Keywords": q.lower()})
    for cat, q in BASE:
        add(cat, q)
    # Subject-specific questions are useful for JEE/NEET/Boards students.
    subject_forms = [
        "How can I improve {s} if it is my weak subject?",
        "How should I revise {s} before a test?",
        "How can I reduce mistakes in {s}?",
        "How can I practise {s} every day?",
        "How can I improve my score in {s}?",
        "What should I do when I cannot understand a {s} topic?",
        "How can I manage {s} with my other subjects?",
        "How can I remember important {s} formulas, facts or rules?",
    ]
    for s in SUBJECTS:
        for form in subject_forms:
            add("Subject Help", form.format(s=s))
    # Frequently encountered contexts, expressed clearly and independently.
    for topic in TOPICS:
        add("JEE/NEET/Boards", f"How can I manage {topic} during JEE preparation?")
        add("JEE/NEET/Boards", f"How can I manage {topic} during NEET preparation?")
        add("JEE/NEET/Boards", f"How can I manage {topic} during Board exam preparation?")
        add("Hostel", f"What is a practical way to handle {topic} while staying in a hostel?")
        add("Day Scholar", f"What is a practical way to handle {topic} as a day scholar?")
        add("School + Coaching", f"How can I manage {topic} with school and coaching?")
    return out[:1000]

MOTIVATION = build_faqs()

PLANS = {
"motivation": ["Choose one task that takes 10-15 minutes.", "Write a measurable target such as 5 questions or 2 pages.", "Put the phone away until the block ends.", "Start before you feel ready; motivation often follows action."],
"concentration": ["Choose one subject and one task before starting.", "Use a 25-40 minute focused block.", "Keep distracting thoughts on a scrap page instead of following them.", "Take a short planned break and return on time."],
"time": ["List fixed commitments first.", "Put difficult work in your best energy period.", "Use shorter blocks for revision and longer blocks for problem solving.", "Keep a small buffer for delays."],
"sleep": ["Keep a consistent bedtime and wake time.", "Prepare books and clothes before sleeping.", "Keep the phone away from the bed when possible.", "Start the morning with one small planned study task."],
"phone": ["Keep the phone outside arm's reach during study.", "Turn off non-essential notifications.", "Use the phone only for planned breaks or required learning.", "If you want to check it, finish five more minutes first."],
"backlog": ["List pending chapters and prerequisites.", "Choose one realistic backlog target per day.", "Keep current classes moving while clearing old work.", "Do not sacrifice regular sleep to chase the backlog."],
"test": ["Analyse important wrong answers.", "Classify mistakes as concept, calculation, reading, time or guessing.", "Redo selected wrong questions without the solution.", "Use the biggest error patterns to plan the next practice block."],
"marks": ["Look at attempted, correct, incorrect and unattempted questions.", "Find the chapters causing the largest mark loss.", "Choose two gaps to work on this week.", "Compare your next test with your previous performance."],
"physics": ["Write given values and units.", "Draw a diagram when useful.", "Estimate the answer before calculation.", "Record the reason for important numerical mistakes."],
"chemistry": ["Identify whether the question is Physical, Organic or Inorganic.", "Check units or reaction conditions before solving.", "Use NCERT carefully for important Inorganic facts.", "Keep a small error list for formulas, reagents and exceptions."],
"maths": ["Identify the chapter and problem type.", "Write the first useful relation.", "If stuck, mark it and move to the next question.", "After checking a solution, close it and reproduce the key steps."],
"biology": ["Read NCERT carefully.", "Turn lists and facts into recall questions.", "Use labelled diagrams for visual memory.", "Practise MCQs after understanding the text."],
"hostel": ["Choose one reliable quiet place.", "Keep books and stationery ready.", "Agree on a simple quiet period with roommates.", "Use short revision tasks when the room is noisy."],
"day scholar": ["Build the timetable around actual travel time.", "Use travel only for light recall when safe and practical.", "Set a fixed study start time after reaching home.", "Prepare the next day's materials before sleeping."],
}


def practical_advice(question):
    q = question.lower()
    if "hostel" in q: key = "hostel"
    elif "day scholar" in q: key = "day scholar"
    elif "physics" in q: key = "physics"
    elif "chemistry" in q: key = "chemistry"
    elif "math" in q: key = "maths"
    elif any(x in q for x in ("biology", "botany", "zoology")): key = "biology"
    elif any(x in q for x in ("backlog", "pending", "behind")): key = "backlog"
    elif any(x in q for x in ("test", "mock", "exam")): key = "test"
    elif any(x in q for x in ("marks", "score", "rank")): key = "marks"
    elif any(x in q for x in ("phone", "youtube", "social media", "gaming", "screen")): key = "phone"
    elif any(x in q for x in ("sleep", "wake", "morning")): key = "sleep"
    elif any(x in q for x in ("time", "timetable", "schedule")): key = "time"
    elif any(x in q for x in ("focus", "concentr", "distract")): key = "concentration"
    else: key = "motivation"
    steps = PLANS[key]
    exam = ""
    if any(x in q for x in ("jee", "neet", "board", "exam", "test")):
        exam = "\n- **Exam connection:** Keep current lessons moving, practise timed questions regularly, and use mistakes to decide what to revise next."
    return "### Practical plan\n" + "\n".join(f"- **Step {i+1}:** {s}" for i, s in enumerate(steps)) + exam + "\n- **Daily check:** Record what you completed, one difficulty, and the first task for the next session.\n- **If it does not work:** Change one part of the method and test it for a week instead of changing everything every day."


def advice(question):
    return practical_advice(question)
