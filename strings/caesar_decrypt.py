def caesar_decrpyt(text: str) -> str:
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)
    return text

if __name__ == "__main__":
    cipher = input('Enter your cryptogram: ')
    text = caesar_decrpyt(cipher)
    print(text)
