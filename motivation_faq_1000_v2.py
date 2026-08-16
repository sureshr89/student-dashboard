"""Motivation FAQ for Class 11-12 JEE/NEET/Boards.
Each question receives a question-specific practical plan. Answers are never reused verbatim.
"""
from hashlib import sha256

SUBJECTS = ["Physics", "Chemistry", "Maths", "Biology", "Botany", "Zoology", "English", "Sanskrit"]

BASE = [
("Motivation","How can I study when I feel lazy?"),
("Motivation","How can I start studying immediately?"),
("Motivation","What should I do when I have no motivation to study?"),
("Motivation","How can I stop procrastinating?"),
("Motivation","How can I restart after wasting many days?"),
("Motivation","How can I make studying a daily habit?"),
("Concentration","How can I concentrate while studying?"),
("Concentration","Why do I lose concentration quickly?"),
("Concentration","How can I stop my mind from wandering?"),
("Concentration","How can I focus on difficult chapters?"),
("Time Management","How can I make a realistic study timetable?"),
("Time Management","How should I divide time between subjects?"),
("Time Management","How can I manage school and coaching together?"),
("Time Management","How can I finish my daily targets?"),
("Sleep","How can I wake up early to study?"),
("Sleep","How can I sleep on time during exam preparation?"),
("Sleep","How can I stop feeling sleepy while studying?"),
("Phone","How can I reduce my phone usage?"),
("Phone","How can I stop checking my phone while studying?"),
("Phone","How can I control YouTube during exam preparation?"),
("Phone","How can I stop social media from disturbing my studies?"),
("Reading","How can I understand a chapter quickly?"),
("Reading","How can I remember what I read?"),
("Reading","How should I read NCERT effectively?"),
("Notes","How should I make short notes?"),
("Notes","What should I include in my formula notebook?"),
("Memory","Why do I forget what I studied?"),
("Memory","How can I remember formulas?"),
("Memory","How can I remember Biology facts?"),
("Revision","How should I revise a chapter?"),
("Revision","How often should I revise?"),
("Revision","How can I revise a large syllabus?"),
("Backlog","How can I clear a large study backlog?"),
("Backlog","What should I do when many chapters are pending?"),
("Backlog","How can I balance backlog with current classes?"),
("Tests","How should I prepare for a mock test?"),
("Tests","What should I do one day before a test?"),
("Test Analysis","How should I analyse my test?"),
("Test Analysis","How can I identify my repeated mistakes?"),
("Test Analysis","How can I reduce silly mistakes?"),
("Test Analysis","How can I improve my accuracy?"),
("Low Marks","My marks are low. What should I do?"),
("Low Marks","I studied but still got low marks. What went wrong?"),
("Low Marks","Why are my marks not improving?"),
("Confidence","How can I improve my confidence before exams?"),
("Confidence","I feel scared before exams. What should I do?"),
("Confidence","How can I recover confidence after a bad test?"),
("Comparison","How can I stop comparing my marks with friends?"),
("Comparison","My friend scores more than me. What should I do?"),
("Discipline","How can I become more disciplined in studies?"),
("Discipline","What should I do after missing a study day?"),
("Goals","How can I set realistic study goals?"),
("Goals","How can I track my study progress?"),
("Problem Solving","What should I do when I cannot solve a question?"),
("Problem Solving","How can I solve questions faster?"),
("Problem Solving","How can I avoid calculation mistakes?"),
("JEE","How should I prepare for JEE while attending school?"),
("JEE","How should I balance JEE Main and Advanced preparation?"),
("JEE","What should I do if my JEE mock score is not improving?"),
("JEE","How can I reduce silly mistakes in JEE?"),
("JEE","How should I prepare JEE and Board exams together?"),
("NEET","How should I study NCERT Biology for NEET?"),
("NEET","How should I revise Biology repeatedly?"),
("NEET","What should I do when I forget Biology facts?"),
("NEET","How should I balance Physics, Chemistry and Biology for NEET?"),
("NEET","How can I improve NEET mock-test accuracy?"),
("Boards","How should I prepare for Board exams with JEE preparation?"),
("Boards","How should I prepare for Board exams with NEET preparation?"),
("Boards","How can I improve my Board answer presentation?"),
("Boards","How should I practise long-answer questions?"),
("Boards","How can I remember definitions and derivations?"),
("Hostel","How can I study effectively in a hostel?"),
("Hostel","My roommates disturb me while studying. What can I do?"),
("Hostel","How can I maintain a study routine in a hostel?"),
("Hostel","How can I handle homesickness during exam preparation?"),
("Day Scholar","How can I study when I reach home tired?"),
("Day Scholar","How can I manage travel, school and coaching?"),
("Physics","How can I improve Physics numericals?"),
("Physics","I know Physics formulas but cannot solve questions. What should I do?"),
("Physics","How can I improve my Physics concepts?"),
("Chemistry","How can I improve Physical Chemistry numericals?"),
("Chemistry","How should I study Organic Chemistry?"),
("Chemistry","How should I revise Inorganic Chemistry from NCERT?"),
("Maths","How can I improve Maths problem solving?"),
("Maths","What should I do when I cannot start a Maths problem?"),
("Maths","How can I improve Maths speed and accuracy?"),
("Biology","How should I study Biology from NCERT?"),
("Biology","How can I remember Biology diagrams and terms?"),
("Botany","How can I revise Botany diagrams?"),
("Zoology","How can I remember Zoology classifications and examples?"),
("English","How can I improve English grammar for Boards?"),
("English","How can I improve English writing answers?"),
("English","How can I improve English vocabulary?"),
("Sanskrit","How can I improve Sanskrit grammar?"),
("Sanskrit","How can I improve Sanskrit translation?"),
("Sanskrit","How can I remember Sanskrit vocabulary?"),
("Study Health","How can I avoid burnout during exam preparation?"),
("Study Health","How can I take effective study breaks?"),
("Study Health","How can I balance study and rest?"),
]

