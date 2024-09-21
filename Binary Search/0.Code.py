# Binary search
# 1) Using loop
def binary_search(arr, target):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if(arr[mid] == target):
            return mid
        elif(arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1 

# 2) Using Recursion
def binary_search1(arr, target, start, end):
    if(start > end):
        return -1
    mid = (start + end) // 2
    if(arr[mid] == target):
        return mid
    elif(arr[mid] > target):
        return binary_search1(arr, target, start, mid-1)
    else:
        return binary_search1(arr, target, mid+1, end)
       
     
#sample case
arr = [1, 2, 4, 5, 67]
result = binary_search(arr, target=67)
print(result)