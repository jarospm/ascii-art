#!/usr/bin/env python3
"""
Test file for the ASCII converter module of ASCII Art Studio.

This script tests the functionality of the AsciiConverter class.
"""

import unittest
from ascii_art_studio.core.image_processor import ImageProcessor
from ascii_art_studio.core.ascii_converter import AsciiConverter

def main():
    """Test the ASCII converter functionality."""
    # Initialize the image processor and ASCII converter
    img_processor = ImageProcessor()
    ascii_converter = AsciiConverter()

    # Print available character sets
    print("Available character sets:")
    char_sets = ascii_converter.get_available_char_sets()
    for name, chars in char_sets.items():
        print(f"  - {name}: {chars}")
    
    # Test with an image if available
    image_path = "chimplie_logo.png"  # Using the image found in the project directory
    
    try:
        # Try to load the image
        img_processor.load_image(image_path)
        print(f"\nLoaded image: {image_path}")
        
        # Get and print image info
        info = img_processor.get_image_info()
        print(f"Image dimensions: {info['width']}x{info['height']}")
        
        # Convert to ASCII with default character set
        print("\nConverting to ASCII with default character set...")
        width = min(100, info['width'])  # Limit width to 100 characters
        ascii_art = ascii_converter.convert_image(img_processor, width=width)
        
        # Print the full ASCII art
        print("\nFull ASCII Art:")
        for line in ascii_art:
            print(line)
        
        # Test with inverted character set
        print("\nConverting with inverted character set...")
        ascii_converter.set_char_set(ascii_converter.DEFAULT_CHAR_SET, inverted=True)
        inverted_ascii_art = ascii_converter.convert_image(img_processor, width=width)
        
        print("\nFull Inverted ASCII Art:")
        for line in inverted_ascii_art:
            print(line)
            
        # Test with extended character set
        print("\nConverting with extended character set...")
        ascii_converter.set_char_set(ascii_converter.EXTENDED_CHAR_SET)
        extended_ascii_art = ascii_converter.convert_image(img_processor, width=width)
        
        print("\nFull Extended ASCII Art:")
        for line in extended_ascii_art:
            print(line)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Test could not be completed due to the error.")

if __name__ == "__main__":
    main() 