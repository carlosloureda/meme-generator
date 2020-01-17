import random
import os
import requests
from flask import Flask, render_template, abort, request

from typing import List
from PIL import Image

from QuoteEngine import Ingestor
# @TODO Import your MemeEngine classes


app = Flask(__name__)

# meme = MemeEngine('./static')


# TODO: Add this to utils or to a class ? Use the pythons standard library os class to find all
# images within the images images_path directory


def get_images(path: str) -> List[Image]:
    """Get all the images in path

    Arguments:
        path {str} -- The path where to look for images

    Return:
        List[Image] -- A List of iamges on Pillow format
    """
    imgs = []
    valid_images = [".jpg", ".gif", ".png", ".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(Image.open(os.path.join(path, f)))

    print(imgs)
    return imgs


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for file in quote_files:
        quotes += Ingestor.parse(file)

    images_path = "./_data/photos/dog/"

    imgs = get_images(images_path)

    return quotes, imgs


quotes, imgs = setup()
# print(quotes, imgs)


@app.route('/')
def meme_rand():
    """Generate a random meme"""
    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = None
    quote = None
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
