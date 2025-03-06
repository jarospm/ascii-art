As a user, I can enter the commands listed below to work with ASCII art.

## Commands

"load filename":
- Load the image file *filename* and set it as the "current image".
- If an error occurs during loading (e.g., the file does not exist, incorrect filename, unreadable file, wrong format, etc.), an error message
should be displayed.

"render":
- Take the current image and print ASCII art representing the image.
- The width of the printed image should be 50 characters.
- The height should be chosen to preserve the image’s proportions, with an adjustment for the fact that the rectangular shapes used by fonts tend to be narrow (and font-dependent).

"info":
- Print information about the current image: filename and size. 
- If no image has been loaded, the message "No image loaded" should be displayed.

"quit":
- Ends the session.

## Example

In the example below, AAS is the program’s prompt. The instructions are:
- load
- render
- quit

Welcome to ASCII Art Studio!
AAS: load grayscale.jpg
AAS: render
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
       .....::::ijjjjxxxxoooOhhhhXXXX%@@@@########
AAS: quit
Bye!

## Requirements

1. ASCII art should be a reasonable representation of the original image. You may choose how to map
grayscale values to characters, but it should be recognizable as ASCII art.
2. The printed ASCII art must have a width of 50 characters.
3. It should be possible to enter commands (see the example!) and display images.
4. A menu system is not accepted as a command interface.