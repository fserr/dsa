from stack import *
from queue import *
from cqueue import *
from pqueue import *

def main():
    # PQUEUE
    arr = []

    insert_node(arr, 3)
    insert_node(arr, 4)
    insert_node(arr, 9)
    insert_node(arr, 5)
    insert_node(arr, 2)
    
    print("Max-Heap array: " + str(arr))
    
    delete_node(arr, 4)
    print("After deleting an element: " + str(arr))

#     # CQUEUE
#     myqueue = CQueue(3)
#     myqueue.enqueue(1)
#     myqueue.enqueue(2)
#     myqueue.enqueue(3)
#     myqueue.enqueue(4)
# 
#     myqueue.print_queue()
# 
#     myqueue.dequeue()
#     myqueue.dequeue()
#     myqueue.enqueue(4)
#     myqueue.enqueue(5)
#     myqueue.enqueue(6)
# 
#     myqueue.print_queue()
# 

    # --- QUEUE ---
   # my_queue = Queue(3)
   # 
   # my_queue.enqueue(1)
   # my_queue.enqueue(2)
   # my_queue.enqueue(3)
   # my_queue.enqueue(4)
   # my_queue.print_queue()
   # my_queue.print_current_size()
   # 
   # my_queue.dequeue()
   # my_queue.dequeue()

   # my_queue.print_queue()   
   # my_queue.print_current_size()

   # my_queue.enqueue(1)
   # my_queue.enqueue(1)

   # my_queue.print_current_size()
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
