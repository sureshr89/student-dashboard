"""Stable 1,000-question Motivation FAQ source for Class 11-12 JEE/NEET/Boards.

This compatibility layer uses the existing motivation_faq_1000.py source and
adds the missing independent FAQs so the dashboard always has exactly 1,000.
"""

from motivation_faq_1000 import MOTIVATION as _SOURCE_MOTIVATION

MOTIVATION = [dict(item) for item in _SOURCE_MOTIVATION]

ADDITIONAL_FAQS = [
    ("Motivation", "How can I restart studying after losing my routine for a week?"),
    ("Motivation", "How can I study when I feel that the syllabus is too large?"),
    ("Motivation", "How can I make myself study after getting a disappointing result?"),
    ("Motivation", "How can I continue studying when progress feels very slow?"),
    ("Motivation", "How can I stop waiting for the perfect mood to study?"),
    ("Concentration", "How can I return to studying after my concentration breaks?"),
    ("Concentration", "How can I concentrate during a long online lecture?"),
    ("Concentration", "How can I focus when I keep thinking about my exam result?"),
    ("Time Management", "How can I plan study time when coaching takes most of my day?"),
    ("Time Management", "How can I decide which subject to study first each day?"),
    ("Time Management", "How can I avoid spending too much time on one difficult question?"),
    ("Time Management", "How can I keep enough time for revision after finishing new chapters?"),
    ("Time Management", "How can I plan study when my school tests and entrance tests overlap?"),
    ("Sleep", "How can I avoid changing my sleep schedule repeatedly during exams?"),
    ("Sleep", "How can I study effectively in the evening without becoming too sleepy?"),
    ("Phone", "How can I use my phone for lectures without getting distracted by other apps?"),
    ("Phone", "How can I stop opening social media automatically while studying?"),
    ("Phone", "How can I control short-video watching during exam preparation?"),
    ("Reading", "How can I tell whether I actually understood a chapter?"),
    ("Reading", "How can I read a difficult Physics theory section effectively?"),
    ("Reading", "How can I read Chemistry NCERT without memorising every sentence blindly?"),
    ("Reading", "How can I read a Biology chapter when I have very little time?"),
    ("Notes", "When should I make notes and when should I avoid making them?"),
    ("Notes", "How can I reduce very long notes into useful revision points?"),
    ("Memory", "How can I remember information that I keep forgetting after revision?"),
    ("Memory", "How can I remember Physics concepts instead of only memorising formulas?"),
    ("Memory", "How can I remember Organic Chemistry reactions more reliably?"),
    ("Memory", "How can I remember confusing Biology terms that look similar?"),
    ("Revision", "How can I revise a chapter that I studied several months ago?"),
    ("Revision", "How can I combine revision with daily question practice?"),
    ("Revision", "How can I decide whether a topic needs revision or relearning?"),
    ("Backlog", "How can I clear backlog without ignoring my current classes?"),
    ("Backlog", "Which backlog chapters should I complete first?"),
    ("Backlog", "How can I prevent one unfinished chapter from creating more backlog?"),
    ("Tests", "How can I manage time during a three-hour entrance exam?"),
    ("Tests", "What should I do if I panic after seeing a difficult first question?"),
    ("Tests", "How can I decide whether to attempt or skip a question in a mock test?"),
    ("Test Analysis", "How can I analyse questions that I guessed correctly?"),
    ("Test Analysis", "How can I find chapters where I lose marks because of poor question selection?"),
    ("Test Analysis", "How can I know whether my problem is speed or accuracy?"),
    ("Low Marks", "What should I change if I keep getting nearly the same marks?"),
    ("Low Marks", "How can I improve after scoring much lower than expected in a mock test?"),
    ("Confidence", "How can I stay confident when my preparation is incomplete?"),
    ("Confidence", "How can I stop one bad test from affecting my next test?"),
    ("Comparison", "How can I handle it when classmates discuss their high scores?"),
    ("Discipline", "How can I study on days when my planned schedule gets disturbed?"),
    ("Problem Solving", "How long should I try a difficult question before checking a solution?"),
    ("Problem Solving", "How can I learn from a solution without simply copying it?"),
    ("JEE", "How can I decide when to practise JEE Main level questions and when to try Advanced level questions?"),
    ("JEE", "How can I improve my JEE question selection during mocks?"),
    ("NEET", "How can I revise Biology when I keep forgetting small NCERT details?"),
    ("NEET", "How can I improve Physics for NEET if Biology is taking most of my study time?"),
    ("Boards", "How can I write complete Board answers without spending too much time on one question?"),
    ("Boards", "How can I balance descriptive Board practice with MCQ practice?"),
    ("Hostel", "How can I study when my hostel timetable changes frequently?"),
    ("Day Scholar", "How can I use the limited study time available after school and coaching?"),
]

seen = {str(item.get("Question", "")).strip().casefold() for item in MOTIVATION}
for category, question in ADDITIONAL_FAQS:
    key = question.strip().casefold()
    if key not in seen and len(MOTIVATION) < 1000:
        MOTIVATION.append({
            "Category": category,
            "Question": question.strip(),
            "Keywords": question.lower(),
        })
        seen.add(key)

assert len(MOTIVATION) == 1000, f"Expected 1000 questions, got {len(MOTIVATION)}"