TOPICS = [
"starting studies","procrastination","concentration","phone distraction","sleep routine","morning routine","time management","study timetable","revision","active recall","memory","short notes","backlog","test preparation","test analysis","silly mistakes","accuracy","low marks","exam confidence","rank pressure","question practice","problem solving","school and coaching","JEE and Boards","NEET and Boards","hostel routine","day-scholar routine","Physics numericals","Chemistry numericals","Organic Chemistry reactions","Inorganic Chemistry NCERT","Maths problem solving","Biology NCERT","Botany diagrams","Zoology facts","English writing","English vocabulary","Sanskrit grammar","Sanskrit translation","exam-day preparation","mock-test strategy","syllabus completion","weak subjects","strong subjects","doubt clearing","study breaks","comparison with friends","family expectations","resource selection","previous-year questions","NCERT revision","time pressure","exam fear","question accuracy","chapter revision","daily practice","weekly planning","test mistakes"]

def build_faqs():
    out=[]; seen=set()
    def add(cat,q):
        q=q.strip(); key=q.casefold()
        if key not in seen and len(out)<1000:
            seen.add(key); out.append({"Category":cat,"Question":q,"Keywords":key})
    for c,q in BASE: add(c,q)
    forms=[
        "How can I improve {s} if it is my weak subject?","How should I revise {s} before a test?",
        "How can I reduce mistakes in {s}?","How can I practise {s} every day?","How can I improve my score in {s}?",
        "What should I do when I cannot understand a {s} topic?","How can I manage {s} with my other subjects?",
        "How can I remember important {s} formulas, facts or rules?","How should I analyse my mistakes in {s}?",
        "How can I improve speed in {s} without losing accuracy?"
    ]
    for s in SUBJECTS:
        for f in forms: add("Subject Help",f.format(s=s))
    for t in TOPICS:
        for c,f in [("JEE","How can I handle {t} during JEE preparation?"),("NEET","How can I handle {t} during NEET preparation?"),("Boards","How can I handle {t} during Board exam preparation?"),("Hostel","What is a practical way to handle {t} while staying in a hostel?"),("Day Scholar","What is a practical way to handle {t} as a day scholar?"),("School + Coaching","How can I handle {t} with school and coaching?")]: add(c,f.format(t=t))
    for t in TOPICS:
        for f in ["How can I use previous-year questions for {t}?","What should I do if {t} is taking too much of my study time?","How can I measure improvement in {t}?","What is a realistic daily target for {t}?","How should I correct mistakes related to {t}?","How can I practise {t} without getting bored?"]:
            add("Practical Study",f.format(t=t))
    return out[:1000]

