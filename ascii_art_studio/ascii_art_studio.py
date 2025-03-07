#!/usr/bin/env python3
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
    
    # Register signal handler for graceful exit on Ctrl+C
    try:
        # Main command loop
        while executor.is_running:
            try:
                # Get user input
                command = input(prompt)
                
                # Execute the command
                result = executor.execute_command(command)
                
                # Print the result
                if result:
                    print(result)
                    
            except EOFError:
                # Handle Ctrl+D (EOF)
                print("\nUse 'quit' or 'exit' to exit the application.")
            except KeyboardInterrupt:
                # Handle Ctrl+C
                print("\nInterrupted. Use 'quit' or 'exit' to exit the application.")
            except Exception as e:
                # Handle any other exceptions
                print(f"Error: {str(e)}")
    
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        return 1
        
    return 0


if __name__ == "__main__":
    sys.exit(main()) 