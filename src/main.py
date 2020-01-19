"""Command line interpreter (CLI) for creating our own memes from some pictures on your local machine."""

import os
import random
import argparse

from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeGenerator import MemeEngine


def generate_meme(path: str = None, body: str = None, author: str = None) -> str:
    """Generate a meme given an path and a quote.

    Arguments:
        path {str} -- The path where to look for original image
        body {str} -- The quote to add to the meme
        author {str} -- The author of the quote

    Return:
        str  {str} -- The path where the new meme is saved
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        # TODO: I had to remove the [0] from here to make it work
        img = path
    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create your own meme !!!")
    parser.add_argument(
        '-p', '--path', type=str, help="Where is the original image located?")
    parser.add_argument(
        '-b', '--body', type=str, help="The main text for the meme quote")
    parser.add_argument('-a', '--author', type=str,
                        help="The author of the quote")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
