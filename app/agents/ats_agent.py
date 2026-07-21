
from app.graph.state import ResumeState
from app.services.resume_service import resume_service


def ats_agent(state: ResumeState):

    ats = resume_service.generate_ats_score(

        state["summary"]

    )

    state["ats_score"] = ats

    return state
