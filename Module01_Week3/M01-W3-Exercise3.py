class Stack:
    # Initiate with the capacity of element
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    # Build the Get function - describe the object
    def get_stack(self):
        return self.__stack

    # Check if the Stack is empty
    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    # Check if Stack is full
    def is_full(self):
        if len(self.__stack) == self.__capacity:
            return True
        elif len(self.__stack) < self.__capacity:
            return False
        elif len(self.__stack) > self.__capacity:
            print('Stack is overflow')
            return True

    # Remove top element in Stack
    def pop(self):
        len_list = len(self.__stack)
        # Check if the element number > 0, else return -1
        if len_list > 0:
            value = self.__stack[len_list-1]
            self.__stack.pop()
            print(value)
            return value
        if len_list == 0:
            print('Stack is empty')
            return -1

    # Add new element to Stack
    def push(self, value):
        len_list = len(self.__stack)
        # Check current capacity
        if len_list < self.__capacity:
            self.__stack.append(value)
            return True
        if len_list >= self.__capacity:
            print('Stack overflow - Can not push a new value into the Stack')
            return False

    # Get the top element of the Stack
    def top(self):
        len_list = len(self.__stack)
        if len_list > 0:
            value = self.__stack[len_list-1]
            print(value)
            return 1

        if len_list == 0:
            print('Stack is empty, no top value to show ')


if __name__ == '__main__':
    stack1 = Stack(capacity=7)
    stack1.push(5)
    stack1.push(4)
    stack1.push(3)
    stack1.push(7)
    stack1.push(2)
    stack1.push(12)

    print(stack1.get_stack())
    print(stack1.is_full())

    stack1.pop()
    print(stack1.get_stack())
    print(stack1.is_empty())
    print(stack1.is_full())
    stack1.pop()
    print(stack1.get_stack())
