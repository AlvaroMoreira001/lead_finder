import re
import requests
from bs4 import BeautifulSoup
from utils.regex import extract_email, extract_social
from config.settings import REQUEST_TIMEOUT


class WebsiteScraper:

    def scrape(self, url):

        data = {
            "email": None,
            "instagram": None,
            "facebook": None,
            "linkedin": None
        }

        try:

            r = requests.get(url, timeout=REQUEST_TIMEOUT)

            soup = BeautifulSoup(r.text, "html.parser")

            html = r.text

            data["email"] = extract_email(html)

            socials = extract_social(html)

            data.update(socials)

        except:
            pass

        return data
