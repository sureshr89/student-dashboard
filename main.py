import pandas as pd
import plotly.express as px
import streamlit as st

# Mobile-friendly layout configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Injected CSS and JavaScript to fully lock down selectbox inputs from typing or editing
st.markdown(
    """
    <style>
    /* Prevent text selection and highlighting across the app */
    html, body, [class*="css"] {
        touch-action: manipulation;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }

    .stApp { background-color: #e9f0fd; color: #1f2937; }

    .main-header {
        background-color: #385b96; color: white; padding: 12px 15px;
        font-size: 24px; font-weight: bold; font-family: sans-serif; margin-bottom: 20px;
        border-radius: 5px;
        text-align: center;
    }

    .section-header {
        color: #385b96; font-size: 18px; font-weight: bold; margin-top: 20px; margin-bottom: 5px; font-family: sans-serif;
        border-bottom: 2px solid #385b96;
        padding-bottom: 5px;
    }

    /* Force all general text to be dark and readable */
    p, span, label, div {
        color: #1f2937;
    }

    /* Ensure tables allow horizontal swipe/scroll without locking touch inputs */
    [data-testid="stDataFrame"] {
        width: 100% !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        pointer-events: auto !important;
    }

    /* Force Streamlit Navigation Buttons to have blue background and bright white text */
    .stButton > button {
        background-color: #385b96 !important;
        color: #ffffff !important;
        border: 1px solid #2c4775 !important;
        font-weight: bold !important;
        border-radius: 6px !important;
        width: 100% !important;
    }
    .stButton > button p {
        color: #ffffff !important;
    }
    .stButton > button:hover {
        background-color: #2c4775 !important;
        color: #ffffff !important;
    }

    /* Fix Streamlit Selectbox and Input boxes */
    [data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background-color: #ffffff !important;
        color: #1f2937 !important;
        border-color: #385b96 !important;
    }

    /* STRICT LOCK: Completely disable text cursor, typing, and deletions inside select boxes */
    [data-baseweb="select"] input {
        caret-color: transparent !important;
        pointer-events: none !important;
        user-select: none !important;
    }
    
    [data-baseweb="select"] div[data-testid="stMarkdownContainer"], 
    [data-baseweb="select"] [role="button"] {
        pointer-events: auto !important;
    }

    [data-baseweb="popover"] div, [role="option"] div {
        color: #1f2937 !important;
        background-color: #ffffff !important;
    }

    @media (max-width: 900px) {
        .main-header {
            font-size: 20px;
            padding: 10px;
        }
        .section-header {
            font-size: 16px;
        }
        [data-testid="column"] {
            width: 100% !important;
            flex: 100% !important;
            min-width: 100% !important;
        }
    }
    </style>

    <!-- Comprehensive JavaScript injection to suppress mobile soft keyboards and block typing -->
    <script>
        function suppressKeyboard() {
            let inputs = document.querySelectorAll('[data-baseweb="select"] input');
            inputs.forEach(input => {
                input.setAttribute('readonly', 'true');
                input.setAttribute('inputmode', 'none');
                input.setAttribute('disabled', 'true');
                input.style.caretColor = 'transparent';
                input.style.pointerEvents = 'none';
            });
        }

        document.addEventListener('DOMContentLoaded', () => {
            suppressKeyboard();
            const observer = new MutationObserver(suppressKeyboard);
            observer.observe(document.body, { childList: true, subtree: true });
        });

        document.addEventListener('click', function(e) {
            setTimeout(() => {
                let activeEl = document.activeElement;
                if (activeEl && activeEl.tagName === 'INPUT') {
                    activeEl.blur();
                }
            }, 10);
        }, true);
    </script>
""",
    unsafe_allow_html=True,
)


