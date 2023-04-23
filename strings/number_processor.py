def sum_of_numbers(line: str) -> str:
    strings = line.split()
    total = 0
    try:
        for substr in strings:
            total += float(substr)
        return f"The total is: {total}"
    except:
        print(substr, "is not a number.")

if __name__ == "__main__":
    line = input("Enter a line of numbers - separate them with spaces: ")
    print(sum_of_numbers(line))
