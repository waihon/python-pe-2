def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n

if __name__ == "__main__:
    print(reciprocal(2)) # Everything went fine\n0.5
    print(reciprocal(0)) # Division failed\nNone
