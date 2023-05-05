class MyClass:
    pass

def inc_ints_i(obj):
    """
    This function gets an object of any class, scans its
    content in order to find all integer attributes with
    names starting with i, and increments them by one.
    """
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

if __name__ == "__main__":
    obj = MyClass()
    obj.a = 1
    obj.b = 2
    obj.i = 3
    obj.ireal = 3.5
    obj.integer = 4
    obj.z = 5
    
    
    print(obj.__dict__)
    # {'a': 1, 'b': 2, 'i': 3, 'ireal': 3.5, 'integer': 4, 'z': 5}
    inc_ints_i(obj)
    print(obj.__dict__)
    # {'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'integer': 5, 'z': 5}
