# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    for i in range(0, len(merged_arr)):
        if len(arrA) < 1:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif len(arrB) < 1:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif arrA[0] <= arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        # I don't understand why "or" does not work in the following
        # if len(arrA) < 1 or arrA[0] > arrB[0]:
        #     merged_arr[i] = arrB[0]
        #     arrB.pop(0)
        # elif len(arrB) < 1 or arrA[0] <= arrB[0]:
        #     merged_arr[i] = arrA[0]
        #     arrA.pop(0)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if(arr == [] or arr[-1] == arr[0]):
        return arr

    return merge(merge_sort(arr[::2]), merge_sort(arr[1::2]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
