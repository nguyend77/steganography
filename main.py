import features

def main_program():
	header = 'Python Steganography Tool'
	print(f'\n\n{header.center(40, "-")}')
	path = input('\nEnter image: ')
	image = features.Img(path)
	confirm = input('\nConfirm that key.py is ready (y/n): ')
	if confirm.lower() == 'y':
		while not features.check_key():
			print('Invalid key! Please try again.')
			input('Adjust key.py and press y to try again\n')
	print('\nChoose your desired action:')
	print('1. Encrypt hidden message')
	print('2. Decrypt hidden message')
	option = input()
	if option == '1':
		print('\nType message to encrypt in image:')
		text = input()
		print('\nEncrypting message into image...')
		image.encrypt(text)
		print('\nEncryption complete.')
		print('See encrypted.png file in working directory.\n')
	elif option == '2':
		print('\nDecrypting hidden message from image...')
		image.decrypt()
		print('\nDecryption complete.')
		print('See decrypted.txt file in working directory.\n')

# main
if __name__ == '__main__':
	main_program()

# seeking more security? add another layer of vigenere cipher.
