import re
import urllib.request
import pandas as pd
import streamlit as st

# Use the known-good dashboard version as the base, then apply only safe patches.
SRC = "https://raw.githubusercontent.com/sureshr89/student-dashboard/5283697e96cdb80eb8c62311f0d7e9c96eb99150/main.py"

try:
    source = urllib.request.urlopen(SRC, timeout=20).read().decode("utf-8")
except Exception as e:
    st.error(f"Unable to load dashboard source: {e}")
    st.stop()

# Remove Concepts completely from the base source.
source, removed_section = re.subn(
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

# IMPORTANT: prevent the base source from calling main() before our fixes are loaded.
source = re.sub(r"\nmain\(\)\s*$", "\n", source, count=1)

if removed_section != 1 or "('📚 Concepts', 'concepts')" in source or "mode == 'concepts'" in source or 'mode == "concepts"' in source:
    st.error("Dashboard safety patch could not be applied.")
    st.stop()

exec(compile(source, "dashboard_base.py", "exec"), globals(), globals())


# -----------------------------------------------------------------------------
# FIX: STUDENT SEARCH MUST SHOW GREETING + TOP 5 RANK ACHIEVEMENTS
# -----------------------------------------------------------------------------
def render_student_search_view(df):
    st.markdown('<div class="section-header">🔎 Search Student Results</div>', unsafe_allow_html=True)
    st.caption("Search by student name and select the correct student. The selected student's name, batch and Top 5 rank achievements are shown immediately.")

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

    options = []
    for _, row in matches.iterrows():
        options.append(f"{row['Student Name']}  |  {row['Classroom']}")

    selected = st.selectbox(
        "🔎 Search Student Name:",
        options,
        index=None,
        placeholder="Type or select a student name...",
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

    # Always show the greeting immediately after selection.
    st.markdown(f"### 👋 Hi, {student_name}!")
    st.markdown(f"**Batch:** {batch}")

    student_data = df[
        (df["Student Key"] == student_key) &
        (df["Classroom"] == batch)
    ].copy()
    student_data = student_data.drop_duplicates(
        subset=["Student Key", "Test Name", "Category"],
        keep="last",
    )

    if student_data.empty:
        st.warning("No test results found for this student.")
        return

    is_neet = "NEET" in batch.upper()

    # Top 5 is calculated against the FULL batch data, not only the student's rows.
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
        st.dataframe(
            pd.DataFrame(rank_rows),
            hide_index=True,
            use_container_width=True,
        )

    st.markdown("---")

    if is_neet:
        allowed_subjects = ["Physics", "Chemistry", "Biology", "Total"]
        categories = [
            "Base Line Test", "NEET RT", "NEET CT", "NEET Part Tests",
            "NEET Practice Tests", "NEET Tests", "Unit Tests", "Quarterly",
            "Half Yearly", "Pre Final 1", "Pre Final 2", "Pre Final 3",
            "Part Tests", "EAPCET", "Other",
        ]
    else:
        allowed_subjects = ["Physics", "Chemistry", "Maths", "Total"]
        categories = [
            "Base Line Test", "RT Mains", "CT Mains", "RT Advanced",
            "CT Advanced", "Part Tests", "EAPCET RT", "EAPCET CT",
            "EAPCET", "Unit Tests", "Quarterly", "Half Yearly",
            "Pre Final 1", "Pre Final 2", "Pre Final 3", "Other",
        ]

    for category in categories:
        if category in student_data["Category"].astype(str).unique():
            render_category_section(student_data, category, allowed_subjects)

    st.markdown("---")
    render_combination_subject_analysis(student_data, is_neet, scope_label="Student")


# Run the dashboard only after the corrected Search Student function exists.
main()
