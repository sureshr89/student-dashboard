import urllib.request

SOURCE_URL = "https://raw.githubusercontent.com/sureshr89/student-dashboard/643305bc8243a7a4a997af10070a1936e5f09609/main.py"

try:
    source = urllib.request.urlopen(SOURCE_URL, timeout=20).read().decode("utf-8")
except Exception as exc:
    import streamlit as st
    st.error(f"Unable to load dashboard source: {exc}")
    st.stop()

# Fix the roster in the source commit: G Rishith Kumar belongs to E only.
old = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {\n            "v_4102643666550411": "Jampala Shanthan Kumar",\n            "v_4102439835972285": "P Rohith",\n            "v_4102643721870649": "Punem Abhinav Sidhardha",\n            "v_4102644496422857": "G Rishith Kumar",\n'''
new = '''        "Dhristi-JEE-WD-Madhapur-(26-27)-C": {\n            "v_4102643666550411": "Jampala Shanthan Kumar",\n            "v_4102439835972285": "P Rohith",\n            "v_4102643721870649": "Punem Abhinav Sidhardha",\n'''
if old not in source:
    import streamlit as st
    st.error("Dashboard source integrity check failed: expected C-batch roster entry was not found.")
    st.stop()
source = source.replace(old, new, 1)

# Apply chart readability fixes without changing the dashboard's data calculations.
# This keeps all Plotly chart text dark/visible and puts numeric average labels on bars.
patch = '''\n# Chart readability patch\nimport plotly.graph_objects as _go\nimport streamlit as _st\n_original_plotly_chart = _st.plotly_chart\n\ndef _readable_plotly_chart(fig, *args, **kwargs):\n    try:\n        if isinstance(fig, _go.Figure):\n            # Make chart text, axes, legends and annotations readable on the light dashboard.\n            fig.update_layout(\n                font=dict(color="#1f2937"),\n                title_font=dict(color="#1f2937"),\n                legend=dict(font=dict(color="#1f2937")),\n                xaxis=dict(\n                    title_font=dict(color="#1f2937"),\n                    tickfont=dict(color="#1f2937"),\n                ),\n                yaxis=dict(\n                    title_font=dict(color="#1f2937"),\n                    tickfont=dict(color="#1f2937"),\n                ),\n            )\n            for _trace in fig.data:\n                if getattr(_trace, "type", None) == "bar":\n                    _trace.texttemplate = "%{y:.2f}"\n                    _trace.textposition = "outside"\n                    _trace.textfont = dict(color="#1f2937", size=14)\n                    _trace.cliponaxis = False\n            for _ann in fig.layout.annotations:\n                _ann.font = dict(color="#1f2937", size=12)\n    except Exception:\n        pass\n    return _original_plotly_chart(fig, *args, **kwargs)\n\n_st.plotly_chart = _readable_plotly_chart\n'''

exec(compile(patch, "chart_readability_patch.py", "exec"), globals(), globals())
exec(compile(source, "main.py", "exec"), globals(), globals())
