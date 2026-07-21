SYSTEM_PROMPT = """
You are an experienced HR Manager.
"""


def build_feedback_prompt(summary, role):

    return [

        {

            "role": "system",

            "content": SYSTEM_PROMPT

        },

        {

            "role": "user",

            "content": f"""

Target Role

{role}

Resume Summary

{summary}

Provide

1. Strengths

2. Weaknesses

3. Missing Skills

4. Hiring Recommendation

"""

        }

    ]
