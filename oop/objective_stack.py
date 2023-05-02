class Stack:
    def __init__(self):
        self.__stack_list = []

if __name__ == "__main__":
    stack_object = Stack()
    # AttributeError: 'Stack' object has no attribute '__stack_list'
    print(len(stack_object.__stack_list))
