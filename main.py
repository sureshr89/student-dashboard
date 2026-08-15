import urllib.request
import re
import difflib
import pandas as pd
import streamlit as st

# Load the original dashboard functions/data, but prevent its original main() from running.
SRC = 'https://raw.githubusercontent.com/sureshr89/student-dashboard/643305bc8243a7a4a997af10070a1936e5f09609/main.py'
try:
    source = urllib.request.urlopen(SRC, timeout=20).read().decode('utf-8')
except Exception as e:
    st.error(f'Unable to load dashboard source: {e}')
    st.stop()

old = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {\n            "v_4102643666550411": "Jampala Shanthan Kumar",\n            "v_4102439835972285": "P Rohith",\n            "v_4102643721870649": "Punem Abhinav Sidhardha",\n            "v_4102644496422857": "G Rishith Kumar",\n'''
new = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {\n            "v_4102643666550411": "Jampala Shanthan Kumar",\n            "v_4102439835972285": "P Rohith",\n            "v_4102643721870649": "Punem Abhinav Sidhardha",\n'''
source = source.replace(old, new, 1)
source = re.sub(r'if __name__\s*==\s*["\']__main__["\']\s*:\s*\n\s*main\(\)\s*$', '# original main disabled\n', source, flags=re.M)
source = source.replace("if __name__ == '__main__':\n    main()\n", '# original main disabled\n')
source = source.replace('if __name__ == "__main__":\n    main()\n', '# original main disabled\n')
exec(compile(source, 'original_dashboard.py', 'exec'), globals(), globals())

# ============================================================
# STUDENT-SAFE MOTIVATION LIBRARY — 300 QUESTIONS
# ============================================================
TOPICS = {
    'Study Motivation': ['lazy', 'motivation', 'start studying', 'procrastination', 'postpone'],
    'Concentration': ['focus', 'concentration', 'distracted', 'attention', 'daydream'],
    'Time Management': ['time', 'timetable', 'schedule', 'planning', 'manage time'],
    'Wake Up and Routine': ['wake', 'early', 'morning', 'sleep', 'routine', 'tired'],
    'Phone and Distractions': ['phone', 'youtube', 'social media', 'gaming', 'screen', 'distraction'],
    'Reading and Study Speed': ['read', 'reading', 'fast', 'speed', 'slow reading', 'understand quickly'],
    'Notes': ['notes', 'notebook', 'short notes', 'formula notes', 'revision notes'],
    'Memory': ['memory', 'remember', 'forget', 'memorise', 'recall'],
    'Revision': ['revision', 'revise', 'review', 'repeat', 'revising'],
    'Backlog': ['backlog', 'pending', 'chapters left', 'behind', 'missed classes'],
    'Test Preparation': ['test', 'exam', 'prepare', 'preparation', 'mock test'],
    'Test Analysis': ['test analysis', 'mistakes', 'wrong answers', 'silly mistakes', 'accuracy'],
    'Low Marks': ['low marks', 'low score', 'marks', 'score', 'improve marks'],
    'Exam Confidence': ['confidence', 'scared', 'nervous', 'pressure', 'panic', 'exam fear'],
    'Goals': ['goal', 'target', 'progress', 'achievement'],
    'Discipline and Habits': ['discipline', 'habit', 'consistent', 'consistency', 'routine'],
    'Subject Improvement': ['physics', 'chemistry', 'maths', 'math', 'biology', 'weak subject'],
    'Problem Solving': ['problem', 'solve', 'questions', 'numerical', 'calculation'],
    'Healthy Study': ['break', 'rest', 'tired', 'energy', 'study balance'],
    'Friends and Comparison': ['friends', 'compare', 'comparison', 'rank', 'competition'],
}

QUESTION_TEMPLATES = [
    'How can I improve this?',
    'How can I get better at this?',
    'What should I do about this?',
    'How can I start improving this?',
    'What is a simple way to handle this?',
    'How can I make this easier?',
    'How can I improve this every day?',
    'Can you give me a simple plan for this?',
    'What should I do if I struggle with this?',
    'What mistakes should I avoid here?',
    'How can I practise this effectively?',
    'What can I do today to improve this?',
    'How can I stay consistent with this?',
    'How can I improve this without wasting time?',
    'What is the best student-friendly way to improve this?',
]

# Use natural questions instead of only generic generated wording.
NATURAL_QUESTIONS = {
    'Study Motivation': [
        'How can I study when I feel lazy?', 'How can I start studying immediately?',
        'What should I do when I have no motivation to study?', 'How can I stop procrastinating?',
        'How can I study every day without waiting for motivation?', 'How can I stop postponing my studies?',
        'How can I make studying a daily habit?', 'How can I study when the subject feels boring?',
    ],
    'Concentration': [
        'How can I concentrate while studying?', 'How can I focus for one hour?',
        'Why do I lose concentration quickly?', 'How can I stop my mind from wandering?',
        'How can I avoid daydreaming while studying?', 'How can I study without distractions?',
        'How can I improve my attention span?', 'How can I focus on difficult chapters?',
    ],
    'Time Management': [
        'How can I make a study timetable?', 'How can I manage school and coaching?',
        'How should I divide time between subjects?', 'How can I stop wasting time?',
        'How can I finish my syllabus on time?', 'How can I plan my study week?',
        'How can I manage revision and new chapters?', 'How can I complete daily targets?',
    ],
    'Wake Up and Routine': [
        'How can I wake up early?', 'How can I stop pressing snooze?',
        'How can I sleep on time?', 'How can I build a good morning routine?',
        'How can I stop feeling sleepy while studying?', 'How can I maintain a regular routine?',
        'How can I balance sleep and study?', 'How can I make my mornings productive?',
    ],
    'Phone and Distractions': [
        'How can I reduce my phone usage?', 'How can I stop checking my phone while studying?',
        'How can I reduce YouTube distractions?', 'How can I control social media while studying?',
        'How can I stop gaming during study hours?', 'How can I create a phone-free study session?',
        'How can I reduce screen time?', 'How can I study without checking notifications?',
    ],
    'Reading and Study Speed': [
        'How can I read faster?', 'How can I understand a chapter quickly?',
        'How can I improve my reading speed?', 'How can I study faster without losing understanding?',
        'How can I read textbooks effectively?', 'How can I avoid reading the same line repeatedly?',
        'How can I remember what I read?', 'How can I understand difficult paragraphs faster?',
    ],
    'Notes': [
        'How should I make short notes?', 'How can I make useful revision notes?',
        'What should I write in my notes?', 'How can I make formula notes?',
        'How can I organize my notes?', 'How can I make one-page revision notes?',
        'How can I make notes without wasting time?', 'How can I make notes that are easy to revise?',
    ],
    'Memory': [
        'Why do I forget what I studied?', 'How can I improve my memory?',
        'How can I remember formulas?', 'How can I remember important concepts?',
        'How can I use active recall?', 'How can I remember what I studied yesterday?',
        'How can I stop forgetting after studying?', 'How can I improve long-term memory for exams?',
    ],
    'Revision': [
        'How should I revise a chapter?', 'How often should I revise?',
        'How can I revise before a test?', 'How can I revise weak topics?',
        'How can I revise without getting bored?', 'How can I make a revision schedule?',
        'How can I revise formulas quickly?', 'How can I check whether my revision is effective?',
    ],
    'Backlog': [
        'How can I complete my study backlog?', 'What should I do if many chapters are pending?',
        'How can I start my backlog without feeling overwhelmed?', 'How can I clear my Physics backlog?',
        'How can I balance backlog and current classes?', 'How can I stop creating new backlog?',
        'How can I recover after falling behind?', 'How can I complete a large backlog?',
    ],
    'Test Preparation': [
        'How should I prepare for a test?', 'What should I do one day before a test?',
        'How should I prepare for a mock test?', 'How can I prepare for a difficult test?',
        'How can I prepare for a full syllabus test?', 'How can I divide preparation between subjects?',
        'How can I avoid panic before a test?', 'How can I prepare formulas before a test?',
    ],
    'Test Analysis': [
        'How should I analyse my test?', 'What should I do after getting low marks?',
        'How can I identify my mistakes?', 'How can I reduce silly mistakes?',
        'How can I improve my accuracy?', 'How can I improve after every test?',
        'How can I identify my weak chapters?', 'How can I avoid repeating the same mistake?',
    ],
    'Low Marks': [
        'My marks are low. What should I do?', 'I studied but still got low marks. Why?',
        'How can I improve my marks?', 'What should I do after a bad test?',
        'Why are my marks not improving?', 'How can I increase my score gradually?',
        'How can I stop losing marks unnecessarily?', 'How can I make a plan after low marks?',
    ],
    'Exam Confidence': [
        'I feel scared before exams. What should I do?', 'How can I stay calm before an exam?',
        'How can I improve my confidence?', 'I lose confidence after low marks. What should I do?',
        'How can I stop worrying about my rank?', 'How can I handle exam pressure?',
        'How can I avoid panic during an exam?', 'How can I trust my preparation?',
    ],
    'Goals': [
        'How can I set a study goal?', 'How can I set realistic academic goals?',
        'How can I track my study goals?', 'How can I create weekly goals?',
        'How can I break a big goal into small tasks?', 'How can I measure my progress?',
        'How can I create a target for my next test?', 'How can I stay focused on my target?',
    ],
    'Discipline and Habits': [
        'How can I become more disciplined?', 'How can I build a study habit?',
        'How can I study at the same time every day?', 'How can I stop making excuses?',
        'How can I maintain consistency?', 'How can I develop better academic habits?',
        'How can I avoid skipping study sessions?', 'How can I return to my routine after a break?',
    ],
    'Subject Improvement': [
        'How can I improve Physics?', 'How can I improve Chemistry?',
        'How can I improve Maths?', 'How can I improve Biology?',
        'How can I identify my weakest subject?', 'How can I improve conceptual understanding?',
        'How can I improve numerical problem solving?', 'How can I become stronger in my weakest topic?',
    ],
    'Problem Solving': [
        'How can I solve questions faster?', 'How can I solve difficult Physics problems?',
        'How can I solve difficult Chemistry problems?', 'How can I solve difficult Maths problems?',
        'What should I do when I cannot solve a question?', 'How can I improve my problem-solving approach?',
        'How can I avoid calculation mistakes?', 'How can I review questions I could not solve?',
    ],
    'Healthy Study': [
        'How can I avoid feeling tired while studying?', 'How can I take effective study breaks?',
        'How long should a study session be?', 'How can I balance study and rest?',
        'How can I avoid burnout during exam preparation?', 'How can I stay active during long study days?',
        'How can I avoid feeling sleepy during revision?', 'How can I make study time more productive?',
    ],
    'Friends and Comparison': [
        'I compare myself with my classmates. What should I do?', 'My friend scores more than me. How should I react?',
        'How can I focus on my own improvement?', 'How can I stop worrying about other students?',
        'How can I learn from high-performing students?', 'How can I stay motivated when my friend performs better?',
        'How can I avoid negative comparison?', 'How can I measure my own progress?',
    ],
}

MOTIVATION = []
for category, keywords in TOPICS.items():
    for question in NATURAL_QUESTIONS.get(category, []):
        MOTIVATION.append({'Category': category, 'Question': question, 'Keywords': ' '.join(keywords)})
    base = NATURAL_QUESTIONS.get(category, [])
    for i, template in enumerate(QUESTION_TEMPLATES):
        if len(MOTIVATION) >= 300:
            break
        seed = keywords[i % len(keywords)]
        MOTIVATION.append({'Category': category, 'Question': template.replace('this', seed), 'Keywords': ' '.join(keywords)})

# Ensure exactly 300 unique questions.
_unique = {}
for item in MOTIVATION:
    _unique.setdefault(item['Question'].lower(), item)
MOTIVATION = list(_unique.values())[:300]


def advice(q):
    q = q.lower()
    if any(x in q for x in ('lazy', 'motivation', 'start studying', 'procrast')):
        return 'Start with one small task for 10 minutes. Decide the exact task, remove distractions and begin. Do not wait for motivation; action often creates motivation.'
    if any(x in q for x in ('phone', 'youtube', 'social media', 'gaming', 'screen', 'distraction')):
        return 'Keep the phone away during focused study time, turn off unnecessary notifications and use planned breaks. Use the phone only for required learning material.'
    if any(x in q for x in ('wake', 'morning', 'sleep', 'tired')):
        return 'Keep a consistent sleep and wake time. Prepare your books the night before and start the morning with one small planned study task.'
    if any(x in q for x in ('remember', 'memory', 'revise', 'formula')):
        return 'Use active recall: close the book and reproduce the idea, formula or steps from memory. Check your answer and revisit the topic later.'
    if any(x in q for x in ('marks', 'score', 'rank', 'test', 'exam')):
        return 'Analyse the result instead of judging yourself. Separate conceptual, calculation, silly and time-management mistakes, then choose the most important areas to improve.'
    if any(x in q for x in ('concentr', 'focus', 'distract')):
        return 'Choose one clear task, remove distractions and study in a focused block of about 25–45 minutes followed by a short break. Increase gradually.'
    if any(x in q for x in ('backlog', 'pending', 'behind')):
        return 'List pending chapters, identify prerequisites and high-priority topics, and complete a small number each day while continuing current classes.'
    if any(x in q for x in ('confidence', 'scared', 'pressure', 'nervous', 'compare')):
        return 'Focus on preparation and your own progress rather than comparison. Break the work into small achievable tasks and use difficult tests as feedback.'
    return 'Break the problem into one small action you can complete today. Make a simple plan, remove distractions, practise actively and review your progress.'


def expand_search(q):
    q = q.lower().strip()
    aliases = {
        'lazy': ['lazy', 'motivation', 'start studying', 'procrastination', 'discipline', 'habit'],
        'motivation': ['motivation', 'lazy', 'start studying', 'procrastination', 'discipline'],
        'fast': ['fast', 'speed', 'read faster', 'reading', 'study faster'],
        'read': ['read', 'reading', 'fast', 'speed', 'understand'],
        'sleep': ['sleep', 'wake', 'morning', 'tired', 'routine'],
        'wake': ['wake', 'early', 'morning', 'sleep', 'routine'],
        'phone': ['phone', 'youtube', 'social media', 'screen', 'distraction'],
        'focus': ['focus', 'concentration', 'attention', 'distraction'],
        'study': ['study', 'motivation', 'concentration', 'time', 'revision', 'notes'],
        'marks': ['marks', 'score', 'test', 'mistakes', 'accuracy'],
        'rank': ['rank', 'marks', 'comparison', 'competition', 'test'],
        'math': ['math', 'maths', 'problem solving', 'questions'],
        'physics': ['physics', 'problem solving', 'numerical'],
        'chemistry': ['chemistry', 'revision', 'formula'],
        'backlog': ['backlog', 'pending', 'behind', 'chapters'],
    }
    words = set(re.findall(r'[a-z]+', q))
    expanded = [q]
    for word in words:
        expanded.extend(aliases.get(word, []))
    return list(dict.fromkeys(expanded))


def motivation_score(query, item):
    queries = expand_search(query)
    question = item['Question'].lower()
    keywords = item['Keywords'].lower()
    score = 0.0
    for q in queries:
        q_words = set(re.findall(r'[a-z]+', q))
        text_words = set(re.findall(r'[a-z]+', question + ' ' + keywords))
        score = max(score, difflib.SequenceMatcher(None, q, question).ratio() + 0.18 * len(q_words & text_words))
        if q in question or q in keywords:
            score += 0.75
    return score


def render_motivation():
    st.markdown('## 💡 Motivation & Study Help')
    st.caption('Type just one word. Related questions appear immediately — like a simple Google-style search.')
    query = st.text_input('Search motivation', placeholder='Try: lazy  •  sleep  •  focus  •  fast  •  phone  •  marks', key='motivation_single_search', label_visibility='collapsed')
    if not query.strip():
        st.info('Start typing a keyword to see related student questions.')
        return
    ranked = sorted(((motivation_score(query, item), item) for item in MOTIVATION), key=lambda z: z[0], reverse=True)
    matches = [item for score, item in ranked[:10] if score > 0.10]
    if not matches:
        st.info('No close match yet. Try: lazy, study, focus, sleep, phone, fast, marks, exam, backlog.')
        st.markdown('### 💡 Quick Guidance')
        st.success(advice(query))
        return
    st.markdown('### 🔎 Related Questions')
    current = st.session_state.get('mot_selected_question')
    visible_questions = {x['Question'] for x in matches}
    if current not in visible_questions:
        st.session_state.pop('mot_selected_question', None)
    for i, item in enumerate(matches):
        if st.button(f"{item['Question']}", key=f'mot_result_{i}', use_container_width=True):
            st.session_state['mot_selected_question'] = item['Question']
    selected = st.session_state.get('mot_selected_question')
    if selected:
        chosen = next((x for x in matches if x['Question'] == selected), None)
        if chosen:
            st.markdown(f"### 💡 {chosen['Category']}")
            st.success(advice(chosen['Question']))
    else:
        st.markdown('### 💡 Quick Guidance')
        st.success(advice(query))


# ============================================================
# CONCEPTS — SEARCH TOPIC + ALL CONTENT, NOT JUST TITLE
# ============================================================
CONCEPTS_URL = 'https://docs.google.com/spreadsheets/d/1UyxZabuO10HsZmD5SDWJlGI5Br57wY-VVvHA4w0eYnU/export?format=xlsx'

@st.cache_data(ttl=600)
def load_concepts():
    try:
        sheets = pd.read_excel(CONCEPTS_URL, sheet_name=None, engine='openpyxl')
    except Exception as e:
        return pd.DataFrame(), str(e)
    out = []
    mappings = [
        (['topic', 'topic name', 'concept', 'concept name'], 'Topic'),
        (['subject', 'sub'], 'Subject'),
        (['definition', 'simple definition', 'meaning'], 'Definition'),
        (['example', 'examples', 'simple example'], 'Example'),
        (['explanation', 'simple explanation'], 'Explanation'),
        (['important point', 'key point', 'key points'], 'Key Point'),
        (['common mistake', 'mistake', 'common mistakes'], 'Common Mistake'),
    ]
    for sheet, d in sheets.items():
        if d.empty:
            continue
        d = d.copy()
        d.columns = [str(c).strip() for c in d.columns]
        rename = {}
        for c in d.columns:
            for names, target in mappings:
                if c.lower().strip() in names:
                    rename[c] = target
                    break
        d = d.rename(columns=rename)
        if 'Topic' not in d.columns:
            continue
        d['Topic'] = d['Topic'].fillna('').astype(str).str.strip()
        d = d[d['Topic'] != ''].copy()
        if 'Subject' not in d.columns:
            d['Subject'] = sheet
        out.append(d)
    if not out:
        return pd.DataFrame(), 'No Topic column found in the Concepts sheet.'
    return pd.concat(out, ignore_index=True).drop_duplicates('Topic').reset_index(drop=True), ''


def concept_score(query, row):
    q = query.lower().strip()
    parts = []
    for col in ('Topic', 'Subject', 'Definition', 'Explanation', 'Example', 'Key Point', 'Common Mistake'):
        if col in row.index:
            parts.append(str(row[col]))
    text = ' '.join(parts).lower()
    q_words = set(re.findall(r'[a-z]+', q))
    text_words = set(re.findall(r'[a-z]+', text))
    score = difflib.SequenceMatcher(None, q, str(row['Topic']).lower()).ratio()
    score += 0.15 * len(q_words & text_words)
    if q in str(row['Topic']).lower():
        score += 1.0
    if q in text:
        score += 0.5
    return score


def render_concepts():
    st.markdown('## 📚 Concepts & Examples')
    st.caption('Type one word or a few letters. Matching topics appear immediately.')
    df, err = load_concepts()
    if df.empty:
        st.warning('The Concepts Google Sheet could not be loaded.')
        st.caption(err)
        return
    query = st.text_input('Search concept', placeholder="Try: electrolysis  •  mole  •  force  •  motion  •  equilibrium", key='concept_single_search', label_visibility='collapsed')
    if not query.strip():
        st.info(f'📚 {len(df)} concepts available. Start typing a topic keyword.')
        return
    ranked = sorted(((concept_score(query, row), idx) for idx, row in df.iterrows()), key=lambda z: z[0], reverse=True)
    indices = [idx for score, idx in ranked[:10] if score > 0.15]
    matches = df.loc[indices].copy()
    if matches.empty:
        st.info('No matching concept yet. Try a broader keyword.')
        return
    st.markdown('### 🔎 Related Topics')
    current = st.session_state.get('concept_selected_topic')
    visible_topics = set(matches['Topic'].astype(str))
    if current not in visible_topics:
        st.session_state.pop('concept_selected_topic', None)
    for i, (_, row) in enumerate(matches.iterrows()):
        subject = str(row.get('Subject', '')).strip()
        label = str(row['Topic']) + (f'  ·  {subject}' if subject and subject.lower() != 'nan' else '')
        if st.button(label, key=f'concept_result_{i}', use_container_width=True):
            st.session_state['concept_selected_topic'] = str(row['Topic'])
    selected = st.session_state.get('concept_selected_topic')
    if not selected:
        return
    row = matches[matches['Topic'].astype(str) == selected].iloc[0]
    st.markdown(f"### 📌 {row['Topic']}")
    for title, col, kind in [
        ('📖 Simple Definition', 'Definition', 'info'),
        ('💡 Easy Explanation', 'Explanation', 'write'),
        ('🧪 Example', 'Example', 'success'),
        ('⭐ Key Point', 'Key Point', 'write'),
        ('⚠️ Common Mistake', 'Common Mistake', 'warning'),
    ]:
        if col not in row.index:
            continue
        value = str(row[col]).strip()
        if not value or value.lower() == 'nan':
            continue
        st.markdown(f'#### {title}')
        {'info': st.info, 'success': st.success, 'warning': st.warning, 'write': st.write}[kind](value)


# ============================================================
# TOP 5 BEST SUBJECT-WISE RANKS
# ============================================================
def top5(data, neet):
    full = st.session_state.get('_dashboard_full_df')
    if data.empty or full is None:
        return pd.DataFrame()
    subjects = ['Physics', 'Chemistry', 'Biology'] if neet else ['Physics', 'Chemistry', 'Maths']
    student_key = data.iloc[0].get('Student Key')
    rows = []
    for _, r in data.iterrows():
        comp = full[(full['Classroom'].astype(str) == str(r.get('Classroom', ''))) & (full['Test Name'].astype(str) == str(r.get('Test Name', ''))) & (full['Category'].astype(str) == str(r.get('Category', '')))].copy()
        for subject in subjects:
            if subject not in comp.columns:
                continue
            marks = pd.to_numeric(r.get(subject), errors='coerce')
            if pd.isna(marks):
                continue
            comp[subject] = pd.to_numeric(comp[subject], errors='coerce')
            comp = comp.dropna(subset=[subject])
            if comp.empty:
                continue
            comp['_rank'] = comp[subject].rank(method='min', ascending=False).astype(int)
            hit = comp[comp['Student Key'] == student_key]
            if not hit.empty:
                rows.append({'Rank': int(hit.iloc[0]['_rank']), 'Subject': subject, 'Test': str(r.get('Test Name', '')), 'Marks': float(marks)})
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows).sort_values(['Rank', 'Test'], ascending=[True, False]).drop_duplicates(['Rank', 'Subject', 'Test']).head(5).reset_index(drop=True)


