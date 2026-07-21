from app.graph.state import ResumeState


def router(state: ResumeState):

    tasks = state["requested_tasks"]

    return tasks
