def caesar_cipher(text: str) -> str:
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1 # A -> B, B -> C, ..., Z -> A
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    return cipher

if __name__ == "__main__":
    text = input("Enter your message: ")
    cipher = caesar_cipher(text)
    print(cipher)
