'''
Priority queue:
    > Each element has a priority value; the one with highest priority get served (popped) first
    > Elements with same priority value get prioritezed by their order in the collection
    > Heap is the most efficient implementation
'''

def Heapify(arr, n, i):
    '''
    n = size of the heap: only elements from 0 to n-1 of arr will be considered
    i = index or the root node
    '''
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i] 


def insert_node(arr, num):
    return

def delete_node(arr, num):
    return


