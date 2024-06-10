arr = [43,22,12,654,23,5,15,86]

def selection_sort(arr):
    n = len( arr )
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j # индекс самого маленького числа
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

result = selection_sort(arr)
print(result)