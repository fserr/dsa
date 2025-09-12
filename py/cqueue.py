'''
Circular queue:
    > last items point to the first => size isn't reduced by popping elemements
'''

class CQueue():
    
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, item):
        if ((self.tail + 1) % self.size == self.head):
            print("The cqueue is full.")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = item

    def dequeue(self):
        if (self.head == -1):
            print("The queue is empty.")
        elif (self.head == self.tail):
            self.head = -1
            self.tail = -1
        else:
            tmp = self.head
            self.head = (self.head + 1) % self.size
            return tmp

    def print_queue(self):
        if (self.head == -1):
            print("The queue is empty.")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.size):
                print(self.queue[i], end=" ")
            for i in range (0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
