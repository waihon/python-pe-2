class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        # put() should append elements to the beginning of the list
        self.__queue.insert(0, elem)

    def get(self):
        # get() should remove the elements from the end of the list
        if len(self.__queue) == 0:
            raise QueueError
        elem = self.__queue[-1]
        del self.__queue[-1]
        return elem

    def size(self):
        return len(self.__queue)

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self) -> bool:
        return Queue.size(self) == 0

if __name__ == "__main__":
    que = Queue()
    que.put(1)
    que.put("dog")
    que.put(False)
    try:
        for i in range(4):
            print(que.get())
    except:
        print("Queue error")
    """
    1
    dog
    False
    Queue error    
    """
    
    que = SuperQueue()
    que.put(1)
    que.put("dog")
    que.put(False)
    for i in range(4):
        if not que.isempty():
            print(que.get())
        else:
            print("Queue empty")
    """
    1
    dog
    False
    Queue empty
    """
