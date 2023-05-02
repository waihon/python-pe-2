class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

if __name__ == "__main__":
    stack_object = Stack()
    
    stack_object.push(1)
    stack_object.push(2)
    stack_object.push(3)
    
    print(stack_object.pop()) # 3
    print(stack_object.pop()) # 2
    print(stack_object.pop()) # 1
    
    stack_object_1 = Stack()
    stack_object_2 = Stack()

    stack_object_1.push(3)
    stack_object_2.push(stack_object_1.pop())

    print(stack_object_2.pop()) # 3
