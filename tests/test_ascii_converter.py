"""
Test file for the ASCII converter module of ASCII Art Studio.

This script tests the functionality of the AsciiConverter class.
"""

import unittest
import os
from ascii_art_studio.core.ascii_converter import AsciiConverter
from ascii_art_studio.core.image_processor import ImageProcessor


class TestAsciiConverter(unittest.TestCase):
    """Test cases for the AsciiConverter class."""

    def setUp(self):
        """Set up test environment."""
        # Create a new converter with default settings
        self.converter = AsciiConverter()
        
        # Set up image processor with a test image
        self.image_proc = ImageProcessor()
        self.test_dir = os.path.join("tests", "test_images")
        self.test_image = os.path.join(self.test_dir, "girl.jpg")
        
        # Load the test image
        self.image_proc.load_image(self.test_image)
    
    def test_pixel_to_ascii_conversion(self):
        """Test converting different pixel values to ASCII characters."""
        # Black pixel (0) should map to the first character
        self.assertEqual(self.converter.pixel_to_ascii(0), AsciiConverter.DEFAULT_CHAR_SET[0])
        
        # White pixel (255) should map to the last character
        self.assertEqual(self.converter.pixel_to_ascii(255), AsciiConverter.DEFAULT_CHAR_SET[-1])
        
        # Gray pixel (128) should map to a middle character
        gray_result = self.converter.pixel_to_ascii(128)
        self.assertEqual(len(gray_result), 1)
        self.assertEqual(type(gray_result), str)

    def test_image_conversion(self):
        """Test converting an image to ASCII art."""
        # Convert the image with a specific width
        ascii_art = self.converter.convert_image(self.image_proc, width=40)
        
        # Check basic properties of the result
        self.assertEqual(type(ascii_art), list)
        
        # Check the first row is a string with expected width
        if ascii_art:  # In case the list is empty
            self.assertEqual(len(ascii_art[0]), 40)
            self.assertEqual(type(ascii_art[0]), str)


if __name__ == '__main__':
    unittest.main() 