def read_int(prompt: str, min: int, max: int) -> int:
    """
    The function:
    - accepts three arguments: a prompt, a low acceptable limit,
      and a high acceptable limit;
    - if the user enters a string that is not an integer value,
      the function should emit the message 'Error: wrong input',
      and ask the user to input the value again;
    - if the user enters a number which falls outside the specified
      range, the function should emit the message 'Error: the value
      is not within permitted range (min..max)' and ask the user to 
      input the value again;
    - if the input value is valid, return it as a result.
    """
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if value < min or value > max:
                print(f"Error: the value is not within permitted range ({min}..{max})")
                continue
            return value
        except ValueError:
            print("Error: wrong input")
            continue

if __name__ == "__main__":    
    v = read_int("Enter an integer from -10 to 10: ", -10, 10)
    print("The number is: ", v)
