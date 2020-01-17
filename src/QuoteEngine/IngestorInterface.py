"""
An abstract base class, IngestorInterface.

Defines the two methods for being overrided on the different strategies.
Separate strategy objects should realize IngestorInterface for each file type (csv, docx, pdf, txt).
A final Ingestor class should realize the IngestorInterface abstract base class and encapsulate your helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.
"""

from abc import ABC, abstractmethod
from typing import List
from QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Defines the two methods for implement the docs ingestion strategies.

    Attributes:
        allowed_extensions {[str]} -- An array of the allowed extensions that can be ingested
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Specify if a given file can be ingested by the class that implements the ingestion strategy.

        Attributes:
            path {str} -- The path of the file which we are going to check if can be ingested

        Returns:
            bool -- if the file can be ingested or not
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest a given file retreiving all the quotes from it.

        Attributes:
            path {str} -- The path of the file which we are going to parse

        Returns:
            List[QuoteModel] -- All the quotes present in that given file
        """
        pass
