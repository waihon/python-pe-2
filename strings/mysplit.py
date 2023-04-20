def mysplit(string):
    if len(string) == 0 or string.isspace():
        return []

    result = []
    substring = ""
    for char in string:
        if char.isspace():
            if len(substring) > 0:
                result.append(substring)
                substring = ""
        else:
            substring += char
    
    if len(substring) > 0:
        result.append(substring)
        substring = ""

    return result

if __name__ == "__main__":
    print(mysplit("To be or not to be, that is the question"))
    print(mysplit("To be or not to be,that is the question"))
    print(mysplit("   "))
    print(mysplit(" abc "))
    print(mysplit(""))
    """
    ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
    ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
    []
    ['abc']
    []
    """
