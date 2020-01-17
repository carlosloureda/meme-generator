"""IngestorInterface strategy operator that implements an Ingestor strategy for docx files."""

from typing import List
import subprocess
import os
import random

from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Defines the two methods for implement the `pdf` ingestion strategies.

    Attributes:
        allowed_extensions {[str]} -- An array of the allowed extensions that can be ingested
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest a given file retreiving all the quotes from it.

        Attributes:
            path {str} -- The path of the file which we are going to parse

        Returns:
            List[QuoteModel] -- All the quotes present in that given file
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                body, author = line.split(' - ')
                quotes.append(QuoteModel(body, author))

        file_ref.close()
        os.remove(tmp)
        return quotes


# ingestor = PDFIngestor.parse('../_data/SimpleLines/SimpleLines.pdf')
# ingestor = PDFIngestor.parse('../_data/DogQuotes/DogQuotesPDF.pdf')
# print(ingestor)
