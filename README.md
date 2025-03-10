# ASCII Art Studio

A command-line tool for converting images to ASCII art.

## How to Use

1. Start the program:
```bash
ascii-art-studio
```

2. Basic commands:
```
AAS: load <image_file>   # Load an image
AAS: render              # Convert and display ASCII art
AAS: info                # Display information about loaded image
AAS: quit                # Exit the program
```

## Installation

### Required Libraries
- Python 3.6+
- Pillow (Python Imaging Library)

### Installing
```bash
# Clone the repository
git clone https://github.com/yourusername/ascii-art-studio.git
cd ascii-art-studio

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Program Structure

- `ascii_art_studio/`: Main package
  - `__main__.py`: Entry point for running the application
  - `ascii_art_studio.py`: Main application logic
  - `core/`: Core functionality
    - `ascii_converter.py`: Converts images to ASCII characters
    - `image_processor.py`: Handles image loading and processing
    - `renderer.py`: Renders ASCII art to the console
  - `cli/`: Command-line interface
    - `command_executor.py`: Executes user commands
    - `command_parser.py`: Parses command-line input
  - `utils/`: Utility functions

## Example Output

```
Welcome to ASCII Art Studio!
AAS: load example.jpg
AAS: render
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       ...
AAS: info
File: example.jpg
Size: 640x480
AAS: quit
Bye!
```