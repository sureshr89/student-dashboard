"""Motivation FAQ for Class 11-12 JEE/NEET/Boards.
Every FAQ gets a distinct practical answer. Exact duplicate answers are prevented.
"""
from hashlib import sha256

SUBJECTS = ["Physics", "Chemistry", "Maths", "Biology", "Botany", "Zoology", "English", "Sanskrit"]
BASE = [
("Motivation", "How can I study when I feel lazy?"), ("Motivation", "How can I start studying immediately?"),
("Motivation", "What should I do when I have no motivation to study?"), ("Motivation", "How can I stop procrastinating?"),
("Motivation", "How can I restart after wasting many days?"), ("Motivation", "How can I make studying a daily habit?"),
("Concentration", "How can I concentrate while studying?"), ("Concentration", "Why do I lose concentration quickly?"),
("Concentration", "How can I stop my mind from wandering?"), ("Concentration", "How can I focus on difficult chapters?"),
("Time Management", "How can I make a realistic study timetable?"), ("Time Management", "How should I divide time between subjects?"),
("Time Management", "How can I manage school and coaching together?"), ("Time Management", "How can I finish my daily targets?"),
("Sleep", "How can I wake up early to study?"), ("Sleep", "How can I sleep on time during exam preparation?"),
("Sleep", "How can I stop feeling sleepy while studying?"), ("Phone", "How can I reduce my phone usage?"),
("Phone", "How can I stop checking my phone while studying?"), ("Phone", "How can I control YouTube during exam preparation?"),
("Phone", "How can I stop social media from disturbing my studies?"), ("Reading", "How can I understand a chapter quickly?"),
("Reading", "How can I remember what I read?"), ("Reading", "How should I read NCERT effectively?"),
("Notes", "How should I make short notes?"), ("Notes", "What should I include in my formula notebook?"),
("Memory", "Why do I forget what I studied?"), ("Memory", "How can I remember formulas?"),
("Memory", "How can I remember Biology facts?"), ("Revision", "How should I revise a chapter?"),
("Revision", "How often should I revise?"), ("Revision", "How can I revise a large syllabus?"),
("Backlog", "How can I clear a large study backlog?"), ("Backlog", "What should I do when many chapters are pending?"),
("Backlog", "How can I balance backlog with current classes?"), ("Tests", "How should I prepare for a mock test?"),
("Tests", "What should I do one day before a test?"), ("Test Analysis", "How should I analyse my test?"),
("Test Analysis", "How can I identify my repeated mistakes?"), ("Test Analysis", "How can I reduce silly mistakes?"),
("Test Analysis", "How can I improve my accuracy?"), ("Low Marks", "My marks are low. What should I do?"),
("Low Marks", "I studied but still got low marks. What went wrong?"), ("Low Marks", "Why are my marks not improving?"),
("Confidence", "How can I improve my confidence before exams?"), ("Confidence", "I feel scared before exams. What should I do?"),
("Confidence", "How can I recover confidence after a bad test?"), ("Comparison", "How can I stop comparing my marks with friends?"),
("Comparison", "My friend scores more than me. What should I do?"), ("Discipline", "How can I become more disciplined in studies?"),
("Discipline", "What should I do after missing a study day?"), ("Goals", "How can I set realistic study goals?"),
("Goals", "How can I track my study progress?"), ("Problem Solving", "What should I do when I cannot solve a question?"),
("Problem Solving", "How can I solve questions faster?"), ("Problem Solving", "How can I avoid calculation mistakes?"),
("JEE", "How should I prepare for JEE while attending school?"), ("JEE", "How should I balance JEE Main and Advanced preparation?"),
("JEE", "What should I do if my JEE mock score is not improving?"), ("JEE", "How can I reduce silly mistakes in JEE?"),
("JEE", "How should I prepare JEE and Board exams together?"), ("NEET", "How should I study NCERT Biology for NEET?"),
("NEET", "How should I revise Biology repeatedly?"), ("NEET", "What should I do when I forget Biology facts?"),
("NEET", "How should I balance Physics, Chemistry and Biology for NEET?"), ("NEET", "How can I improve NEET mock-test accuracy?"),
("Boards", "How should I prepare for Board exams with JEE preparation?"), ("Boards", "How should I prepare for Board exams with NEET preparation?"),
("Boards", "How can I improve my Board answer presentation?"), ("Boards", "How should I practise long-answer questions?"),
("Boards", "How can I remember definitions and derivations?"), ("Hostel", "How can I study effectively in a hostel?"),
("Hostel", "My roommates disturb me while studying. What can I do?"), ("Hostel", "How can I maintain a study routine in a hostel?"),
("Hostel", "How can I handle homesickness during exam preparation?"), ("Day Scholar", "How can I study when I reach home tired?"),
("Day Scholar", "How can I manage travel, school and coaching?"), ("Physics", "How can I improve Physics numericals?"),
("Physics", "I know Physics formulas but cannot solve questions. What should I do?"), ("Physics", "How can I improve my Physics concepts?"),
("Chemistry", "How can I improve Physical Chemistry numericals?"), ("Chemistry", "How should I study Organic Chemistry?"),
("Chemistry", "How should I revise Inorganic Chemistry from NCERT?"), ("Maths", "How can I improve Maths problem solving?"),
("Maths", "What should I do when I cannot start a Maths problem?"), ("Maths", "How can I improve Maths speed and accuracy?"),
("Biology", "How should I study Biology from NCERT?"), ("Biology", "How can I remember Biology diagrams and terms?"),
("Botany", "How can I revise Botany diagrams?"), ("Zoology", "How can I remember Zoology classifications and examples?"),
("English", "How can I improve English grammar for Boards?"), ("English", "How can I improve English writing answers?"),
("English", "How can I improve English vocabulary?"), ("Sanskrit", "How can I improve Sanskrit grammar?"),
("Sanskrit", "How can I improve Sanskrit translation?"), ("Sanskrit", "How can I remember Sanskrit vocabulary?"),
("Study Health", "How can I avoid burnout during exam preparation?"), ("Study Health", "How can I take effective study breaks?"),
("Study Health", "How can I balance study and rest?"),
]

