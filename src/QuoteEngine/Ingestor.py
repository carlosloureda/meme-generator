"""Strategy operator that implements all Ingestor strategies."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Defines a method to parse all files calling the different Ingestors.

    Attributes:
        ingestors {[IngestorInterface]} -- An array of all the ingestor to test
    """

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest a given file retreiving all the quotes from it.

        Attributes:
            path {str} -- The path of the file which we are going to parse

        Returns:
            List[QuoteModel] -- All the quotes present in that given file
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)


# quote_files = ['../_data/DogQuotes/DogQuotesTXT.txt',
#                '../_data/DogQuotes/DogQuotesDOCX.docx',
#                '../_data/DogQuotes/DogQuotesPDF.pdf',
#                '../_data/DogQuotes/DogQuotesCSV.csv']
# ingestors = []
# for file in quote_files:
#     ingestors += Importer.parse(file)

# for ingestor in ingestors:
#     print("ingestor.body: ", ingestor.body)
# print("ingestors: ", ingestors)
