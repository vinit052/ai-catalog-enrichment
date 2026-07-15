import csv
import io

from parsers.base_parser import BaseParser

class CSVParser(BaseParser):
    async def parse(self, file):
        content = await file.read()
        reader = csv.DictReader(
            io.StringIO(
                content.decode("utf-8")
            )
        )

        return list(reader)