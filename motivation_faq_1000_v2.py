"""Compatibility wrapper for the clean 1,000-question Motivation FAQ."""

from motivation_faq_1000_clean import MOTIVATION

assert len(MOTIVATION) == 1000, f"Expected 1000 questions, got {len(MOTIVATION)}"
assert len({str(x.get('Question', '')).strip().casefold() for x in MOTIVATION}) == 1000
