alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = input("Enter the key value")
key = int(key)
newMessage = ''
message = input("Enter the message you want to encrypt")

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    elif character in ALPHABET:
        position = ALPHABET.find(character)
        newPosition = (position + key) % 26
        newCharacter = ALPHABET[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character
print("Encrypted message: " + newMessage)
