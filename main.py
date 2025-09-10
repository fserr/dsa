from stack import *

def main():
    my_stack = stack_create()
    stack_push(my_stack, 1)
    stack_push(my_stack, 2)
    stack_push(my_stack, 3)
    stack_pop(my_stack)
    
    print(my_stack)

if __name__ == "__main__":
	main()
