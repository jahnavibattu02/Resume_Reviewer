class ReportService:

    def generate(

        self,

        feedback,

        ats,

        suggestions

    ):

        return f"""
# Resume Review Report

## Feedback

{feedback}

---

## ATS Score

{ats}

---

## Suggestions

{suggestions}

"""


report_service = ReportService()
