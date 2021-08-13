def cube_list():
    lyst = [num ** 3 for num in range(1, 11)]
    return lyst

print(cube_list())




characters = []
characters += 'Birthday'
print(characters)




num = (123.45,)
print(num)




high_low = ('Monday', 35, 21)
for element in high_low:
    print(element)




names = ['Dean', 'Connor', 'Noah', 'Stacey']
for idx, name in enumerate(names):
    print(f'{idx + 1}: {name}')




numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers[0:3] = ['two', 'three', 'five']
print(numbers)
numbers[0:3] = []
print(numbers)




numbers = [num for num in range(1, 16)]
print(numbers[1::2])

numbers[5:10] = [0, 0, 0, 0, 0]
print(numbers)

numbers = numbers[0:5]
print(numbers)

numbers = []
print(numbers)