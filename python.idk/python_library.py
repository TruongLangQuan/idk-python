def array_input(array, n):
    for i in range(n):
        v = int(input())
        array.append(v)
    return(array)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

def hoan_vi(arr, i):
    if i == len(arr) - 1:
        print(arr)
        return
    for j in range(len(arr)):
        arr[i], arr[j] = arr[j] , arr[i]
        hoan_vi(arr,i + 1)
        arr[i] ,arr[j] = arr[j] , arr[i]

def tim_phan_tu(arr, a):
    indi = [i + 1 for i, n in enumerate(arr) if n == a]  
    if indi:
        print(f"element {a} index in1 array: {indi}")
    else:
        print(f"element {a} not found.")

def giaithua(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * giaithua(n - 1)