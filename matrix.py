# nums = [
#     [1,2],
#     [4,5,2,1],
#     [7,8,12,423,6536,45]
# ]
#
# for i in range( len(nums) ):
#     for j in range(len(nums[i])):
#         print(nums[i][j])


nums = [
    [3,2],
    [6,2],
    [7,1]
]
result = ""
for i in range(len(nums)):
    for j in range(len(nums[i])):
        result += str(nums[i][j])

print(result)
# def transpose_matrix(arr):
#     n = len(arr)
#     transposed = [ [0]*n for _ in range(n) ]
#
#     for i in range(n):
#         for j in range(len(arr[i])):
#             transposed[j][i] = arr[i][j]
#     return transposed
#
# print( transpose_matrix(nums) )

# # Поиск максимального элемента
# max = num[0][0]
# for i in range(len(num)):
#     for j in range(len(num[i])):
#         if num[i][j] > max:
#             max = num[i][j]
# print(max)

# # Найти сумму элементов списка
# summ = 0
# for i in range( len(num)):
#     for j in range(len(num[i])):
#         summ += num[i][j]
#
# print(summ)