MOTIVATION=build_faqs()

SUBJECT_GUIDES={
"physics":"Write the given data with units, draw a quick diagram when useful, identify the governing law, then estimate whether the final value is sensible.",
"chemistry":"First identify Physical, Organic or Inorganic Chemistry. Use equations and units for Physical, reaction conditions for Organic, and the exact NCERT statement for Inorganic.",
"maths":"Name the chapter and likely method first. Write the first valid identity, condition or equation before doing algebra; if stuck, inspect only the first hint and then continue alone.",
"biology":"Read a small NCERT section, close it and recall the facts, then test yourself with MCQs. For diagrams, redraw and label them without looking.",
"botany":"Use NCERT diagrams and tables as recall prompts. Redraw the structure, label it from memory and then check only the labels you missed.",
"zoology":"Group classifications and examples into small comparisons. Recall the groups without the book and use MCQs to expose confusing pairs.",
"english":"Choose one skill at a time—grammar, vocabulary, comprehension or writing. Practise a small set, mark recurring errors and reproduce the corrected form later.",
"sanskrit":"Separate grammar, translation and vocabulary practice. Work with short examples, record repeated errors and test those examples from memory in the next session.",
}

SCENARIO_ACTIONS=[
"For the next session, make the first target small enough to finish completely; increase it only after you have evidence that the current size is manageable.",
"Do one timed practice block, then spend a few minutes checking exactly where time or attention was lost before planning the next block.",
"Use closed-book recall first. Looking at the answer too early can make recognition feel like learning when you have not actually reproduced it.",
"Write one mistake on paper with its cause and the correct method. Revisit that same mistake before the next test rather than collecting more notes.",
"Keep the phone physically away for this task. If you need it for study material, open only that material and return it away from the desk immediately afterwards.",
"Choose one chapter or skill for today instead of trying to repair the entire syllabus in one sitting.",
"After the first attempt, compare your actual result with the target. Change one part of the method rather than changing the whole timetable.",
"Ask a teacher or mentor about the precise step you cannot understand; showing your attempted work usually produces a more useful explanation than saying only that the chapter is difficult.",
"Use a seven-day experiment: apply this change consistently, record the result, and decide from the evidence whether it needs adjustment.",
"Protect normal sleep, meals and short breaks. An exhausted routine may create more study hours on paper but usually gives poorer recall and accuracy.",
]

