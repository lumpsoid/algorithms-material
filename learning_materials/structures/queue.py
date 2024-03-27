def check_queue_empty(func):
    def wrapper(self, *args, **kwargs):
        if len(self.data) == 0:
            raise EmptyQueueError('Queue is empty. Cannot perform the operation on the empty queue')
        return func(self, *args, **kwargs)
    return wrapper


class EmptyQueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.data = []
    

    def add(self, data):
        self.data.append(data)
    
    
    @check_queue_empty
    def delete(self):
        return self.data.pop(0)
    

    @check_queue_empty
    def peek(self):
        return self.data[0]
    

    def size(self):
        return len(self.data)
