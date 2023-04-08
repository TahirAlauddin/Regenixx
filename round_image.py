from PIL import Image, ImageDraw
import os

def add_corners(im, rad=250, bg=True, bg_color='white', bgPix=5):
    """
    Adds rounded corners to an image and optionally places it on a background.

    :param im: The image to add rounded corners to.
    :type im: PIL.Image.Image

    :param rad: The radius of the rounded corners in pixels (default: 250).
    :type rad: int

    :param bg: Whether to place the image on a background with rounded corners (default: True).
    :type bg: bool

    :param bg_color: The color of the background (default: 'white').
    :type bg_color: str or tuple

    :param bgPix: The size of the border around the image when placed on the background (default: 5).
    :type bgPix: int

    :return: The modified image with rounded corners.
    :rtype: PIL.Image.Image
    """
    # Create a new image for the background
    bg_im = Image.new('RGB', tuple(x+(bgPix*2) for x in im.size), bg_color)
    # Create a list of images to paste onto the background
    ims = [im if not bg else im, bg_im]
    # Create a new image with a circle of radius rad
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    # Loop over the images and paste the circle onto them
    for i in ims:
        # Create a new alpha channel with the same size as the image
        alpha = Image.new('L', i.size, 'white')
        w, h = i.size
        # Paste the circle onto each corner of the alpha channel
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        # Apply the alpha channel to the image
        i.putalpha(alpha)
    # Paste the original image onto the background
    bg_im.paste(im, (bgPix, bgPix), im)
    # Return the final image (either the original image or the background with the image pasted on it)
    return im if not bg else bg_im


def add_rounded_border(image_path):
    im = Image.open(image_path)
    size = min(im.width, im.height)
    im = im.crop((0, 0, size, size))
    new_im = add_corners(im, rad=400)
    new_path = f"pdf-images/{os.path.splitext(os.path.basename(image_path))[0]}.webp"
    new_im.save(new_path, format='webp')
    return new_path


def main():
    image_file = "images/team2.jpg"
    im = Image.open(image_file)
    # im = im.resize((2000, 2000))
    size = min(im.width, im.height)
    im = im.crop((0, 0, size, size))
    new_im = add_corners(im, rad=400)
    new_im.save("output.webp", format='webp')


if __name__ == '__main__':
    main()