def render_student(data, batch):
    neet = 'NEET' in batch.upper()
    students = sorted(data['Student Name'].astype(str).unique())
    if not students:
        st.warning('No students found in this batch.')
        return
    name = st.selectbox('Select Student Name:', students, key='student_data_selector')
    sd = data[data['Student Name'] == name].copy().drop_duplicates(['Student Key', 'Test Name', 'Category'], keep='last')
    st.markdown(f'### 👋 Hi, {name}!')
    ranks = top5(sd, neet)
    if ranks.empty:
        st.info('Your Top 5 rank achievements will appear here when subject-wise ranking data is available.')
    else:
        st.markdown('### 🏆 Your Top 5 Rank Achievements')
        medals = {1: '🥇', 2: '🥈', 3: '🥉'}
        st.dataframe(pd.DataFrame([{'Rank': medals.get(int(x.Rank), f'#{int(x.Rank)}'), 'Subject': x.Subject, 'Test': x.Test, 'Marks': int(round(x.Marks))} for _, x in ranks.iterrows()]), hide_index=True, use_container_width=True)
    st.markdown('---')
    subjects = ['Physics', 'Chemistry', 'Biology', 'Total'] if neet else ['Physics', 'Chemistry', 'Maths', 'Total']
    categories = ['Base Line Test', 'NEET RT', 'NEET CT', 'NEET Part Tests', 'NEET Practice Tests', 'NEET Tests', 'Unit Tests', 'Quarterly', 'Half Yearly', 'Pre Final 1', 'Pre Final 2', 'Pre Final 3', 'Part Tests', 'EAPCET', 'Other'] if neet else ['Base Line Test', 'RT Mains', 'CT Mains', 'RT Advanced', 'CT Advanced', 'Part Tests', 'EAPCET RT', 'EAPCET CT', 'EAPCET', 'Unit Tests', 'Quarterly', 'Half Yearly', 'Pre Final 1', 'Pre Final 2', 'Pre Final 3', 'Other']
    for category in categories:
        if category in sd['Category'].astype(str).unique():
            render_category_section(sd, category, subjects)
    st.markdown('---')
    render_combination_subject_analysis(sd, neet, scope_label='Student')


