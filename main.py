import re
import urllib.request
import streamlit as st

# Keep the restored, known-good dashboard version and remove only the Concepts feature.
SRC = "https://raw.githubusercontent.com/sureshr89/student-dashboard/5283697e96cdb80eb8c62311f0d7e9c96eb99150/main.py"

try:
    source = urllib.request.urlopen(SRC, timeout=20).read().decode("utf-8")
except Exception as e:
    st.error(f"Unable to load dashboard source: {e}")
    st.stop()

# Remove the complete Concepts section from the restored source.
source, removed_section = re.subn(
    r"\n# ={20,}\n# CONCEPTS.*?\n# ={20,}\n# TOP 5 BEST SUBJECT-WISE RANKS",
    "\n# ============================================================\n# TOP 5 BEST SUBJECT-WISE RANKS",
    source,
    count=1,
    flags=re.S,
)

# Remove the Concepts navigation button.
source = source.replace("('📚 Concepts', 'concepts')", "")
source = source.replace(",\n        )\n", "\n        )\n")

# Remove the Concepts navigation route if present.
source = re.sub(
    r"\n\s*if mode == ['\"]concepts['\"]:\n\s*render_concepts\(\)\n\s*return\n",
    "\n",
    source,
    count=1,
)

if removed_section != 1 or "('📚 Concepts', 'concepts')" in source or "mode == 'concepts'" in source or 'mode == "concepts"' in source:
    st.error("Concept removal patch could not be applied safely.")
    st.stop()

# Execute the restored dashboard with Concepts removed.
exec(compile(source, "dashboard_without_concepts.py", "exec"), globals(), globals())
