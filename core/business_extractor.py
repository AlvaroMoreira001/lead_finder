class BusinessExtractor:

    def __init__(self, page):
        self.page = page

    def extract(self):

        data = {}

        # Nome do negócio
        try:
            # Tenta primeiro um heading principal
            name = self.page.locator('h1[role="heading"]').first.inner_text()
            if not name.strip():
                # Fallback para variações comuns do layout do Google Maps
                name = self.page.locator('h1 span').first.inner_text()
            data["name"] = name.strip()
        except:
            try:
                # Último fallback: título da aba
                data["name"] = self.page.title()
            except:
                data["name"] = None

        try:
            data["phone"] = self.page.locator('button[data-item-id^="phone"]').inner_text()
        except:
            data["phone"] = None

        try:
            data["address"] = self.page.locator('button[data-item-id="address"]').inner_text()
        except:
            data["address"] = None

        try:
            data["website"] = self.page.locator('a[data-item-id="authority"]').get_attribute("href")
        except:
            data["website"] = None

        return data
