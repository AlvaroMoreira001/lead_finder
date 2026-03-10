import pandas as pd
from pathlib import Path


class Exporter:

    def export(self, leads, keyword, city):

        df = pd.DataFrame(leads)

        filename = f"{keyword}_{city}.xlsx".replace(" ", "_")

        path = Path("data/outputs") / filename

        df.to_excel(path, index=False)

        return path
