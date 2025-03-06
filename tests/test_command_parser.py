import unittest
from ascii_art_studio.cli.command_parser import CommandParser


class TestCommandParser(unittest.TestCase):
    """Test cases for the CommandParser class."""

    def setUp(self):
        """Set up a CommandParser instance for each test."""
        self.parser = CommandParser()

    def test_load_command(self):
        """Test parsing of the 'load' command."""
        cmd_type, args = self.parser.parse_command("load test.jpg")
        self.assertEqual(cmd_type, "load")
        self.assertEqual(args, {"filename": "test.jpg"})

        # Test with path
        cmd_type, args = self.parser.parse_command("load /path/to/image.png")
        self.assertEqual(cmd_type, "load")
        self.assertEqual(args, {"filename": "/path/to/image.png"})

    def test_render_command(self):
        """Test parsing of the 'render' command."""
        # Basic render
        cmd_type, args = self.parser.parse_command("render")
        self.assertEqual(cmd_type, "render")
        self.assertEqual(args, {})

        # Render with width
        cmd_type, args = self.parser.parse_command("render 80")
        self.assertEqual(cmd_type, "render")
        self.assertEqual(args, {"width": 80})

        # Render with width and charset
        cmd_type, args = self.parser.parse_command("render 100 standard")
        self.assertEqual(cmd_type, "render")
        self.assertEqual(args, {"width": 100, "charset": "standard"})

        # Render with just charset
        cmd_type, args = self.parser.parse_command("render standard")
        self.assertEqual(cmd_type, "render")
        self.assertEqual(args, {"charset": "standard"})
        
        # Numbers should not be parsed as charset
        cmd_type, args = self.parser.parse_command("render 123")
        self.assertEqual(cmd_type, "render")
        self.assertEqual(args, {"width": 123})
        self.assertNotIn("charset", args)

    def test_info_command(self):
        """Test parsing of the 'info' command."""
        cmd_type, args = self.parser.parse_command("info")
        self.assertEqual(cmd_type, "info")
        self.assertEqual(args, {})

    def test_quit_command(self):
        """Test parsing of the 'quit' and 'exit' commands."""
        cmd_type, args = self.parser.parse_command("quit")
        self.assertEqual(cmd_type, "quit")
        self.assertEqual(args, {})

        cmd_type, args = self.parser.parse_command("exit")
        self.assertEqual(cmd_type, "quit")
        self.assertEqual(args, {})

    def test_help_command(self):
        """Test parsing of the 'help' command."""
        # Basic help
        cmd_type, args = self.parser.parse_command("help")
        self.assertEqual(cmd_type, "help")
        self.assertEqual(args, {})

        # Help for specific command
        cmd_type, args = self.parser.parse_command("help load")
        self.assertEqual(cmd_type, "help")
        self.assertEqual(args, {"command": "load"})

    def test_empty_command(self):
        """Test parsing of empty input."""
        cmd_type, args = self.parser.parse_command("")
        self.assertEqual(cmd_type, "empty")
        self.assertEqual(args, {})

        cmd_type, args = self.parser.parse_command("   ")
        self.assertEqual(cmd_type, "empty")
        self.assertEqual(args, {})

    def test_unknown_command(self):
        """Test parsing of unknown commands."""
        cmd_type, args = self.parser.parse_command("unknown_command")
        self.assertEqual(cmd_type, "unknown")
        self.assertEqual(args, {"input": "unknown_command"})

    def test_help_text(self):
        """Test the help text functionality."""
        # Help for specific command
        load_help = self.parser.get_help_text("load")
        self.assertIn("load <filename>", load_help)

        # General help
        general_help = self.parser.get_help_text()
        self.assertIn("Available commands:", general_help)
        self.assertIn("load <filename>", general_help)
        self.assertIn("render [width] [charset]", general_help)


if __name__ == "__main__":
    unittest.main() 