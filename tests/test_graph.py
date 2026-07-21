
from app.graph.workflow import graph


state = {

    "resume": "Python developer with 3 years experience",

    "target_role": "Machine Learning Engineer",

    "summary": "",

    "feedback": "",

    "ats_score": "",

    "suggestions": "",

    "keyword_matches": [],

    "report": ""

}

result = graph.invoke(state)

print(result["summary"])

print(result["feedback"])

print(result["ats_score"])

print(result["suggestions"])

print(result["report"])
