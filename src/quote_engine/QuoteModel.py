"""QuoteModel will represent our quotes, for adding them in the memes."""


class QuoteModel():
    """Represent the quotes of our module.

    A quote contains a body and an author(e.g. "this is a quote body" - Author).

    Attributes:
        body {str} -- The quote itself.
        author {str} -- The author of the quote.

    """

    def __init__(self, body: str, author: str) -> None:
        """Init QuoteModel with body and author."""
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Override the "official" string representation of an object."""
        return f'"{self.body}" - {self.author}'
