def caesar_cipher(text: str, shift=1) -> str:
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
        else:
            code = ord(char) + shift
            if ord(char) >= ord('a'):
                if code > ord('z'):
                    code -= ord('z') + ord('a') - 1
            else: 
                if code > ord('Z'):
                    code -= ord('Z') + ord('A') - 1
            cipher += chr(code)
    return cipher

if __name__ == "__main__":
    print(caesar_cipher("abcxyzABCxyz 123", 2))
    print(caesar_cipher("The die is cast", 25))
