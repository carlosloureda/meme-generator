"""The Meme Engine Module is responsible for manipulating and drawing text onto images."""
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont
import os


class MemeEngine():
    """Lets us create new memes from our images and strings folders.

    Attributes:
        output_dir {str} -- The path for the folder where to save the generated memes
        font_size {int}  -- The size of the font we are going to use for the texts
    """

    def __init__(self, output_dir: str, font_size: int = 40) -> None:
        """Init QuoteModel with the output_dir."""
        if not output_dir:
            raise Exception(
                "You need to specify an output directory for the generated memes")
        if output_dir[-1] != "/":
            output_dir += "/"
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        self.output_dir = output_dir
        self.font_size = font_size

    def _resize_image(self, img: Image, width: int) -> Image:
        """Resizes an image at the given width,  the height is scaled proportionally."""
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        return img

    def _add_text_to_image(self, img: Image, text: str, is_footer: bool = False, pos: Tuple[int, int] = None) -> None:
        """Write a text into an image.

        This private method will align center the texts depending on the image and text width, also
        considering the font size. We will use this for a header text and a footer text so it calculates
        the position

        Arguments:
            img      {Image} -- The image on which to add the text
            text      {str}  -- The text to be written on the image.
            is_footer {bool} -- If the text is a footer text we will write it on the footer of the image otherwise it will go on the header
            pos  (int, int)} -- The position where we want to set the text in case we want to manually set it
        """
        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(
                "./_data/fonts/impact.ttf", size=self.font_size)

            # We want the texts centered
            if not pos:
                text_width, text_height = draw.textsize(text, font=font)
                image_width, image_height = img.size

                x_position = (image_width - text_width) / 2
                y_position = self.font_size if not is_footer else image_height - self.font_size*2

                pos = (x_position, y_position)

            draw.text(pos, text, fill="white",  font=font)

    def _save_meme_to_folder(self, img: Image, img_path: str) -> str:
        """Save the new created meme into the proper image folder.

        It gets the original file path to get the new name of the meme file, this will work like this:
        if img_path is `xander_1.jpq` the new meme generated file name will be `xender_1_meme_0.jpg`. If `xender_1_meme_0.jpg`
        exists it will keep increase the index until the file doesn't exist

        Arguments:
            img      {Image} -- The image/meme to be saved
            img_path  {str}  -- The path for the original image so we can get filename/basename to name properly our meme

        Returns:
            out_path {str} -- The path where that new meme was saved.
        """
        img_basename = os.path.basename(img_path)

        index = 0
        img_filename, extension = os.path.splitext(img_basename)
        while True:
            out_path = f'{self.output_dir}{img_filename}_meme_{index}_{extension}'
            index += 1
            if not os.path.exists(out_path):
                break

        img.save(out_path)
        return out_path

    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        """Instance method to create a meme from an image.

        Arguments:
            img_path  {str} -- The path for the original image to create the meme from
            text      {str} -- The text of the quote to add in the new meme
            author    {str} -- The author of the quote to add in the new meme
            width     {int} -- Defaults to 500. The width for the image to resize it

        Returns:
            out_path {str} -- The path where that new meme was saved.
        """
        # TODO: check if this is possible??
        img_path = img_path
        img = Image.open(img_path)

        img = self._resize_image(img, width)

        self._add_text_to_image(img, text)
        self._add_text_to_image(img, author, is_footer=True)

        out_path = self._save_meme_to_folder(img, img_path)
        return out_path


# memeGenerator = MemeEngine("./output_memes")
# memeGenerator.make_meme(
#     "../_data/photos/dog/xander_1.jpg", "Quote 1", "Author 1")
