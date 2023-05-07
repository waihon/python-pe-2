class SampleClass:
    def __init__(self, val):
        self.val = val

if __name__ == "__main__":
    object_1 = SampleClass(0)
    object_2 = SampleClass(2)
    object_3 = object_1
    object_3.val += 1
    
    print(object_1 is object_2) # False
    print(object_2 is object_3) # False
    # object_1 and object_3 are actually the same objects
    print(object_3 is object_1) # True
    print(object_1.val, object_2.val, object_3.val) # 1 2 1
    
    string_1 = "Mary had a little "
    string_2 = "Mary had a little lamb"
    string_1 += "lamb"
    
    # string_1 and string_2 aren't the same objects despite having the same contents
    print(string_1 == string_2, string_1 is string_2) # True False