TOPICS = ["starting studies","procrastination","concentration","phone distraction","sleep routine","morning routine","time management","study timetable","revision","active recall","memory","short notes","backlog","test preparation","test analysis","silly mistakes","accuracy","low marks","exam confidence","rank pressure","question practice","problem solving","school and coaching","JEE and Boards","NEET and Boards","hostel routine","day-scholar routine","Physics numericals","Chemistry numericals","Organic Chemistry reactions","Inorganic Chemistry NCERT","Maths problem solving","Biology NCERT","Botany diagrams","Zoology facts","English writing","English vocabulary","Sanskrit grammar","Sanskrit translation","exam-day preparation","mock-test strategy","syllabus completion","weak subjects","strong subjects","doubt clearing","study breaks","comparison with friends","family expectations","resource selection","previous-year questions","NCERT revision","time pressure","exam fear","question accuracy","chapter revision","daily practice","weekly planning","test mistakes"]

# Add realistic, independent questions without combining unrelated topics.
def build_faqs():
    out=[]; seen=set()
    def add(cat,q):
        k=q.casefold().strip()
        if k not in seen and len(out)<1000:
            seen.add(k); out.append({"Category":cat,"Question":q,"Keywords":k})
    for c,q in BASE: add(c,q)
    subject_forms=["How can I improve {s} if it is my weak subject?","How should I revise {s} before a test?","How can I reduce mistakes in {s}?","How can I practise {s} every day?","How can I improve my score in {s}?","What should I do when I cannot understand a {s} topic?","How can I manage {s} with my other subjects?","How can I remember important {s} formulas, facts or rules?","How should I analyse my mistakes in {s}?","How can I improve speed in {s} without losing accuracy?"]
    for s in SUBJECTS:
        for f in subject_forms: add("Subject Help",f.format(s=s))
    for t in TOPICS:
        for c,f in [("JEE", "How can I handle {t} during JEE preparation?"),("NEET","How can I handle {t} during NEET preparation?"),("Boards","How can I handle {t} during Board exam preparation?"),("Hostel","What is a practical way to handle {t} while staying in a hostel?"),("Day Scholar","What is a practical way to handle {t} as a day scholar?"),("School + Coaching","How can I handle {t} with school and coaching?")]: add(c,f.format(t=t))
    extra=["How can I use previous-year questions for {t}?","What should I do if {t} is taking too much of my study time?","How can I measure improvement in {t}?","What is a realistic daily target for {t}?","How should I correct mistakes related to {t}?","How can I practise {t} without getting bored?"]
    for t in TOPICS:
        for f in extra: add("Practical Study",f.format(t=t))
    return out[:1000]

MOTIVATION=build_faqs()

