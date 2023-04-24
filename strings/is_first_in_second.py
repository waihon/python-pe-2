def is_first_in_second(first: str, second: str) -> bool:
    # This function answers the following question:
    # Are the characters comprising the first string
    # hidden inside the second string?
    # For example, given the first string "dog":
    # if the second string is given as "vcxzxduybfdsobywuefgas",
    # the answer is yes;
    # if the second string is "vcxzxdcybfdstbywuefsas", the answer
    # is no (as there are neither the letters "d", "o", or "g",
    # in this order)
    first = first.lower()
    second = second.lower()
    index = 0
    for char in first:
        find_index = second.find(char, index) # -1 if not found
        if find_index < index:
            return False
        else:
            index = find_index
    return True

if __name__ == "__main__":
    assert is_first_in_second("donor", "Nabucodonosor") == True
    assert is_first_in_second("donut", "Nabucodonosor") == False
