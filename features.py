from PIL import Image
from itertools import product
from key import schematic

class Img:
    def __init__(self, path):
        # open the image, 'with' handels the closing to avoid memory leaks
        with Image.open(path) as img:
            # convert the image to RGB mode
            self.rgb_image = img.convert('RGB')
        # get the dimensions of the image
        self.width, self.height = self.rgb_image.size
    # extract a list of 8 bits rgb values
    def extract(self):
        byte_list = []
        for y in range(self.height):
            for x in range(self.width):
                for color in range(3):
                    pixel_byte = self.rgb_image.getpixel((x,y))[color]
                    byte_list.append(f'{pixel_byte:08b}')
        return byte_list
    # decrypt hidden message in image using key and translate to text
    def decrypt(self):
        message = ascii(apply_schematic(bool_convert(self.extract())))
        # open new text file to write down decrypted message
        with open("decrypted.txt", "w") as f:
              f.write(message)
    # find a rgb value for a pixel that fits the message encryption
    def find_rgb_val(self, x, y, color, bit):
        bool = True if bit == '1' else False
        channel_val = self.rgb_image.getpixel((x,y))[color]
        pixel_dec = channel_val % 256
        pixel_bin = f'{pixel_dec:08b}'
        bit_list = [False, False, False, False, False, False, False, False]
        for i in range(8):
            bit_list[i] = True if pixel_bin[i] == '1' else False
        while schematic(bit_list[0], bit_list[1], bit_list[2], bit_list[3], bit_list[4], bit_list[5], bit_list[6], bit_list[7]) != bool:
            channel_val += 1
            pixel_dec = channel_val % 256
            pixel_bin = f'{pixel_dec:08b}'
            for i in range(8):
                bit_list[i] = True if pixel_bin[i] == '1' else False
        return pixel_dec
    # create a copy of original image and modify pixels to encrypt message
    def encrypt(self, message):
        new_img = self.rgb_image.copy()
        new_pixel = new_img.load()
        hidden = bits(message)
        x = 0
        y = 0
        for i in range(0, len(hidden), 3):
            red = self.find_rgb_val(x, y, 0, hidden[i])
            if i + 1 < len(hidden):
                green = self.find_rgb_val(x, y, 1, hidden[i+1])
            else:
                green = self.rgb_image.getpixel((x,y))[1]
            if i + 2 < len(hidden):
                blue = self.find_rgb_val(x, y, 2, hidden[i+2])
            else:
                blue = self.rgb_image.getpixel((x,y))[2]
            new_pixel[x, y] = (red, green, blue)
            x += 1
            if x == self.width:
                x = 0
                y += 1
        new_img.save('encrypted.png')

# convert 0s and 1s to boolean
def bool_convert(byte_list):
	# initialize a list of tuple of 8 bools
	bool_list = []
	# loop through each set of 8 bits in the extracted list
	for byte in byte_list:
		b0 = True if byte[0] == '1' else False
		b1 = True if byte[1] == '1' else False
		b2 = True if byte[2] == '1' else False
		b3 = True if byte[3] == '1' else False
		b4 = True if byte[4] == '1' else False
		b5 = True if byte[5] == '1' else False
		b6 = True if byte[6] == '1' else False
		b7 = True if byte[7] == '1' else False
		# append a tuple of 8 bools to the list
		bool_list.append((b0, b1, b2, b3, b4, b5, b6, b7))
	return bool_list

# apply provided logical circuit
def apply_schematic(bool_list):
	# initialize a string of 0s and 1s
	bin_str = ''
	# loop through each tuple of 8 bools in the converted list
	for bool in bool_list:
		bin_str += '1' if schematic(*bool) else '0'
	return bin_str

# translate binary sequence to text
def ascii(bin_str):
	chr_list = []
	for i in range(0, len(bin_str), 8):
		byte = bin_str[i:i+8]
		decimal = int(byte, 2) # base 2 to base 10
		char = chr(decimal)
		chr_list.append(char)
	return ''.join(chr_list)

# translate text to binary sequence
def bits(text):
	byte_list = []
	for char in text:
		byte = bin(ord(char))[2:].zfill(8) # 8 digits
		byte_list.append(byte)
	return ''.join(byte_list)

# check if provided key is valid
def check_key():
    null = schematic(False, False, False, False, False, False, False, False)
    for combination in product([False, True], repeat=8):
        output = schematic(*combination)
        if output != null:
            return True
    return False