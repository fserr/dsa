'''
Priority queue:
    > Each element has a priority value; the one with highest priority get served (popped) first
    > Elements with same priority value get prioritezed by their order in the collection
    > Heap is the most efficient implementation
'''

def heapify(arr, n, i):
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
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert_node(arr, num):
    size = len(arr)
    if size == 0:
        arr.append(num)
    else:
        arr.append(num)
        for i in range((size // 2) - 1, -1, -1):
            heapify(arr, size, i)


def delete_node(arr, num):
    size = len(arr)
    i = 0
    for i in range(0, size):
        if arr[i] == num:
            break

    arr[i], arr[size - 1] = arr[size - 1], arr[i]
    arr.pop()
    for i in range((size // 2) - 1, -1, -1):
        heapify(arr, len(arr), i)
