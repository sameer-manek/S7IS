import os 

# monoalphabetic cipher encryption

def encrypt(msg, key):
	enc_msg = ''
	gap = ord('a') - ord('A')
	
	for c in msg:
		# conversion of upper to lower
		if ord(c) < ord('a'):
			c = chr(ord(c)+gap)
		i = key[ord(c)-97]
		if ord(c) == ord(' '):
			i = ' '
		enc_msg += i
	return enc_msg

if __name__ == "__main__":
	msg = input("Enter the message: ")
	key = input("Enter 26 character key: ")
	
	print("encrypted message: {}".format(encrypt(msg, key)))
