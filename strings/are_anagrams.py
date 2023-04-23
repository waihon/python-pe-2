def are_anagrams(text1: str, text2: str) -> bool:
    # This function:
    # - assumes that two empty strings are not anagrams;
    # - treats upper- and lower-case letters as equal;
    # - treat spaces as non-existent
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()
    
    if text1 == "" and text2 == "":
        return False
    else:
        text1 = str(sorted(list(text1)))
        text2 = str(sorted(list(text2)))
        return text1 == text2

if __name__ == "__main__":
    assert are_anagrams("Listen", "Silent") == True
    assert are_anagrams("modern", "norman") == False