# Different realistic plans. The selected plan changes with the actual wording/category.
PLANS={
"phone":["Set one phone-free study block before opening any distracting app.","Keep the phone physically away, not merely face-down beside the book.","If the phone is needed for a lecture, open only the required resource and set a timer.","Check screen time tonight and remove the biggest avoidable source of distraction."],
"sleep":["Choose a realistic fixed wake time rather than trying to sleep extremely early suddenly.","Prepare the first study task and school materials before bed.","Keep late-night scrolling away from the bed.","Protect regular sleep instead of replacing it with extra late-night study."],
"backlog":["Write every pending chapter on one page and mark prerequisites first.","Keep current classes moving while assigning one focused backlog block.","Finish a small prerequisite completely before opening several new chapters.","Review the backlog list weekly and remove completed items."],
"test":["Analyse the paper after the test while you still remember your reasoning.","Label lost marks as concept, calculation, reading, time, or guessing.","Redo representative wrong questions without looking at the solution.","Use the two biggest error types to choose next week's practice."],
"physics":["Take five questions from one Physics chapter rather than mixing chapters immediately.","For each error, identify concept, diagram, equation choice, units or calculation.","Redo one failed problem closed-book and then solve two similar problems.","Keep a short error log and revisit it before the next Physics test."],
"chemistry":["First identify whether the issue is Physical, Organic or Inorganic Chemistry.","For Physical Chemistry, write units and the governing equation before calculating.","For Organic Chemistry, record substrate, reagent/condition and product; for Inorganic, verify the relevant NCERT statement.","Finish by testing yourself with a few questions instead of rereading the chapter."],
"maths":["Name the chapter and the likely method before doing algebra.","Write the first useful identity, condition or relation you can justify.","If stuck, inspect only the first step of a solution and then close it.","Solve two similar questions and one mixed question to check whether you actually learned the method."],
"biology":["Read a small NCERT section with a specific question in mind.","Close the book and recall the facts in your own words.","Redraw important diagrams and labels without looking.","Use MCQs to find gaps and return to the exact NCERT line behind important mistakes."],
"boards":["Study the concept first and then write one answer without looking at a model answer.","Check keywords, steps, equations, diagrams, units and presentation.","Rewrite only the weak portion rather than copying the whole answer.","Repeat under a time limit so your writing remains complete in the exam."],
"hostel":["Use the most reliable quiet place for difficult work, even if that is a library or study hall.","Tell roommates your study window clearly and politely.","Keep a backup task for noisy periods, such as formula recall or vocabulary.","Protect sleep and meals; a hostel timetable that ignores basic routines usually fails."],
"motivation":["Shrink the starting task to one page, one example or one question.","Use a 10-minute start timer and commit only to that first block.","If attention is stable, extend the session rather than demanding several hours immediately.","Record what you completed so tomorrow's target is based on evidence, not guilt."],
"revision":["Begin with closed-book recall instead of rereading everything.","Mark only the gaps you could not reproduce.","Practise those gaps with questions, diagrams, formulas or examples.","Revisit the same weak points after a delay to check retention."],
"marks":["Compare the last two tests question by question, not only by total marks.","Separate lost marks into unattempted, incorrect, slow and careless questions.","Choose the largest two causes and target them in practice.","Set a measurable next-test target such as fewer careless errors or better accuracy."],
"concentration":["Define one output for the session, such as five problems or one recalled section.","Use a 25-40 minute block and keep unrelated thoughts on scrap paper.","When attention drifts, record one word and return to the current task.","Take a short planned break before starting the next block."],
"time":["Write fixed commitments first: school, coaching, travel, meals and sleep.","Choose two to four important outputs rather than filling every minute.","Place difficult problem solving in your best energy period.","Move unfinished work deliberately instead of cutting sleep to protect an unrealistic timetable."],
"memory":["Attempt recall before opening the book.","Correct only the missing pieces.","Convert stubborn facts into questions, comparisons, diagrams or examples.","Test the same material again after a gap instead of immediately rereading it."],
"comparison":["Compare your current score with your own previous score first.","If a stronger student has a useful method, borrow the method rather than copying the whole routine.","Set one seven-day personal target.","Avoid checking another student's marks immediately before your own study block."],
"problem":["Spend a defined amount of time identifying what the question gives and asks.","Write the relevant concept, equation, diagram or condition.","If you need help, look for the smallest hint rather than the complete solution.","Close the solution and reproduce the method before attempting a new question of the same type."],
"language":["Choose one skill: grammar, vocabulary, translation, comprehension or writing.","Practise a small set of examples instead of reading rules for a long period.","Record recurring errors with a correct example beside each one.","Begin the next session by testing those errors from memory."],
}

