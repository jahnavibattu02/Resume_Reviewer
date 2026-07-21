
"""
Shared state used by all LangGraph agents.
"""

from typing import TypedDict, List


class ResumeState(TypedDict):

    # Inputs
    resume: str
    target_role: str

    # Intermediate outputs
    summary: str
    feedback: str
    ats_score: str
    suggestions: str

    keyword_matches: List[str]

    # Final output
    report: str
