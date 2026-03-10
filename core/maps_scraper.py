import time
from config.settings import SCROLL_ITERATIONS, MAX_BUSINESSES


class MapsScraper:

    def __init__(self, page):
        self.page = page

    def search(self, keyword, city):

        query = f"{keyword} {city}".replace(" ", "+")

        url = f"https://www.google.com/maps/search/{query}"

        self.page.goto(url)

        # pequena espera inicial para carregar a página
        time.sleep(5)

        # faz scroll até atingir a quantidade máxima configurada
        self.scroll_until(MAX_BUSINESSES)

        return self.page.query_selector_all('div[role="article"]')

    def scroll_until(self, desired_count):

        for _ in range(SCROLL_ITERATIONS):

            self.page.mouse.wheel(0, 15000)

            time.sleep(1.5)

            elements = self.page.query_selector_all('div[role="article"]')

            if len(elements) >= desired_count:
                break

    def open_business(self, element):

        element.click()

        # espera um pouco menos para carregar os detalhes do negócio
        self.page.wait_for_timeout(2000)
