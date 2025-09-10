from stack import *
from queue import *

def main():
    # --- QUEUE ---
    my_queue = Queue(3)
    
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)

    my_queue.print_queue()

    my_queue.dequeue()
    my_queue.dequeue()

    my_queue.print_queue()
    
    # --- STACK ---
    # my_stack = stack_create()
    # stack_push(my_stack, 1)
    # stack_push(my_stack, 2)
    # stack_push(my_stack, 3)
    # stack_pop(my_stack)
    # print("test1")
    # print("test2")
    # print(my_stack)

if __name__ == "__main__":
	main()
