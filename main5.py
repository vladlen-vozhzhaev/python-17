# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# print(num1 / num2)

try:
    nums = [521,21,14]
    print(nums[3])
except:
    print("Что-то произошо, но ничего страшного!")
finally:
    print("Блок finally!")