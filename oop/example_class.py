class ExampleClass:
    __counter = 0
    varia = 1

    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.varia = val
        ExampleClass.__counter += 1
        if val % 2 != 0:
            self.a = val
        else:
            self.b = val

    def set_second(self, val):
        self.__second = val

if __name__ == "__main__":
    print(ExampleClass.__dict__) # {..., '_ExampleClass__counter': 0, 'varia': 1, ...``}
    example_object_1 = ExampleClass()

    example_object_2 = ExampleClass(2)
    example_object_2.set_second(3)
    print(ExampleClass.__dict__) # {..., '_ExampleClass__counter': 2, 'varia': 2, ...``}

    example_object_3 = ExampleClass(4)
    example_object_3.__third = 5

    print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
    # {'_ExampleClass__first': 1} 3
    print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
    # {'_ExampleClass__first': 2, '_ExampleClass__second': 3} 3
    print(example_object_3.__dict__, example_object_3._ExampleClass__counter)
    # {'_ExampleClass__first': 4, '__third': 5} 3

    example_object = ExampleClass(1)
    if hasattr(example_object, 'a'):
        print('a:', example_object.a) # a: 1
    if hasattr(example_object, 'b'):
        print('b:', example_object.b)
