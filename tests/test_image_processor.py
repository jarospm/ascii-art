"""
Test file for the image processor module of ASCII Art Studio.

This script tests the essential functionality of the ImageProcessor class.
"""

import unittest
import os
from ascii_art_studio.core.image_processor import ImageProcessor


class TestImageProcessor(unittest.TestCase):
    """Test cases for the ImageProcessor class."""

    def setUp(self):
        """Set up test environment."""
        self.processor = ImageProcessor()
        self.test_dir = os.path.join("tests", "test_images")
        self.test_image = os.path.join(self.test_dir, "girl.jpg")

    def test_load_valid_image(self):
        """Test loading a valid image."""
        success, error = self.processor.load_image(self.test_image)
        self.assertTrue(success)
        self.assertIsNone(error)
        self.assertTrue(self.processor.is_image_loaded())

    def test_load_invalid_image(self):
        """Test loading a non-existent image."""
        success, error = self.processor.load_image("nonexistent.jpg")
        self.assertFalse(success)
        self.assertIsNotNone(error)
        self.assertFalse(self.processor.is_image_loaded())

    def test_image_info(self):
        """Test retrieving image information."""
        self.processor.load_image(self.test_image)
        
        info = self.processor.get_image_info()
        self.assertEqual(info["filename"], self.test_image)
        
        width, height = self.processor.get_image_dimensions()
        self.assertEqual(width, info["width"])
        self.assertEqual(height, info["height"])

    def test_pixel_access(self):
        """Test pixel access functionality."""
        self.processor.load_image(self.test_image)
        
        width, height = self.processor.get_image_dimensions()
        center_x, center_y = width // 2, height // 2
        
        pixel = self.processor.get_pixel(center_x, center_y)
        self.assertIsNotNone(pixel)
        self.assertGreaterEqual(pixel, 0)
        self.assertLessEqual(pixel, 255)


if __name__ == '__main__':
    unittest.main() 