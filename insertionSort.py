arr = [43,22,12,654,23,5,15,86]

def insertion_sort(arr):
    n = len( arr )
    for i in range(1, n):
        num = arr[i]
        j = i - 1
        while num < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = num
    return arr

result = insertion_sort(arr)
print(result)