
from app.graph.state import ResumeState
from app.services.resume_service import resume_service


def feedback_agent(state: ResumeState):

    feedback = resume_service.generate_feedback(

        state["summary"],

        state["target_role"]

    )

    state["feedback"] = feedback

    return state
