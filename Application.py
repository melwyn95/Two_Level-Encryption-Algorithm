import Encryption
import DivideInBlocks
import KeyGeneration
import Encryption
import Decryption

print "This is a two-level encrytion algorithm."
UserInput = raw_input("Enter Text To be Encrypted: ")

print "User Input is divided in blocks of 9 charactes."
blocks = DivideInBlocks.divide_in_blocks(UserInput)

print "Public and Private keys of Alice and Bob are randomly chosen.\nThe keys chosen are minimum 9 digit prime numbers."
p, q, a, b = KeyGeneration.generate_public_and_private_keys()

print "Keys are exchanged between Alice and Bob using Diffie-Hellman Algorithm."
key = KeyGeneration.diffie_hellman(p, q, a, b)

decrypted_blocks = []
encryped_blocks = []

print "A common symmetric key is calculated by echanging the public and private keys."
for block in blocks:
    pt = block
    print "Plain Text Block at Alice's side: " + str(pt)
    ct = Encryption.encrypt(pt, key)
    print "The plain text block is Encryted using two-level algoirithm......"
    print "Cipher Text at Alice's side:"
    print ct

    print "This Cipher Text is sent to Bob:"
    print "Cipher Text at Bob's side:"
    print ct
    encryped_blocks.append(ct)

    print "The Cipher Text is Decrypted using the reverse process used during encryption......"
    print "Plain Text Decrypted at Bob's side: "
    pt = Decryption.decrypt(ct, key)
    decrypted_blocks.append(pt)
    print pt

print "#############################################"
print "\n\n"
print "User Input(Alice)[Text encrpted]: "
print UserInput

print "\n\n"
print "Encrypted Text : "
print "".join(encryped_blocks)
print "\n\n"

print "Text Decypted at Bob's side: "
print "".join(decrypted_blocks)









