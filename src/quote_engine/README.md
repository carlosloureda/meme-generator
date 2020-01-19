# quote_engine

The Quote Engine Module is responsible for ingesting many types of files that contain quotes. A quote contains a body and an author (e.g. "this is a quote body" - Author). This module is composed of many classes to demonstrate the understanding of complex inheritance, abstract classes, classmethods, strategy objects, and other fundamental programming principles. The responsibility of this module is to load and parse quotes from file.

As at this moment, this module has a built-in classes:

- **IngestorInterface** Abstract base class to define the _can_ingest_ and the _parse_ methods. The rest of the classes in this module will be the ones that will implement this interface to digest different text file documents

- **TextIngestor:** IngestorInterface strategy operator that implements an Ingestor strategy for text files.
- **CSVIngestor:** IngestorInterface strategy operator that implements an Ingestor strategy for CSV files.
- **DocxIngestor:** IngestorInterface strategy operator that implements an Ingestor strategy for docx files.
- **PDFIngestor:** IngestorInterface strategy operator that implements an Ingestor strategy for PDF files.

- **Ingestor:** Strategy operator that implements all Ingestor strategies.

## Table of Contents

- [Dependencies](#dependencies)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Dependencies

- You need **Python3** to run this project, and also the following modules:

- [typing](https://pypi.org/project/typing/)

```
pip install typing
```

- [pandas](https://pypi.org/project/pandas/)

```
pip install pandas
```

- [docx](https://pypi.org/project/python-docx/)

```
pip install python-docx
```

## Usage

- A few examples of how to use the module.

* Add this module into your project.
* Import it:

```
from quote_engine import Ingestor
```

- Call the `Ingestor.parse()` class method with the path of the file you want to ingest:

```
Ingestor.parse("../_data/DogQuotes/DogQuotesCSV.csv")
```

If you want further instructions on how to run the complete program please go to the main README.md file of this project.

## Support

Please [open an issue](https://github.com/carlosloureda/meme-generator/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/carlosloureda/meme-generator/compare/).
