"""IngestorInterface strategy operator that implements an Ingestor strategy for docx files."""

from typing import List
# pip3 install python-docx
from docx import Document
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Defines the two methods for implement the `docx` ingestion strategies.

    Attributes:
        allowed_extensions {[str]} -- An array of the allowed extensions that can be ingested
    """

    allowed_extensions = ['docx']

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
        doc = Document(path)

        for paragraph in doc.paragraphs:
            if paragraph.text != "":
                quote, author = paragraph.text.split(' - ')
                quotes.append(QuoteModel(quote, author))

        return quotes


# ingestor = DocxIngestor.parse('../_data/SimpleLines/SimpleLines.docx')
# ingestor = DocxIngestor.parse('../_data/DogQuotes/DogQuotesDOCX.docx')
# print(ingestor)
