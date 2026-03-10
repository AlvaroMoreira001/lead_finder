from infra.browser_manager import BrowserManager
from core.maps_scraper import MapsScraper
from core.business_extractor import BusinessExtractor
from core.website_scraper import WebsiteScraper
from core.exporter import Exporter
from config.settings import MAX_BUSINESSES


class LeadPipeline:

    def run(self, keyword, city, max_leads):

        manager = BrowserManager()

        page = manager.start()

        maps = MapsScraper(page)

        extractor = BusinessExtractor(page)

        site_scraper = WebsiteScraper()

        exporter = Exporter()

        elements = maps.search(keyword, city)

        leads = []

        # Garante que não vamos além do limite global definido em settings
        limit = min(max_leads, MAX_BUSINESSES)

        # Percorre todos os elementos, mas para assim que atingir o limite desejado de leads válidos
        for el in elements:

            if len(leads) >= limit:
                break

            try:

                maps.open_business(el)
                data = extractor.extract()

                if data.get("website"):

                    website_data = site_scraper.scrape(data["website"])

                    data.update(website_data)

                leads.append(data)

            except:
                continue

        manager.close()

        return exporter.export(leads, keyword, city)

