def is_palindrome(text: str) -> bool:
    # This function:
    # - assumes that an empty string isn't a palindrome;
    # - treats upper- and lower-case letters as equal;
    # - spaces are not taken into account during the check - 
    #   treat them as non-existent
    text = text.replace(" ", "").lower()
    if text == "":
        return False
    else:
        return text == text[::-1]

if __name__ == "__main__":
    assert is_palindrome("Ten animals I slam in a net") == True
    assert is_palindrome("Eleven animals I slam in a net") == False
