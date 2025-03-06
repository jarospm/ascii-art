#!/usr/bin/env python3
"""
Demo script for using the renderer with the ASCII converter.
"""

import os
import sys
from ascii_art_studio.core.image_processor import ImageProcessor
from ascii_art_studio.core.ascii_converter import AsciiConverter
from ascii_art_studio.core.renderer import AsciiRenderer


def main():
    """
    Demonstrate the functionality of the ASCII renderer.
    """
    # Initialize components
    image_proc = ImageProcessor()
    ascii_conv = AsciiConverter()
    ascii_renderer = AsciiRenderer(width=100, colorize=False)

    # Get the absolute path to the project root directory
    # This allows the script to work regardless of where it's run from
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    # Try to load an image
    try:
        # Check for sample images in the project
        sample_images = [
            os.path.join(project_root, "tests", "test_images", "chimplie_logo.png"),
            os.path.join(project_root, "tests", "test_images", "Mmm.png"),
            # Fallback to the original locations in case images weren't moved
            os.path.join(project_root, "chimplie_logo.png"),
            os.path.join(project_root, "Mmm.png")
        ]
        
        for image_path in sample_images:
            try:
                print(f"\nTrying to load image: {image_path}")
                if image_proc.load_image(image_path):
                    print(f"Successfully loaded {image_path}")
                    break
            except Exception as e:
                print(f"Could not load {image_path}: {str(e)}")
        else:
            # If no sample images were loaded, prompt for a file path
            image_path = input("Enter the path to an image file: ")
            image_proc.load_image(image_path)
            print(f"Successfully loaded {image_path}")

        # Display image information
        image_info = image_proc.get_image_info()
        print("\nImage Information:")
        print(f"Filename: {image_info['filename']}")
        print(f"Dimensions: {image_info['width']}x{image_info['height']}")
        print(f"Format: {image_info['format']}")

        # Convert the image to ASCII
        print("\nConverting image to ASCII art...")
        ascii_art = ascii_conv.convert_image(image_proc, width=ascii_renderer.width)

        # Render ASCII art to the terminal
        print("\nRendering ASCII art to terminal:")
        ascii_renderer.render_to_terminal(ascii_art)

        # Save ASCII art to a file
        print("\nSaving ASCII art to file...")
        output_file = os.path.join(os.getcwd(), "ascii_art_output.txt")
        if ascii_renderer.render_to_file(ascii_art, output_file):
            print(f"ASCII art saved to {output_file}")

        # Demonstrate different character sets
        print("\nDemonstrating different character sets:")
        char_sets = ascii_conv.get_available_char_sets()
        
        for name, char_set in char_sets.items():
            print(f"\nCharacter set: {name}")
            ascii_conv.set_char_set(char_set)
            ascii_art = ascii_conv.convert_image(image_proc, width=ascii_renderer.width)
            ascii_renderer.render_to_terminal(ascii_art)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main() 