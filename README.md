# Steganography Encryption and Decryption Tool
❗❗❗ SPOILER ALERT: This project was completed as a part of the 2025 Hack the North Capture the Flag challenge. I strongly reccommend everyone to give it a try [here](https://hackthenorth.com/).

## About
Image steganography is the technique of hiding a secret message within an ordinary picture. It works by subtly altering the Least Significant Bits (LSBs) of the image's pixel data, which are typically undetectable changes to the naked eye. In this project, I built a tool to encrypt and decrypt hidden messages in image files using the Pillow library in Python. While similar tools have been created based on the technique of modifying LSBs in an image's RGB values, my program adds another layer of security by incorporating a secret key that determine the rules of encryption and decryption. The idea was presented to me by the team behind Hack the North, to whom I want to send a massive thank you for creating the Capture the Flag challenge.

## Features
* **Image-based Steganography**: Embed and extract hidden messages within image files.
* **Customizable Encryption Key**: Utilizes a user-defined Boolean function in `key.py` as a secret key, adding an extra layer of security beyond traditional LSB methods.
* **Encryption**: Encrypts text messages into an image, saving the result as `encrypted.png`.
* **Decryption**: Decrypts hidden messages from an image, saving the extracted text to `decrypted.txt`.

## Example
<img width="1200" height="1200" alt="Original image" src="https://github.com/user-attachments/assets/f66cbc02-fe27-4609-867e-b8d1b4ea0583" />

## Mechanism
The core idea behind this tool is to manipulate the RGB values of an image based on a secret Boolean function defined in `key.py`.
### Encryption
1. The message to be hidden is converted into a binary sequence.
2. For each bit of the message, the program iterates through the pixels, left to right, top to bottom, and color channels (Red, Green, Blue) of the image.
3. For each pixel's color channel, the program finds a new RGB value such that when its 8-bit binary representation is passed through your secret key, the output matches the current bit of the message.
4. The modified image is saved as `encrypted.png`.
### Decryption
1. The program extracts the 8-bit binary representation of each color channel from every pixel in the image.
2. Each 8 bits (byte) are then passed through your secret key, a Boolean function.
3. The output (True/False) from the schematic function is converted back into a '1' or '0' bit.
4. These bits are concatenated to form a binary sequence, which is then translated back into readable ASCII text.
5. The decrypted message is saved to `decrypted.txt`.

## Usage
### Prerequisites
Python 3.x

Make sure the Pillow (PIL Fork) library is installed by running:

`pip install Pillow` or `pip3 install Pillow`
### Define your Secret Key:
Open `key.py` and modify the `schematic` function. This function takes 8 boolean inputs (b0 to b7) and should return a single boolean output. This is your secret key.

```
def schematic(b0, b1, b2, b3, b4, b5, b6, b7):
    # Assign your Boolean function to bool_out as encryption key. Example:
    bool_out = b5 or (b6 and b7)
    return bool_out
```
**Important**: Ensure your schematic function is not trivial (i.e., it doesn't always return True or False regardless of input), otherwise, the key validation will fail.
### Run the main program
Set the wokring directory with all 3 files `features.py`, `key.py`, and `main.py`.

`cd <project_directory>`


Run `main.py`.

`python main.py` or `python3 main.py`

Follow the prompts.

## Contributing
Feel free to fork the repository, make improvements, and submit pull requests.

Got feedbacks? Send them to dung.nguyen@365.elmhurst.edu
