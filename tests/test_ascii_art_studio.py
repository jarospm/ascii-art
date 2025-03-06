import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from ascii_art_studio.ascii_art_studio import print_welcome
from ascii_art_studio.cli.command_executor import CommandExecutor


class TestAsciiArtStudio(unittest.TestCase):
    """Test cases for the main ASCII Art Studio application."""

    def test_welcome_message(self):
        """Test that the welcome message is displayed correctly."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_welcome()
            output = fake_out.getvalue()
            self.assertIn("ASCII Art Studio", output)
            self.assertIn("Convert your images to beautiful ASCII", output)
    
    def test_command_executor(self):
        """Test that CommandExecutor can handle basic commands."""
        executor = CommandExecutor()
        
        # Test help command
        result = executor.execute_command("help")
        self.assertIn("Available commands", result)
        
        # Test unknown command
        result = executor.execute_command("unknown_command")
        self.assertIn("Unknown command", result)
        
        # Test quit command
        result = executor.execute_command("quit")
        self.assertIn("Goodbye", result)
        self.assertFalse(executor.is_running)


if __name__ == "__main__":
    unittest.main() 