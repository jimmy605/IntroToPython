# fig03_03.py
"""Using nested control statements to analyze examination results."""

# Initialization phase
passes = 0
fails = 0

# Processing phase
for student in range(10):
    result = int(input('Enter the exam result (1=pass, 2=fail): '))
    
    if result == 1:
        passes += 1
    else:
        fails += 1

# Termination phase
print(f'Passes: {passes}')
print(f'Fails: {fails}')

if passes > 8:
    print('Bonus to instructor')