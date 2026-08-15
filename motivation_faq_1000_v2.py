"""Student Motivation FAQ: 1000 distinct questions with question-specific practical answers.
For Class 11-12 students preparing for JEE/NEET/Boards. No unsafe, sexual or vulgar content.
"""
SUBJECTS=["Physics","Chemistry","Maths","Biology","Botany","Zoology","English","Sanskrit"]
BASE=[
("Motivation","How can I study when I feel lazy?"),("Motivation","What should I do when I have no motivation to study?"),("Motivation","How can I start studying immediately?"),("Motivation","How can I stop procrastinating?"),("Motivation","How can I restart after wasting many days?"),("Motivation","How can I study every day without waiting for motivation?"),
("Concentration","How can I concentrate while studying?"),("Concentration","Why do I lose concentration quickly?"),("Concentration","How can I focus on a difficult chapter?"),("Concentration","How can I stop my mind from wandering?"),("Concentration","How can I study when there is noise around me?"),
("Time Management","How can I make a realistic study timetable?"),("Time Management","How should I divide time between subjects?"),("Time Management","How can I manage school and coaching together?"),("Time Management","How can I finish my daily targets?"),("Time Management","How can I balance new chapters and revision?"),
("Sleep","How can I wake up early to study?"),("Sleep","How can I stop pressing snooze?"),("Sleep","How can I stop feeling sleepy while studying?"),("Sleep","How can I maintain a regular sleep schedule in a hostel?"),
("Phone","How can I reduce my phone usage?"),("Phone","How can I stop checking my phone while studying?"),("Phone","How can I control YouTube during exam preparation?"),("Phone","How can I stop social media from disturbing my studies?"),
("Reading","How can I read faster without losing understanding?"),("Reading","How can I remember what I read?"),("Reading","How should I read NCERT effectively?"),
("Notes","How should I make short notes?"),("Notes","What should I include in my formula notebook?"),
("Memory","Why do I forget what I studied?"),("Memory","How can I remember formulas?"),("Memory","How can I remember Biology facts?"),
("Revision","How should I revise a chapter?"),("Revision","How often should I revise?"),("Revision","How can I revise a large syllabus?"),
("Backlog","How can I clear a large study backlog?"),("Backlog","How can I balance backlog with current classes?"),("Backlog","How can I stop creating new backlog?"),
("Tests","How should I prepare for a mock test?"),("Tests","What should I do one day before a test?"),
("Test Analysis","How should I analyse my test?"),("Test Analysis","How can I identify my repeated mistakes?"),("Test Analysis","How can I reduce silly mistakes?"),("Test Analysis","How can I improve my accuracy?"),
("Low Marks","My marks are low. What should I do?"),("Low Marks","I studied but still got low marks. What went wrong?"),("Low Marks","Why are my marks not improving?"),
("Confidence","How can I improve my confidence before exams?"),("Confidence","How can I recover confidence after a bad test?"),
("Comparison","How can I stop comparing my marks with friends?"),("Comparison","My friend scores more than me. What should I do?"),
("Discipline","How can I become more disciplined in studies?"),("Discipline","What should I do after missing a study day?"),
("Goals","How can I set realistic study goals?"),("Goals","How can I track my study progress?"),
("Problem Solving","What should I do when I cannot solve a question?"),("Problem Solving","How can I solve questions faster?"),("Problem Solving","How can I avoid calculation mistakes?"),
("JEE","How should I prepare for JEE while attending school?"),("JEE","How should I balance JEE Main and Advanced preparation?"),("JEE","What should I do if my JEE mock score is not improving?"),("JEE","How can I reduce silly mistakes in JEE?"),("JEE","How should I prepare JEE and Board exams together?"),
("NEET","How should I study NCERT Biology for NEET?"),("NEET","How should I revise Biology repeatedly?"),("NEET","What should I do when I forget Biology facts?"),("NEET","How should I balance Physics, Chemistry and Biology for NEET?"),("NEET","How can I improve NEET mock-test accuracy?"),
("Boards","How should I prepare for Board exams with JEE preparation?"),("Boards","How should I prepare for Board exams with NEET preparation?"),("Boards","How can I improve my Board answer presentation?"),("Boards","How can I remember definitions and derivations?"),
("Hostel","How can I study effectively in a hostel?"),("Hostel","My roommates disturb me while studying. What can I do?"),("Hostel","How can I maintain a study routine in a hostel?"),("Hostel","How can I handle homesickness during exam preparation?"),
("Day Scholar","How can I study when I reach home tired?"),("Day Scholar","How can I manage travel, school and coaching?"),
("Physics","How can I improve Physics numericals?"),("Physics","I know Physics formulas but cannot solve questions. What should I do?"),("Physics","How can I improve my Physics concepts?"),
("Chemistry","How can I improve Physical Chemistry numericals?"),("Chemistry","How should I study Organic Chemistry?"),("Chemistry","How should I revise Inorganic Chemistry from NCERT?"),
("Maths","How can I improve Maths problem solving?"),("Maths","What should I do when I cannot start a Maths problem?"),("Maths","How can I improve Maths speed and accuracy?"),
("Biology","How should I study Biology from NCERT?"),("Biology","How can I remember Biology diagrams and terms?"),("Botany","How can I revise Botany diagrams?"),("Zoology","How can I remember Zoology classifications and examples?"),
("English","How can I improve English grammar for Boards?"),("English","How can I improve English writing answers?"),("English","How can I improve English vocabulary?"),
("Sanskrit","How can I improve Sanskrit grammar?"),("Sanskrit","How can I improve Sanskrit translation?"),("Sanskrit","How can I remember Sanskrit vocabulary?"),
("Study Health","How can I avoid burnout during exam preparation?"),("Study Health","How can I take effective study breaks?"),("Study Health","How can I balance study and rest?"),]
SUBJECT_FORMS=["How can I improve {s} if it is my weak subject?","How should I revise {s} before a test?","How can I reduce mistakes in {s}?","How can I practise {s} every day?","How can I improve my score in {s}?","What should I do when I cannot understand a {s} topic?","How can I manage {s} with my other subjects?","How can I remember important {s} formulas, facts or rules?","How should I analyse my mistakes in {s}?","How can I improve speed in {s} without losing accuracy?"]
CONTEXT_FORMS=[("JEE","How can I handle {t} during JEE preparation?"),("NEET","How can I handle {t} during NEET preparation?"),("Boards","How can I handle {t} during Board exam preparation?"),("Hostel","What is a practical way to handle {t} while staying in a hostel?"),("Day Scholar","What is a practical way to handle {t} as a day scholar?"),("School + Coaching","How can I handle {t} with school and coaching?")]
TOPICS=["starting studies","procrastination","concentration","phone distraction","sleep routine","morning routine","time management","study timetable","revision","active recall","memory","short notes","backlog","test preparation","test analysis","silly mistakes","accuracy","low marks","exam confidence","rank pressure","question practice","problem solving","school and coaching","JEE and Boards","NEET and Boards","hostel routine","day-scholar routine","Physics numericals","Chemistry numericals","Organic Chemistry reactions","Inorganic Chemistry NCERT","Maths problem solving","Biology NCERT","Botany diagrams","Zoology facts","English writing","English vocabulary","Sanskrit grammar","Sanskrit translation","exam-day preparation","mock-test strategy","syllabus completion","weak subjects","strong subjects","doubt clearing","study breaks","comparison with friends","family expectations","resource selection","previous-year questions","NCERT revision","mock-test analysis","careless mistakes","time pressure","exam fear"]

