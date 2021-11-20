import string
# Exercises code for chapter 5

#5.3
# output = list(map(lambda x: (x, x * 0.0254), [69, 77, 54]))
# print(output)  




#5.4 
# grades = [[89, 76, 66],
#           [90, 87, 88]]

# Part A
# count = 1
# for scores in grades:
#     for score in scores:
#         print(f'{count}: {score}')
#         count += 1

# Part B (ugly code i know. Couldn't be bothered refactoring)
# print('    C1    C2    C3')
# for idx, scores in enumerate(grades):
#     print(f'R{idx + 1}', end='')
    
#     for idx, score in enumerate(scores):
#         if idx < len(scores) - 1:
#             print(f'{score:>4}', end='  ')
#         else:
#             print(f'{score:>4}')




#5.5
alphabet = string.ascii_lowercase

# The first half of the string using starting and ending indices
print(alphabet[0:len(alphabet) // 2])

# The first half of the string using only the ending index
print(alphabet[len(alphabet) // 2:])

# The second half of the string using starting and ending indices
