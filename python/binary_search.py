def binarysearch_first(arr,target):
    left,right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2  
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def binarysearch_last(arr,target):
    left,right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

idk = int(input("Input array :="))
arr = []
for i in range(idk):
    value = int(input(f"Input element {i}:="))
    arr.append(value)
target = int(input("Just input:="))

result1 = binarysearch_first(arr, target)
result2 = binarysearch_last(arr,target)

if result1 != -1 and result2 != -1:
    print(f"Target found at index {result1},{result2}")
else:
    print("Target not found")
