# ASCII Art Studio

A command-line application that converts images to ASCII art.

## Features

- Load image files and convert them to ASCII art
- Render ASCII art with a fixed width of 50 characters
- Display information about the loaded image
- Simple command-line interface

## Requirements

- Python 3.6+
- Pillow (Python Imaging Library)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/ascii-art-studio.git
   cd ascii-art-studio
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```
python ascii_art_studio.py
```

### Commands

- `load filename`: Load an image file
- `render`: Display ASCII art for the current image
- `info`: Show information about the current image
- `quit`: Exit the application

## Example

```
Welcome to ASCII Art Studio!
AAS: load example.jpg
AAS: render
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       ...
AAS: info
File: example.jpg
Size: 640x480
AAS: quit
Bye!
```