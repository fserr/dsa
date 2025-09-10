""" STACK """

def stack_create():
    """ Return 'stack' as an empty array """
    stack = []
    return stack

def stack_is_empty(stack):
    """ Check if 'stack' is empty """
    return len(stack) == 0

def stack_push(stack, item):
    """ Add 'item' to the end of 'stack' """
    stack.append(item)

def stack_pop(stack):
    """ Remove and return the last element of the stack """
    if stack_is_empty(stack):
        print("stack is empty")
        return
    return stack.pop()
