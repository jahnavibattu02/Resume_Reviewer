SYSTEM_PROMPT = """
You are an expert Resume Reviewer.

You analyze resumes and produce structured summaries.
"""


def build_summary_prompt(resume: str):

    return [

        {

            "role": "system",

            "content": SYSTEM_PROMPT

        },

        {

            "role": "user",

            "content": f"""

Analyze the resume.

Extract:

1. Skills

2. Experience

3. Education

4. Projects

5. Certifications

Resume

{resume}

"""

        }

    ]