@st.cache_data()
def load_and_process_data():
    sheet_url = "https://docs.google.com/spreadsheets/d/1J8daLHn7YCZTDQ1nCREmQIUCVi3wXuJx9Qv8h1ntay0/export?format=xlsx"
    try:
        xls = pd.read_excel(sheet_url, sheet_name=None, engine="openpyxl")
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

    all_data = []
    ignore_sheets = [
        "Executive_Dashboard",
        "Comprehensive_Student_Deep_Dive",
        "Top_Performers_Summary",
    ]

    student_roster = {
        "Sankalp-JEE-WD-Madhapur-(26-27)-A": {
            "v_4102627828036953": "Kommu Navya",
            "v_4102623071293199": "Sharani Ch",
            "v_4102523600588089": "Nitya Santhoshini",
            "v_4102628924914015": "Anyasri Vangapalli",
            "v_4102632679443523": "Chittanoori Sharanya",
            "v_4102634480786059": "Balakrishna Reddy",
            "v_4102650842335369": "Sanjana",
            "v_4102630248538279": "Supriya",
            "v_4102635833967519": "Varshitha",
            "v_4102638143043823": "K Jhansi Karthika",
            "v_4102631802555815": "Juluri Shruthi",
            "v_4102627329281627": "Paladi manicharitha",
            "v_4102627597260617": "Venna Sree Roshitha Sai",
            "v_4102651255800021": "A Ahidvishini",
            "v_4102614316393167": "B Deekshitha",
            "v_4102635730773063": "A tejaswini",
            "v_4102627550531633": "Namratha Patel",
            "v_4102650638174583": "Sidhiksha",
            "v_4102631322532821": "Onna akshara sri",
            "v_4102452464248681": "Yamsani Sahithi",
            "v_4102627563811191": "Swarna Rekha",
            "v_4102645865483471": "Ravula Sathwika",
            "v_4102630403436735": "Kasoju Sahasra",
            "v_4102635773377785": "Soma Renuka Sri",
            "v_4102459718100771": "Kadire Praharsha",
            "v_4102634060004155": "Mula Rujula Goud",
            "v_4102637023521377": "Ch Veda Pranathi",
            "v_4102637877391781": "Yamini Pachipala",
            "v_4102635086792899": "Ananyaa K",
            "v_4102650971571665": "Nunela Tanuja",
            "v_4102635084111339": "Eekshitha Devaveth",
            "v_4102650108877253": "T Srujana Sri",
            "v_4102635333011287": "P Sanjana",
            "v_4102631847207581": "Vasavi Kambhampati",
            "v_4102650740844153": "G Srii Sahasra",
            "v_4102486214809077": "G Ananya",
            "v_4102630956969607": "Alampally Snehitha",
            "v_4102628748993393": "Raga Harshini",
            "v_4102637560371807": "Pasupuleti Sreevidhya",
            "v_4102637382658911": "Y Shiridi Sree",
            "v_4102635764655735": "Rachakonda Varshini",
            "v_4102637562197363": "Guvva Venu",
            "v_4102634998788583": "Mallu Sahithya",
            "v_4102518892161407": "Annapurna",
            "v_4102443818784431": "Akshaya",
            "v_4102637886529049": "Lasya Priya Katta",
            "v_4102512152214977": "Himaja",
            "v_4102635725361565": "Zaiba",
        },
        "Dhristi-JEE-WD-Madhapur-(26-27)-A": {
            "v_4102645727270519": "A Geethika Manyu",
            "v_4102401107774195": "Ankitha Boya",
            "v_4102645828451675": "Kavya Thanmayi Reddy",
            "v_4102645727827251": "Ruthika Gudi",
            "v_4102645797622745": "Naga Pranavi",
            "v_4102483883331591": "Swapnika",
            "v_4102647244744109": "D Gayathri",
            "v_4102636602459575": "Sahasra",
            "v_4102388559707123": "Santosh Reddy",
            "v_4102647266716239": "Sanjana",
            "v_4102647394649605": "Akshara",
            "v_4102647174524251": "Pathangi Archana",
            "v_4102614218956389": "Chaya Krishna",
            "v_4102648152223315": "Ramya Sowmya Sri",
            "v_4102648531881313": "Ashritha Boorla",
            "v_4102642327198855": "M Srija",
            "v_4102650134288681": "Rithvi Sree Muttavarapu",
            "v_4102643056297737": "Gangadevi Vipasyenaa",
            "v_4102651336517623": "Sindhu",
            "v_4102647850851099": "Sulochana",
            "v_4102651562635467": "Dyapa Aishwarya",
            "v_4102644574580053": "Hemalatha",
            "v_4102651903094885": "N Sheshanalaxmi",
            "v_4102652396509247": "Yamsani Vaishnavi",
            "v_4102652103879301": "Vengala Pranitha",
            "v_4102477276826079": "N Sandhya Rani",
            "v_4102652615057209": "K Sharanya",
            "v_4102512050759011": "Akshaya K",
            "v_4102634393217841": "Shanmukha Priya",
            "v_4102652743214533": "Sai Vaishnavi",
            "v_4102652743818187": "Sravani",
            "v_4102652782757147": "Durga Rawal",
            "v_4102652740627381": "Lithika",
            "v_4102643428135957": "B Disyasree Aishwarya",
            "v_4102652816566403": "Amima Tahreem",
            "v_4102653253098055": "M Archana Reddy",
            "v_4102653184093243": "Tejaswini",
            "v_4102634120062719": "N Rakshitha",
            "v_4102653152493329": "Krishnaveni",
            "v_4102653284309827": "Anjum Khatoon",
            "v_4102653126102915": "R Rishitha",
            "v_4102652825965509": "Kuppala Yashaswini",
            "v_4102653692885741": "Shafiya Jabin",
            "v_4102464019708919": "D Akshara",
            "v_4102653706787393": "K Niharika",
            "v_4102653870942183": "Srinidhi Nandigama",
        },
        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {
            "v_4102643666550411": "Jampala Shanthan Kumar",
            "v_4102439835972285": "P Rohith",
            "v_4102643721870649": "Punem Abhinav Sidhardha",
            "v_4102644496422857": "G Rishith Kumar",
            "v_4102613269351659": "U Hari Prasad",
            "v_4102415182975883": "Mani Harsha",
            "v_4102644808411807": "Elpula Ashwan Chandra",
            "v_4102644700590709": "Akshith Reddy",
            "v_4102644700701071": "Karthik",
            "v_4102489841476749": "Sripada Sai Keerthan",
            "v_4102645184935871": "Sripada Sai Harsha",
            "v_4102645551580585": "Ganesh Abhinay Kumar",
            "v_4102645547833057": "Nakarakommula Shiva Charan",
            "v_4102644928048957": "Munagala Dhaatre Sree Yajwin",
            "v_4102627775739499": "B Lukesh Naga Pavan Tej",
            "v_4102645180293809": "Gaganesh Kanagala",
            "v_4102644939624363": "Varun Sai",
            "v_4102435964362941": "Ganesh",
            "v_4102645868374797": "Siva Sai Manideep Mopuri",
            "v_4102627775749941": "Tavva Bhanu Prakash Reddy",
            "v_4102646371497291": "M Sriman",
            "v_4102533072184425": "J Thaneesh",
            "v_4102646368654085": "Anurag Varma Tipirisetty",
            "v_4102646368565483": "Y Srikar Bramha",
            "v_4102643397901715": "S Venkata Damodar",
            "v_4102647196005235": "N Suchethan Reddy",
            "v_4102622732890075": "B Joshua",
            "v_4102635820106845": "Abhi Vardhan Reddy",
            "v_4102627777617719": "Yshashikumar",
            "v_4102647246451011": "Jagjith Krishna Murthi",
            "v_4102427522159893": "Y Sampreeth",
            "v_4102456127546577": "Lingapuram Saaiganesan",
            "v_4102427865228253": "Shashish Pallerla",
            "v_4102425212615451": "Srivanth Dussa",
            "v_4102650234363763": "Harshaa Sanapala",
            "v_4102650890655949": "Mcb Somesh",
            "v_4102561394089445": "R Pradhasaradhi",
            "v_4102647992096861": "Amruth Sagar",
            "v_4102651561481929": "S Arun",
            "v_4102651530962021": "S Saiteja",
            "v_4102650371874285": "M Srinad Chary",
            "v_4102651769793913": "T Sumanth",
            "v_4102649172509667": "Beniwal Raghav Priyansh",
            "v_4102637057851105": "D Gagan Ranesh",
            "v_4102534990079985": "G Vignesh",
            "v_4102651968411315": "Saharsh",
            "v_4102651481687971": "Ram Charan Teja",
            "v_4102652256327965": "Matam Veera Prakash Swami",
            "v_4102651971090273": "Thuma Shanmukh Reddy",
            "v_4102434593109347": "M Sai Charan",
            "v_4102649312245099": "G Dinesh Yadav",
            "v_4102653374842789": "Hima Shankar Yashwanth",
            "v_4102648017567625": "Karthikeya Reddy Rachamallu",
        },
        "Dhristi-JEE-WD-Madhapur-(26-27)-E": {
            "v_4102630661117777": "T Sahith",
            "v_4102645790154227": "P Lokesh Goud",
            "v_4102647322018111": "B Abhinav",
            "v_4102647211675845": "Akshith Sayini",
            "v_4102577186467051": "Johann Alvyn",
            "v_4102649288557761": "B Kushal",
            "v_4102651648660565": "Dhanraj Mustala Salient Killer",
            "v_4102651907979961": "E Sanketh",
            "v_4102652513900157": "M Hari Kiran",
            "v_4102652689994975": "M Adi Charan",
            "v_4102459350652615": "B Bhavyesh",
            "v_4102409913567341": "K Harshith",
            "v_4102652786998627": "Ramavath Thirupathi",
            "v_4102640485523647": "Kannaji Ramcharan",
            "v_4102653048276523": "R Gopal Charan",
            "v_4102635674261011": "Nagelli Gowtham",
            "v_4102652962267887": "B Amruth Varma",
            "v_4102653313674765": "M Dinesh/U dhinesh",
            "v_4102653453645603": "G Gnaneshwar",
            "v_4102650770797103": "N Ajay Reddy",
            "v_4102623937069667": "Budidapadu Eswar Reddy",
            "v_4102653662570681": "Macharla Manideep",
            "v_4102653689961765": "A Sujith",
            "v_4102653863528969": "S Avinash",
            "v_4102546153520849": "Sai Vikranth",
            "v_4102653634589779": "G Sai Varun",
            "v_4102653972531697": "Nitturi Siddarth",
            "v_4102650316292857": "Akshay",
            "v_4102654190368535": "B Vignan",
            "v_4102654195272069": "S Shiva Sai",
            "v_4102654393979495": "Harish",
            "v_4102628254215171": "C Manohar",
            "v_4102644496422857": "G Rishith Kumar",
            "v_4102642289606091": "Md Sohail",
            "v_4102653186903085": "Ch Harshavardhan Reddy",
            "v_4102653253168799": "M Akshay Kiran Reddy",
            "v_4102650143245809": "K Karthikeya",
        },
        "Dhristi-NEET-WD-Madhapur-(26-27)-A": {
            "v_4102643480684961": "B Vanshika",
            "v_4102644556073159": "Vishishta",
            "v_4102637539201437": "K Brammini",
            "v_4102645831164057": "D Soukhya",
            "v_4102646329288525": "K Vashishta",
            "v_4102603971545807": "Konduru Vishwateja",
            "v_4102437710242015": "Ch Prudhvi Teja",
            "v_4102647796216789": "Bhanu Teja",
            "v_4102647863300435": "Geethika",
            "v_4102648618743607": "Gujjeti Manaswi",
            "v_4102610689230795": "G Rithika",
            "v_4102651350713031": "Vadla Manoghnya",
            "v_4102651578743187": "B Akshaya",
            "v_4102650579507433": "N Alekhya",
            "v_4102650579440079": "N Meghana",
            "v_4102652081777189": "A Nithya Sri",
            "v_4102631744984203": "Navya Sri",
            "v_4102651422561677": "Ashreeth Reddy",
            "v_4102650465823267": "Sidam Gomukhi",
            "v_4102652782264705": "N Victoria",
            "v_4102650979247345": "Pasupunoori Samskruthi",
            "v_4102652488688651": "J Gokul",
            "v_4102652683013555": "Karthik",
            "v_4102652572604671": "Chalkuti Kranthi Lakshitha",
            "v_4102648539804057": "Thadepu Rahul",
            "v_4102631901998873": "T Akshara",
            "v_4102653481141521": "Sri Vineetha Sri Vineetha",
            "v_4102653091443327": "V Rahithya",
            "v_4102653549632173": "Shravanthi P",
            "v_4102473017254525": "Sharath Chandra",
            "v_4102441387257305": "Pundikura Abhignya Reddy Abhignya",
            "v_4102642920912055": "Sushanth",
            "v_4102654394357387": "M Gayatri",
        },
    }

    id_to_batch = {}
    id_to_proper_name = {}
    name_to_batch = {}
    name_to_proper_name = {}

    ordered_batches = [
        "Sankalp-JEE-WD-Madhapur-(26-27)-A",
        "Dhristi-JEE-WD-Madhapur-(26-27)-A",
        "Dhristi-JEE-WD-Madhapur-(26-27)-C",
        "Dhristi-NEET-WD-Madhapur-(26-27)-A",
        "Dhristi-JEE-WD-Madhapur-(26-27)-E"
    ]

    for batch in ordered_batches:
        if batch in student_roster:
            students = student_roster[batch]
            for uid, proper_name in students.items():
                id_to_batch[uid] = batch
                id_to_proper_name[uid] = proper_name
                clean_name_lower = proper_name.strip().lower()
                name_to_batch[clean_name_lower] = batch
                name_to_proper_name[clean_name_lower] = proper_name

    global_counter = 0

    for sheet_name, df in xls.items():
        if any(ign in sheet_name for ign in ignore_sheets):
            continue

        df.columns = [str(c).strip() for c in df.columns]
        required_cols = ["Student Name", "Physics", "Chemistry", "Total"]

        if all(col in df.columns for col in required_cols):
            if "Test Name" not in df.columns:
                df["Test Name"] = sheet_name

            cols_to_keep = [
                "Student Name",
                "Test Name",
                "Physics",
                "Chemistry",
                "Total",
            ]
            has_uid = "User ID" in df.columns
            if has_uid:
                cols_to_keep.append("User ID")
            if "Maths" in df.columns:
                cols_to_keep.append("Maths")
            if "Biology" in df.columns:
                cols_to_keep.append("Biology")

            subset = df[cols_to_keep].copy()
            subset = subset.dropna(subset=["Student Name"])

            valid_rows = []

            for _, test_row in subset.iterrows():
                sheet_name_val = str(test_row["Student Name"]).strip()
                name_lower = sheet_name_val.lower()
                uid_val = str(test_row["User ID"]).strip() if has_uid else ""

                assigned_batch = None
                final_clean_name = sheet_name_val

                if uid_val and uid_val in id_to_batch:
                    assigned_batch = id_to_batch[uid_val]
                    final_clean_name = id_to_proper_name[uid_val]
                elif name_lower in name_to_batch:
                    assigned_batch = name_to_batch[name_lower]
                    final_clean_name = name_to_proper_name[name_lower]

                if assigned_batch:
                    test_str_upper = str(test_row["Test Name"]).upper()
                    
                    if assigned_batch.startswith("Dhristi-NEET"):
                        if "12" in test_str_upper or "JEE" in test_str_upper or "MAINS" in test_str_upper or "ADV" in test_str_upper:
                            continue

                    row_dict = test_row.to_dict()
                    row_dict["Classroom"] = assigned_batch
                    row_dict["Student Name"] = final_clean_name
                    row_dict["row_index"] = global_counter
                    global_counter += 1
                    valid_rows.append(row_dict)

            if not valid_rows:
                continue

            processed_subset = pd.DataFrame(valid_rows)

            def categorize_test(tr):
                name_upper = str(tr["Test Name"]).upper()
                sheet_upper = str(sheet_name).upper()
                combined = f"{sheet_upper} {name_upper}"

                # Explicitly separate Practice Tests, Revision Tests (RT), and general NEET Tests
                if "PRACTICE" in combined:
                    return "Practice Tests"
                if "RT" in combined:
                    return "Revision Tests (RT)"
                if "PART" in combined:
                    return "Part Tests"
                if "RT" in combined and "MAIN" in combined:
                    return "RT Mains"
                if "CT" in combined and "MAIN" in combined:
                    return "CT Mains"
                if "RT" in combined and "ADV" in combined:
                    return "RT Advanced"
                if "CT" in combined and "ADV" in combined:
                    return "CT Advanced"
                if (
                    "UT" in combined
                    or "UNIT" in combined
                    or "IPE" in combined
                ):
                    return "Unit Tests"
                if "EAPCET" in combined:
                    return "EAPCET"
                if "BASE LINE" in combined or "BLT" in combined:
                    return "Base Line Test"
                if "NEET" in combined:
                    return "NEET Tests"
                return "Other"

            processed_subset["Category"] = processed_subset.apply(
                categorize_test, axis=1
            )

            for subj in ["Physics", "Chemistry", "Maths", "Biology", "Total"]:
                if subj in processed_subset.columns:
                    processed_subset[subj] = pd.to_numeric(
                        processed_subset[subj], errors="coerce"
                    )

            all_data.append(processed_subset)

    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        
        combined_df = combined_df.sort_values(by="row_index", ascending=True)

        combined_df = combined_df.drop_duplicates(
            subset=["Student Name", "Classroom", "Test Name", "Category"],
            keep="last",
        )
        
        combined_df["Test Name"] = combined_df["Test Name"].astype(str)
        combined_df["Rank"] = combined_df.groupby(["Classroom", "Test Name"])["Total"].rank(
            ascending=False, method="min"
        )
        return combined_df
    return pd.DataFrame()


