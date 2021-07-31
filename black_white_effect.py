"""
black_white_effect.py

Example of usage of Pillow lib to convert an image to black and white
version, using sys.argv to have a command line file input.
The os lib made possible remove file extension keeping the path.
The sys lib allow command line input.
"""

import os
import sys

from PIL import Image


def black_white_effect(img):
    try:
        title = os.path.splitext(img)[0]
        new_image = Image.open(img)
        bwi = new_image.convert('L')
        bwi.save(f'{title}_black_white.png')
        bwi.show()
    except Exception as err:
        return(err)


if __name__ == '__main__':
    try:
        if sys.argv:
            black_white_effect(sys.argv[1])
    except Exception as err:
        print(err)
