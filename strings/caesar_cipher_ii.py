def caesar_cipher(text: str, shift=1) -> str:
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
        else:
            code = ord(char) + shift
            if ord(char) >= ord('a'):
                if code > ord('z'):
                    code = code - ord('z') + ord('a') - 1
            else: 
                if code > ord('Z'):
                    code = code - ord('Z') + ord('A') - 1
            cipher += chr(code)
    return cipher

if __name__ == "__main__":
    assert caesar_cipher("abcxyzABCxyz 123", 2) == "cdezabCDEzab 123"
    assert caesar_cipher("The die is cast", 25) == "Sgd chd hr bzrs"
