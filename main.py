import re
import urllib.request
import pandas as pd
import streamlit as st

SRC = "https://raw.githubusercontent.com/sureshr89/student-dashboard/5283697e96cdb80eb8c62311f0d7e9c96eb99150/main.py"

try:
    source = urllib.request.urlopen(SRC, timeout=20).read().decode("utf-8")
except Exception as e:
    st.error(f"Unable to load dashboard source: {e}")
    st.stop()

source, removed_concepts = re.subn(
    r"\n# ={20,}\n# CONCEPTS.*?\n# ={20,}\n# TOP 5 BEST SUBJECT-WISE RANKS",
    "\n# ============================================================\n# TOP 5 BEST SUBJECT-WISE RANKS",
    source, count=1, flags=re.S,
)
source = source.replace("('📚 Concepts', 'concepts')", "")
source = re.sub(r"\n\s*if mode == ['\"]concepts['\"]:\n\s*render_concepts\(\)\n\s*return\n", "\n", source, count=1)
source = re.sub(r"\nmain\(\)\s*$", "\n", source, count=1)

if removed_concepts != 1:
    st.error("Dashboard safety check failed while removing Concepts.")
    st.stop()

exec(compile(source, "dashboard_base.py", "exec"), globals(), globals())

# -----------------------------------------------------------------------------
# MOTIVATION: QUESTION-SPECIFIC PRACTICAL ANSWERS
# -----------------------------------------------------------------------------
try:
    from motivation_library import MOTIVATION, practical_advice, advice
except Exception as e:
    st.error(f"Unable to load Motivation library: {e}")
    st.stop()

_motivation_rows = []
for item in MOTIVATION:
    if not isinstance(item, dict):
        continue
    q = str(item.get("Question", "")).strip()
    if not q:
        continue
    _motivation_rows.append({
        "Category": str(item.get("Category", "Study Help")),
        "Question": q,
        "Answer": str(practical_advice(q) or advice(q) or "").strip(),
    })

_motivation_df = pd.DataFrame(_motivation_rows).drop_duplicates(subset=["Question"], keep="first")
if _motivation_df.empty:
    st.error("Motivation library contains no searchable questions.")
    st.stop()

# -----------------------------------------------------------------------------
# CLEARABLE SEARCH BOXES
# Uses a Streamlit callback to clear the widget state safely. Do NOT assign
# st.session_state[key] after the widget has already been created; that causes
# StreamlitValueAssignmentNotAllowedError on the next rerun.
# -----------------------------------------------------------------------------
def _clear_search_value(widget_key):
    st.session_state[widget_key] = None


