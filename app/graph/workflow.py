
from langgraph.graph import StateGraph, END

from app.graph.state import ResumeState

from app.agents.summary_agent import summary_agent
from app.agents.feedback_agent import feedback_agent
from app.agents.ats_agent import ats_agent
from app.agents.suggestion_agent import suggestion_agent
from app.agents.report_agent import report_agent


workflow = StateGraph(ResumeState)

# Nodes

workflow.add_node(

    "summary",

    summary_agent

)

workflow.add_node(

    "feedback",

    feedback_agent

)

workflow.add_node(

    "ats",

    ats_agent

)

workflow.add_node(

    "suggestions",

    suggestion_agent

)

workflow.add_node(

    "report",

    report_agent

)

# Entry

workflow.set_entry_point(

    "summary"

)

# Flow

workflow.add_edge(

    "summary",

    "feedback"

)

workflow.add_edge(

    "feedback",

    "ats"

)

workflow.add_edge(

    "ats",

    "suggestions"

)

workflow.add_edge(

    "suggestions",

    "report"

)

workflow.add_edge(

    "report",

    END

)

graph = workflow.compile()
