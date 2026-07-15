from abc import ABC, abstractmethod


class BaseParser(ABC):

    @abstractmethod
    async def parse(self, file):
        pass