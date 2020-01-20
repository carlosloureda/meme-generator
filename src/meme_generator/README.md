# meme_generator

This module is built for helping its users to create a **meme** from a given original image. It is ment to add some quotes to this images after resizing them (it also can add the author of the quote to the meme).

As at this moment, this module has a built-in class: **MemeEngine** that will let you generate these memes with ease.

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

- [Pillow](https://pypi.org/project/Pillow/)

```
pip install Pillow
```

## Usage

- Add this module into your project.
- Import it:

```
from meme_generator import MemeEngine
```

- Create a `MemeEngine` instance, here is when we set the output folder for our new generated memes:

```
memeGenerator = MemeEngine("./output_memes")
```

- Call the `make_meme` instance method with the 3 arguments:
  - original image path
  - quote body
  - quote author

```
memeGenerator.make_meme("../_data/photos/dog/xander_1.jpg", "Quote 1", "Author 1")
```

If you want further instructions on how to run the complete program please go to the main README.md file of this project.

## Support

Please [open an issue](https://github.com/carlosloureda/meme-generator/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/carlosloureda/meme-generator/compare/).