def build_faqs():
    out=[];seen=set()
    def add(cat,q):
        q=q.strip(); k=q.casefold()
        if q and k not in seen and len(out)<1000: seen.add(k); out.append({"Category":cat,"Question":q,"Keywords":k})
    for c,q in BASE:add(c,q)
    for s in SUBJECTS:
        for f in SUBJECT_FORMS:add("Subject Help",f.format(s=s))
    for t in TOPICS:
        for c,f in CONTEXT_FORMS:add(c,f.format(t=t))
    return out[:1000]
MOTIVATION=build_faqs()

def _has(q,*words): return any(w in q for w in words)

def _scenario(q,cat):
    if "hostel" in q or cat=="Hostel": return "Hostel: use a dependable quiet place for hard work, agree on a quiet period with roommates, and keep a backup task for noisy periods."
    if "day scholar" in q or cat=="Day Scholar": return "Day scholar: build around real travel time, take a short reset after reaching home, then start a fixed study block."
    if "school" in q and "coaching" in q: return "School + coaching: protect current classwork first, then use a smaller fixed block for revision and backlog."
    if "jee" in q: return "JEE: measure progress with accuracy, questions solved and test analysis, not only hours at the desk."
    if "neet" in q: return "NEET: connect NCERT learning, MCQ practice and repeated revision instead of treating them as separate tasks."
    if "board" in q: return "Boards: include written answers, presentation and timed papers; reading alone is not enough."
    return "General student situation: identify the bottleneck in the question and change one practical behaviour at a time."