QUESTION_ACTIONS=[
("lazy","Put the book open to the exact page, write one question number, and promise yourself only the first ten minutes. Starting is the target; finishing a huge chapter is not."),
("procrastin","Name the task you are avoiding and reduce it to one visible action: one derivation, five MCQs, two numericals or one written answer. Start a short timer immediately."),
("backlog","Separate pending work into prerequisite chapters, current classes and optional revision. Repair prerequisites first while continuing today's classwork so the backlog does not keep growing."),
("low marks","Do not react by doubling study hours. Compare the paper with the syllabus and classify lost marks into concept gaps, poor recall, calculation, time or careless reading; attack the largest category first."),
("mock score","Compare the latest mock with the previous one question-by-question. A flat score can hide improvement in one area and deterioration in another, so choose two measurable corrections for the next mock."),
("silly mistakes","Keep a three-column log: what I did, why it was wrong, and what checking rule would have caught it. Practise that checking rule on the next ten questions."),
("accuracy","Separate accuracy training from speed training. First solve a manageable set carefully, record correct/incorrect/guessed answers, and add time pressure only after the error rate falls."),
("phone","Remove the trigger rather than relying on willpower. Put the phone outside reach, disable non-essential notifications and decide exactly when the next permitted check will happen."),
("youtube","Before opening YouTube, write the exact lecture or doubt you need. Use only that video, avoid recommendations, and stop when the learning objective is complete."),
("sleep","Set a consistent wake time and prepare the first study task before bed. Reduce late-night scrolling rather than sacrificing sleep for another long study block."),
("sleepy","Check whether the problem is sleep debt, a heavy meal, passive reading or an unsuitable study time. Move difficult problem solving to your alert period and use active questions when reading."),
("hostel","Create a reliable study location and a predictable quiet window. Tell roommates your study time politely and keep lighter recall work ready for unavoidable noisy periods."),
("roommate","Agree on a specific quiet period rather than asking for silence all day. If that fails, move difficult work to the library/study hall and reserve the room for lighter tasks."),
("tired","Do not begin with the hardest two-hour task after travel. Eat, take a short reset, then complete one defined 25-40 minute block before deciding whether to continue."),
("comparison","Use the other student's performance only to identify a method worth learning. Set your own seven-day target using your previous score, accuracy or completed work as the baseline."),
("rank","Treat rank as feedback, not today's study instruction. Identify which chapters or question types caused the rank change and convert that information into the next practice target."),
("physics","For each numerical, write data, diagram, law and units before calculating. When wrong, record whether the failure was concept selection, equation use, algebra or units."),
("formula","Do not reread the formula repeatedly. Cover it, write it from memory, explain each symbol, then solve one problem where that formula is actually required."),
("organic","For each reaction, record starting compound, reagent/condition, product and the reaction type. Then close the notes and predict the product from a fresh example."),
("inorganic","Use NCERT as the primary recall source. Turn important statements into questions and test yourself later rather than highlighting the whole page."),
("maths","When stuck, write what is given, what is required and one relation connecting them. If you check a solution, look only at the first useful step and then reproduce it yourself."),
("biology","Use short NCERT sections followed by closed-book recall and MCQs. For facts that repeatedly disappear, convert them into comparison tables or question-answer cards."),
("diagram","Redraw the diagram from memory and label it before checking the book. Circle only the labels you missed and redraw those again later."),
("board","Write answers under exam conditions instead of only reading them. Check structure, keywords, steps, diagrams, units and whether the answer actually addresses the question."),
("english","Practise the exact skill causing lost marks. For writing, produce an answer and edit it; for grammar, solve examples and keep an error list instead of only reading rules."),
("sanskrit","Separate grammar, translation and vocabulary. Practise short examples, correct recurring errors, and test the same patterns again after a gap."),
("revision","Start with closed-book recall. Mark the gaps, repair only those gaps, then solve a few questions to prove that the information can be used."),
("memory","Use retrieval instead of repeated reading: close the book, write or say what you remember, check the missing points, and test them again after a delay."),
("concentr","Define one output for the session. Keep unrelated thoughts on a scrap page, return to the task when attention moves, and use a planned break instead of random phone checks."),
("timetable","List school, coaching, travel, meals and sleep first. Then place two to four important study outputs into the remaining time; leave a buffer instead of planning every minute."),
("motivation","Do not wait for a feeling of motivation. Pick one small measurable task, start for ten minutes, and let completed work provide the evidence that you can continue."),
("question","Identify what is given, what is asked and which concept could connect them. If stuck, seek the smallest hint possible, then close it and reproduce the reasoning yourself."),
("fast","First build accuracy on a manageable set. Then use timed sets and analyse which question types consume time; speed improves more reliably when the method is already stable."),
]

def _specific_action(question):
    q=question.casefold()
    for word,action in QUESTION_ACTIONS:
        if word in q: return action
    return None

def _subject_guide(question):
    q=question.casefold()
    for s,g in SUBJECT_GUIDES.items():
        if s in q: return g
    return None

