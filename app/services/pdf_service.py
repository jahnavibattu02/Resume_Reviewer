
"""
PDF extraction service.
Responsible only for extracting text from PDF files.
"""

import re
import fitz


class PDFService:

    @staticmethod
    def extract_text(uploaded_file):

        try:

            with fitz.open(
                stream=uploaded_file.read(),
                filetype="pdf"
            ) as doc:

                text = "\n".join(
                    page.get_text()
                    for page in doc
                )

            text = re.sub(r"\n+", "\n", text)
            text = re.sub(r"[^\x00-\x7F]+", " ", text)

            return text.strip()

        except Exception as e:

            raise RuntimeError(
                f"Failed to extract PDF text: {e}"
            )
