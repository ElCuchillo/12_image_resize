import os
import argparse
from PIL import Image


def get_script_arguments():
    parser = argparse.ArgumentParser(description='Image resizing by '
                                                 'width/height or scale')
    parser.add_argument('original_file',
                        help='Filepath to original image to be resized')
    parser.add_argument('-o', '--output',
                        help='Filepath to save resized image')
    parser.add_argument('-w', '--width', type=int, default=0,
                        help='Target width')
    parser.add_argument('-ht', '--height', type=int, default=0,
                        help='Target height')
    parser.add_argument('-s', '--scale', type=float, default=0,
                        help='Scale for resizing')
    args = parser.parse_args()
    return args.original_file, args.output, args.width, args.height, \
           args.scale


def get_new_sizes(source_image, arg_width, arg_height,
                          arg_scale):
    warning = None
    if arg_scale:
        if arg_width or arg_height:
            raise ValueError("Too many parameters. "
                             "Either scale or sizes to be specified")
        else:
            new_width = round(arg_scale * source_image.size[0])
            new_height = round(arg_scale * source_image.size[1])
            return  new_width, new_height, warning

    else:
        width_scale = round(arg_width / source_image.size[0], 3)
        height_scale = round(arg_height / source_image.size[1], 3)

        if arg_width and arg_height:
            if width_scale != height_scale:
                warning = "WARNING! Can't keep original image ratio!"
            return arg_width, arg_height, warning

        if arg_width or arg_height:
            new_scale = width_scale + height_scale
            new_width = round(new_scale * source_image.size[0])
            new_height = round(new_scale * source_image.size[1])
            return new_width, new_height, warning


if __name__ == '__main__':
    source_file, destination_file,  arg_width, arg_height, \
    arg_scale = get_script_arguments()
    try:
        source_image = Image.open(source_file)

        new_width, new_height, warning = \
            get_new_sizes(source_image, arg_width, arg_height, arg_scale)

        if warning:
            print(warning)

        if not destination_file:
            file_name, file_ext = os.path.splitext(source_file)
            destination_file = '{}__{}x{}{}'.format(file_name, new_width,
                                                     new_height, file_ext)

        new_image = source_image.resize((new_width, new_height))
        new_image.save(destination_file)
        print('New image saved in {}'.format(destination_file))

    except ValueError as error:
        print(error)

    except FileNotFoundError as error:
        print(error)

    except OSError as error:
        print(error)