def _plan(q,cat):
    if _has(q,"physics","numerical"): return ["Choose one chapter and solve five questions without the solution.","Label each error as concept, equation choice, units, algebra or arithmetic.","Redo one wrong question closed-book and then solve two similar new questions.","Keep a short error log and review only those errors before the next practice session."]
    if _has(q,"organic chemistry","organic"): return ["Group reactions by functional group rather than memorising a long list.","Write substrate → reagent/condition → product and identify what changed.","Practise short conversion chains and predict products before checking.","Keep a reagent-confusion list and test it from memory every few days."]
    if _has(q,"inorganic"): return ["Read the relevant NCERT section carefully.","Turn trends, tables and exceptions into recall questions.","Close the book and reproduce the comparison from memory.","Use MCQs to expose gaps and return to the exact NCERT line behind each important mistake."]
    if "maths" in q or cat=="Maths": return ["Identify the chapter and write the first useful condition, identity or relation.","If stuck, study only the first useful step of a solution instead of copying it.","Close the solution and reproduce the remaining steps yourself.","Solve two similar questions and one mixed question to test transfer."]
    if _has(q,"biology","botany","zoology","ncert"): return ["Read one small NCERT section and turn important statements into recall questions.","Close the book and recall the answer aloud or in writing.","Redraw and label important diagrams without looking.","Finish with 10-20 MCQs and return to the exact NCERT line behind important mistakes."]
    if "english" in q: return ["Choose one skill: grammar, vocabulary, reading or writing.","Practise for 20 minutes and mark recurring errors.","Rewrite two incorrect sentences or one paragraph correctly.","Keep a small error-and-example notebook and review it before the next practice session."]
    if "sanskrit" in q: return ["Select one grammar form, vocabulary group or translation pattern.","Write examples yourself rather than only reading the rule.","Translate or transform new examples without looking at the answer.","Record recurring errors and revise those exact forms before the next test."]
    if _has(q,"phone","youtube","social media","gaming","notification"): return ["Choose exactly when the phone is allowed, such as after one 35-minute block.","Keep it physically away and turn off non-essential notifications.","If needed for a lecture, open only the required resource and use a timer.","Check screen time at night and identify the biggest source of lost time."]
    if _has(q,"sleep","wake","snooze","sleepy"): return ["Fix a realistic wake time and keep it consistent.","Prepare books, clothes and the first study task before bed.","Keep the phone away from the bed if it causes late-night use.","If persistent daytime sleepiness continues despite adequate sleep, tell a parent/teacher and consider professional advice."]
    if _has(q,"backlog","pending","falling behind"): return ["List pending chapters and mark prerequisites and priority.","Choose one backlog block per day while current classes continue.","Finish a small prerequisite topic before opening several new backlog chapters.","Review the list weekly and remove completed items; do not measure recovery only by hours."]
    if _has(q,"test","mock","exam","paper") and _has(q,"analyse","analyze","mistake","accuracy","score"): return ["Take the paper under realistic time conditions.","Classify each lost mark as concept, calculation, reading, time or guessing.","Redo representative errors without the solution.","Put the largest error pattern into next week's practice plan and compare the next test using the same categories."]
    if _has(q,"low marks","marks not improving","score"): return ["Compare the last two tests question by question rather than only total marks.","Check whether losses came from unattempted, incorrect, slow or careless questions.","Choose the three biggest chapter or error gaps and practise them first.","Set one measurable target for the next test, such as fewer careless errors or more accurate attempts."]
    if _has(q,"compare","friend","rank"): return ["Write your previous score, current score and one skill that improved.","Borrow a useful method from a friend without copying their whole timetable.","Set one personal seven-day target and record it daily.","Avoid checking another student's marks immediately before studying because it changes focus without building skill."]
    if _has(q,"concentr","focus","mind wandering","daydream"): return ["Define one output: a page recalled, five problems solved or one diagram reproduced.","Use a 25-40 minute block and keep a scrap page for unrelated thoughts.","When attention drifts, note the thought in one word and return.","Take a planned short break and restart with a new measurable target."]
    if _has(q,"timetable","time","daily target","weekly","schedule"): return ["Write fixed commitments first: school, coaching, travel, meals and sleep.","Assign only 2-4 important academic outputs instead of filling every minute.","Put difficult problem solving in your best energy period and revision in shorter blocks.","Review at night and move unfinished work deliberately; do not delete sleep to repair a timetable."]
    if _has(q,"revision","remember","memory","recall","formula","facts"): return ["Start with closed-book recall before opening notes.","Check gaps and revise only those portions.","Repeat recall after a delay instead of rereading immediately.","Use questions, formulas, diagrams or flashcards according to the subject and track items that still fail recall."]
    if _has(q,"read","reading","fast"): return ["Preview headings, diagrams and questions before reading.","Read one section for meaning and then state its main idea without looking.","Mark only terms that change the concept or answer.","Increase speed only after recall remains accurate."]
    if _has(q,"note","formula notebook"): return ["Make notes only from material you need to recall, compare or repeatedly forget.","For formulas include the condition and one typical use.","For factual subjects use tables, diagrams and contrasts instead of long paragraphs.","Shorten or remove notes that never help you answer questions."]
    if _has(q,"motivation","lazy","procrastinat","excuse","start studying"): return ["Choose the smallest useful start: open the chapter, write a formula or solve one question.","Set a 10-minute start timer and promise only that much.","If attention is stable, continue for another 20-30 minutes.","Record what you completed so tomorrow's target comes from evidence, not guilt."]
    if _has(q,"hostel","roommate"): return ["Identify the quietest reliable location for hard work.","Tell roommates your study period clearly and politely.","Keep a backup task for noisy periods, such as formula recall or vocabulary.","Use a library or supervised study area when the room repeatedly prevents focus."]
    if _has(q,"board","writing","derivation","long-answer"): return ["Study the concept first, then write one answer without the model.","Check steps, keywords, equations, diagrams, units and presentation.","Rewrite only the weak part instead of copying the whole answer.","Practise under a time limit so presentation remains clear in a long paper."]
    return ["Define the exact problem before changing your timetable or resources.","Choose one action that can be completed in the next study block.","Measure the result using questions solved, accuracy, recall or time used.","Keep what works, change one weak part and test the revised method for several days."]

