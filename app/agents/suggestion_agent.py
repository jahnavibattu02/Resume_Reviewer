
from app.graph.state import ResumeState
from app.services.resume_service import resume_service


def suggestion_agent(state: ResumeState):

    suggestions = resume_service.generate_suggestions(

        state["summary"],

        state["target_role"]

    )

    state["suggestions"] = suggestions

    return state