def main():
    st.markdown('<div class="main-header">Student Performance Dashboard</div>', unsafe_allow_html=True)
    with st.spinner('Loading data from Google Sheets...'):
        df = load_and_process_data()
    if df.empty:
        st.warning('No data found matching the supplied student roster.')
        return
    st.session_state['_dashboard_full_df'] = df.copy()
    st.session_state.setdefault('nav_mode', 'student')

    nav = [
        ('🔄 Refresh', 'refresh'), ('👤 Student Data', 'student'),
        ('📊 Batch Analysis', 'batch'), ('🏆 Top Performers', 'topper'),
        ('🔎 Search Student', 'search'), ('💡 Motivation', 'motivation'),
        ('📚 Concepts', 'concepts')
    ]
    for col, (label, mode) in zip(st.columns(7), nav):
        with col:
            if st.button(label, use_container_width=True, key='nav_' + mode):
                if mode == 'refresh':
                    load_and_process_data.clear()
                    load_concepts.clear()
                    st.rerun()
                else:
                    st.session_state['nav_mode'] = mode

    st.markdown('---')
    mode = st.session_state['nav_mode']
    if mode == 'motivation':
        render_motivation()
        return
    if mode == 'concepts':
        render_concepts()
        return
    if mode == 'search':
        render_student_search_view(df)
        return

    ordered = [
        'Sankalp-JEE-WD-Madhapur-(26-27)-A',
        'Dhristi-JEE-WD-Madhapur-(26-27)-A',
        'Dhristi-JEE-WD-Madhapur-(26-27)-C',
        'Dhristi-NEET-WD-Madhapur-(26-27)-A',
        'Dhristi-JEE-WD-Madhapur-(26-27)-E'
    ]
    available = set(df['Classroom'].astype(str).unique())
    batches = [b for b in ordered if b in available]
    if not batches:
        st.warning('No batches available.')
        return
    batch = st.selectbox('Select Batch / Classroom:', batches, key='main_batch_selector')
    data = df[df['Classroom'] == batch].copy()
    neet = 'NEET' in batch.upper()
    if mode == 'batch':
        render_batch_analysis_view(data, neet)
    elif mode == 'topper':
        render_top_performers_view(data, neet)
    else:
        render_student(data, batch)


main()
