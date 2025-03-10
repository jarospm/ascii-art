"""
Image processor module for ASCII Art Studio.

This module handles loading and processing images for conversion to ASCII art.
"""

import os
from PIL import Image
from typing import Dict, Tuple, Optional, Any


class ImageProcessor:
    """Class for handling image loading and processing."""

    def __init__(self):
        """Initialize the image processor."""
        self.current_image = None
        self.filename = None

    def load_image(self, filename: str) -> Tuple[bool, Optional[str]]:
        """
        Load an image from a file.

        Args:
            filename (str): Path to the image file.

        Returns:
            Tuple[bool, Optional[str]]: A tuple containing:
                - bool: True if the image was loaded successfully, False otherwise
                - Optional[str]: None on success, error message on failure
        """
        try:
            # Check for None or empty filename
            if not filename:
                return False, "No filename provided"
                
            # Check if file exists
            if not os.path.exists(filename):
                return False, f"File not found: {filename}"

            # Try to load the image and convert to grayscale
            image = Image.open(filename)
            self.current_image = image.convert(mode='L')
            self.filename = filename
            return True, None

        except Exception as e:
            return False, f"Error loading image: {str(e)}"

    def get_image_info(self) -> Optional[Dict[str, Any]]:
        """
        Get information about the current image.

        Returns:
            dict: A dictionary containing image information or None if no image is loaded.
        """
        if self.current_image is None:
            return None

        return {
            "filename": self.filename,
            "width": self.current_image.width,
            "height": self.current_image.height,
        }

    def get_pixel(self, x: int, y: int) -> Optional[int]:
        """
        Get the grayscale value of a pixel.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.

        Returns:
            int: Grayscale value (0-255) or None if no image is loaded.
                0  = black
                255 = white
        """
        if self.current_image is None:
            return None

        if x < 0 or x >= self.current_image.width or y < 0 or y >= self.current_image.height:
            return None

        pos = (x, y)
        return self.current_image.getpixel(pos)

    def get_image_dimensions(self) -> Optional[Tuple[int, int]]:
        """
        Get the dimensions of the current image.

        Returns:
            tuple: (width, height) or None if no image is loaded.
        """
        if self.current_image is None:
            return None

        return (self.current_image.width, self.current_image.height)

    def is_image_loaded(self) -> bool:
        """
        Check if an image is currently loaded.

        Returns:
            bool: True if an image is loaded, False otherwise.
        """
        return self.current_image is not None 