class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val):
        self.__second = val

if __name__ == "__main__":
    example_object_1 = ExampleClass()
    example_object_2 = ExampleClass(2)

    example_object_2.set_second(3)

    example_object_3 = ExampleClass(4)
    example_object_3.__third = 5

    print(example_object_1.__dict__) # {'_ExampleClass__first': 1}
    print(example_object_2.__dict__) # {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
    print(example_object_3.__dict__) # {'_ExampleClass__first': 4, '__third': 5}