def highlight_average_row(row):
    if row["Test Name"] == "Average":
        return ["background-color: #00e600; color: #1f2937; font-weight: bold"] * len(
            row
        )
    return ["background-color: #ffffff; color: #1f2937"] * len(row)


def render_category_section(student_df, category_name, allowed_subjects):
    cat_df = student_df[student_df["Category"] == category_name].copy()

    if cat_df.empty:
        return

    cat_df = cat_df.sort_values(by="Test Name")
    st.markdown(
        f'<div class="section-header">{category_name}</div>',
        unsafe_allow_html=True,
    )

    available_cols = ["Test Name"]
    for col in allowed_subjects:
        if col in cat_df.columns and col not in available_cols:
            available_cols.append(col)
    
    if "Rank" in cat_df.columns and "Rank" not in available_cols:
        available_cols.append("Rank")

    display_df = cat_df[available_cols].copy()

    for col in available_cols:
        if col == "Test Name":
            continue
        elif col == "Rank":
            display_df[col] = display_df[col].apply(
                lambda x: "N/A" if pd.isna(x) else str(int(round(x)))
            )
        else:
            display_df[col] = display_df[col].apply(
                lambda x: "Absent" if pd.isna(x) else str(int(round(x)))
            )

    avgs = {"Test Name": "Average"}
    for col in available_cols:
        if col != "Test Name":
            numeric_series = pd.to_numeric(cat_df[col], errors="coerce").dropna()
            if not numeric_series.empty:
                avgs[col] = f"{numeric_series.mean():.2f}"
            else:
                avgs[col] = "N/A"

    display_df = pd.concat(
        [display_df, pd.DataFrame([avgs])], ignore_index=True
    )
    styled_df = display_df.style.apply(highlight_average_row, axis=1)

    column_config_dict = {}
    for col in display_df.columns:
        if col != "Test Name":
            column_config_dict[col] = st.column_config.TextColumn(col)

    col_table, col_chart = st.columns([7, 3])

    with col_table:
        st.dataframe(
            styled_df,
            column_config=column_config_dict,
            hide_index=True,
            use_container_width=True,
            selection_mode=None,
        )

    with col_chart:
        st.markdown(
            f"<div style='text-align: center; color: #385b96; font-weight: bold;"
            f" margin-top: 10px;'>Improvement Trajectory</div>",
            unsafe_allow_html=True,
        )

        plot_df = (
            cat_df[["Test Name", "Total"]].copy()
            if "Total" in cat_df.columns
            else pd.DataFrame()
        )
        if not plot_df.empty:
            plot_df["Total"] = pd.to_numeric(plot_df["Total"], errors="coerce")
            plot_df = plot_df.dropna(subset=["Total"])

        if not plot_df.empty:
            fig = px.line(plot_df, x="Test Name", y="Total", markers=True)
            fig.update_xaxes(visible=False)
            fig.update_yaxes(
                title=None,
                showgrid=True,
                gridcolor="rgba(200, 200, 200, 0.3)",
                zeroline=False,
            )
            fig.update_layout(
                margin=dict(l=0, r=0, t=10, b=0),
                height=220,
                hovermode="x unified",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#1f2937"),
            )
            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displayModeBar": False,
                    "staticPlot": True,
                    "scrollZoom": False,
                    "doubleClick": False,
                },
                theme="streamlit",
            )
        else:
            st.info("No valid test scores for trajectory.")


