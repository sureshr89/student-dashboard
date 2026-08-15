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
# MOTIVATION: GOOGLE-STYLE TYPE-AHEAD SEARCH
# -----------------------------------------------------------------------------
def render_motivation():
    st.markdown("## 💡 Motivation & Study Help")
    st.caption("Search like Google: open the box, type a word or phrase, and matching questions appear as suggestions.")

    # Keep the search list clean and unique.
    question_list = []
    seen = set()
    for item in MOTIVATION:
        q = str(item.get("Question", "")).strip()
        if q and q.lower() not in seen:
            seen.add(q.lower())
            question_list.append(q)

    # Native Streamlit selectbox provides Google-like type-ahead filtering:
    # tap the box -> suggestions, type -> suggestions narrow immediately.
    suggestions = ["Search motivation questions..."] + question_list
    selected = st.selectbox(
        "Search motivation",
        suggestions,
        index=0,
        key="motivation_google_search",
        label_visibility="collapsed",
    )

    # Make the search box visually closer to a Google-style search field.
    st.markdown(
        """
        <style>
        div[data-testid="stSelectbox"] > div > div {
            border-radius: 28px !important;
            min-height: 48px !important;
            border: 1px solid #d9d9d9 !important;
            box-shadow: 0 1px 5px rgba(0,0,0,0.12) !important;
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

    if selected == suggestions[0]:
        st.markdown("### 🔎 Suggested searches")
        # Useful suggestions shown immediately when the box is opened.
        starter_topics = [
            "How can I study when I feel lazy?",
            "How can I concentrate while studying?",
            "How can I stop procrastinating?",
            "How can I improve my marks?",
            "How can I complete my study backlog?",
            "How can I reduce my phone usage?",
            "How can I improve my memory?",
            "How can I prepare for a test?",
        ]
        cols = st.columns(2)
        for i, question in enumerate(starter_topics):
            with cols[i % 2]:
                if st.button(question, key=f"motivation_suggestion_{i}", use_container_width=True):
                    st.session_state["motivation_selected_question"] = question
                    st.rerun()
        selected_question = st.session_state.get("motivation_selected_question")
    else:
        selected_question = selected
        st.session_state["motivation_selected_question"] = selected

    if not selected_question:
        return

    # Find the selected question and show its guidance immediately.
    selected_item = next(
        (item for item in MOTIVATION if str(item.get("Question", "")).strip() == selected_question),
        None,
    )
    if selected_item is None:
        st.info("Select one of the suggested questions to see guidance.")
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
