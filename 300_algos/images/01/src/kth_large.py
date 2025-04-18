def kth_largest(arr, k):
    return sorted(arr, reverse=True)[k-1]

#e.g
arr = [3, 2, 1, 5, 4]
k =2
print(kth_largest(arr, k))

arr2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 2
print(kth_largest(arr2, k2))

arr3 = [3, 2, 1, 5, 6, 4]
k3 = 2
print(kth_largest(arr3, k3))

arr4 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k4 = 1
print(kth_largest(arr4, k4))
print("3rd largest in arr4 is: ", kth_largest(arr4, 3)) #what's the time complexity of this?