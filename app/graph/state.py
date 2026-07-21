from typing import TypedDict, List, Optional


class ResumeState(TypedDict):

    # Inputs
    resume: str
    target_role: str
    requested_tasks: List[str]

    # Outputs
    summary: Optional[str]
    feedback: Optional[str]
    ats_score: Optional[str]
    suggestions: Optional[str]
    keyword_matches: List[str]
    report: Optional[str]

    # Metadata
    completed_tasks: List[str]
