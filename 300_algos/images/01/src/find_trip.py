def find_triplets_with_zero_sum(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left, right = i + 1, len(arr) - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left -1 ]:
                    left +=1 
                    right -= 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
            elif s < 0: 
                left += 1
            else: 
                right -= 1

            return triplets
        