def _clearable_selectbox(label, options, *, key, placeholder):
    clear_key = f"{key}_clear_button"

    left, right = st.columns([0.91, 0.09], gap="small", vertical_alignment="bottom")
    with left:
        value = st.selectbox(
            label,
            options,
            index=None,
            placeholder=placeholder,
            key=key,
            label_visibility="collapsed",
        )
    with right:
        st.markdown("<div style='height:2px'></div>", unsafe_allow_html=True)
        st.button(
            "✕",
            key=clear_key,
            help="Clear search",
            use_container_width=True,
            on_click=_clear_search_value,
            args=(key,),
        )

    st.markdown(
        """
        <style>
        div[data-testid="stHorizontalBlock"] button[kind="secondary"] {
            min-height: 44px !important;
            height: 44px !important;
            padding: 0 !important;
            border-radius: 22px !important;
            font-size: 20px !important;
            font-weight: 600 !important;
        }
        div[data-testid="stSelectbox"] > div > div {
            border-radius: 28px !important;
            min-height: 50px !important;
            border: 1px solid #d9d9d9 !important;
            box-shadow: 0 1px 6px rgba(0,0,0,0.14) !important;
            background: #ffffff !important;
        }
        div[data-testid="stSelectbox"] input {
            color: #202124 !important;
            font-size: 16px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    return value


def render_motivation():
    st.markdown("## 💡 Motivation & Study Help")
    st.caption("Start typing — matching questions appear as suggestions. Tap ✕ to clear the search.")

    selected_question = _clearable_selectbox(
        "Search motivation questions",
        _motivation_df["Question"].tolist(),
        key="motivation_google_search_fixed",
        placeholder="🔍 Type here — e.g. lazy, focus, JEE, NEET, Physics, hostel...",
    )

    if selected_question is None:
        return

    selected = _motivation_df[_motivation_df["Question"] == selected_question]
    if selected.empty:
        return

    category = str(selected.iloc[0]["Category"])
    answer_text = str(selected.iloc[0]["Answer"])
    st.markdown("### 💭 Your question")
    st.markdown(f"**{selected_question}**")
    st.markdown("### 💡 Practical answer")
    st.markdown(answer_text)
    st.caption(f"Topic: {category}")

# -----------------------------------------------------------------------------
# STUDENT SEARCH: KEEP GREETING + TOP 5 WORKING, WITH CLEAR X
# -----------------------------------------------------------------------------
def render_student_search_view(df):
    st.markdown('<div class="section-header">🔎 Search Student Results</div>', unsafe_allow_html=True)
    st.caption("Search by student name and select the correct student. The student's name and Top 5 rank achievements appear immediately.")
    required = ["Student Name", "Classroom", "Student Key"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        st.error(f"Student Search data is missing: {', '.join(missing)}")
        return
    matches = (df[required].dropna(subset=required).drop_duplicates(subset=["Student Key", "Classroom"]).sort_values(["Student Name", "Classroom"]).reset_index(drop=True))
    if matches.empty:
        st.warning("No students found.")
        return
    options = [f"{row['Student Name']}  |  {row['Classroom']}" for _, row in matches.iterrows()]
    selected = _clearable_selectbox(
        "🔎 Search Student Name:",
        options,
        key="searched_student_option_fixed",
        placeholder="Type student name to see suggestions...",
    )
    if selected is None:
        st.info("Select a student to view the student's dashboard and Top 5 rank achievements.")
        return
    row = matches.iloc[options.index(selected)]
    student_name, batch, student_key = str(row["Student Name"]), str(row["Classroom"]), row["Student Key"]
    st.markdown(f"### 👋 Hi, {student_name}!")
    st.markdown(f"**Batch:** {batch}")
    student_data = df[(df["Student Key"] == student_key) & (df["Classroom"] == batch)].copy()
    student_data = student_data.drop_duplicates(subset=["Student Key", "Test Name", "Category"], keep="last")
    if student_data.empty:
        st.warning("No test results found for this student.")
        return
    is_neet = "NEET" in batch.upper()
    ranks = top5(student_data, is_neet)
    st.markdown("### 🏆 Your Top 5 Rank Achievements")
    if ranks.empty:
        st.info("No subject-wise Top 5 rank achievements are available for this student yet.")
    else:
        medals = {1: "🥇", 2: "🥈", 3: "🥉"}
        rank_rows = [{"Rank": medals.get(int(x["Rank"]), f"#{int(x['Rank'])}"), "Subject": str(x["Subject"]), "Test": str(x["Test"]), "Marks": int(round(float(x["Marks"]))) } for _, x in ranks.iterrows()]
        st.dataframe(pd.DataFrame(rank_rows), hide_index=True, use_container_width=True)
    st.markdown("---")
    if is_neet:
        allowed_subjects = ["Physics", "Chemistry", "Biology", "Total"]
        categories = ["Base Line Test", "NEET RT", "NEET CT", "NEET Part Tests", "NEET Practice Tests", "NEET Tests", "Unit Tests", "Quarterly", "Half Yearly", "Pre Final 1", "Pre Final 2", "Pre Final 3", "Part Tests", "EAPCET", "Other"]
    else:
        allowed_subjects = ["Physics", "Chemistry", "Maths", "Total"]
        categories = ["Base Line Test", "RT Mains", "CT Mains", "RT Advanced", "CT Advanced", "Part Tests", "EAPCET RT", "EAPCET CT", "EAPCET", "Unit Tests", "Quarterly", "Half Yearly", "Pre Final 1", "Pre Final 2", "Pre Final 3", "Other"]
    for category in categories:
        if category in student_data["Category"].astype(str).unique():
            render_category_section(student_data, category, allowed_subjects)
    st.markdown("---")
    render_combination_subject_analysis(student_data, is_neet, scope_label="Student")

main()
