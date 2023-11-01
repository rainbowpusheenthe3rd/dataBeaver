import os
from metabeaver.Formatting.printControl import conditional_print as cprint

def heapify(arr, n, i):

    cprint('Got array, length and index: ')
    cprint(arr, n, i)
    largest = i  # Assume the current node (at index i) is the largest.
    left = 2 * i + 1  # Calculate the index of the left child.
    cprint('Left and Right indices: ')
    cprint(left)
    right = 2 * i + 2  # Calculate the index of the right child.
    cprint(right)

    # If the left child exists and is greater than the current largest, update 'largest'.
    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        # If the right child exists and is greater than the current largest, update 'largest'.
        largest = right

    if largest != i:
        # If the largest element is not the current node, swap them.
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Build a heap and then sort the heap
def heapSort(arr):
    n = len(arr)

    cprint("Building a Max Heap:")
    # Build a max heap by starting from the middle and going to the root.
    for i in range(n // 2 - 1, -1, -1):
        cprint(f"Heapifying at index {i}")
        heapify(arr, n, i)
        cprint(arr)

    cprint("\nSorting the Heap:")
    # Extract elements one by one from the heap.
    for i in range(n - 1, 0, -1):
        # Swap the largest element with the last element.
        arr[i], arr[0] = arr[0], arr[i]
        cprint(f"Swapping {arr[i]} with {arr[0]}")
        heapify(arr, i, 0)
        cprint(arr)

    return arr

# Establish a test case for heapSort and print the results if os env BEAVER_PRINTING is a string equal to "True"
os.environ["BEAVER_PRINTING"] = "True" # Update to inherit from your desired settings, e.g. test server

if os.environ["BEAVER_PRINTING"] == "True":
    print()














# Example usage:
#input_list = [13, 11, 10, 5, 6, 7]
input_list = [11, 13, 10, 5, 6, 17]
cprint("Original array:", input_list)
sorted_list = heapSort(input_list)
cprint("\nSorted array:", sorted_list)


input_list = [1, 2, 3, 4, 5, 6]
cprint("Original array:", input_list)
sorted_list = heapSort(input_list)
cprint("\nSorted array:", sorted_list)