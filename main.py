import features

def main_program():
	header = 'Python Steganography Tool'
	print(f'\n{header.center(40, "*")}\n')
	path = input('Enter image: ')
	image = features.Img(path)
	confirm = input('Confirm that key.py is ready (y/n): ')
	if confirm.lower() == 'y':
		while not features.check_key():
			print('Invalid key! Please try again.')
			input('Adjust key.py and press y to try again\n')
	print('Choose your desired action:')
	print('1. Encrypt hidden message')
	print('2. Decrypt hidden message')
	option = input()
	if option == '1':
		print('Type message to encrypt in image:')
		text = input()
		print('Encrypting message into image...')
		image.encrypt(text)
		print('Encryption complete. See encrypted.png file in working directory.')
	elif option == '2':
		print('Decrypting hidden message from image...')
		image.decrypt()
		print('Decryption complete. See decrypted.txt file in working directory.')

# main
if __name__ == '__main__':
	main_program()

# seeking more security? add another layer of vigenere cipher.