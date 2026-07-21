
from app.graph.state import ResumeState
from app.services.resume_service import resume_service


def summary_agent(state: ResumeState):

    summary = resume_service.generate_summary(
        state["resume"]
    )

    state["summary"] = summary

    return state
