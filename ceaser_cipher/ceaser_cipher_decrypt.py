import os

# decrypt ceaser cipher

def decrypt(msg, key):
	dec_msg = ''
	gap = ord('a') - ord('A')

	for c in msg:
		if ord(c)<ord('a'):
			c = chr(ord(c)+gap)
		i = chr(ord(c)-key)
		
		if ord(i) < ord('a'):
			# finding delta
			delta = ord('a') - ord(i)
			i = chr(ord('z') - delta + 1)
		if ord(c) == ord(' '):
			i = ord(' ')
		dec_msg += i
	
	return dec_msg

if __name__ == "__main__":
	msg = input("Enter the message: ")
	key = int(input("please enter the key (should be numeric): "))
	
	print(decrypt(msg, key))
