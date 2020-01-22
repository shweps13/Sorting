def quicksort_out_of_place(arr):
    # 1. Pick a pivot and move it until everything
    # on the left is smaller & everything on the right is greater
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    smaller = []
    larger = []
    for i in range(len(arr) - 1):
        element = arr[i]
        if element < pivot:
            smaller.append(element)
        else:
            larger.append(element)
    return quicksort_out_of_place(smaller) + [pivot] + quicksort_out_of_place(larger)