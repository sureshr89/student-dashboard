"""Compatibility wrapper: the dashboard keeps importing motivation_library,
but the actual FAQ data now lives in the clean 1000-question library.
"""
from motivation_faq_1000 import MOTIVATION, practical_advice, advice

__all__ = ["MOTIVATION", "practical_advice", "advice"]
