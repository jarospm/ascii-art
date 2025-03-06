#!/usr/bin/env python3
"""
Test file for the renderer module of ASCII Art Studio.
"""

import unittest
import os
import tempfile
from ascii_art_studio.core.renderer import AsciiRenderer


class TestAsciiRenderer(unittest.TestCase):
    """Test cases for the AsciiRenderer class."""

    def setUp(self):
        """Set up test cases."""
        self.renderer = AsciiRenderer()
        self.ascii_rows = [
            "@@@@@@@@@@@",
            "###########",
            "+++++++++++",
            "-----------",
            ":::::::::::"
        ]

    def test_render_to_string(self):
        """Test rendering ASCII art to a string."""
        result = self.renderer.render_to_string(self.ascii_rows)
        expected = "@@@@@@@@@@@\n###########\n+++++++++++\n-----------\n:::::::::::"
        self.assertEqual(result, expected)

        # Test with empty rows
        result = self.renderer.render_to_string([])
        self.assertEqual(result, "")

        # Test with None
        result = self.renderer.render_to_string(None)
        self.assertEqual(result, "")

    def test_render_to_file(self):
        """Test rendering ASCII art to a file."""
        # Create a temporary file for testing
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name

        try:
            # Test writing to file
            result = self.renderer.render_to_file(self.ascii_rows, temp_filename)
            self.assertTrue(result)

            # Verify file contents
            with open(temp_filename, 'r') as f:
                content = f.read().strip()

            expected = "@@@@@@@@@@@\n###########\n+++++++++++\n-----------\n:::::::::::"
            self.assertEqual(content, expected)

            # Test with empty rows
            result = self.renderer.render_to_file([], temp_filename)
            self.assertFalse(result)

            # Test with None
            result = self.renderer.render_to_file(None, temp_filename)
            self.assertFalse(result)

        finally:
            # Clean up temporary file
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)

    def test_set_dimensions(self):
        """Test setting dimensions."""
        # Initial values
        self.assertEqual(self.renderer.width, 80)
        self.assertIsNone(self.renderer.height)

        # Set new values
        self.renderer.set_dimensions(100, 50)
        self.assertEqual(self.renderer.width, 100)
        self.assertEqual(self.renderer.height, 50)

        # Test invalid values
        with self.assertRaises(ValueError):
            self.renderer.set_dimensions(-10)

        with self.assertRaises(ValueError):
            self.renderer.set_dimensions(100, -5)

    def test_set_colors(self):
        """Test setting colors."""
        # Initial values
        self.assertFalse(self.renderer.colorize)
        self.assertEqual(self.renderer.fg_color, "\033[37m")
        self.assertEqual(self.renderer.bg_color, "\033[40m")

        # Set new values
        self.renderer.set_colors("\033[32m", "\033[43m", True)
        self.assertTrue(self.renderer.colorize)
        self.assertEqual(self.renderer.fg_color, "\033[32m")
        self.assertEqual(self.renderer.bg_color, "\033[43m")

        # Partial update
        self.renderer.set_colors(colorize=False)
        self.assertFalse(self.renderer.colorize)
        self.assertEqual(self.renderer.fg_color, "\033[32m")
        self.assertEqual(self.renderer.bg_color, "\033[43m")


if __name__ == "__main__":
    unittest.main() 