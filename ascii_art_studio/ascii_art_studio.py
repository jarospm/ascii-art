"""
ASCII Art Studio - A command-line application to convert images to ASCII art.

This module serves as the main entry point for the application.
"""

import sys
from ascii_art_studio.cli import CommandExecutor


def print_welcome():
    """Print the welcome message for the application."""
    welcome_text = """
    ┌─────────────────────────────────────────────────┐
    │                ASCII Art Studio                 │
    │                                                 │
    │      Convert your images to beautiful ASCII     │
    │                                                 │
    │           Type 'help' to get started            │
    └─────────────────────────────────────────────────┘
    """
    print(welcome_text)


def main():
    """
    Main entry point for the ASCII Art Studio application.
    Initializes the application and starts the command loop.
    """
    print_welcome()
    
    # Initialize the command executor
    executor = CommandExecutor()
    prompt = "AAS> "
    
    # Main command loop
    while executor.is_running:
        try:
            # Get user input and execute command
            command = input(prompt)
            result = executor.execute_command(command)
            
            # Print the result if any
            if result:
                print(result)
                
        except KeyboardInterrupt:
            # Simple handler for Ctrl+C
            print("\nTo exit the application, type 'quit' or 'exit'")
            
        except Exception as e:
            # Simple catch-all for any other errors
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main() 