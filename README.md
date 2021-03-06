# Meme Generator

Simple meme generator developed with Python & Flask.
This project is for the BETA nanodegree **Intermediate Python** at Udacity that I am testing to become a mentor and project reviewer once it gets released.

## Table of Contents

- [Installation](#installation)
- [Starter Code Overview](#startercode)
- [Usage](#usage)
- [What I will learn](#learn)
- [Arquitecture](#arquitecture)
- [Support](#support)
- [Contributing](#contributing)
- [About me](#about)

## Installation

You need to have **python3** and **python-pip** installed on your machine

Download to your project directory, (python3 required):

```sh
git clone git@github.com:carlosloureda/meme-generator.git
cd meme-generator
pip install -r requirements.txt
```

## Starter Code Overview

We've provided some code and data to get you started. Sample quotes and images of Xander the pup in `src/_data/`.

There's also a basic flask server which will consume your modules and make it usable through a web interface. The main code for this flask service is in `app.py`, templates are in `templates/` and generated images should be saved to `static/`. You'll need to install the flask dependency with `pip install flask` and you can run the server with `python3 app.py`.

## Usage

### CLI Application - main.py

Command line interpreter (CLI) for creating our own memes from some pictures on your local machine.

```
python3 main.py

# For help:
python3 main.py --help
```

### Web App - app.py

For running the web page under flask, you need to have `flask` installed.

```
flask run
```

If you want to enable hot reloadin (through the development environment):

```
export FLASK_ENV=development
flask run
```

## Learn

- Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a `data engineering role`.
- Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
- Load, manipulate, and save images.
- Accept dynamic user input through a command line tool and a web service. This emulates the kind of work you’ll encounter as a `full stack developer`.

We will cover the learned topics on the course:

- Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
- DRY (don’t repeat yourself) principles of class and method design.
- Working with modules and packages in Python.

This project starts from a [starter code repository](https://github.com/udacity/PYND/tree/master/02_meme_gen_starter) provided by Udacity.
For those users that have access to the nanodegree, here is a direct [link to the rubric](https://review.udacity.com/#!/rubrics/2709/view) for this project

## Arquitecture

- Entry point: `app.py`
  - templates are on: `templates/`
  - generated images should be saved on `static/`

This project focuses in 3 main `modules`:

## Quote Engine Module

Take a look to the [README](src/meme_generator/README.md)

The Quote Engine Module is responsible for ingesting many types of files that contain quotes. A quote contains a body and an author (e.g. "this is a quote body" - Author). This module will be composed of many classes and demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

Review rubric for specific details.

**Quote Format**
Example quotes are provided in a variety of files, take a moment to review the file formats in `./_data/SimpleLines` and `./_data/DogQuotes`. Your task is to design a system to extract each quote line-by-line from these files.

**Ingestors**
An abstract base class, IngestorInterface should define two methods with the following class method signatures:

```python
def can_ingest(cls, path) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
```

Separate strategy objects should realize `IngestorInterface` for each file type (csv, docx, pdf, txt).

A final Ingestor class should realize the `IngestorInterface` abstract base class and encapsulate your helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.

Take a look to the module's [README](src/quote_engine/README.md)

## Meme Generator Module

The Generator Module is built for helping its users to create a **meme** from a given original image. It is ment to add some quotes to this images after resizing them (it also can add the author of the quote to the meme).

As at this moment, this module has a built-in class: **MemeEngine** that will let you generate these memes with ease.

Take a look to the [README](src/meme_generator/README.md)

## Support

Please [open an issue](https://github.com/carlosloureda/meme-generator/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/carlosloureda/meme-generator/compare/).

## About

Hi! I am Carlos Loureda, a senior Full Stack Developer, entrepeneur and now mentor at Udacity. If you want to have me in your network, feel free to follow me on [Twitter](https://twitter.com/carlosloureda) and [Linkedin](https://www.linkedin.com/in/carlos-loureda-parrado)