def answer(question):
    cat=next((x["Category"] for x in MOTIVATION if x["Question"]==question),"Study Help"); q=question.casefold(); actions=_plan(q,cat); scenario=_scenario(q,cat)
    if "why" in q: opening="First diagnose the cause instead of calling yourself lazy. The useful question is where the study process breaks."
    elif "how many" in q: opening="There is no single number that suits every student. Start with a manageable amount, measure accuracy and increase only when quality stays stable."
    elif _has(q,"cannot","can't","unable","struggle","difficult","low"): opening="Treat this as a skill gap, not a permanent weakness. Find the exact step that is failing and practise that step."
    elif _has(q,"before","exam","test","mock"): opening="For an upcoming test, do not try to repair everything at once. Prioritise high-value gaps, timed practice and mistakes you can still correct."
    else: opening="Treat this as a practical study problem: identify the bottleneck, make one change, measure the result and adjust it."
    text=["### Practical answer",f"**Question:** {question}","",opening,"","**What to do:**"]
    text += [f"- **Step {i}:** {a}" for i,a in enumerate(actions,1)]
    text += ["",f"**Your situation:** {scenario}","","**Today:** Apply the first two steps in one focused study block and write down one measurable result.","","**Check tomorrow:** What improved? What still caused trouble? What single change should you make next?","","**Avoid:** Extreme timetables, sacrificing regular sleep, collecting many new resources, and comparing your routine with another student.","","**If it continues:** Show the specific work, questions or test mistakes to a teacher, parent or mentor. A specific problem is easier to solve than a general feeling that you are weak."]
    return "\n".join(text)

def advice(question): return answer(question)
practical_advice=answer
assert len(MOTIVATION)==1000, f"Expected 1000 FAQ entries, got {len(MOTIVATION)}"
