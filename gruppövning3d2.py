import string

def encrypt(message, key):
    newmessage=""
    for i in range(len(message)):
        if message[i].isupper():
            old_ascii = ord(message[i])
            new_ascii = (old_ascii + key - 65) % 26 + 65
            newcharacter = chr(new_ascii)
            newmessage+=newcharacter
        elif message [i].islower():
            old_ascii = ord(message[i])
            new_ascii = (old_ascii + key - 97) % 26 + 97
            newcharacter = chr(new_ascii)
            newmessage+=newcharacter
        else:
            newmessage+=message[i]
    return newmessage
            
def decrypt(message, key):
    newmessage=""
    for i in range(len(message)):
        if message[i].isupper():
            old_ascii = ord(message[i])
            new_ascii = (old_ascii - key - 65) % 26 + 65
            newcharacter = chr(new_ascii)
            newmessage+=newcharacter
        elif message [i].islower():
            old_ascii = ord(message[i])
            new_ascii = (old_ascii - key - 97) % 26 + 97
            newcharacter = chr(new_ascii)
            newmessage+=newcharacter
        else:
            newmessage+=message[i]
    return newmessage

def break_crypt(message):
    for i in range(1,26,1): # key can be 1-25 --> k=26 gives the same result as the encrypted message
        newmessage=""
        key = i
        for i in range(len(message)):
            if message[i].isupper():
                old_ascii = ord(message[i])
                new_ascii = (old_ascii - key - 65) % 26 + 65
                newcharacter = chr(new_ascii)
                newmessage+=newcharacter
            elif message [i].islower():
                old_ascii = ord(message[i])
                new_ascii = (old_ascii - key - 97) % 26 + 97
                newcharacter = chr(new_ascii)
                newmessage+=newcharacter
            else:
                newmessage+=message[i]
        print(newmessage)

def get_key():
    # Only let user input ints
    while True:
        try:
            key=int(input("Input key (integer): "))
            return key
        except ValueError:
            print("The key must be an integer!")

def get_message():
    message=input("Write a message: ")
    return message

def action():
    while True:
        print("\nWhat would you like to do? ")
        choice = input("e: encrypt\nd: decrypt\nb: break (brute-force)\nq: quit\n>")

        if choice.lower() == 'q':
            break

        elif choice.lower() == 'd': # decrypt
            message=get_message()
            key=get_key()
            plaintext = decrypt(message, key)
            print("\nDecrypted message:", plaintext)

        elif choice.lower() == 'e': # encrypt
            message=get_message()
            key=get_key()
            encryptedtext = encrypt(message, key)
            print("Encrypted message:", encryptedtext)

        elif choice.lower() == 'b': # brute-force encrypted message
            message=get_message()
            break_crypt(message)

        else:
            print("\nThe only options currently available are:\n<e> to encrypt\n<d> to decrypt\n<b> to break (brute-force)\n<q> to quit")
            continue


# Exec action
action()