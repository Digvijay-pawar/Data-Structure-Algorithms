def floor_number(arr, target):
    start, end = 0, len(arr)
    while start <= end:
        mid = (start + end) // 2
        if (arr[mid] == target):
            return arr[mid]
        elif (arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return arr[end]

#Test case
arr = [12, 34, 56, 78, 90, 123]
target = 35
result = floor_number(arr, target)
print(result)