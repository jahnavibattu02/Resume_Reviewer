from langgraph.graph import StateGraph, END

from app.graph.state import ResumeState

from app.agents.summary_agent import summary_agent
from app.agents.feedback_agent import feedback_agent
from app.agents.ats_agent import ats_agent
from app.agents.suggestion_agent import suggestion_agent
from app.agents.report_agent import report_agent

workflow = StateGraph(ResumeState)

workflow.add_node("summary", summary_agent)
workflow.add_node("feedback", feedback_agent)
workflow.add_node("ats", ats_agent)
workflow.add_node("suggestions", suggestion_agent)
workflow.add_node("report", report_agent)

workflow.set_entry_point("summary")

# Fan-out
workflow.add_edge("summary", "feedback")
workflow.add_edge("summary", "ats")
workflow.add_edge("summary", "suggestions")

# Fan-in
workflow.add_edge("feedback", "report")
workflow.add_edge("ats", "report")
workflow.add_edge("suggestions", "report")

workflow.add_edge("report", END)

graph = workflow.compile()
