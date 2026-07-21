
import re


def keyword_match(

    resume,

    keywords

):

    matched = [

        keyword

        for keyword in keywords

        if re.search(

            rf"\b{re.escape(keyword)}\b",

            resume,

            re.IGNORECASE

        )

    ]

    if matched:

        return matched

    return []
