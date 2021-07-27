# fig03_02.py
"""Class average program with sentinel-controlled iteration."""

# Initialization phase
total = 0
grader_counter = 0

# Processing phase
grade = int(input('Enter a grade, -1 to end: '))

while grade != -1:
    total += grade
    grader_counter += 1
    grade = int(input('Enter a grade: '))

# Termination phase
if grader_counter != 0:
    average = total / grader_counter
    print(f'The average grade is: {average}')
else:
    print('No grades were entered')