def render_batch_analysis_view(batch_data, is_neet):
    st.markdown(
        '<div class="section-header">Executive Batch Dashboard - Class Averages</div>',
        unsafe_allow_html=True,
    )

    if is_neet:
        subject_cols = ["Physics", "Chemistry", "Biology"]
        categories = ["Base Line Test", "Unit Tests", "Practice Tests", "Revision Tests (RT)", "Part Tests", "EAPCET", "NEET Tests", "Other"]
    else:
        subject_cols = ["Physics", "Chemistry", "Maths"]
        categories = ["Base Line Test", "RT Mains", "CT Mains", "RT Advanced", "CT Advanced", "Unit Tests", "Part Tests", "EAPCET", "Other"]

    for cat in categories:
        cat_data = batch_data[batch_data["Category"] == cat]
        if cat_data.empty:
            continue

        grouped = cat_data.groupby("Test Name")[subject_cols + ["Total"]].mean().reset_index()
        grouped = grouped.sort_values(by="Test Name")

        if grouped.empty:
            continue

        st.markdown(f"### {cat}")
        c1, c2 = st.columns(2)

        with c1:
            st.markdown(f"<div style='text-align: center; font-weight: bold; color: #385b96;'>{cat} Subject Trend</div>", unsafe_allow_html=True)
            melted_df = grouped.melt(id_vars=["Test Name"], value_vars=[s for s in subject_cols if s in grouped.columns], var_name="Subject", value_name="Average Marks")
            fig_subj = px.line(melted_df, x="Test Name", y="Average Marks", color="Subject", markers=True)
            fig_subj.update_layout(
                margin=dict(l=0, r=0, t=10, b=0),
                height=260,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#1f2937"),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#1f2937"))
            )
            st.plotly_chart(
                fig_subj, 
                use_container_width=True, 
                config={
                    "displayModeBar": False,
                    "staticPlot": True,
                    "scrollZoom": False,
                    "doubleClick": False,
                }, 
                theme="streamlit"
            )

        with c2:
            st.markdown(f"<div style='text-align: center; font-weight: bold; color: #385b96;'>{cat} Overall Trend</div>", unsafe_allow_html=True)
            fig_tot = px.line(grouped, x="Test Name", y="Total", markers=True, color_discrete_sequence=["#385b96"])
            fig_tot.update_layout(
                margin=dict(l=0, r=0, t=10, b=0),
                height=260,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#1f2937"),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#1f2937"))
            )
            st.plotly_chart(
                fig_tot, 
                use_container_width=True, 
                config={
                    "displayModeBar": False,
                    "staticPlot": True,
                    "scrollZoom": False,
                    "doubleClick": False,
                }, 
                theme="streamlit"
            )
        
        st.markdown("---")


