class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
    def get_sum(self):
        return self.__sum

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.pop_count = 0        

    def get_counter(self):
        return self.pop_count

    def pop(self):
        val = Stack.pop(self)
        self.pop_count += 1
        return val

if __name__ == "__main__":
    # Single stack
    stack_object = Stack()
    
    stack_object.push(1)
    stack_object.push(2)
    stack_object.push(3)
    
    print(stack_object.pop()) # 3
    print(stack_object.pop()) # 2
    print(stack_object.pop()) # 1
    
    # Multiple stacks
    stack_object_1 = Stack()
    stack_object_2 = Stack()

    stack_object_1.push(3)
    stack_object_2.push(stack_object_1.pop())

    print(stack_object_2.pop()) # 3

    # Juggle the stacks
    little_stack = Stack()
    another_stack = Stack()
    funny_stack = Stack()

    little_stack.push(1)
    another_stack.push(little_stack.pop() + 1)
    funny_stack.push(another_stack.pop() - 2)

    print(funny_stack.pop()) # 0

    # Init and use AddingStack object
    stack_object = AddingStack()

    for i in range(5):
        stack_object.push(i)
    print(stack_object.get_sum()) # 10

    for i in range(5):
        print(stack_object.pop()) # 4 3 2 1 0

    # Init and use CountingStack object
    stk = CountingStack()
    for i in range(100):
        stk.push(i)
        stk.pop()
        continue
    print(stk.get_counter()) # 100
