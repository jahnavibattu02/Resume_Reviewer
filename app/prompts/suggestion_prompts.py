SYSTEM_PROMPT = """
You are a Senior Career Coach.
"""


def build_suggestion_prompt(summary, role):

    return [

        {

            "role": "system",

            "content": SYSTEM_PROMPT

        },

        {

            "role": "user",

            "content": f"""

Role

{role}

Resume Summary

{summary}

Give detailed improvements.

"""

        }

    ]
