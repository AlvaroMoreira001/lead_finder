import re


def extract_email(html):

    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)

    if match:
        return match.group(0)


def extract_social(html):

    data = {}

    insta = re.search(r"instagram\.com/[A-Za-z0-9_.]+", html)

    fb = re.search(r"facebook\.com/[A-Za-z0-9_.]+", html)

    linkedin = re.search(r"linkedin\.com/[A-Za-z0-9_/]+", html)

    if insta:
        data["instagram"] = "https://" + insta.group(0)

    if fb:
        data["facebook"] = "https://" + fb.group(0)

    if linkedin:
        data["linkedin"] = "https://" + linkedin.group(0)

    return data
