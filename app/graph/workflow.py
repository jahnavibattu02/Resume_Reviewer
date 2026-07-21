from langgraph.graph import StateGraph, END

from app.graph.state import ResumeState

from app.agents.planner_agent import planner_agent
from app.agents.summary_agent import summary_agent
from app.agents.feedback_agent import feedback_agent
from app.agents.ats_agent import ats_agent
from app.agents.suggestion_agent import suggestion_agent
from app.agents.report_agent import report_agent


builder = StateGraph(ResumeState)

builder.add_node("planner", planner_agent)

builder.add_node("summary", summary_agent)

builder.add_node("feedback", feedback_agent)

builder.add_node("ats", ats_agent)

builder.add_node("suggestions", suggestion_agent)

builder.add_node("report", report_agent)

builder.set_entry_point("planner")

builder.add_edge("planner", "summary")

builder.add_edge("summary", "feedback")

builder.add_edge("feedback", "ats")

builder.add_edge("ats", "suggestions")

builder.add_edge("suggestions", "report")

builder.add_edge("report", END)

graph = builder.compile()
