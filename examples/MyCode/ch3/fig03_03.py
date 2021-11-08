# Fig03_03.py 
"""Using nested control statements to analyze examination results."""

# Initialisation phase
passes = 0

# Proccessing phase
for student in range(10):
    result = int(input('Enter result: '))
    
    while result not in [1, 2]:
        result = int(input('Enter result: '))
    
    if result == 1:
        passes += 1

# Termination phase
print(f'\nThere was {passes} passes.')
print(f'There was {10 - passes} failures.')

if passes > 8:
    print('Bonus to instructor')