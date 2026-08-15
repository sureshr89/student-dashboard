import urllib.request
import re
import difflib
import pandas as pd
import streamlit as st

# ============================================================
# LOAD EXISTING DASHBOARD SOURCE
# ============================================================

SOURCE_URL = (
    "https://raw.githubusercontent.com/sureshr89/student-dashboard/"
    "643305bc8243a7a4a997af10070a1936e5f09609/main.py"
)

try:
    source = urllib.request.urlopen(SOURCE_URL, timeout=20).read().decode("utf-8")
except Exception as exc:
    st.error(f"Unable to load dashboard source: {exc}")
    st.stop()


# ============================================================
# EXISTING ROSTER FIX
# G Rishith Kumar belongs to E only
# ============================================================

old = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {
            "v_4102643666550411": "Jampala Shanthan Kumar",
            "v_4102439835972285": "P Rohith",
            "v_4102643721870649": "Punem Abhinav Sidhardha",
            "v_4102644496422857": "G Rishith Kumar",
'''

new = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {
            "v_4102643666550411": "Jampala Shanthan Kumar",
            "v_4102439835972285": "P Rohith",
            "v_4102643721870649": "Punem Abhinav Sidhardha",
'''

if old not in source:
    st.error(
        "Dashboard source integrity check failed: "
        "expected C-batch roster entry was not found."
    )
    st.stop()

source = source.replace(old, new, 1)


# ============================================================
# CHART READABILITY PATCH
# ============================================================

chart_patch = r'''
# ============================================================
# CHART READABILITY PATCH
# ============================================================

import plotly.graph_objects as _go
import streamlit as _st

_original_plotly_chart = _st.plotly_chart


def _readable_plotly_chart(fig, *args, **kwargs):
    try:
        if isinstance(fig, _go.Figure):

            fig.update_layout(
                font=dict(color="#1f2937"),
                title_font=dict(color="#1f2937"),
                legend=dict(font=dict(color="#1f2937")),
                xaxis=dict(
                    title_font=dict(color="#1f2937"),
                    tickfont=dict(color="#1f2937"),
                ),
                yaxis=dict(
                    title_font=dict(color="#1f2937"),
                    tickfont=dict(color="#1f2937"),
                ),
            )

            for trace in fig.data:
                if getattr(trace, "type", None) == "bar":
                    trace.texttemplate = "%{y:.2f}"
                    trace.textposition = "outside"
                    trace.textfont = dict(
                        color="#1f2937",
                        size=14
                    )
                    trace.cliponaxis = False

            for annotation in fig.layout.annotations:
                annotation.font = dict(
                    color="#1f2937",
                    size=12
                )

    except Exception:
        pass

    return _original_plotly_chart(fig, *args, **kwargs)


_st.plotly_chart = _readable_plotly_chart
'''


source = source.replace(
    'if __name__ == "__main__":',
    chart_patch + '\n\nif __name__ == "__main__":',
    1,
)


# ============================================================
# EXTRA DASHBOARD CODE
# ============================================================

extra_code = r'''

# ============================================================
# STUDENT MOTIVATION + CONCEPTS EXTENSION
# ============================================================

import difflib
import re
import pandas as pd
import streamlit as st


# ============================================================
# 300 STUDENT-SAFE MOTIVATION QUESTIONS
# 20 CATEGORIES × 15 QUESTIONS = 300
# ============================================================

MOTIVATION_DATA = {

"Study Motivation": [
"How can I study when I don't feel like studying?",
"How can I stop being lazy while studying?",
"How can I start studying immediately?",
"What should I do when I have no motivation to study?",
"How can I make myself study every day?",
"How can I develop a regular study habit?",
"How can I study even when the subject feels boring?",
"How can I stop postponing my studies?",
"How can I become more disciplined in studies?",
"How can I study without waiting for motivation?",
"What should I do if I waste the whole day?",
"How can I restart my studies after a long break?",
"How can I make studying a daily habit?",
"How can I stay consistent with my timetable?",
"How can I motivate myself before starting a chapter?",
],

"Concentration": [
"How can I concentrate while studying?",
"How can I study for one hour without distraction?",
"How can I improve my concentration?",
"Why do I lose concentration quickly?",
"How can I focus on difficult chapters?",
"How can I stop my mind from wandering while studying?",
"How can I improve my attention span?",
"How can I concentrate during online classes?",
"How can I focus when there is noise around me?",
"How can I study without checking my phone?",
"How can I concentrate when I feel tired?",
"How can I focus on one subject at a time?",
"How can I avoid daydreaming while studying?",
"How can I improve my focus during revision?",
"How can I concentrate before an important test?",
],

"Time Management": [
"How should I make my daily study timetable?",
"How can I manage school and coaching together?",
"How should I divide time between subjects?",
"How can I complete my daily targets?",
"How can I stop wasting time?",
"How can I finish my syllabus on time?",
"How can I manage difficult and easy subjects?",
"How much time should I spend on each subject?",
"How can I plan my week?",
"How can I manage revision with new chapters?",
"How can I study when I have very little time?",
"How can I recover time after wasting a day?",
"How can I make realistic study targets?",
"How can I follow my timetable consistently?",
"How can I manage multiple tests in the same week?",
],

"Wake Up and Routine": [
"How can I wake up early?",
"How can I build a good morning routine?",
"How can I stop pressing snooze?",
"How can I sleep on time?",
"How can I create a regular study routine?",
"How can I become more active in the morning?",
"What should I do if I feel sleepy while studying?",
"How can I avoid staying awake late at night?",
"How can I prepare for the next day before sleeping?",
"How can I make my mornings productive?",
"How can I maintain a consistent daily routine?",
"How can I balance sleep and study?",
"How can I avoid studying at random times?",
"How can I build a healthy student routine?",
"How can I become more punctual?",
],

"Phone and Distractions": [
"How can I reduce my phone usage?",
"How can I stop checking my phone while studying?",
"How can I control YouTube usage?",
"How can I reduce social media distractions?",
"Should I keep my phone away while studying?",
"How can I stop gaming during study hours?",
"How can I avoid unnecessary notifications?",
"How can I study without opening social media?",
"How can I control my screen time?",
"What should I do if my phone keeps distracting me?",
"How can I use my phone only for studying?",
"How can I avoid watching videos when I should study?",
"How can I make my study environment distraction free?",
"How can I stop checking messages repeatedly?",
"How can I create a phone-free study session?",
],

"Reading and Study Speed": [
"How can I read faster?",
"How can I understand a chapter quickly?",
"How can I improve my reading speed?",
"How can I avoid reading the same line repeatedly?",
"How can I read textbooks effectively?",
"How can I study a long chapter efficiently?",
"How can I identify important points while reading?",
"How can I read without losing concentration?",
"How can I understand difficult paragraphs?",
"How can I study faster without reducing understanding?",
"How can I improve comprehension?",
"How can I read a chapter before a test?",
"How can I make active reading easier?",
"How can I remember what I read?",
"How can I avoid wasting time on one topic?",
],

"Notes": [
"How should I make short notes?",
"How can I make useful revision notes?",
"What should I write in my notes?",
"How can I make formula notes?",
"How can I make Chemistry reaction notes?",
"How can I organize my notes?",
"How can I make notes without wasting too much time?",
"Should I rewrite my textbook into notes?",
"How can I make one-page revision notes?",
"How can I highlight important points?",
"How can I make notes for difficult chapters?",
"How can I make notes for last-minute revision?",
"How can I organize Physics formulas?",
"How can I organize Maths formulas?",
"How can I make notes that are easy to revise?",
],

"Memory": [
"Why do I forget what I studied?",
"How can I improve my memory?",
"How can I remember formulas?",
"How can I remember Chemistry reactions?",
"How can I remember important concepts?",
"How can I remember what I studied yesterday?",
"How often should I revise a topic?",
"How can I use active recall?",
"How can I revise without rereading everything?",
"How can I remember mistakes from previous tests?",
"How can I remember difficult definitions?",
"How can I improve long-term memory for exams?",
"How can I remember important facts?",
"How can I revise formulas quickly?",
"How can I stop forgetting after studying?",
],

"Revision": [
"How should I revise a chapter?",
"How often should I revise?",
"How should I revise before a test?",
"How can I revise the entire syllabus?",
"How can I revise weak topics?",
"How can I revise without getting bored?",
"How can I revise formulas every day?",
"How can I revise mistakes?",
"How can I make a revision schedule?",
"How should I revise one week before an exam?",
"How should I revise one day before a test?",
"How can I balance revision and new topics?",
"How can I revise multiple subjects?",
"How can I revise using questions?",
"How can I check whether my revision is effective?",
],

"Backlog": [
"How can I complete my study backlog?",
"What should I do if I have many chapters pending?",
"How can I start my backlog without feeling overwhelmed?",
"Should I complete old chapters before new ones?",
"How can I clear my Physics backlog?",
"How can I clear my Chemistry backlog?",
"How can I clear my Maths backlog?",
"How can I make a backlog recovery plan?",
"How many pending topics should I complete each day?",
"What should I do if my backlog keeps increasing?",
"How can I balance backlog and current classes?",
"How can I identify the most important pending topics?",
"How can I complete a large backlog before exams?",
"How can I stop creating new backlog?",
"How can I restart after falling behind?",
],

"Test Preparation": [
"How should I prepare for a test?",
"What should I do one week before a test?",
"What should I do one day before a test?",
"How should I revise before a mock test?",
"How can I prepare for a difficult test?",
"How can I prepare for a full syllabus test?",
"How can I divide preparation between subjects?",
"How can I improve my test preparation?",
"How can I prepare formulas before a test?",
"How can I prepare important concepts quickly?",
"How can I avoid panic before a test?",
"How can I make a test preparation checklist?",
"How can I prepare after finishing the syllabus?",
"How can I prepare for repeated tests?",
"How can I use previous tests for preparation?",
],

"Test Analysis": [
"How should I analyse my test?",
"What should I do after getting low marks?",
"How can I identify my mistakes?",
"How can I reduce silly mistakes?",
"How can I analyse wrong answers?",
"How can I analyse questions I guessed?",
"How can I improve after every test?",
"How can I identify my weak chapters?",
"How can I identify my strongest subject?",
"How can I track my improvement?",
"How can I learn from a bad test?",
"How can I improve my accuracy?",
"How can I improve my speed in tests?",
"How can I avoid repeating the same mistake?",
"How can I make a test-analysis notebook?",
],

"Low Marks": [
"My marks are low. What should I do?",
"I studied but still got low marks. Why?",
"How can I improve my marks?",
"What should I do after a bad test?",
"How can I recover after low marks?",
"Why are my marks not improving?",
"How can I increase my score gradually?",
"How can I improve my weak subject?",
"What should I change if my score stays the same?",
"How can I turn mistakes into improvement?",
"How can I improve from average marks?",
"How can I become better than my previous score?",
"How can I stop losing marks unnecessarily?",
"How can I improve my accuracy?",
"How can I make a plan after low marks?",
],

"Exam Confidence": [
"I feel scared before exams. What should I do?",
"How can I stay calm before an exam?",
"How can I improve my confidence?",
"I lose confidence after low marks. What should I do?",
"I compare my marks with friends. What should I do?",
"How can I stop worrying about my rank?",
"How can I stay positive after a difficult test?",
"How can I handle exam pressure?",
"How can I avoid panic during an exam?",
"How can I stay confident when others score more?",
"How can I trust my preparation?",
"How can I stay calm when I don't know an answer?",
"How can I manage nervousness before a test?",
"How can I become mentally prepared for exams?",
"How can I stop thinking negatively about my performance?",
],

"Goals": [
"How can I set a study goal?",
"How can I set realistic academic goals?",
"How can I track my study goals?",
"How can I create weekly goals?",
"How can I create monthly goals?",
"How can I stay focused on my target?",
"How can I break a big goal into small tasks?",
"How can I measure my progress?",
"How can I improve my academic performance step by step?",
"How can I create a target for my next test?",
"How can I set subject-wise goals?",
"How can I set revision goals?",
"How can I stay consistent with my goals?",
"How can I recover when I miss my goal?",
"How can I celebrate improvement without becoming careless?",
],

"Discipline and Habits": [
"How can I become more disciplined?",
"How can I build a study habit?",
"How can I study at the same time every day?",
"How can I stop procrastinating?",
"How can I finish what I start?",
"How can I avoid making excuses?",
"How can I maintain consistency?",
"How can I build a productive routine?",
"How can I make studying automatic?",
"How can I develop better academic habits?",
"How can I avoid skipping study sessions?",
"How can I stay disciplined during holidays?",
"How can I return to my routine after a break?",
"How can I make small improvements every day?",
"How can I become more responsible for my studies?",
],

"Subject Improvement": [
"How can I improve Physics?",
"How can I improve Chemistry?",
"How can I improve Maths?",
"How can I improve Biology?",
"How can I understand Physics concepts better?",
"How can I improve Chemistry problem solving?",
"How can I improve Maths problem solving?",
"How can I improve Biology revision?",
"How can I identify my weakest subject?",
"How should I divide time between weak and strong subjects?",
"How can I improve one subject in 30 days?",
"How can I practise difficult questions?",
"How can I improve conceptual understanding?",
"How can I improve numerical problem solving?",
"How can I become stronger in my weakest topic?",
],

"Problem Solving": [
"How can I solve questions faster?",
"How can I solve difficult Physics problems?",
"How can I solve difficult Chemistry problems?",
"How can I solve difficult Maths problems?",
"What should I do when I cannot solve a question?",
"How long should I try a difficult question?",
"How can I learn from solved examples?",
"How can I improve my problem-solving approach?",
"How can I identify the correct formula?",
"How can I avoid making calculation mistakes?",
"How can I improve numerical accuracy?",
"How can I practise effectively?",
"How many questions should I practise daily?",
"How can I move from easy questions to difficult questions?",
"How can I review questions I could not solve?",
],

"Healthy Study": [
"How can I avoid feeling tired while studying?",
"How can I take effective study breaks?",
"How long should a study session be?",
"How can I sit and study comfortably?",
"How can I maintain a healthy study routine?",
"How can I avoid studying continuously without breaks?",
"How can I stay active during long study days?",
"How can I balance study and rest?",
"How can I avoid burnout during exam preparation?",
"How can I keep my study environment comfortable?",
"How can I maintain energy during study?",
"How can I avoid feeling sleepy during revision?",
"How can I organize breaks during a long study session?",
"How can I maintain a balanced daily schedule?",
"How can I make study time more productive?",
],

"Friends and Comparison": [
"I compare myself with my classmates. What should I do?",
"My friend scores more than me. How should I react?",
"How can I focus on my own improvement?",
"How can I stop worrying about other students?",
"How can I learn from high-performing students?",
"How can I compete with myself instead of others?",
"How can I handle someone getting a better rank?",
"How can I stay motivated when my friend performs better?",
"How can I avoid negative comparison?",
"How can I use competition positively?",
"How can I learn good study habits from friends?",
"How can I stay focused when others are ahead?",
"How can I measure my own progress?",
"How can I stay confident among high-performing students?",
"How can I turn comparison into motivation?",
],

"Daily Student Problems": [
"What should I study first today?",
"What should I do if I don't know where to start?",
"What should I do when today's target is incomplete?",
"What should I do if I missed a class?",
"What should I do if I don't understand today's topic?",
"What should I do when I feel too much syllabus is pending?",
"What should I do if I keep changing subjects?",
"What should I do when I cannot solve questions?",
"What should I do after finishing my homework?",
"What should I do when I have a test tomorrow?",
"What should I do if I wasted my study time?",
"What should I do if I feel tired after classes?",
"What should I do when I don't understand my mistakes?",
"What should I do when I lose concentration?",
"What should I do when I feel stuck in my preparation?",
],
}


# ============================================================
# VERIFY 300 QUESTIONS
# ============================================================

ALL_MOTIVATION_QUESTIONS = []

for category, questions in MOTIVATION_DATA.items():
    for question in questions:
        ALL_MOTIVATION_QUESTIONS.append(
            {
                "Category": category,
                "Question": question,
            }
        )

# Remove accidental duplicates while preserving order.
_seen_questions = set()
_unique_questions = []

for item in ALL_MOTIVATION_QUESTIONS:
    key = item["Question"].strip().lower()

    if key not in _seen_questions:
        _seen_questions.add(key)
        _unique_questions.append(item)

ALL_MOTIVATION_QUESTIONS = _unique_questions


# ============================================================
# MOTIVATION ANSWER ENGINE
# ============================================================

def motivation_answer(question, category):
    q = question.lower()

    if any(word in q for word in [
        "lazy",
        "motivation",
        "don't feel like",
        "do not feel like",
        "start studying",
        "procrast",
        "postpon"
    ]):
        return (
            "Do not wait until you feel motivated. Start with a very small task, "
            "such as studying for 10 minutes or completing 5 questions. "
            "Once you begin, continuing becomes easier. Keep your phone away "
            "and decide the exact task before starting."
        )

    if any(word in q for word in [
        "phone",
        "youtube",
        "social media",
        "instagram",
        "gaming",
        "screen"
    ]):
        return (
            "Create a distraction-free study session. Keep the phone away or "
            "use a study-only setting, turn off unnecessary notifications, and "
            "take planned breaks instead of checking the phone repeatedly."
        )

    if any(word in q for word in [
        "wake",
        "morning",
        "sleep",
        "sleepy",
        "tired"
    ]):
        return (
            "Keep a consistent sleep and wake time. Prepare your books and "
            "study plan the previous night. When you wake up, get out of bed "
            "immediately instead of repeatedly checking the phone."
        )

    if any(word in q for word in [
        "remember",
        "forget",
        "memory",
        "formula",
        "revise"
    ]):
        return (
            "Use active recall instead of only rereading. Close the book and "
            "try to recall the important points, formulas or steps. Review "
            "the topic again after increasing time gaps and practise questions."
        )

    if any(word in q for word in [
        "low marks",
        "bad test",
        "marks are low",
        "score",
        "rank"
    ]):
        return (
            "Do not judge your preparation only from one score. Analyse the "
            "test carefully: identify conceptual mistakes, calculation mistakes, "
            "silly mistakes, unanswered questions and time-management problems. "
            "Then choose the two most important areas to improve before the next test."
        )

    if any(word in q for word in [
        "concentr",
        "focus",
        "distract",
        "daydream"
    ]):
        return (
            "Use a short focused study block. Choose one specific task, remove "
            "distractions, and study for 25–45 minutes before taking a short break. "
            "Gradually increase the focused study time."
        )

    if any(word in q for word in [
        "backlog",
        "pending",
        "behind"
    ]):
        return (
            "Do not try to finish the entire backlog at once. List the pending "
            "topics, identify prerequisites and high-priority chapters, and "
            "complete a small number every day while continuing your current classes."
        )

    if any(word in q for word in [
        "test",
        "exam",
        "prepare"
    ]):
        return (
            "Start by listing the topics included in the test. Mark each topic "
            "as strong, average or weak. Revise the weak and important areas, "
            "practise questions, and finish with a short test-analysis review."
        )

    if any(word in q for word in [
        "confidence",
        "scared",
        "pressure",
        "nervous",
        "compare"
    ]):
        return (
            "Focus on preparation rather than comparison. Break the work into "
            "small achievable tasks and measure yourself against your previous "
            "performance. A difficult test is feedback, not a final judgment."
        )

    if any(word in q for word in [
        "note",
        "notes"
    ]):
        return (
            "Keep notes short and useful. Write formulas, definitions, key ideas, "
            "important examples and mistakes. Avoid copying the entire textbook. "
            "Your notes should make revision faster."
        )

    if any(word in q for word in [
        "fast",
        "faster",
        "reading speed"
    ]):
        return (
            "Do not sacrifice understanding just to read faster. Preview the "
            "topic first, identify headings and key ideas, then read actively. "
            "After each section, recall the main idea without looking at the book."
        )

    if any(word in q for word in [
        "math",
        "physics",
        "chemistry",
        "biology"
    ]):
        return (
            "First understand the concept, then study a worked example, and "
            "finally practise questions without looking at the solution. "
            "Record mistakes and revisit them during revision."
        )

    return (
        "Break the problem into a small action you can complete today. "
        "Make a simple plan, remove distractions, practise actively, and "
        "review your progress at the end of the study session."
    )


# ============================================================
# SEARCH MOTIVATION QUESTIONS
# ============================================================

def search_motivation_questions(query="", category="All Categories"):
    results = ALL_MOTIVATION_QUESTIONS

    if category != "All Categories":
        results = [
            x for x in results
            if x["Category"] == category
        ]

    query = str(query).strip().lower()

    if not query:
        return results

    scored = []

    for item in results:
        text = item["Question"].lower()

        score = difflib.SequenceMatcher(
            None,
            query,
            text
        ).ratio()

        query_words = set(re.findall(r"[a-zA-Z]+", query))
        text_words = set(re.findall(r"[a-zA-Z]+", text))

        overlap = len(query_words.intersection(text_words))

        score += overlap * 0.08

        if query in text:
            score += 0.5

        scored.append(
            (score, item)
        )

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item
        for score, item in scored[:20]
        if score > 0.05
    ]


# ============================================================
# CONCEPTS GOOGLE SHEET
# ============================================================

CONCEPTS_SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1UyxZabuO10HsZmD5SDWJlGI5Br57wY-VVvHA4w0eYnU/"
    "export?format=xlsx"
)


@st.cache_data(ttl=600)
def load_concepts_sheet():

    try:
        sheets = pd.read_excel(
            CONCEPTS_SHEET_URL,
            sheet_name=None,
            engine="openpyxl"
        )
    except Exception as exc:
        return pd.DataFrame(), str(exc)

    frames = []

    for sheet_name, data in sheets.items():

        if data.empty:
            continue

        data = data.copy()

        data.columns = [
            str(c).strip()
            for c in data.columns
        ]

        # Normalize common column names.
        rename_map = {}

        for col in data.columns:
            low = col.lower().strip()

            if low in [
                "topic",
                "topic name",
                "concept",
                "concept name",
            ]:
                rename_map[col] = "Topic"

            elif low in [
                "subject",
                "sub",
            ]:
                rename_map[col] = "Subject"

            elif low in [
                "definition",
                "simple definition",
                "meaning",
            ]:
                rename_map[col] = "Definition"

            elif low in [
                "example",
                "examples",
                "simple example",
            ]:
                rename_map[col] = "Example"

            elif low in [
                "explanation",
                "simple explanation",
            ]:
                rename_map[col] = "Explanation"

            elif low in [
                "important point",
                "key point",
                "key points",
            ]:
                rename_map[col] = "Key Point"

            elif low in [
                "common mistake",
                "mistake",
                "common mistakes",
            ]:
                rename_map[col] = "Common Mistake"

        data = data.rename(
            columns=rename_map
        )

        if "Topic" not in data.columns:
            continue

        data["Topic"] = (
            data["Topic"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        data = data[
            data["Topic"] != ""
        ].copy()

        if "Subject" not in data.columns:
            data["Subject"] = sheet_name

        frames.append(data)

    if not frames:
        return (
            pd.DataFrame(),
            "No Topic column was found in the Concepts Google Sheet."
        )

    concepts = pd.concat(
        frames,
        ignore_index=True
    )

    concepts = concepts.drop_duplicates(
        subset=["Topic"],
        keep="first"
    )

    return concepts.reset_index(drop=True), ""


# ============================================================
# CONCEPT SEARCH
# ============================================================

def search_concepts(concepts, query="", subject="All Subjects"):

    if concepts.empty:
        return concepts

    result = concepts.copy()

    if (
        subject != "All Subjects"
        and "Subject" in result.columns
    ):
        result = result[
            result["Subject"].astype(str) == subject
        ]

    query = str(query).strip().lower()

    if not query:
        return result

    topic_series = (
        result["Topic"]
        .fillna("")
        .astype(str)
    )

    mask = topic_series.str.lower().str.contains(
        re.escape(query),
        na=False
    )

    exact = result[mask].copy()

    if not exact.empty:
        return exact.head(50)

    scores = []

    for idx, topic in topic_series.items():

        score = difflib.SequenceMatcher(
            None,
            query,
            topic.lower()
        ).ratio()

        scores.append(
            (score, idx)
        )

    scores.sort(
        reverse=True
    )

    selected_indices = [
        idx
        for score, idx in scores[:30]
        if score > 0.15
    ]

    return result.loc[
        selected_indices
    ]


# ============================================================
# RENDER CONCEPTS TAB
# ============================================================

def render_concepts_view():

    st.markdown(
        '<div class="section-header">📚 Concepts & Examples</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Search or select a topic to see a simple definition, "
        "explanation and example."
    )

    concepts, error = load_concepts_sheet()

    if concepts.empty:

        st.warning(
            "The Concepts Google Sheet could not be loaded."
        )

        if error:
            st.caption(error)

        st.info(
            "Make sure the Google Sheet is accessible and contains "
            "a Topic column."
        )

        return

    subjects = ["All Subjects"]

    if "Subject" in concepts.columns:
        subjects += sorted(
            [
                x for x in
                concepts["Subject"]
                .dropna()
                .astype(str)
                .unique()
                if x.strip()
            ]
        )

    c1, c2 = st.columns([2, 1])

    with c1:

        concept_search = st.text_input(
            "🔎 Search Topic",
            placeholder="Type Physics, Electrolysis, Laws of Motion...",
            key="concept_search_box"
        )

    with c2:

        selected_subject = st.selectbox(
            "Subject",
            subjects,
            key="concept_subject_filter"
        )

    filtered = search_concepts(
        concepts,
        concept_search,
        selected_subject
    )

    if filtered.empty:
        st.info(
            "No matching topic found. Try another topic name."
        )
        return

    topic_options = filtered[
        "Topic"
    ].astype(str).tolist()

    selected_topic = st.selectbox(
        "📌 Select Topic",
        topic_options,
        key="selected_concept_topic"
    )

    selected = filtered[
        filtered["Topic"].astype(str) == selected_topic
    ]

    if selected.empty:
        return

    row = selected.iloc[0]

    st.markdown("---")

    st.markdown(
        f"### 📌 {row['Topic']}"
    )

    if "Subject" in row.index:
        subject_value = str(row["Subject"]).strip()

        if subject_value:
            st.caption(
                f"Subject: {subject_value}"
            )

    if "Definition" in row.index:
        value = str(row["Definition"]).strip()

        if value and value.lower() != "nan":
            st.markdown(
                "#### 📖 Simple Definition"
            )
            st.info(value)

    if "Explanation" in row.index:
        value = str(row["Explanation"]).strip()

        if value and value.lower() != "nan":
            st.markdown(
                "#### 💡 Easy Explanation"
            )
            st.write(value)

    if "Example" in row.index:
        value = str(row["Example"]).strip()

        if value and value.lower() != "nan":
            st.markdown(
                "#### 🧪 Example"
            )
            st.success(value)

    if "Key Point" in row.index:
        value = str(row["Key Point"]).strip()

        if value and value.lower() != "nan":
            st.markdown(
                "#### ⭐ Key Point"
            )
            st.write(value)

    if "Common Mistake" in row.index:
        value = str(row["Common Mistake"]).strip()

        if value and value.lower() != "nan":
            st.markdown(
                "#### ⚠️ Common Mistake"
            )
            st.warning(value)


# ============================================================
# RENDER MOTIVATION TAB
# ============================================================

def render_motivation_view():

    st.markdown(
        '<div class="section-header">💡 Motivation & Study Help</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Ask a normal student-study question or select one from "
        "the 300+ study-help questions."
    )

    st.info(
        f"📚 {len(ALL_MOTIVATION_QUESTIONS)} student-safe "
        "questions are available."
    )

    categories = [
        "All Categories"
    ] + list(
        MOTIVATION_DATA.keys()
    )

    selected_category = st.selectbox(
        "📂 Select Category",
        categories,
        key="motivation_category"
    )

    typed_question = st.text_input(
        "✍️ Type your own question",
        placeholder=(
            "Example: I study Physics but forget the formulas..."
        ),
        key="motivation_typed_question"
    )

    search_question = st.text_input(
        "🔎 Search Questions",
        placeholder="Search motivation or study questions...",
        key="motivation_search_question"
    )

    if typed_question.strip():

        st.markdown("---")

        st.markdown(
            "### ✍️ Your Question"
        )

        st.write(
            typed_question
        )

        st.markdown(
            "### 💡 Suggested Guidance"
        )

        st.success(
            motivation_answer(
                typed_question,
                selected_category
            )
        )

    query = (
        search_question
        if search_question.strip()
        else typed_question
    )

    results = search_motivation_questions(
        query,
        selected_category
    )

    if not query.strip():
        results = results[:30]

    st.markdown("---")

    st.markdown(
        "### 📚 Select a Question"
    )

    if not results:

        st.info(
            "No matching question found. "
            "Try different words."
        )

        return

    question_labels = [
        f"{x['Category']} — {x['Question']}"
        for x in results
    ]

    selected_label = st.selectbox(
        "Choose a question",
        question_labels,
        key="selected_motivation_question"
    )

    selected_index = question_labels.index(
        selected_label
    )

    selected_item = results[selected_index]

    st.markdown("---")

    st.markdown(
        f"### ❓ {selected_item['Question']}"
    )

    st.caption(
        f"Category: {selected_item['Category']}"
    )

    st.markdown(
        "### 💡 Suggested Guidance"
    )

    st.success(
        motivation_answer(
            selected_item["Question"],
            selected_item["Category"]
        )
    )


# ============================================================
# TOP 5 BEST RANKS
# ============================================================

def calculate_top_5_ranks(student_data, is_neet):

    if student_data.empty:
        return pd.DataFrame()

    subjects = (
        ["Physics", "Chemistry", "Biology"]
        if is_neet
        else ["Physics", "Chemistry", "Maths"]
    )

    records = []

    for subject in subjects:

        if subject not in student_data.columns:
            continue

        for _, student_row in student_data.iterrows():

            value = pd.to_numeric(
                student_row.get(subject),
                errors="coerce"
            )

            if pd.isna(value):
                continue

            batch = student_row.get(
                "Classroom",
                ""
            )

            test_name = str(
                student_row.get(
                    "Test Name",
                    ""
                )
            )

            category = str(
                student_row.get(
                    "Category",
                    ""
                )
            )

            # Find all students from same batch/test/category.
            all_data = st.session_state.get(
                "_dashboard_full_df"
            )

            if all_data is None or all_data.empty:
                continue

            comparison = all_data[
                (all_data["Classroom"] == batch)
                &
                (all_data["Test Name"].astype(str) == test_name)
                &
                (all_data["Category"].astype(str) == category)
            ].copy()

            if subject not in comparison.columns:
                continue

            comparison[subject] = pd.to_numeric(
                comparison[subject],
                errors="coerce"
            )

            comparison = comparison.dropna(
                subset=[subject]
            )

            if comparison.empty:
                continue

            rank = (
                comparison[subject]
                .rank(
                    ascending=False,
                    method="min"
                )
            )

            student_key = student_row.get(
                "Student Key"
            )

            matching = comparison[
                comparison["Student Key"] == student_key
            ]

            if matching.empty:
                continue

            rank_value = rank.loc[
                matching.index[0]
            ]

            if pd.isna(rank_value):
                continue

            records.append(
                {
                    "Rank": int(rank_value),
                    "Subject": subject,
                    "Test": test_name,
                    "Category": category,
                    "Marks": float(value),
                }
            )

    if not records:
        return pd.DataFrame()

    result = pd.DataFrame(records)

    # Best rank = smallest number.
    result = result.sort_values(
        by=[
            "Rank",
            "Test"
        ],
        ascending=[
            True,
            False
        ]
    )

    # If same rank/subject/test is repeated, keep one.
    result = result.drop_duplicates(
        subset=[
            "Rank",
            "Subject",
            "Test"
        ],
        keep="first"
    )

    # ONLY FIVE BEST ACHIEVEMENTS.
    return result.head(5).reset_index(drop=True)


def render_top_5_student_ranks(
    student_data,
    student_name,
    is_neet
):

    st.markdown(
        f"### 👋 Hi, {student_name}!"
    )

    top5 = calculate_top_5_ranks(
        student_data,
        is_neet
    )

    if top5.empty:

        st.info(
            "Your rank achievements will appear here "
            "when subject-wise test ranking data is available."
        )

        return

    st.markdown(
        "### 🏆 Your Top 5 Rank Achievements"
    )

    rank_rows = []

    medals = {
        1: "🥇",
        2: "🥈",
        3: "🥉",
    }

    for _, row in top5.iterrows():

        rank_number = int(
            row["Rank"]
        )

        rank_display = medals.get(
            rank_number,
            f"#{rank_number}"
        )

        rank_rows.append(
            {
                "Rank": rank_display,
                "Subject": row["Subject"],
                "Test": row["Test"],
                "Marks": int(round(row["Marks"])),
            }
        )

    rank_display_df = pd.DataFrame(
        rank_rows
    )

    st.dataframe(
        rank_display_df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Rank": st.column_config.TextColumn(
                "🏆 Rank"
            ),
            "Subject": st.column_config.TextColumn(
                "Subject"
            ),
            "Test": st.column_config.TextColumn(
                "Test"
            ),
            "Marks": st.column_config.NumberColumn(
                "Marks"
            ),
        },
    )


# ============================================================
# REPLACE STUDENT DATA VIEW
# ============================================================

_original_student_data_view = render_student_data_view


def render_student_data_view(batch_data, selected_batch):

    is_neet = (
        "NEET"
        in selected_batch.upper()
    )

    students = sorted(
        batch_data[
            "Student Name"
        ]
        .astype(str)
        .unique()
    )

    if not students:

        st.warning(
            "No students found in this batch."
        )

        return

    selected_student = st.selectbox(
        "Select Student Name:",
        students,
        index=0,
        key="student_name_dropdown"
    )

    student_data = (
        batch_data[
            batch_data["Student Name"]
            == selected_student
        ]
        .copy()
        .drop_duplicates(
            subset=[
                "Student Key",
                "Test Name",
                "Category"
            ],
            keep="last"
        )
    )

    # --------------------------------------------
    # BEST 5 RANKS BEFORE MARKS
    # --------------------------------------------

    render_top_5_student_ranks(
        student_data,
        selected_student,
        is_neet
    )

    st.markdown("---")

    # --------------------------------------------
    # EXISTING MARKS DASHBOARD
    # --------------------------------------------

    _original_student_data_view(
        batch_data[
            batch_data["Student Name"]
            == selected_student
        ].copy(),
        selected_batch
    )


# ============================================================
# REPLACE MAIN
# ============================================================

_original_main = main


def main():

    # Existing source creates df internally.
    # We need access to it for rank calculations.
    # Therefore use the existing loader directly.

    st.markdown(
        '<div class="main-header">'
        'Student Performance Dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    with st.spinner(
        "Loading data from Google Sheets..."
    ):
        df = load_and_process_data()

    if df.empty:

        st.warning(
            "No data found matching the supplied student roster."
        )

        return

    # Store globally for Top 5 rank calculations.
    st.session_state[
        "_dashboard_full_df"
    ] = df.copy()

    if "nav_mode" not in st.session_state:
        st.session_state[
            "nav_mode"
        ] = "student"

    # --------------------------------------------------------
    # 7 BUTTONS
    # --------------------------------------------------------

    b1, b2, b3, b4, b5, b6, b7 = st.columns(7)

    with b1:

        if st.button(
            "🔄 Refresh",
            use_container_width=True
        ):

            load_and_process_data.clear()
            load_concepts_sheet.clear()

            st.rerun()

    with b2:

        if st.button(
            "👤 Student Data",
            use_container_width=True
        ):

            st.session_state[
                "nav_mode"
            ] = "student"

    with b3:

        if st.button(
            "📊 Batch Analysis",
            use_container_width=True
        ):

            st.session_state[
                "nav_mode"
            ] = "batch"

    with b4:

        if st.button(
            "🏆 Top Performers",
            use_container_width=True
        ):

            st.session_state[
                "nav_mode"
            ] = "topper"

    with b5:

        if st.button(
            "🔎 Search Student",
            use_container_width=True
        ):

            st.session_state[
                "nav_mode"
            ] = "search"

    with b6:

        if st.button(
            "💡 Motivation",
            use_container_width=True
        ):

            st.session_state[
                "nav_mode"
            ] = "motivation"

    with b7:

        if st.button(
            "📚 Concepts",
            use_container_width=True
        ):

            st.session_state[
                "nav_mode"
            ] = "concepts"

    st.markdown("---")

    # --------------------------------------------------------
    # MOTIVATION
    # --------------------------------------------------------

    if st.session_state[
        "nav_mode"
    ] == "motivation":

        render_motivation_view()

        return

    # --------------------------------------------------------
    # CONCEPTS
    # --------------------------------------------------------

    if st.session_state[
        "nav_mode"
    ] == "concepts":

        render_concepts_view()

        return

    # --------------------------------------------------------
    # SEARCH STUDENT
    # --------------------------------------------------------

    if st.session_state[
        "nav_mode"
    ] == "search":

        render_student_search_view(
            df
        )

        return

    # --------------------------------------------------------
    # BATCH LIST
    # --------------------------------------------------------

    ordered_batches = [
        "Sankalp-JEE-WD-Madhapur-(26-27)-A",
        "Dhristi-JEE-WD-Madhapur-(26-27)-A",
        "Dhristi-JEE-WD-Madhapur-(26-27)-C",
        "Dhristi-NEET-WD-Madhapur-(26-27)-A",
        "Dhristi-JEE-WD-Madhapur-(26-27)-E",
    ]

    available_batches = set(
        df[
            "Classroom"
        ]
        .astype(str)
        .unique()
    )

    batches = [
        batch
        for batch in ordered_batches
        if batch in available_batches
    ]

    if not batches:

        st.warning(
            "No batches available."
        )

        return

    selected_batch = st.selectbox(
        "Select Batch / Classroom:",
        batches,
        key="main_batch_selector"
    )

    batch_data = df[
        df["Classroom"]
        == selected_batch
    ].copy()

    is_neet = (
        "NEET"
        in selected_batch.upper()
    )

    # --------------------------------------------------------
    # BATCH ANALYSIS
    # --------------------------------------------------------

    if st.session_state[
        "nav_mode"
    ] == "batch":

        render_batch_analysis_view(
            batch_data,
            is_neet
        )

    # --------------------------------------------------------
    # TOP PERFORMERS
    # --------------------------------------------------------

    elif st.session_state[
        "nav_mode"
    ] == "topper":

        render_top_performers_view(
            batch_data,
            is_neet
        )

    # --------------------------------------------------------
    # STUDENT DATA
    # --------------------------------------------------------

    else:

        render_student_data_view(
            batch_data,
            selected_batch
        )


# ============================================================
# RUN
# ============================================================

main()
'''


# ------------------------------------------------------------
# Inject the extension immediately before the original
# "__main__" execution block.
# ------------------------------------------------------------

marker = 'if __name__ == "__main__":'

if marker not in source:
    st.error(
        "Unable to locate the dashboard main execution block."
    )
    st.stop()

source = source.replace(
    marker,
    extra_code + "\n\n" + marker,
    1,
)


# ============================================================
# EXECUTE FINAL DASHBOARD
# ============================================================

try:
    exec(
        compile(
            source,
            "main.py",
            "exec"
        ),
        globals(),
        globals()
    )

except Exception as exc:

    st.error(
        "Dashboard startup error:"
    )

    st.exception(exc)
