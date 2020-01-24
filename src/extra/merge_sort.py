### STEP 1: Split our list into sub-lists until they are all length 1 or less
def merge_sort(arr):
    # Check if it's length 1 or less. If so, return the list
    if len(arr) <= 1:
        return arr
    # Divide in half
    left = arr[ : len(arr) // 2]
    right = arr[len(arr) // 2 : ]
    # Sort the left
    left = merge_sort(left)
    # Sort the right
    right = merge_sort(right)
    # Merge together
    return merge(left, right)
# STEP 2: Merge two sorted sublists and return the sorted merged list
def merge(arr_a, arr_b):
    total_elements = len(arr_a) + len(arr_b)
    merged_arr = [None] * total_elements
    # Declare indices for each sublist
    a = 0
    b = 0
    for i in range(total_elements):
        # Check if either list is empty, if so append the other
        if a >= len(arr_a):
            merged_arr[i] = arr_b[b]
            b += 1
        elif b >= len(arr_b):
            merged_arr[i] = arr_a[a]
            a += 1
        # Otherwise, compare and append the smallest of the two
        elif arr_a[a] < arr_b[b]:
            merged_arr[i] = arr_a[a]
            a += 1
        else:
            merged_arr[i] = arr_b[b]
            b += 1
    return merged_arr