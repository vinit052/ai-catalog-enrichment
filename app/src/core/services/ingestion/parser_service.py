from parsers.csv_parser import CSVParser
from parsers.excel_parser import ExcelParser
from parsers.image_parser import ImageParser


class ParserService:


    def __init__(self):

        self.parsers = {
            "csv": CSVParser(),
            "xls": ExcelParser(),
            "xlsx": ExcelParser(),
            "jpg": ImageParser(),
            "jpeg": ImageParser(),
            "png": ImageParser(),
        }


    async def parse(self, file):

        extension = (
            file.filename
            .split(".")[-1]
            .lower()
        )


        parser = self.parsers.get(extension)


        if not parser:
            raise ValueError(
                "Unsupported file format"
            )


        return await parser.parse(file)