def bubble_sort_count(arr):
    n = len(arr)
    count = 0

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[i] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                count += 1
    return count

ls = input("input(space):=")
mylist = list(map(int,ls.split()))
print(bubble_sort_count(mylist))