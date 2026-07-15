import pandas as pd

from parsers.base_parser import BaseParser


class ExcelParser(BaseParser):

    async def parse(self, file):

        content = await file.read()

        df = pd.read_excel(
            content
        )

        return df.to_dict(
            orient="records"
        )