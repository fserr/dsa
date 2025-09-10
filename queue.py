''' ============================= QUEUE ===================================== 


'''

class Queue():
    
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1
    
    def enqueue(self, item):
        if (self.tail == self.size - 1):
            print("The queue is full.")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail += 1
            self.queue[self.tail] = item

    def dequeue(self):
        if (self.head == -1):
            print("The queue is empty.")
        elif (self.tail == self.head):
            tmp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return tmp
        else:
            tmp = self.queue[self.head]
            self.head += 1
            return tmp

    def print_queue(self):
        if (self.head == -1):
            print("The queue is empty")
        else:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

