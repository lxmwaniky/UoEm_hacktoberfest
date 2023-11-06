def encrypt(payload, shift):
    result = ""

    #traverse text
    for i in range(len(text)):
        char = text[i]

        #Encrypt Uppercase 
        if(char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)

        #encrypt lowercase
        else:
            result += chr((ord(char) + shift - 97 ) % 26 + 97)
    return result

text = input("Input Your Payload")
print("Type for Payload" type(text))
shift = input("Caeser Says? ")
