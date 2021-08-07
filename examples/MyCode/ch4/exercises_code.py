import datetime
import math 

#4.1




#4.2 - The stack could overflow. Computer could run out of memory.




#4.3 - There is no return. It should be "return x ** 3"




#4.4 - Iterates through the list squaring each element and then added to y. Once iterated through the list the total of y is returned




#4.5
def seconds_since_midnight(*time_now):
    hour_in_seconds = 60 * 60
    minute_in_seconds = 60
    
    return sum([time_now[0] * hour_in_seconds, time_now[1] * minute_in_seconds, time_now[2]])

# print(seconds_since_midnight(13, 30, 45))




#4.6
def average(num, *args):
    if not args:
        return num 
    
    length = len(args) + 1
    total_sum = sum(args) + num
    return total_sum / length

# print(average(1, 2, 3))




#4.7
def date_and_time():
    print(datetime.datetime.today())

# date_and_time()




#4.8
def round_num(num_float):
    rounding = {
        'integer': 0,
        'tenth': 1,
        'hundredth': 2,
        'thousandth': 3
    }
    
    for rounded, num in rounding.items():
        print(f'To the nearest {rounded}: {round(num_float, num)}')

round_num(13.56449)