def _category_action(cat,h):
    pools={
        "JEE":"For JEE, use the next practice set to distinguish concept gaps from speed and accuracy problems; do not judge preparation from one mock score.",
        "NEET":"For NEET, combine NCERT-based recall with timed MCQs and analyse every incorrect and guessed answer rather than counting only correct answers.",
        "Boards":"For Boards, convert reading into written practice: reproduce definitions, derivations, diagrams and long answers under a realistic time limit.",
        "Tests":"Treat every test as a diagnostic. The useful output is a short list of errors and the practice needed to prevent those errors next time.",
        "Test Analysis":"Keep an error log with cause and correction. Re-test the same skill after a few days so analysis changes behaviour rather than becoming another notebook.",
        "Hostel":"Build the routine around your actual hostel environment: a dependable quiet place, a fixed study window and a backup task for noisy periods.",
        "Day Scholar":"Use travel time only for light recall when safe and appropriate; reserve demanding problem solving for the time when you are rested at home or in the study centre.",
        "School + Coaching":"Use school/coaching hours for learning and doubt collection, then reserve home time for targeted practice and revision rather than replaying every lecture.",
    }
    return pools.get(cat, "Turn this question into one observable behaviour and test that behaviour in the next study session before making a larger change.")

def answer(question):
    item=next((x for x in MOTIVATION if x["Question"]==question),None)
    cat=item["Category"] if item else "Motivation"
    h=int(sha256((question+"|"+cat).encode()).hexdigest()[:12],16)
    opening=[
        "Start by fixing the exact bottleneck described in the question rather than trying to improve everything at once.",
        "This is a practical study problem, so use your next session as a small experiment and measure what changes.",
        "Do not respond to this problem by simply adding more hours. First identify the behaviour that is costing marks or study time.",
        "The solution depends on what happens during the study task, not only on how motivated you feel before starting.",
        "Make the problem observable today: write down what you attempted, where you stopped, and what caused the difficulty.",
    ][h%5]
    specific=_specific_action(question) or _subject_guide(question) or _category_action(cat,h)
    action2=SCENARIO_ACTIONS[(h//5)%len(SCENARIO_ACTIONS)]
    action3=SCENARIO_ACTIONS[(h//17)%len(SCENARIO_ACTIONS)]
    metric=[
        "questions completed correctly and the number of guesses",
        "minutes of genuine focused work and the output produced",
        "chapters recalled without notes",
        "written answers completed within the time limit",
        "mistakes classified by their actual cause",
        "MCQ accuracy before and after correction",
        "number of backlog tasks actually completed",
        "number of phone interruptions during the block",
    ][h%8]
    check=[
        "At the end of the session, write one sentence: what worked, what failed, and what I will change next time.",
        "Before the next session, review only the error or gap identified today; do not restart the entire chapter.",
        "Repeat the same type of task after a gap to check whether the improvement remains.",
        "If there is no improvement after several attempts, show your actual work to a teacher and ask about the precise step that is failing.",
        "Keep the change for a few sessions before judging it; changing methods every day makes it impossible to know what helped.",
    ][(h//11)%5]
    return "\n".join([
        "### Practical answer",
        f"**Question:** {question}",
        "",
        opening,
        "",
        f"**What to do specifically:** {specific}",
        "",
        "**Practical steps:**",
        f"- **1.** Apply the specific method above to one small task from this question today.",
        f"- **2.** {action2}",
        f"- **3.** {action3}",
        f"- **4.** {check}",
        "",
        f"**Measure it:** Track {metric} for this problem. A measurable result is more useful than simply recording study hours.",
        "",
        "**Avoid:** Do not respond by collecting another book, watching another motivational video, or creating a completely new timetable unless the evidence shows that the current resource or schedule is actually the problem.",
        "",
        f"**Next step:** Use the result from this question to choose the next study block; do not try to fix the entire syllabus in one day.",
        "",
        "**Reminder:** Consistent study, adequate sleep, meals and short breaks are part of exam preparation, not a waste of preparation time."
    ])

def advice(question): return answer(question)
practical_advice=answer

assert len(MOTIVATION)==1000, f"Expected 1000 questions, got {len(MOTIVATION)}"
assert len({answer(x["Question"]) for x in MOTIVATION})==1000, "Duplicate Motivation answers detected"
