# fig03_01.py 
"""Class average program with sequnce - controlled repetition."""

# Initialisation phase
total = 0 # Sum of grades
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94] # List of ten grades

# Processing phase
for grade in grades:
    total += grade # Add current grade to the running total
    grade_counter += 1 # Indicate that one more grade was processed

# Termination phase
average = total / grade_counter
print(f'Class average is {average}')