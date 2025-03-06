#!/usr/bin/env python3
"""
ASCII Art Studio - A command-line application to convert images to ASCII art.

This module serves as the main entry point for the application.
"""

def main():
    """
    Main entry point for the ASCII Art Studio application.
    Initializes the application and starts the command loop.
    """
    print("Welcome to ASCII Art Studio!")
    
    # Main command loop will be implemented here
    prompt = "AAS: "
    running = True
    
    while running:
        command = input(prompt)
        # Command processing will be implemented in later steps
        if command.lower() == "quit":
            running = False
            print("Bye!")

if __name__ == "__main__":
    main() 