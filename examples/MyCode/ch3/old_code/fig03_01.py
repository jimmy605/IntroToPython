# fig03_01.py
"""Class average program with sequence-controlled repetition."""

# Initilization phase
total = 0
# List of 10 grades
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94] 

# Processing phase
for grade in grades:
    total += grade

# Termination phase
average = total / len(grades)
print(f'Class average is {average}')