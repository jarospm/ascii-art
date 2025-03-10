"""
Test file for the command parser module of ASCII Art Studio.

This script tests the functionality of the CommandParser class.
"""

import unittest
from ascii_art_studio.cli.command_parser import CommandParser


class TestCommandParser(unittest.TestCase):
    """Test cases for the CommandParser class."""

    def setUp(self):
        """Set up test environment."""
        self.parser = CommandParser()

    def test_parse_load_command(self):
        """Test parsing load command with different arguments."""
        # Simple filename
        cmd_type, args = self.parser.parse_command("load test.jpg")
        self.assertEqual(cmd_type, "load")
        self.assertEqual(args, {'filename': 'test.jpg'})
        
        # Path with filename
        cmd_type, args = self.parser.parse_command("load path/to/test.jpg")
        self.assertEqual(cmd_type, "load")
        self.assertEqual(args, {'filename': 'path/to/test.jpg'})
        
        # Invalid load command (no filename)
        cmd_type, args = self.parser.parse_command("load")
        self.assertEqual(cmd_type, "unknown")
        self.assertEqual(args, {'input': 'load'})

    def test_parse_help_command(self):
        """Test parsing help commands."""
        # General help
        cmd_type, args = self.parser.parse_command("help")
        self.assertEqual(cmd_type, "help")
        self.assertEqual(args, {})
        
        # Command-specific help
        cmd_type, args = self.parser.parse_command("help load")
        self.assertEqual(cmd_type, "help")
        self.assertEqual(args, {'command': 'load'})

    def test_unknown_commands(self):
        """Test parsing unknown commands."""
        cmd_type, args = self.parser.parse_command("unknown")
        self.assertEqual(cmd_type, "unknown")
        self.assertEqual(args, {'input': 'unknown'})
        
        # Invalid command format
        cmd_type, args = self.parser.parse_command("render extra")
        self.assertEqual(cmd_type, "unknown")
        self.assertEqual(args, {'input': 'render extra'})


if __name__ == '__main__':
    unittest.main() 