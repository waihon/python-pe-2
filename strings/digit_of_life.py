def digit_of_life(birthdate: int) -> int:
    # Thr birthdate can be in the format
    # YYYYMMDD, or YYYYDDMM, or MMDDYYYY
    birthdate = str(birthdate)
    if not birthdate.isdigit():
        return None
    
    total = 0
    for digit in birthdate:
        digit = int(digit)
        total += digit
    
    while total > 9:
        digits = str(total)
        total = 0
        for digit in digits:
            digit = int(digit)
            total += digit
    
    return total

if __name__ == "__main__":
    assert digit_of_life(19991229) == 6
    assert digit_of_life(19992912) == 6
    assert digit_of_life(12291999) == 6
    assert digit_of_life(20000101) == 4
    assert digit_of_life(1012000) == 4
    birthdate = input("Enter your birthdate in the YYYYMMDD format: ")
    print(digit_of_life(int(birthdate)))
