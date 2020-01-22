# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, pivot, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    merged_arr = arrA + pivot + arrB
    # print(merged_arr)
    return merged_arr

# merge([1,2,3], [5], [4,5,6])

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    smaller = []
    larger = []
    for i in range(len(arr) - 1):
        el = arr[i]
        if el < pivot:
            smaller.append(el)
        else:
            larger.append(el)
    return merge(merge_sort(smaller), [pivot], merge_sort(larger))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
