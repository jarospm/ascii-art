#!/usr/bin/env python3
"""
Renderer module for ASCII Art Studio.

This module handles rendering ASCII art with proper width and aspect ratio preservation.
"""


class AsciiRenderer:
    """Class for rendering ASCII art."""

    def __init__(self, width=80, height=None, colorize=False):
        """
        Initialize the ASCII renderer.

        Args:
            width (int, optional): Default width for rendering ASCII art. Defaults to 80.
            height (int, optional): Default height for rendering ASCII art. Defaults to None.
            colorize (bool, optional): Whether to use color in terminal output. Defaults to False.
        """
        self.width = width
        self.height = height
        self.colorize = colorize
        # Set default values for terminal colors if colorize is enabled
        self.fg_color = "\033[37m"  # White text
        self.bg_color = "\033[40m"  # Black background
        self.reset_color = "\033[0m"  # Reset colors

    def render_to_terminal(self, ascii_rows):
        """
        Render ASCII art to the terminal.

        Args:
            ascii_rows (list): List of strings representing rows of ASCII art.

        Returns:
            bool: True if rendering was successful, False otherwise.
        """
        if not ascii_rows:
            return False

        try:
            # Apply colors if colorize is enabled
            if self.colorize:
                print(f"{self.fg_color}{self.bg_color}")

            # Print each row of ASCII art
            for row in ascii_rows:
                print(row)

            # Reset colors if colorize was enabled
            if self.colorize:
                print(self.reset_color, end="")

            return True
        except Exception as e:
            print(f"Error rendering ASCII art: {str(e)}")
            return False

    def render_to_string(self, ascii_rows):
        """
        Render ASCII art to a single string.

        Args:
            ascii_rows (list): List of strings representing rows of ASCII art.

        Returns:
            str: A single string containing the ASCII art with newlines.
                 Returns empty string if ascii_rows is None or empty.
        """
        if not ascii_rows:
            return ""

        return "\n".join(ascii_rows)

    def render_to_file(self, ascii_rows, filename, mode="w"):
        """
        Render ASCII art to a file.

        Args:
            ascii_rows (list): List of strings representing rows of ASCII art.
            filename (str): Path to the output file.
            mode (str, optional): File opening mode. Defaults to "w".

        Returns:
            bool: True if rendering was successful, False otherwise.
        """
        if not ascii_rows:
            return False

        try:
            with open(filename, mode, encoding="utf-8") as f:
                for row in ascii_rows:
                    f.write(row + "\n")
            return True
        except Exception as e:
            print(f"Error writing to file {filename}: {str(e)}")
            return False

    def set_dimensions(self, width=None, height=None):
        """
        Set the dimensions for ASCII art rendering.

        Args:
            width (int, optional): Width in characters. Defaults to None (keeps current).
            height (int, optional): Height in characters. Defaults to None (keeps current).
        """
        if width is not None:
            if width <= 0:
                raise ValueError("Width must be positive")
            self.width = width

        if height is not None:
            if height <= 0:
                raise ValueError("Height must be positive")
            self.height = height

    def set_colors(self, fg_color=None, bg_color=None, colorize=None):
        """
        Set color options for terminal rendering.

        Args:
            fg_color (str, optional): ANSI foreground color code. Defaults to None (keeps current).
            bg_color (str, optional): ANSI background color code. Defaults to None (keeps current).
            colorize (bool, optional): Whether to use color. Defaults to None (keeps current).
        """
        if fg_color is not None:
            self.fg_color = fg_color

        if bg_color is not None:
            self.bg_color = bg_color

        if colorize is not None:
            self.colorize = colorize 