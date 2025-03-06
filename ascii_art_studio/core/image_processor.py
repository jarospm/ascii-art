#!/usr/bin/env python3
"""
Image processor module for ASCII Art Studio.

This module handles loading and processing images for conversion to ASCII art.
"""

from PIL import Image, UnidentifiedImageError
import os


class ImageProcessor:
    """Class for handling image loading and processing."""

    def __init__(self):
        """Initialize the image processor."""
        self.current_image = None
        self.filename = None

    def load_image(self, filename):
        """
        Load an image from a file.

        Args:
            filename (str): Path to the image file.

        Returns:
            bool: True if the image was loaded successfully, False otherwise.

        Raises:
            FileNotFoundError: If the file does not exist.
            UnidentifiedImageError: If the file is not a valid image.
            Exception: For other errors during image loading.
        """
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File not found: {filename}")

            # Load the image and convert to grayscale
            image = Image.open(filename)
            self.current_image = image.convert(mode='L')
            self.filename = filename
            return True

        except FileNotFoundError as e:
            raise e
        except UnidentifiedImageError:
            raise UnidentifiedImageError(f"Cannot identify image file: {filename}")
        except Exception as e:
            raise Exception(f"Error loading image: {str(e)}")

    def get_image_info(self):
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
            "format": self.current_image.format
        }

    def get_pixel(self, x, y):
        """
        Get the grayscale value of a pixel.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.

        Returns:
            int: Grayscale value (0-255) or None if no image is loaded.
        """
        if self.current_image is None:
            return None

        if x < 0 or x >= self.current_image.width or y < 0 or y >= self.current_image.height:
            return None

        pos = (x, y)
        return self.current_image.getpixel(pos)

    def get_image_dimensions(self):
        """
        Get the dimensions of the current image.

        Returns:
            tuple: (width, height) or None if no image is loaded.
        """
        if self.current_image is None:
            return None

        return (self.current_image.width, self.current_image.height)

    def is_image_loaded(self):
        """
        Check if an image is currently loaded.

        Returns:
            bool: True if an image is loaded, False otherwise.
        """
        return self.current_image is not None 