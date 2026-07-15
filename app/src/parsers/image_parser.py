from parsers.base_parser import BaseParser


class ImageParser(BaseParser):

    async def parse(self, file):

        return [
            {
                "filename": file.filename,
                "type": "image"
            }
        ]