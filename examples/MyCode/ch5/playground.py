# a_list = [] 

# for number in range(1, 6):
#     a_list += [number]

# print(a_list)




# def cube_list():
#     numbers = [num for num in range(1, 11)]
#     output = []
    
#     for number in numbers:
#         output += [number ** 3]
    
#     return output

# print(cube_list())




# characters = []
# characters += 'Birthday'
# print(characters)




# time_tuple = (9, 16, 1)
# print(time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2])




# student_tuple = ('Amanda', 'Blue', [98, 75, 87])
# student_tuple[2][1] = 85
# print(student_tuple)




# score = (123.45, )
# print(score)




# first, second = 'hi'
# print(first, second, sep='  **  ')




# number1 = 99
# number2 = 22
# number1, number2 = (number2, number1)
# print(number1, number2)




# colors = ['red', 'orange', 'yellow']
# print(list(enumerate(colors)))




# high_low = ('Monday', 31, 14)
# day, high, low = high_low

# print(f'{day} was a high of {high} and a low of {low}')




# names = ['Connor', 'Noah', 'Stacey']
# for num, name in enumerate(names):
#     print(f'{num}: {name}')



# numbers = list(range(1, 16))
# print(numbers)

# even_numbers = numbers[1::2]
# print(even_numbers)

# numbers[5:10] = [0] * len(numbers[5:10])
# print(numbers)

# numbers[:] = numbers[:5]
# print(numbers)

# numbers[:] = []




# numbers = list(range(0, 10))
# del numbers[-1]
# print(numbers)

# del numbers[::2]
# print(numbers)




# numbers = list(range(1, 16))
# del numbers[:4]
# print(numbers)

# del numbers[:]
# print(numbers)




# def modify_elements(items):
#     """Multiplies all element values in items by 2."""
#     for i in range(len(items)):
#         items[i] *= 2

# numbers = [10, 3, 7, 1, 9]
# modify_elements(numbers)

# print(numbers)



# numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)



# numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# ascending_numbers = sorted(numbers)
# print(ascending_numbers)




# foods = ['Cookies', 'pizza', 'Grapes', 'apples', 'steak', 'Bacon']
# foods.sort()
# print(foods)



# numbers = [3, 7, 1, 4, 2, 8, 5, 6]
# print(numbers.index(5))




# elements = [67, 12, 46, 43, 13]
# number_index = elements.index(43)
# print(number_index)

# search = 44
# if search in elements:
#     print(elements.index(search))
# else:
#     print(f'{search} is not in elements.')



# color_names = ['orange', 'yellow', 'green']
# color_names.insert(0, 'red')
# print(color_names)

# color_names.append('blue')
# print(color_names)

# color_names.extend(['indigo', 'violet'])
# print(color_names)




# sample_list = []
# s = 'abc'
# sample_list.extend(s)
# print(sample_list)

# t = tuple(range(1, 4))
# sample_list.extend(t)
# print(sample_list)

# sample_list.extend((4, 5, 6))
# print(sample_list)




# color_names = ['orange', 'yellow', 'green']
# color_names.remove('green')
# print(color_names)

# color_names.clear()
# print(color_names)


# responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

# for i in range(1, 6):
#     print(f'{i} appears {responses.count(i)} times in responses')



# color_names = ['red', 'orange', 'yellow', 'green', 'blue']
# color_names.reverse()
# print(color_names)




# rainbow = ['green', 'orange', 'violet']
# rainbow.insert(rainbow.index('violet'), 'red')
# print(rainbow)

# rainbow.append('yellow')
# print(rainbow)

# rainbow.reverse()
# print(rainbow)

# rainbow.remove('orange')
# print(rainbow)




# list_1 = []
# for item in range(1, 6):
#     list_1.append(item)

# print(list_1)

# list_2 = [item for item in range(1, 6)]
# print(list_2)

# list_3 = [item ** 3 for item in range(1, 6)]
# print(list_3)


# list_4 = [item for item in range(1, 11) if item % 2 == 0]
# print(list_4)

# colors = ['red', 'orange', 'yellow', 'green', 'blue']
# colors_2 = [color.upper() for color in colors]
# print(colors_2)

# data = [(item, item ** 3) for item in range(1, 6)]
# print(data)

# threes = list(range(3, 30, 3))
# print(threes)

# numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# for value in (x ** 2 for x in numbers if x % 2 != 0):
    # print(value, end='  ')
    
# square_of_odds = (x ** 2 for x in numbers if x % 2 != 0)
# print(square_of_odds)

# gen_list = list(item ** 3 for item in [10,3,7,1,9,4,2] if item % 2 == 0)
# print(gen_list)


# numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

# def is_odd(x):
#     """Returns True only if x is odd."""
#     return x % 2 != 0

# print(list(filter(is_odd, numbers)))

# print(list(filter(lambda x: x % 2 != 0, numbers)))


# print(list(map(lambda x: x ** 2, numbers)))


# print(list(map(lambda x: x ** 2, 
#                filter(lambda x: x % 2 != 0, numbers))))




# numbers = list(range(1, 16))

# even_numbers = list(filter(lambda x: x %2 == 0, numbers))
# print(even_numbers)

# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)

# dup_func = list(filter(lambda x: x % 2 == 0,
#                        map(lambda x: x ** 2, numbers)))
# print(dup_func)


# name = 'Dean'
# print(list(name))



# fahrenheit = [41, 32, 212]

# temps = list(map(lambda f: (f, (f - 32) * (5/9)), fahrenheit))
# print(temps)

# colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']
# print(min(colors, key=lambda s: s.lower()))
# print(max(colors, key=lambda s: s.lower()))



