import urllib.request
import re
import difflib
import pandas as pd
import streamlit as st

SRC = 'https://raw.githubusercontent.com/sureshr89/student-dashboard/643305bc8243a7a4a997af10070a1936e5f09609/main.py'
try:
    source = urllib.request.urlopen(SRC, timeout=20).read().decode('utf-8')
except Exception as e:
    st.error(f'Unable to load dashboard source: {e}')
    st.stop()

old = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {\n            "v_4102643666550411": "Jampala Shanthan Kumar",\n            "v_4102439835972285": "P Rohith",\n            "v_4102643721870649": "Punem Abhinav Sidhardha",\n            "v_4102644496422857": "G Rishith Kumar",\n'''
new = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {\n            "v_4102643666550411": "Jampala Shanthan Kumar",\n            "v_4102439835972285": "P Rohith",\n            "v_4102643721870649": "Punem Abhinav Sidhardha",\n'''
if old in source:
    source = source.replace(old, new, 1)
source = re.sub(r'if __name__\s*==\s*["\']__main__["\']\s*:\s*\n\s*main\(\)\s*$', '# original main disabled\n', source, flags=re.M)
source = source.replace("if __name__ == '__main__':\n    main()\n", '# original main disabled\n')
source = source.replace('if __name__ == "__main__":\n    main()\n', '# original main disabled\n')
exec(compile(source, 'original_dashboard.py', 'exec'), globals(), globals())

TOPICS = {
    'Study Motivation': 'start studying when I do not feel like studying',
    'Concentration': 'concentrate while studying',
    'Time Management': 'manage my study time',
    'Wake Up and Routine': 'wake up early and follow a routine',
    'Phone and Distractions': 'control phone and other distractions',
    'Reading and Study Speed': 'read and study more efficiently',
    'Notes': 'make short and useful notes',
    'Memory': 'remember what I study',
    'Revision': 'revise topics effectively',
    'Backlog': 'complete pending chapters',
    'Test Preparation': 'prepare properly for a test',
    'Test Analysis': 'analyse my test and mistakes',
    'Low Marks': 'improve my marks',
    'Exam Confidence': 'stay calm and confident in exams',
    'Goals': 'set and follow study goals',
    'Discipline and Habits': 'build consistent study habits',
    'Subject Improvement': 'improve a weak subject',
    'Problem Solving': 'solve questions better',
    'Healthy Study': 'balance study and rest',
    'Friends and Comparison': 'focus on my own progress instead of comparing with friends',
}
FORMS = [
    'How can I {t}?', 'What is a simple way to {t}?', 'What should I do to {t}?',
    'How can I start to {t}?', 'How can I get better at {t}?', 'What daily habit can help me {t}?',
    'How can I {t} consistently?', 'How can I {t} without feeling stressed?',
    'What mistakes should I avoid when trying to {t}?', 'Can you give me a simple plan to {t}?',
    'What can I do today to {t}?', 'How can I practise so that I can {t}?',
    'How can I make it easier to {t}?', 'How can I improve step by step to {t}?',
    'What should I do if I am struggling to {t}?'
]
MOTIVATION = [{'Category': c, 'Question': f.format(t=t)} for c, t in TOPICS.items() for f in FORMS]
BLOCKED = ('sex', 'sexual', 'porn', 'nude', 'naked', 'adult', 'xxx', 'vulgar', 'drug', 'weapon', 'suicide', 'self harm')
MOTIVATION = [x for x in MOTIVATION if not any(b in x['Question'].lower() for b in BLOCKED)]


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


def motivation_score(query, question):
    q_words = set(re.findall(r'[a-z]+', query.lower()))
    t_words = set(re.findall(r'[a-z]+', question.lower()))
    return difflib.SequenceMatcher(None, query.lower(), question.lower()).ratio() + 0.08 * len(q_words & t_words) + (0.5 if query.lower() in question.lower() else 0)


def render_motivation():
    st.markdown('## 💡 Motivation & Study Help')
    st.caption('Type a keyword or your own question. Results appear instantly. Student-safe content only.')
    query = st.text_input('🔎 Search motivation / study question', placeholder='Try: lazy, wake up early, read fast, concentration, backlog, low marks...', key='motivation_single_search', label_visibility='collapsed')
    if not query.strip():
        st.info(f'📚 {len(MOTIVATION)} student-safe questions available. Start typing a keyword.')
        return
    ranked = sorted(((motivation_score(query, x['Question']), x) for x in MOTIVATION), key=lambda z: z[0], reverse=True)
    matches = [x for score, x in ranked[:12] if score > 0.05]
    if not matches:
        st.info('No matching question found. Try another keyword.')
        st.markdown('### 💡 Guidance for your question')
        st.success(advice(query))
        return
    st.markdown('### 🔎 Matching Questions')
    for i, item in enumerate(matches):
        if st.button(f"{item['Category']} — {item['Question']}", key=f'mot_result_{i}', use_container_width=True):
            st.session_state['mot_selected_question'] = item['Question']
    selected = st.session_state.get('mot_selected_question')
    if selected:
        st.markdown('### 💡 Suggested Guidance')
        st.success(advice(selected))
    else:
        st.markdown('### 💡 Quick Guidance')
        st.success(advice(query))


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


def render_concepts():
    st.markdown('## 📚 Concepts & Examples')
    st.caption('Type a topic keyword. Matching concepts appear instantly.')
    df, err = load_concepts()
    if df.empty:
        st.warning('The Concepts Google Sheet could not be loaded.')
        st.caption(err)
        return
    query = st.text_input('🔎 Search concept', placeholder="Try: Electrolysis, Mole concept, Newton's laws...", key='concept_single_search', label_visibility='collapsed')
    if not query.strip():
        st.info(f'📚 {len(df)} concepts available. Start typing a topic name or keyword.')
        return
    q = query.lower().strip()
    scored = []
    for idx, topic in df['Topic'].items():
        text = str(topic)
        score = difflib.SequenceMatcher(None, q, text.lower()).ratio() + (0.7 if q in text.lower() else 0)
        scored.append((score, idx))
    scored.sort(reverse=True)
    matches = df.loc[[idx for score, idx in scored[:12] if score > 0.15]].copy()
    if matches.empty:
        st.info('No matching concept found. Try another keyword.')
        return
    st.markdown('### 🔎 Matching Topics')
    for i, (_, row) in enumerate(matches.iterrows()):
        subject = str(row.get('Subject', '')).strip()
        label = str(row['Topic']) + (f'  ·  {subject}' if subject and subject.lower() != 'nan' else '')
        if st.button(label, key=f'concept_result_{i}', use_container_width=True):
            st.session_state['concept_selected_topic'] = str(row['Topic'])
    selected = st.session_state.get('concept_selected_topic')
    if selected is None or selected not in set(matches['Topic'].astype(str)):
        return
    row = matches[matches['Topic'].astype(str) == selected].iloc[0]
    st.markdown(f"### 📌 {row['Topic']}")
    for title, col, kind in [('📖 Simple Definition', 'Definition', 'info'), ('💡 Easy Explanation', 'Explanation', 'write'), ('🧪 Example', 'Example', 'success'), ('⭐ Key Point', 'Key Point', 'write'), ('⚠️ Common Mistake', 'Common Mistake', 'warning')]:
        if col not in row.index:
            continue
        value = str(row[col]).strip()
        if not value or value.lower() == 'nan':
            continue
        st.markdown(f'#### {title}')
        {'info': st.info, 'success': st.success, 'warning': st.warning, 'write': st.write}[kind](value)


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
    nav = [('🔄 Refresh', 'refresh'), ('👤 Student Data', 'student'), ('📊 Batch Analysis', 'batch'), ('🏆 Top Performers', 'topper'), ('🔎 Search Student', 'search'), ('💡 Motivation', 'motivation'), ('📚 Concepts', 'concepts')]
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
    ordered = ['Sankalp-JEE-WD-Madhapur-(26-27)-A', 'Dhristi-JEE-WD-Madhapur-(26-27)-A', 'Dhristi-JEE-WD-Madhapur-(26-27)-C', 'Dhristi-NEET-WD-Madhapur-(26-27)-A', 'Dhristi-JEE-WD-Madhapur-(26-27)-E']
    batches = [b for b in ordered if b in set(df['Classroom'].astype(str).unique())]
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
