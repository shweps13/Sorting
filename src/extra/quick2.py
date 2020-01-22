def quicksort(arr):
    return quicksortHelper(arr, 0, len(arr) - 1)
    
def quicksortHelper(arr, low, high):
    pivotIndex = high
    if low >= high:
        return

    for compareIndex in range(low, high):
        value = arr[compareIndex]
        pivot = arr[pivotIndex]
        if value > pivot:
            arr[compareIndex], arr[pivotIndex] = arr[pivotIndex], arr[compareIndex]
            pivotIndex, compareIndex = compareIndex, pivotIndex
            newPivotIndex = compareIndex - 1
            arr[pivotIndex], arr[newPivotIndex] = arr[newPivotIndex], arr[pivotIndex]
            pivotIndex = newPivotIndex

    quicksortHelper(arr, 0, pivotIndex - 1)
    quicksortHelper(arr, pivotIndex, high)
    return arr