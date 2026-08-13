import urllib.request

SOURCE_URL = "https://raw.githubusercontent.com/sureshr89/student-dashboard/643305bc8243a7a4a997af10070a1936e5f09609/main.py"

try:
    source = urllib.request.urlopen(SOURCE_URL, timeout=20).read().decode("utf-8")
except Exception as exc:
    import streamlit as st
    st.error(f"Unable to load dashboard source: {exc}")
    st.stop()

# The previous commit accidentally listed G Rishith Kumar in both C and E.
# Remove ONLY the C-batch entry; the E-batch entry remains authoritative.
old = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {\n            "v_4102643666550411": "Jampala Shanthan Kumar",\n            "v_4102439835972285": "P Rohith",\n            "v_4102643721870649": "Punem Abhinav Sidhardha",\n            "v_4102644496422857": "G Rishith Kumar",\n'''
new = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {\n            "v_4102643666550411": "Jampala Shanthan Kumar",\n            "v_4102439835972285": "P Rohith",\n            "v_4102643721870649": "Punem Abhinav Sidhardha",\n'''
if old not in source:
    import streamlit as st
    st.error("Dashboard source integrity check failed: expected C-batch roster entry was not found.")
    st.stop()
source = source.replace(old, new, 1)

exec(compile(source, "main.py", "exec"), globals(), globals())
