import os

# hill cipher

'''
    # matrix multiplication
'''

def convert(text):
    # returns text in matrix form

    x = list()
    A = ord('A')

    for l in text:
        if l == " ":
            # skipping white spaces
            pass
        # returns a numeric constant for the alphabet
        x.append(ord(l)-A+1)
    return x

def map_to_text(rm):
    # map matrix to alphas
    s = ""
    for l in rm:
        s += chr(ord('A') + l-1)
    return s

def encrypt(key, x):
    # perform matrix multiplication
    fin = list()
    for row in key:
        sum = 0
        for i in range(len(row)):
            sum += int(row[i])*x[i]
        fin.append(sum%26)
    print(key, x)
    return fin

if __name__ == "__main__":
    x = input("please enter the message").upper()
    key = list()
    for i in range(len(x)):
        s = "Enter comma seperated digits for key matrix row {}".format(i)
        key.append(input(s).split(' '))
    mox = convert(x)
    print(map_to_text(encrypt(key, mox)))
        