def render_top_performers_view(batch_data, is_neet):
    st.markdown(
        '<div class="section-header">Batch Top Performers (Top 3 per Test)</div>',
        unsafe_allow_html=True,
    )

    if is_neet:
        allowed_subjects = ["Physics", "Chemistry", "Biology", "Total"]
    else:
        allowed_subjects = ["Physics", "Chemistry", "Maths", "Total"]

    if batch_data.empty or "Test Name" not in batch_data.columns:
        st.info("No test data available for this batch.")
        return

    tests = sorted(batch_data["Test Name"].dropna().astype(str).unique().tolist())

    if not tests:
        st.info("No test data available for this batch.")
        return

    for test_name in tests:
        test_df = batch_data[batch_data["Test Name"].astype(str) == test_name].copy()
        if "Total" not in test_df.columns:
            continue
            
        test_df["Total"] = pd.to_numeric(test_df["Total"], errors="coerce")
        test_df = test_df.dropna(subset=["Total"])

        if test_df.empty:
            continue

        top_3 = test_df.sort_values(by="Total", ascending=False).head(3)

        st.markdown(f"### 🏆 {test_name}")

        display_cols = ["Student Name"] + [s for s in allowed_subjects if s in top_3.columns]
        if "Rank" in top_3.columns:
            display_cols.append("Rank")

        top_display = top_3[display_cols].copy()

        for col in top_display.columns:
            if col != "Student Name":
                top_display[col] = top_display[col].apply(
                    lambda x: "N/A" if pd.isna(x) else str(int(round(x)))
                )

        st.dataframe(
            top_display,
            hide_index=True,
            use_container_width=True,
            selection_mode=None,
        )
        st.markdown("---")