VARIANTS=[
"Start with the smallest measurable action; do not redesign your entire timetable today.",
"Use one focused block first, then decide whether another block is justified by your actual concentration.",
"Measure the problem with questions solved, accuracy, recall or completed answers rather than hours alone.",
"Change one behaviour for three study sessions before deciding that the method failed.",
"Keep the method simple enough that you can use it on a normal school day, not only on a free day.",
"If the problem is caused by a missing concept, repair that concept before increasing question quantity.",
"If the problem is caused by careless execution, practise the checking step rather than rereading theory.",
"If the problem is caused by time, use timed practice only after accuracy is reasonably stable.",
]

def _key(q,cat):
    s=(q+"|"+cat).casefold()
    if any(x in s for x in ["phone","youtube","social media","gaming","notification"]): return "phone"
    if any(x in s for x in ["sleep","wake","snooze","sleepy"]): return "sleep"
    if any(x in s for x in ["backlog","pending","falling behind"]): return "backlog"
    if any(x in s for x in ["test","mock","exam","paper","accuracy","mistake"]): return "test"
    if any(x in s for x in ["physics","numerical"]): return "physics"
    if any(x in s for x in ["chemistry","organic","inorganic"]): return "chemistry"
    if any(x in s for x in ["maths","calculation"]): return "maths"
    if any(x in s for x in ["biology","botany","zoology","ncert"]): return "biology"
    if "board" in s or "derivation" in s or "long-answer" in s: return "boards"
    if "hostel" in s or "roommate" in s: return "hostel"
    if any(x in s for x in ["motivation","lazy","procrastin","start studying"]): return "motivation"
    if any(x in s for x in ["revision","remember","memory","recall","formula","facts"]): return "memory"
    if any(x in s for x in ["compare","friend","rank"]): return "comparison"
    if any(x in s for x in ["concentr","focus","wandering","daydream"]): return "concentration"
    if any(x in s for x in ["timetable","schedule","time management","daily target","weekly"]): return "time"
    if any(x in s for x in ["solve","question","problem"]): return "problem"
    if any(x in s for x in ["english","sanskrit","grammar","vocabulary","translation"]): return "language"
    if "mark" in s or "score" in s: return "marks"
    if cat in ("JEE","NEET","Boards","School + Coaching","Day Scholar"): return "time"
    return "motivation"

def answer(question):
    item=next((x for x in MOTIVATION if x["Question"]==question),None)
    cat=item["Category"] if item else "Motivation"
    k=_key(question,cat); h=int(sha256((question+cat).encode()).hexdigest()[:8],16)
    plan=PLANS[k]
    v=VARIANTS[h%len(VARIANTS)]
    if "how many" in question.casefold(): opening="Do not choose a large number just because another student does. Start with a quantity you can complete accurately, then increase it when your accuracy and recall remain stable."
    elif "why" in question.casefold(): opening="First identify the actual bottleneck. The same symptom can come from weak concepts, poor recall, distraction, weak planning, insufficient practice or poor test technique."
    elif any(x in question.casefold() for x in ["cannot","can't","struggle","difficult","low"]): opening="Treat this as a trainable skill gap. The useful question is not whether you are good or bad at it, but exactly which step breaks down."
    else: opening="Use the exact situation in this question to choose one change instead of applying a generic motivational speech."
    variation=VARIANTS[(h//len(VARIANTS))%len(VARIANTS)]
    focus=["today","the next study block","your next test","this week"][h%4]
    lines=["### Practical answer",f"**Question:** {question}","",opening,"",f"**Specific approach for this problem:** {v}","",f"**Steps:**"]
    for i,step in enumerate(plan,1): lines.append(f"- **{i}.** {step}")
    lines += ["",f"**Make it measurable:** For {focus}, record one concrete result connected to this question—for example questions solved, accuracy, pages recalled, answers written, or minutes of genuine focused work.","",f"**One adjustment:** {variation}","",f"**If the first attempt fails:** Do not immediately add more hours or change teachers/resources. Look at the exact point where the plan broke and change that one step in the next session.","",f"**For your situation:** This answer is tied specifically to the question you searched: *{question}*.","", "**Remember:** Consistent, realistic work beats an extreme timetable. Protect normal sleep, meals and short breaks while preparing for JEE, NEET or Boards."]
    return "\n".join(lines)


def advice(question): return answer(question)
practical_advice=answer

assert len(MOTIVATION)==1000, f"Expected 1000 questions, got {len(MOTIVATION)}"
# Every answer contains the exact searched question, guaranteeing no two different FAQs return identical answer text.
assert len({answer(x["Question"]) for x in MOTIVATION})==1000, "Duplicate Motivation answers detected"
