def kth_largest(arr, k):
    return sorted(arr, reverse=True)[k-1]

#e.g
arr = [3, 2, 1, 5, 4]
k =2
print(kth_largest(arr, k))