from operator import indexOf
import string

# CEASAR CIPHER ENCRPTION AND DECRYPTION

# Create and store alphabet in a list
def alphabet():
    alphabet = string.ascii_uppercase
    alphabet_list = list(alphabet)
    return alphabet_list
        
# Word to cipher
def input_word():
    while(True):
        try:
            plaintext = input("Enter the word: ")
            if(plaintext.isalpha()):
                return plaintext
        except Exception as e:
            print(e)
            continue
        
# Switching key
def input_key():
    while(True):
        try:
            key = int(input("Enter Shifting Key: "))
            return key
        except Exception as e:
            continue

# Encrypt plaintext
def encrypt(plaintext, alphabets, key, num_plaintext, num_cipher):
    # A list to store the numeric ciphertext
    num_ciphertext = []

    for letter in plaintext:
        num_plaintext.append(alphabets.index(letter))
        num_ciphertext.append(alphabets.index(letter)+key)
    
    # A loop to resolve indexes out of the range of the alphabets
    for num in num_ciphertext:
        if(num > 25):
            num = num%25 - 1
            num_cipher.append(num)
        else:
            num_cipher.append(num)
    
    print(f"\nNumeric plaintext is {num_plaintext}")
    print(f"Numeric ciphertext is {num_cipher}")
    print("Encrypted message is:", end=" ")

    for num in num_cipher:
       print(alphabets[num], end="")
    
# Decrypt ciphertext
def decrypt(word, alphabets, key, num_plaintext, num_cipher):
    # A list to store the numeric plaintext
    num_plain_text = []

    for letter in word:
        num_cipher.append(alphabets.index(letter))
        num_plain_text.append(alphabets.index(letter)-key)
    
    # A loop to resolve indexes out of the range of the alphabets
    for num in num_plain_text:
        if(num < 0):
            num = num + 26
            num_plaintext.append(num)
        else:
            num_plaintext.append(num)
    
    print(f"\nNumeric ciphertext is {num_cipher}")
    print(f"Numeric plaintext is {num_plaintext}")
    print("Decrypted message is:", end=" ")

    for num in num_plaintext:
       print(alphabets[num], end="")


# Program runs from here
print("CAESAR CIPHER ENCRYPTION AND DECRYPTION")
print("=======================================")
print("Using the formular Ciphertext = plaintext + shifting key")
word = input_word()
word = list(word.upper())
key = input_key()
alphabets = alphabet()
num_cipher = []
num_plaintext = []


try:
    selection = int(input("\nSelect 1 to encrypt, 2 to decrypt the message: "))
    if(selection == 1):
        encrypt(word, alphabets, key, num_plaintext, num_cipher)
    elif(selection == 2):
        decrypt(word, alphabets, key, num_plaintext, num_cipher)
except Exception as e:
    print("Wrong input")