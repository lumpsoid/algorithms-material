def empty_check(func):
    def wrapper(self, *args, **kwargs):
        if len(self.data) == 0:
            raise StackIsEmptyError("Stack is empty. Cannot perform the operation on an empty stack.")
        return func(self, *args, **kwargs)
    return wrapper


class StackIsEmptyError(Exception):
    pass


class Stack:
    def __init__(self):
        self.data = []
    

    def add(self, data):
        self.data.append(data)
    

    @empty_check
    def delete(self):
        return self.data.pop()
    

    def size(self):
        return len(self.data)
    

    @empty_check
    def peek(self):
        return self.data[-1]