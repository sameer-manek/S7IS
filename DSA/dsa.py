import Crypto
import hashlib
from Crypto.PublicKey import RSA
import base64
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))
# Creating Season Key
seasonCipher = AESCipher("IsitmatterwhoIam")

# Creating Private keys for users

# Source Private key
user1PrivateKey = RSA.generate(2048)
print ("Source private key")
print (user1PrivateKey.exportKey())

# Destination Private key
user2PrivateKey = RSA.generate(2048)
print ("Destination private key")
print (user2PrivateKey.exportKey())


# Creating Public keys for users

# Source Public key
user1PublicKey = user1PrivateKey.publickey()
print ("Source public key")
print (user1PublicKey.exportKey())

# Destination Public key
user2PublicKey = user2PrivateKey.publickey()
print ("Destination public key")
print (user2PublicKey.exportKey())


# Read data from file
with open("/Users/macbookproretina/Desktop/RSA 1024/ID.txt", "r", ) as id:
    id_data = id.readlines('<path-to-id.txt>', 'r')

# Convert array from two dimension to 1 dimension
personal_id = []
for i in range(len(id_data)):
    personal_id.append(id_data[i].splitlines())
for i in range(len(personal_id)):
    personal_id[i] = personal_id[i][0]
print(personal_id)

# Hash ID file elements
hash_object = hashlib.sha384(b"{}".format(personal_id))
hex_dig = hash_object.hexdigest()
print("Hash code of personal id's = {}".format(hex_dig))

# Encrypt Hash with Destination public key
hashEncryption = user2PublicKey.encrypt(hex_dig,None)
print ("---Encrypted Hash Code---")
print (hashEncryption) # Checked

# Concatenate Operation with Encryption
print ("---Concatenate operation and season key encryption sequence started---")
packageEncryption = []
for i in range(len(personal_id)):
    packageEncryption.append(seasonCipher.encrypt(personal_id[i]))
packageEncryption.append(seasonCipher.encrypt(hashEncryption[0])) # Checked

print ("-----Package-----")
print packageEncryption

# Season key encrypt sequence with destination public key
print ("---Season key Encryption sequence started----")
seasonKeyEncryption = user2PublicKey.encrypt("IsitmatterwhoIam",None)
print ("---Encrypted Season key---")
print (seasonKeyEncryption)

# Final Concatenate Operation
print ("---Final Concatenate operation sequence started---")
packageEncryption.append(seasonKeyEncryption)
print ("---Final Package---")
print packageEncryption

# -----------------------------Decryption Sequence--------------------------------------------

print("---Decryption Sequence Started---")
seasonKey = user2PrivateKey.decrypt(packageEncryption[-1])
print ("---Season key---")
print (seasonKey)
seasonEncryptedCipher = AESCipher(str(seasonKey))

decryptedPackage = []
# Decryption and unboxing package
for i in range(len(packageEncryption)-1):
    decryptedPackage.append(seasonEncryptedCipher.decrypt(packageEncryption[i]))
print ("---Decrypted Package---")
print (decryptedPackage)

# Decryption Hash Value
print ("---Package Hash Decryption Sequence---")
decryptedHash = user2PrivateKey.decrypt(decryptedPackage[-1])
print ("Decrypted Hash : {} ".format(decryptedHash))

# Re-Hash De ID file elements
print ("---Re-Hash Decrypted File Elements---")
decryptedPersonalElements = []
for i in range(len(decryptedPackage)-1):
    decryptedPersonalElements.append(decryptedPackage[i])
decrypted_hash_object = hashlib.sha384(b"{}".format(decryptedPersonalElements))
decrypted_hex_dig = hash_object.hexdigest()
print("Re-Hash code of personal id's = {}".format(decrypted_hex_dig))

# Check Hashes
print ("---Last stage Hash Check---")
if(decryptedHash == decrypted_hex_dig):
    print ("Signature Check Completed, Signature is original ")
else:
    print ("Signature Check Completed, Signature is not original")