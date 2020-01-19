"""IngestorInterface strategy operator that implements an Ingestor strategy for text files."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Defines the two methods for implement the `txt` ingestion strategies.

    Attributes:
        allowed_extensions {[str]} -- An array of the allowed extensions that can be ingested
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest a given file retreiving all the quotes from it.

        Attributes:
            path {str} -- The path of the file which we are going to parse

        Returns:
            List[QuoteModel] -- All the quotes present in that given file
        """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        quote_file = open(path, 'r')
        quotes = []
        for line in quote_file.read().splitlines():
            if len(line) > 1:
                quote, author = line.split(" - ")
                quotes.append(QuoteModel(quote, author))

        quote_file.close()
        return quotes


# ingestor = TextIngestor.parse('../_data/SimpleLines/SimpleLines.txt')
# ingestor = TextIngestor.parse('../_data/DogQuotes/DogQuotesTXT.txt')
# print(ingestor)