def main():
    st.markdown(
        '<div class="main-header">Student Performance Dashboard</div>',
        unsafe_allow_html=True,
    )

    with st.spinner("Loading data from Google Sheets..."):
        df = load_and_process_data()

    if df.empty:
        st.warning("No data found matching the specified student user IDs or names.")
        return

    if "nav_mode" not in st.session_state:
        st.session_state["nav_mode"] = "student"

    b1, b2, b3, b4 = st.columns(4)
    with b1:
        if st.button("🔄 Refresh Data"):
            load_and_process_data.clear()
            st.rerun()
    with b2:
        if st.button("👤 Student Data"):
            st.session_state["nav_mode"] = "student"
    with b3:
        if st.button("📊 Batch Analysis"):
            st.session_state["nav_mode"] = "batch"
    with b4:
        if st.button("🏆 Top Performers"):
            st.session_state["nav_mode"] = "topper"

    st.markdown("---")

    batches = sorted(df["Classroom"].astype(str).unique())
    selected_batch = st.selectbox("Select Batch / Classroom:", batches)

    batch_data: pd.DataFrame = df[df["Classroom"] == selected_batch]
    is_neet = "NEET" in selected_batch.upper()

    if st.session_state["nav_mode"] == "batch":
        render_batch_analysis_view(batch_data, is_neet)
    elif st.session_state["nav_mode"] == "topper":
        render_top_performers_view(batch_data, is_neet)
    else:
        students = sorted(batch_data["Student Name"].astype(str).unique())
        if students:
            selected_student = st.selectbox("Select Student Name:", students)
        else:
            st.warning("No students found in this batch.")
            return

        mask = batch_data["Student Name"] == selected_student
        student_data: pd.DataFrame = batch_data.loc[mask].drop_duplicates(
            subset=["Test Name", "Category"], keep="last"
        )

        if is_neet:
            allowed_subjects = ["Physics", "Chemistry", "Biology", "Total"]
            categories = [
                "Base Line Test",
                "Unit Tests",
                "Practice Tests",
                "Revision Tests (RT)",
                "Part Tests",
                "EAPCET",
                "NEET Tests",
                "Other",
            ]
        else:
            allowed_subjects = ["Physics", "Chemistry", "Maths", "Total"]
            categories = [
                "Base Line Test",
                "RT Mains",
                "CT Mains",
                "RT Advanced",
                "CT Advanced",
                "Unit Tests",
                "Part Tests",
                "EAPCET",
                "Other",
            ]

        for cat in categories:
            render_category_section(student_data, cat, allowed_subjects)


if __name__ == "__main__":
    main()
