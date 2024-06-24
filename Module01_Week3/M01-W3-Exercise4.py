class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def get_queue(self):
        return self.__queue

    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False

    def is_full(self):
        # Check if Queue is full compare with capacity
        if len(self.__queue) == self.__capacity:
            return True
        elif len(self.__queue) < self.__capacity:
            return False
        elif len(self.__queue) > self.__capacity:
            print('The Queue is overloaded')
            return True

    def dequeue(self):
        len_list = len(self.__queue)
        if len_list > 0:
            value = self.__queue[0]
            self.__queue.pop(0)
            print(value)
            return value
        if len_list == 0:
            print('Queue is empty, no value is dequeued')
            return -1

    def enqueue(self, value):
        len_list = len(self.__queue)
        if len_list < self.__capacity:
            self.__queue.append(value)
            return 1
        if len_list >= self.__capacity:
            print('Can not enqueue a new value due to the Queue was already full')
            return -1

    def front(self):
        len_list = len(self.__queue)
        if len_list > 0:
            value = self.__queue[0]
            print(value)
            return 1

        if len_list == 0:
            print('Queue is empty, no top value to show ')


if __name__ == '__main__':
    queue1 = MyQueue(7)
    queue1.enqueue(5)
    queue1.enqueue(4)
    queue1.enqueue(3)
    queue1.enqueue(7)
    queue1.enqueue(2)
    queue1.enqueue(1)
    print(queue1.get_queue())
    queue1.dequeue()
    print(queue1.get_queue())
    print(queue1.is_empty())
    print(queue1.is_full())
    queue1.dequeue()
    print(queue1.get_queue())
