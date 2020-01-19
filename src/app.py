"""Flask server file. We will be serving a '/'  and a '/create'  endpoints so \
the user can see random created memes or create a custom one."""

import random
import os
import requests
import json
from flask import Flask, render_template, abort, request, redirect, url_for

from typing import List, Tuple
from PIL import Image

from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine

app = Flask(__name__)
meme = MemeEngine('./static')


def get_images(path: str) -> List[str]:
    """Get all the images in path.

    Arguments:
        path {str} -- The path where to look for images

    Return:
        List[str] -- A List of images paths
    """
    imgs = []
    valid_images = [".jpg", ".gif", ".png", ".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(os.path.join(path, f))
    return imgs


def setup() -> Tuple[List[str], List[str]]:
    """Load all resources.

    Returns:
        (quotes, imgs)  { Tuple[List[str], List[str]] } -- Get all the quotes
                                                        and Images to work with
    """
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


@app.route('/')
def meme_rand():
    """Generate a random meme.

    Returns:
        The result of rendering the `meme.html` template
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information.

    Returns:
        The result of rendering the `meme_form.html` template
    """
    messages = request.args['messages']  # counterpart for url_for()
    # return render_template('meme_form.html', error=json.loads(messages.error))
    return render_template('meme_form.html')


# https://i.redd.it/me6ijotn0kq31.jpg
# I love you 3000
# Tony Stark
@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    Returns:
        The result of rendering the `meme.html` template
    """
    if not request or not request.form:
        raise Exception("Not proper request")

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    data = request.form.to_dict(flat=True)
    # if data["image_url"] == "" or data["body"] == "":
    #     messages = json.dumps(
    #         {"error": "Sorry human! I need an image and a quote for builing a meme for you :)"})
    #     return redirect(url_for('meme_form', messages=messages))

    image_url = data["image_url"]
    image_tmp_path = f'./tmp/{image_url[image_url.rfind("/") +1:]}'
    r = requests.get(image_url, allow_redirects=False)

    open(image_tmp_path, 'wb').write(r.content)

    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    path = meme.make_meme(image_tmp_path, data["body"], data["author"])
    # 3. Remove the temporary saved image.
    os.remove(image_tmp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
