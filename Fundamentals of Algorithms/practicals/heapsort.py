import heapq

def heapsort(arr):
    result = []
    for i in range(len(arr)):
        heapq._heapify_max(arr)
        arr[0], arr[-1] = arr[-1], arr[0]
        result.insert(0, arr[-1])
        del arr[-1]
    return result

arr = [81, 89, 9, 11, 14, 76, 54, 22]
print(f"Original: {arr}")
print(f"Sorted: {heapsort(arr)}")