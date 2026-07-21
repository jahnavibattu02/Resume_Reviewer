
SYSTEM_PROMPT = """
You are an Applicant Tracking System.
"""


def build_ats_prompt(summary):

    return [

        {

            "role": "system",

            "content": SYSTEM_PROMPT

        },

        {

            "role": "user",

            "content": f"""

Resume Summary

{summary}

Return

ATS Score /100

Reasons

Keyword Coverage

Formatting Feedback

"""

        }

    ]
