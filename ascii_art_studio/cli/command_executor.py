"""
Command executor module for ASCII Art Studio.

This module handles executing commands parsed by the command parser.
"""

import os
from typing import Dict, Any, Optional, Tuple

from ascii_art_studio.core.image_processor import ImageProcessor
from ascii_art_studio.core.ascii_converter import AsciiConverter
from ascii_art_studio.core.renderer import AsciiRenderer
from ascii_art_studio.cli.command_parser import CommandParser


class CommandExecutor:
    """
    Class for executing commands in the ASCII Art Studio application.
    
    This class handles the execution of commands parsed by the CommandParser,
    interacting with the core modules to perform image processing, ASCII
    conversion, and rendering.
    """
    
    def __init__(self):
        """Initialize the command executor with necessary components."""
        self.image_processor = ImageProcessor()
        self.ascii_converter = AsciiConverter()
        self.renderer = AsciiRenderer()
        self.parser = CommandParser()
        self.is_running = True
        
    def execute_command(self, command_str: str) -> str:
        """
        Execute a command string.
        
        Args:
            command_str: The command string to execute
            
        Returns:
            A string containing the command output or error message
        """
        cmd_type, args = self.parser.parse_command(command_str)
        
        # Call the appropriate method based on the command type
        command_methods = {
            'load': self._execute_load,
            'render': self._execute_render,
            'info': self._execute_info,
            'quit': self._execute_quit,
            'help': self._execute_help,
            'empty': self._execute_empty,
            'unknown': self._execute_unknown
        }
        
        # Get the method for the command type or use unknown handler as fallback
        handler = command_methods.get(cmd_type, self._execute_unknown)
        return handler(args)
    
    def _execute_load(self, args: Dict[str, Any]) -> str:
        """
        Execute the 'load' command.
        
        Args:
            args: Dictionary containing command arguments
            
        Returns:
            A string containing the command output or error message
        """
        filename = args.get('filename')
        
        try:
            if self.image_processor.load_image(filename):
                return f"Successfully loaded image: {filename}"
            else:
                return f"Failed to load image: {filename}"
        except Exception as e:
            return f"Error loading image: {str(e)}"
    
    def _execute_render(self, args: Dict[str, Any]) -> str:
        """
        Execute the 'render' command.
        
        Args:
            args: Dictionary containing command arguments
            
        Returns:
            A string containing the rendered ASCII art or error message
        """
        if not self.image_processor.is_image_loaded():
            return "No image is currently loaded. Use 'load <filename>' to load an image."
        
        width = args.get('width')
        charset = args.get('charset')
        
        # Set the character set if specified
        if charset:
            char_sets = self.ascii_converter.get_available_char_sets()
            if charset in char_sets:
                self.ascii_converter.set_char_set(char_sets[charset])
            else:
                # If not a predefined set, use the string directly as a custom charset
                self.ascii_converter.set_char_set(charset)
        
        # Set the width if specified
        if width:
            self.renderer.set_dimensions(width=width)
        
        try:
            # Convert the image to ASCII art
            ascii_rows = self.ascii_converter.convert_image(
                self.image_processor, 
                width=self.renderer.width
            )
            
            # Return the rendered ASCII art
            return self.renderer.render_to_string(ascii_rows)
        except Exception as e:
            return f"Error rendering image: {str(e)}"
    
    def _execute_info(self, args: Dict[str, Any]) -> str:
        """
        Execute the 'info' command.
        
        Args:
            args: Dictionary containing command arguments
            
        Returns:
            A string containing information about the loaded image
        """
        if not self.image_processor.is_image_loaded():
            return "No image is currently loaded. Use 'load <filename>' to load an image."
        
        info = self.image_processor.get_image_info()
        
        # Format the information
        lines = [
            f"Filename: {info['filename']}",
            f"Dimensions: {info['width']}x{info['height']} pixels",
            f"Format: {info['format']}",
            f"Mode: {info['mode']}"
        ]
        
        return "\n".join(lines)
    
    def _execute_quit(self, args: Dict[str, Any]) -> str:
        """
        Execute the 'quit' command.
        
        Args:
            args: Dictionary containing command arguments
            
        Returns:
            A farewell message
        """
        self.is_running = False
        return "Goodbye! Thank you for using ASCII Art Studio."
    
    def _execute_help(self, args: Dict[str, Any]) -> str:
        """
        Execute the 'help' command.
        
        Args:
            args: Dictionary containing command arguments
            
        Returns:
            Help text for the specified command or general help
        """
        command = args.get('command')
        return self.parser.get_help_text(command)
    
    def _execute_empty(self, args: Dict[str, Any]) -> str:
        """
        Handle empty input.
        
        Args:
            args: Dictionary containing command arguments
            
        Returns:
            A prompt for input
        """
        return "Please enter a command. Type 'help' for a list of available commands."
    
    def _execute_unknown(self, args: Dict[str, Any]) -> str:
        """
        Handle unknown commands.
        
        Args:
            args: Dictionary containing command arguments
            
        Returns:
            An error message for unknown commands
        """
        user_input = args.get('input', 'Unknown command')
        return f"Unknown command: '{user_input}'. Type 'help' for a list of available commands." 