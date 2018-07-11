import os

# implementing encryption

def encrypt(msg, key):
	enc_msg = ''
	gap = ord('a') - ord('A')
	for c in msg:
		#handling non capital letters
		if ord(c)<ord('a'):
			i = ord(c) + gap + key
		else:	
			i = ord(c) + key
	
		if i > ord('z'):
			print("{}\n".format(c,i))
			delta = i - ord('z')
			i = ord('a')+delta-1
		if ord(c) == ord(' '):
			i = ord(' ')
		enc_msg += chr(i)
		
	return enc_msg

if __name__ == '__main__':
	msg = input('Enter the message: ')
	key = int(input('Enter the key (must be numeric)'))
	
	print('message is : {}'.format(encrypt(msg, key)))
