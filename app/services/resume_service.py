
from app.llm.inference import llm

from app.prompts.summary_prompt import build_summary_prompt
from app.prompts.feedback_prompt import build_feedback_prompt
from app.prompts.ats_prompt import build_ats_prompt
from app.prompts.suggestion_prompt import build_suggestion_prompt


class ResumeService:

    def generate_summary(
        self,
        resume_text: str
    ):

        prompt = build_summary_prompt(resume_text)

        return llm.chat(prompt)

    def generate_feedback(

        self,

        summary,

        role

    ):

        prompt = build_feedback_prompt(

            summary,

            role

        )

        return llm.chat(prompt)

    def generate_ats_score(

        self,

        summary

    ):

        prompt = build_ats_prompt(summary)

        return llm.chat(prompt)

    def generate_suggestions(

        self,

        summary,

        role

    ):

        prompt = build_suggestion_prompt(

            summary,

            role

        )

        return llm.chat(prompt)


resume_service = ResumeService()
