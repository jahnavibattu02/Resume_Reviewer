from app.graph.state import ResumeState


def planner_agent(state: ResumeState):

    if not state.get("requested_tasks"):

        state["requested_tasks"] = [

            "summary",

            "feedback",

            "ats",

            "suggestions",

            "report"

        ]

    return state
