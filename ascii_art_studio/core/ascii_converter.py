"""
ASCII converter module for ASCII Art Studio.

This module handles converting grayscale images to ASCII characters.
"""

from typing import List, Optional
# Import the ImageProcessor for type hints
from ascii_art_studio.core.image_processor import ImageProcessor


class AsciiConverter:
    """Class for converting grayscale images to ASCII art."""

    # Fixed character set from lightest to darkest
    DEFAULT_CHAR_SET = " .:-=+*#%@"

    def __init__(self, char_set: Optional[str] = None) -> None:
        """
        Initialize the ASCII converter.

        Args:
            char_set (str, optional): Custom character set to use for conversion.
                                      Defaults to None (uses DEFAULT_CHAR_SET).
        """
        # Always use the specified fixed character set or default
        self.char_set = char_set if char_set is not None else self.DEFAULT_CHAR_SET
        self.char_range = len(self.char_set) - 1

    def pixel_to_ascii(self, pixel_value: int) -> str:
        """
        Convert a grayscale pixel value to an ASCII character.

        Args:
            pixel_value (int): Grayscale pixel value (0-255).

        Returns:
            str: Corresponding ASCII character.
        """
        # Map the pixel value (0-255) to a character in the set
        # 0 is black, 255 is white
        # proportional mapping, based on the number of ascii characters in the set
        index = int(pixel_value * self.char_range / 255)
        return self.char_set[index]

    def convert_image(self, image_processor: ImageProcessor, width: int = 50) -> Optional[List[str]]:
        """
        Convert an image to ASCII art.

        Args:
            image_processor (ImageProcessor): An image processor with a loaded image.
            width (int, optional): The width of the ASCII art in characters.
                                   Default is 50.

        Returns:
            list: List of strings representing rows of ASCII art.
            None: If no image is loaded in the image processor.

        Raises:
            ValueError: If the width is not positive.
        """
        if not image_processor.is_image_loaded():
            return None

        dimensions = image_processor.get_image_dimensions()
        if dimensions is None:
            return None
            
        img_width, img_height = dimensions
        
        # Width is fixed at 50 or the value provided
        if width <= 0:
            raise ValueError("Width must be positive")

        # Calculate height to maintain aspect ratio
        aspect_ratio = img_height / img_width
        height = int(width * aspect_ratio / 2)  # Divide by 2 because characters are taller than wide
        
        # Calculate how many image pixels to move for each ASCII character
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
                if pixel is not None:
                    row += self.pixel_to_ascii(pixel)
                else:
                    # Use a default character (space) if pixel is None
                    row += " "
            ascii_rows.append(row)
            
        return ascii_rows 

    def render_to_string(self, ascii_rows: Optional[List[str]]) -> str:
        """
        Render ASCII art rows to a single string.

        Args:
            ascii_rows (List[str]): List of strings representing rows of ASCII art.

        Returns:
            str: A single string containing the ASCII art with newlines.
                 Returns empty string if ascii_rows is None or empty.
        """
        if not ascii_rows:
            return ""

        return "\n".join(ascii_rows) 