import re
import urllib.request
import pandas as pd
import streamlit as st

# Keep the known-good dashboard as the base and apply only the requested UI fixes.
SRC = "https://raw.githubusercontent.com/sureshr89/student-dashboard/5283697e96cdb80eb8c62311f0d7e9c96eb99150/main.py"

try:
    source = urllib.request.urlopen(SRC, timeout=20).read().decode("utf-8")
except Exception as e:
    st.error(f"Unable to load dashboard source: {e}")
    st.stop()

# Remove Concepts completely.
source, removed_concepts = re.subn(
    r"\n# ={20,}\n# CONCEPTS.*?\n# ={20,}\n# TOP 5 BEST SUBJECT-WISE RANKS",
    "\n# ============================================================\n# TOP 5 BEST SUBJECT-WISE RANKS",
    source,
    count=1,
    flags=re.S,
)
source = source.replace("('📚 Concepts', 'concepts')", "")
source = source.replace(",\n        )\n", "\n        )\n")
source = re.sub(
    r"\n\s*if mode == ['\"]concepts['\"]:\n\s*render_concepts\(\)\n\s*return\n",
    "\n",
    source,
    count=1,
)
# Stop the base source from running main before our overrides are defined.
source = re.sub(r"\nmain\(\)\s*$", "\n", source, count=1)

if removed_concepts != 1:
    st.error("Dashboard safety check failed while removing Concepts.")
    st.stop()

exec(compile(source, "dashboard_base.py", "exec"), globals(), globals())


# -----------------------------------------------------------------------------
# MOTIVATION: TRUE TYPE-AHEAD SEARCH
# -----------------------------------------------------------------------------
def render_motivation():
    st.markdown("## 💡 Motivation & Study Help")
    st.caption("Type in the search box. Matching questions will appear in the box as suggestions.")

    # Build one clean list of unique questions.
    question_list = []
    seen = set()
    for item in MOTIVATION:
        q = str(item.get("Question", "")).strip()
        if q and q.lower() not in seen:
            seen.add(q.lower())
            question_list.append(q)

    # IMPORTANT: this is the actual searchable Streamlit select box.
    # Do NOT add a fake first option or separate suggestion buttons.
    # Streamlit filters the options inside this same box as the user types.
    selected_question = st.selectbox(
        "Search motivation questions",
        question_list,
        index=None,
        placeholder="🔍 Start typing — e.g. lazy, focus, sleep, marks...",
        key="motivation_google_search",
        label_visibility="collapsed",
    )

    # Google-like visual styling for the search box.
    st.markdown(
        """
        <style>
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
        div[data-testid="stSelectbox"] svg {
            color: #5f6368 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Nothing is shown until the student actually selects a suggestion.
    if not selected_question:
        return

    selected_item = next(
        (
            item for item in MOTIVATION
            if str(item.get("Question", "")).strip() == selected_question
        ),
        None,
    )

    if selected_item is None:
        return

    st.markdown("### 💭 Your question")
    st.markdown(f"**{selected_question}**")
    st.markdown("### 💡 Simple guidance")
    st.success(advice(selected_question))
    st.caption(f"Topic: {selected_item.get('Category', 'Study Help')}")


# -----------------------------------------------------------------------------
# STUDENT SEARCH: KEEP GREETING + TOP 5 WORKING
# -----------------------------------------------------------------------------
def render_student_search_view(df):
    st.markdown('<div class="section-header">🔎 Search Student Results</div>', unsafe_allow_html=True)
    st.caption("Search by student name and select the correct student. The student's name and Top 5 rank achievements appear immediately.")

    required = ["Student Name", "Classroom", "Student Key"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        st.error(f"Student Search data is missing: {', '.join(missing)}")
        return

    matches = (
        df[required]
        .dropna(subset=required)
        .drop_duplicates(subset=["Student Key", "Classroom"])
        .sort_values(["Student Name", "Classroom"])
        .reset_index(drop=True)
    )
    if matches.empty:
        st.warning("No students found.")
        return

    options = [f"{row['Student Name']}  |  {row['Classroom']}" for _, row in matches.iterrows()]
    selected = st.selectbox(
        "🔎 Search Student Name:",
        options,
        index=None,
        placeholder="Type student name to see suggestions...",
        key="searched_student_option_fixed",
    )
    if selected is None:
        st.info("Select a student to view the student's dashboard and Top 5 rank achievements.")
        return

    selected_index = options.index(selected)
    row = matches.iloc[selected_index]
    student_name = str(row["Student Name"])
    batch = str(row["Classroom"])
    student_key = row["Student Key"]

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
        rank_rows = []
        for _, x in ranks.iterrows():
            rank_num = int(x["Rank"])
            rank_rows.append({
                "Rank": medals.get(rank_num, f"#{rank_num}"),
                "Subject": str(x["Subject"]),
                "Test": str(x["Test"]),
                "Marks": int(round(float(x["Marks"]))),
            })
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


# Run only after the corrected functions have been defined.
main()