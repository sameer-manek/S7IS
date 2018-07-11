import os

# decrypt monoalphabetic cipher

def decrypt(msg, key):
	dec_msg = ''
	gap = ord('a') - ord('A')
	
	for c in msg:
		#conversion from lower to upper
		if ord(c) > ord('a')-1:
			c = chr(ord(c)-gap)
		if c == ' ':
			index = ord(' ')
		else:
			index = [pos for pos, char in enumerate(key) if char == c]
			index = int(index[0])
		#print(index, chr(index+97))
		dec_msg += chr(index+97)
	print(dec_msg)

if __name__ == '__main__':
	msg = input("Enter the message: ")
	key = input("Enter 26 character key: ")
	
	decrypt(msg, key)
