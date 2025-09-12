'''
Deque:
    > insert / delete can be done both from the front or rear of the queue
    > can be input or output restricted
        > input restricted: insert on single end, delete on both ends
        > output restricted: insert on both end, delete on one end
'''

class Deque:

    def __init__(self):
        self.items = []

    def is_empty():
        return self.items == []

    def add_rear(self, item):
        self.items.append(item)

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print(self):
        print(self.items)
