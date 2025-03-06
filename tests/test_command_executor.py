import unittest
from unittest.mock import patch, MagicMock
from ascii_art_studio.cli.command_executor import CommandExecutor


class TestCommandExecutor(unittest.TestCase):
    """Test cases for the CommandExecutor class."""

    def setUp(self):
        """Set up a CommandExecutor instance for each test."""
        self.executor = CommandExecutor()

    def test_initialization(self):
        """Test that the CommandExecutor initializes correctly."""
        self.assertTrue(hasattr(self.executor, 'image_processor'))
        self.assertTrue(hasattr(self.executor, 'ascii_converter'))
        self.assertTrue(hasattr(self.executor, 'renderer'))
        self.assertTrue(hasattr(self.executor, 'parser'))
        self.assertTrue(self.executor.is_running)

    @patch('ascii_art_studio.core.image_processor.ImageProcessor.load_image')
    def test_execute_load_command(self, mock_load_image):
        """Test the execution of the 'load' command."""
        # Test successful load
        mock_load_image.return_value = True
        result = self.executor.execute_command("load test.jpg")
        self.assertIn("Successfully loaded", result)
        mock_load_image.assert_called_with("test.jpg")

        # Test failed load
        mock_load_image.return_value = False
        result = self.executor.execute_command("load test.jpg")
        self.assertIn("Failed to load", result)

    @patch('ascii_art_studio.core.image_processor.ImageProcessor.is_image_loaded')
    def test_execute_render_without_image(self, mock_is_image_loaded):
        """Test rendering without an image loaded."""
        mock_is_image_loaded.return_value = False
        result = self.executor.execute_command("render")
        self.assertIn("No image is currently loaded", result)

    @patch('ascii_art_studio.core.image_processor.ImageProcessor.is_image_loaded')
    @patch('ascii_art_studio.core.ascii_converter.AsciiConverter.convert_image')
    @patch('ascii_art_studio.core.renderer.AsciiRenderer.render_to_string')
    def test_execute_render_with_image(self, mock_render, mock_convert, mock_is_loaded):
        """Test rendering with an image loaded."""
        mock_is_loaded.return_value = True
        mock_convert.return_value = ["test", "ascii", "art"]
        mock_render.return_value = "test\nascii\nart"

        result = self.executor.execute_command("render")
        self.assertEqual(result, "test\nascii\nart")
        mock_convert.assert_called_once()
        mock_render.assert_called_once_with(["test", "ascii", "art"])

    @patch('ascii_art_studio.core.image_processor.ImageProcessor.is_image_loaded')
    def test_execute_info_without_image(self, mock_is_image_loaded):
        """Test info command without an image loaded."""
        mock_is_image_loaded.return_value = False
        result = self.executor.execute_command("info")
        self.assertIn("No image is currently loaded", result)

    @patch('ascii_art_studio.core.image_processor.ImageProcessor.is_image_loaded')
    @patch('ascii_art_studio.core.image_processor.ImageProcessor.get_image_info')
    def test_execute_info_with_image(self, mock_get_info, mock_is_loaded):
        """Test info command with an image loaded."""
        mock_is_loaded.return_value = True
        mock_get_info.return_value = {
            'filename': 'test.jpg',
            'width': 100,
            'height': 100,
            'format': 'JPEG',
            'mode': 'RGB'
        }

        result = self.executor.execute_command("info")
        self.assertIn("Filename: test.jpg", result)
        self.assertIn("Dimensions: 100x100 pixels", result)
        self.assertIn("Format: JPEG", result)
        self.assertIn("Mode: RGB", result)

    def test_execute_quit_command(self):
        """Test the execution of the 'quit' command."""
        result = self.executor.execute_command("quit")
        self.assertFalse(self.executor.is_running)
        self.assertIn("Goodbye", result)

        # Reset is_running for other tests
        self.executor.is_running = True

    def test_execute_help_command(self):
        """Test the execution of the 'help' command."""
        result = self.executor.execute_command("help")
        self.assertIn("Available commands", result)

        result = self.executor.execute_command("help load")
        self.assertIn("load <filename>", result)

    def test_execute_empty_command(self):
        """Test handling of empty commands."""
        result = self.executor.execute_command("")
        self.assertIn("Please enter a command", result)

    def test_execute_unknown_command(self):
        """Test handling of unknown commands."""
        result = self.executor.execute_command("unknown")
        self.assertIn("Unknown command", result)


if __name__ == "__main__":
    unittest.main() 