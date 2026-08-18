import re
import urllib.request
import pandas as pd
import streamlit as st

# Professional student-dashboard branding.
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="student_logo.svg",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SRC = "https://raw.githubusercontent.com/sureshr89/student-dashboard/5283697e96cdb80eb8c62311f0d7e9c96eb99150/main.py"

try:
    source = urllib.request.urlopen(SRC, timeout=20).read().decode("utf-8")
except Exception as e:
    st.error(f"Unable to load dashboard source: {e}")
    st.stop()

# Remove the old Concepts section from the dynamically loaded dashboard.
source, removed_concepts = re.subn(
    r"\n# ={20,}\n# CONCEPTS.*?\n# ={20,}\n# TOP 5 BEST SUBJECT-WISE RANKS",
    "\n# ============================================================\n# TOP 5 BEST SUBJECT-WISE RANKS",
    source,
    count=1,
    flags=re.S,
)
source = source.replace("('📚 Concepts', 'concepts')", "")
source = re.sub(
    r"\n\s*if mode == ['\"]concepts['\"]:\n\s*render_concepts\(\)\n\s*return\n",
    "\n",
    source,
    count=1,
)
source = re.sub(r"\nmain\(\)\s*$", "\n", source, count=1)

if removed_concepts != 1:
    st.error("Dashboard safety check failed while removing the old Concepts module.")
    st.stop()

source = source.replace("load_concepts.clear()", "")

exec(compile(source, "dashboard_base.py", "exec"), globals(), globals())

# -----------------------------------------------------------------------------
# NOTES & MATERIALS
# -----------------------------------------------------------------------------
# Notes are currently assigned only to Sankalp-JEE-WD-Madhapur-(26-27)-A.
# The uploaded handwritten PDFs will be connected through external/cloud
# storage so the Git repository remains lightweight.
NOTES_ALLOWED_BATCH = "Sankalp-JEE-WD-Madhapur-(26-27)-A"


def render_notes_materials():
    st.markdown("## 📚 Notes & Materials")
    st.caption("Notes and study materials for Sankalp-JEE-WD-Madhapur-(26-27)-A.")

    categories = [
        ("🧪 Physical Chemistry", "physical"),
        ("🧬 Organic Chemistry", "organic"),
        ("⚛️ Inorganic Chemistry", "inorganic"),
        ("📝 Assignment & Mixed Notes", "mixed"),
    ]

    cols = st.columns(4)
    for col, (label, key) in zip(cols, categories):
        with col:
            st.markdown(
                f"""
                <div style='padding:18px;border:1px solid #e6e6e6;border-radius:14px;
                            background:#ffffff;box-shadow:0 1px 6px rgba(0,0,0,0.08);
                            text-align:center;min-height:105px;'>
                    <div style='font-size:18px;font-weight:700;'>{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    selected = st.selectbox(
        "Select a notes category",
        ["Physical Chemistry", "Organic Chemistry", "Inorganic Chemistry", "Assignment & Mixed Notes"],
        key="notes_materials_category",
    )

    category_map = {
        "Physical Chemistry": "physical",
        "Organic Chemistry": "organic",
        "Inorganic Chemistry": "inorganic",
        "Assignment & Mixed Notes": "mixed",
    }
    category_key = category_map[selected]

    st.info(
        f"📁 {selected} selected. The individual PDF files will appear here when the notes storage is connected. "
        "Your existing folder structure can be preserved."
    )

    manifest_url = f"https://raw.githubusercontent.com/sureshr89/student-dashboard/main/notes_manifest_{category_key}.json"
    try:
        manifest = urllib.request.urlopen(manifest_url, timeout=5).read().decode("utf-8")
        import json
        items = json.loads(manifest)
        if isinstance(items, list) and items:
            st.markdown("### 📄 Files")
            for item in items:
                if not isinstance(item, dict):
                    continue
                name = str(item.get("name", "Untitled PDF"))
                url = str(item.get("url", "")).strip()
                if url:
                    st.markdown(f"- [📄 {name}]({url})")
    except Exception:
        pass

# -----------------------------------------------------------------------------
# CLEARABLE SEARCH BOXES
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

# -----------------------------------------------------------------------------
# STUDENT SEARCH
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
        rank_rows = [
            {
                "Rank": medals.get(int(x["Rank"]), f"#{int(x['Rank'])}"),
                "Subject": str(x["Subject"]),
                "Test": str(x["Test"]),
                "Marks": int(round(float(x["Marks"]))),
            }
            for _, x in ranks.iterrows()
        ]
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


def main():
    st.markdown('<div class="main-header">🎓 Student Performance Dashboard</div>', unsafe_allow_html=True)
    with st.spinner("Loading data from Google Sheets..."):
        df = load_and_process_data()
    if df is None or df.empty:
        st.warning("No data found matching the supplied student roster.")
        return

    st.session_state["_dashboard_full_df"] = df.copy()
    st.session_state.setdefault("nav_mode", "student")

    ordered = [
        "Sankalp-JEE-WD-Madhapur-(26-27)-A",
        "Dhristi-JEE-WD-Madhapur-(26-27)-A",
        "Dhristi-JEE-WD-Madhapur-(26-27)-C",
        "Dhristi-NEET-WD-Madhapur-(26-27)-A",
        "Dhristi-JEE-WD-Madhapur-(26-27)-E",
    ]
    available = set(df["Classroom"].astype(str).unique())
    batches = [b for b in ordered if b in available]
    if not batches:
        st.warning("No batches available.")
        return

    # Select the batch before navigation so Notes & Materials can be restricted
    # to the authorized Sankalp batch only.
    batch = st.selectbox("Select Batch / Classroom:", batches, key="main_batch_selector")
    notes_allowed = batch == NOTES_ALLOWED_BATCH

    nav = [
        ("🔄 Refresh", "refresh"),
        ("🎓 Student Data", "student"),
        ("📊 Batch Analysis", "batch"),
        ("🏆 Top Performers", "topper"),
        ("🔎 Search Student", "search"),
    ]
    if notes_allowed:
        nav.append(("📚 Notes & Materials", "notes"))

    # If a non-authorized batch is selected while Notes was active, return to
    # Student Data and prevent the old Notes view from remaining accessible.
    if not notes_allowed and st.session_state.get("nav_mode") == "notes":
        st.session_state["nav_mode"] = "student"

    cols = st.columns(len(nav))
    for col, (label, mode_name) in zip(cols, nav):
        with col:
            pressed = st.button(label, use_container_width=True, key=f"nav_{mode_name}")
        if pressed:
            if mode_name == "refresh":
                try:
                    load_and_process_data.clear()
                except Exception:
                    pass
                st.session_state.pop("_dashboard_full_df", None)
                st.rerun()
            else:
                st.session_state["nav_mode"] = mode_name
                st.rerun()

    st.markdown("---")
    mode = st.session_state.get("nav_mode", "student")
    data = df[df["Classroom"] == batch].copy()
    is_neet = "NEET" in batch.upper()

    if mode == "notes":
        if not notes_allowed:
            st.error("📚 Notes & Materials are available only for Sankalp-JEE-WD-Madhapur-(26-27)-A.")
            return
        render_notes_materials()
        return
    if mode == "search":
        render_student_search_view(df)
        return

    if mode == "batch":
        render_batch_analysis_view(data, is_neet)
    elif mode == "topper":
        render_top_performers_view(data, is_neet)
    else:
        render_student(data, batch)


main()
