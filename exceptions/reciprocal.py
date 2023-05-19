def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n

if __name__ == "__main__":
    print(reciprocal(2))
    """
    Everything went fine
    It's time to say goodbye
    0.5
    """
    print(reciprocal(0))
    """
    Division failed
    It's time to say goodbye
    None
    """
