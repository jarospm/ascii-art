import re
from typing import Dict, Any, Optional, Tuple


class CommandParser:
    """
    Parser for ASCII Art Studio commands using regular expressions.
    
    This class provides functionality to parse and validate user input commands.
    """
    
    # Command patterns
    LOAD_PATTERN = r'^load\s+(?P<filename>.+)$'
    RENDER_PATTERN = r'^render$'
    INFO_PATTERN = r'^info$'
    QUIT_PATTERN = r'^(quit|exit)$'
    HELP_PATTERN = r'^help(?:\s+(?P<command>\S+))?$'
    
    def __init__(self):
        """Initialize the command parser with compiled regex patterns."""
        self.patterns = {
            'load': re.compile(self.LOAD_PATTERN),
            'render': re.compile(self.RENDER_PATTERN),
            'info': re.compile(self.INFO_PATTERN),
            'quit': re.compile(self.QUIT_PATTERN),
            'help': re.compile(self.HELP_PATTERN),
        }
    
    def parse_command(self, command_str: str) -> Tuple[str, Dict[str, Any]]:
        """
        Parse a command string and return the command type and its arguments.
        
        Args:
            command_str: The command string to parse
            
        Returns:
            A tuple containing (command_type, arguments_dict)
            where command_type is 'unknown' if the command is not recognized
        """
        # Strip whitespace and normalize
        command_str = command_str.strip().lower()
        
        if not command_str:
            return 'empty', {}
        
        # Try to match each command pattern
        for cmd_type, pattern in self.patterns.items():
            match = pattern.match(command_str)
            if match:
                # Extract named groups as arguments
                args = {k: v for k, v in match.groupdict().items() if v is not None}
                return cmd_type, args
        
        # If no patterns match, it's an unknown command
        return 'unknown', {'input': command_str}
    
    def get_help_text(self, command: Optional[str] = None) -> str:
        """
        Get help text for commands.
        
        Args:
            command: Optional specific command to get help for
            
        Returns:
            Help text as a string
        """
        help_texts = {
            'load': "load <filename> - Load an image file for conversion",
            'render': "render - Convert the loaded image to ASCII art with fixed width (50px)",
            'info': "info - Display information about the currently loaded image",
            'quit': "quit or exit - Exit the application",
            'help': "help [command] - Display help information"
        }
        
        if command and command in help_texts:
            return help_texts[command]
        
        # If no specific command or unknown command, return general help
        return "\n".join([
            "Available commands:",
            *[text for text in help_texts.values()]
        ]) 