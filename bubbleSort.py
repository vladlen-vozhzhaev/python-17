# for i in range( len(arr) ):
#     for j in range( len(arr) ):
#         for k in range( len(arr) ):
#             print(i, j, k)


arr = [43,22,12,654,23,5,15,86]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

resultArr = bubble_sort(arr)
print(resultArr)