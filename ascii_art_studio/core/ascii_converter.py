#!/usr/bin/env python3
"""
ASCII converter module for ASCII Art Studio.

This module handles converting grayscale images to ASCII characters.
"""

class AsciiConverter:
    """Class for converting grayscale images to ASCII art."""

    # Standard ASCII character set from darkest to lightest
    DEFAULT_CHAR_SET = "@%#*+=-:. "
    # Reversed character set (from lightest to darkest)
    REVERSED_CHAR_SET = " .:-=+*#%@"
    # Extended character set for more detail
    EXTENDED_CHAR_SET = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    def __init__(self, char_set=None, inverted=False):
        """
        Initialize the ASCII converter.

        Args:
            char_set (str, optional): Custom character set to use for conversion.
                                      Defaults to None (uses DEFAULT_CHAR_SET).
            inverted (bool, optional): Whether to invert the character set (light to dark).
                                       Defaults to False.
        """
        if char_set is None:
            self.char_set = self.DEFAULT_CHAR_SET
        else:
            self.char_set = char_set

        if inverted:
            self.char_set = self.char_set[::-1]  # Reverse the character set
            
        self.char_range = len(self.char_set) - 1

    def pixel_to_ascii(self, pixel_value):
        """
        Convert a grayscale pixel value to an ASCII character.

        Args:
            pixel_value (int): Grayscale pixel value (0-255).

        Returns:
            str: Corresponding ASCII character.
        """
        # Map the pixel value (0-255) to a character in the set
        # 0 is black, 255 is white
        index = int(pixel_value * self.char_range / 255)
        return self.char_set[index]

    def convert_image(self, image_processor, width=None):
        """
        Convert an image to ASCII art.

        Args:
            image_processor (ImageProcessor): An image processor with a loaded image.
            width (int, optional): The width of the ASCII art in characters.
                                   Defaults to None (uses image width).

        Returns:
            list: List of strings representing rows of ASCII art.
            None: If no image is loaded in the image processor.

        Raises:
            ValueError: If the width is not positive.
        """
        if not image_processor.is_image_loaded():
            return None

        img_width, img_height = image_processor.get_image_dimensions()
        
        # If width is not specified, use the image width
        if width is None:
            width = img_width
        elif width <= 0:
            raise ValueError("Width must be positive")

        # Calculate height to maintain aspect ratio
        aspect_ratio = img_height / img_width
        height = int(width * aspect_ratio / 2)  # Divide by 2 because characters are taller than wide
        
        # Calculate step size to sample the image
        x_step = img_width / width
        y_step = img_height / height
        
        # Generate ASCII art
        ascii_rows = []
        for y in range(height):
            row = ""
            for x in range(width):
                # Sample the image at calculated positions
                img_x = int(x * x_step)
                img_y = int(y * y_step)
                pixel = image_processor.get_pixel(img_x, img_y)
                row += self.pixel_to_ascii(pixel)
            ascii_rows.append(row)
            
        return ascii_rows

    def set_char_set(self, char_set, inverted=False):
        """
        Set a new character set for the converter.

        Args:
            char_set (str): New character set to use.
            inverted (bool, optional): Whether to invert the character set. Defaults to False.
        """
        self.char_set = char_set
        if inverted:
            self.char_set = self.char_set[::-1]
        self.char_range = len(self.char_set) - 1

    def get_available_char_sets(self):
        """
        Get information about available character sets.

        Returns:
            dict: Dictionary of available character sets.
        """
        return {
            "default": self.DEFAULT_CHAR_SET,
            "reversed": self.REVERSED_CHAR_SET,
            "extended": self.EXTENDED_CHAR_SET
        } 