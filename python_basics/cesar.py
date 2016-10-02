#cesar encryption
#
from random import randint


def encrypt(poop, key):
	
	sNuevo = ''
	key = int(key)
	while key > 25:
		key -= 25

	for letter in poop:
		sNuevo += chr(ord(letter)+int(key))
	return sNuevo


def main():
	#username = raw_input('Type your username: ')
	password = raw_input('Type your password: ')
	key = raw_input('type key: ')
	password = encrypt(password, key)
	print 'password encrypted'
	print password
main()