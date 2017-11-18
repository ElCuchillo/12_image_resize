# Image Resizer

The script changes sizes of the image due to specified by user width, height or scale.

# How to use

The script takes positional and optional arguments for processing. When launching it is necessary to specify a path to file with source image to be resized.
Other parameters of the script are up to user and can be indicated by the optional keys:
- o, --output  - there is path to destination file to store processed image
- -w, --width - there is a width of new image
- -ht, --height - there is a height of new image
- -s, --scale - there is a scale for resizing
- -h - indicates usage of the script

Note, either scale or width, height can be specified for processing otherwise the script terminates with error message.
If only width or height got missing dimension will calculated to save source image ratio.
If desired wifth and height break original image ratio the script output the porper warning message and would do resizing with specified width and height.
When missing output filename there will be created a new image file with name based on the source filename with  info of the new image width and height added.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python3 image_resize.py some_image.jpg -w 300 -h 400
```

Output examples:

```bash

New image saved in some_image__300x400.jpg
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
