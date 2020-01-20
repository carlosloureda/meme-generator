"""IngestorInterface strategy operator that implements an Ingestor strategy for docx files."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Defines the two methods for implement the `csv` ingestion strategies.

    Attributes:
        allowed_extensions {[str]} -- An array of the allowed extensions that can be ingested
    """

    allowed_extensions = ['csv']

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
        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes


# ingestor = CSVIngestor.parse('../_data/SimpleLines/SimpleLines.csv')
# ingestor = CSVIngestor.parse('../_data/DogQuotes/DogQuotesCSV.csv')
# print(ingestor)
