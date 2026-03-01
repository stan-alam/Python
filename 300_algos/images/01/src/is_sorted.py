def is_sorted(arr):
    ascending, descending = True, True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]: #check for ascending order
            ascending = False
        if arr[i] > arr[ i - 1]: #check for descending order
            descending = False
    return ascending or descending
