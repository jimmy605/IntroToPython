import json 
import os 
import csv 
import pandas as pd 

# def create_file():
#     with open(input('Filename: '), mode='w') as data:
#         for i in range(3):
#             string = input() + '\n'
#             data.write(string)

# create_file()




# with open('accounts.txt', mode='r') as accounts:
#     print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    
#     for record in accounts:
#         account, name, balance = record.split()
#         print(f'{account:<10}{name:<10}{balance:>10}')




# with open('grades.txt', mode='r') as data:
#     # Print out the header
#     print(f'{"ID":^4}{"Name":^8}{"Grade":^6}')
    
#     for user in data:
#         user_id, name, grade = user.split()
#         print(f'{user_id:^4}{name:^8}{grade:^6}')




# accounts = open('accounts.txt', 'r')
# temp_file = open('temp_file.txt', 'w')

# with accounts, temp_file:
#     for record in accounts:
#         account, name, balance = record.split()
#         if account != '300':
#             temp_file.write(record)
#         else:
#             new_record = ' '.join([account, 'Williams', balance])
#             temp_file.write(new_record + '\n')

# os.remove('accounts.txt')
# os.rename('temp_file.txt', 'accounts.txt')




# accounts = open('accounts.txt', 'r')
# temp_file = open('temp_file.txt', 'w')

# with accounts, temp_file:
#     for record in accounts:
#         account, name, balance = record.split()
#         if name != 'Doe':
#             temp_file.write(record)
#         else:
#             temp_file.write(' '.join([account, 'Smith', balance]) + '\n')

# os.remove('accounts.txt')
# os.rename('temp_file.txt', 'accounts.txt')




# accounts_dict = { 'accounts': [
#     {'account': 100, 'name': 'Jones', 'balance': 24.98},
#     {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

# with open('accounts.json', 'w') as accounts:
#     json.dump(accounts_dict, accounts)

# with open('accounts.json', 'r') as accounts:
#     accounts.json = json.load(accounts)

# print(accounts.json['accounts'][0], accounts.json['accounts'][1])

# with open('accounts.json', 'r') as accounts:
#     print(json.dumps(json.load(accounts), indent=4))




# grades_dict = {'gradebook':
#                [{'student_id': 1, 'name': 'Red', 'grade': 'A'},
#                 {'student_id': 2, 'name': 'Green', 'grade': 'B'},
#                 {'student_id': 3, 'name': 'White', 'grade': 'A'}]}

# with open('grades.json', 'w') as data:
#     json.dump(grades_dict, data)

# with open('grades.json', 'r') as data:
#     print(json.dumps(json.load(data), indent=4))




# with open('accounts.csv', mode='w', newline='') as accounts:
#     writer = csv.writer(accounts)
#     writer.writerow([100, 'Jones', 24.98])
#     writer.writerow([200, 'Doe', 345.67])
#     writer.writerow([300, 'White', 0.00])
#     writer.writerow([400, 'Stone', -42.16])
#     writer.writerow([500, 'Rich', 244.62])

# with open('accounts.csv', mode='r', newline='') as accounts:
#     print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
#     reader = csv.reader(accounts)
    
#     for record in reader:
#         account, name, balance = record
#         print(f'{account:<10}{name:<10}{balance:>10}')




# with open('grades.csv', mode='w', newline='') as data:
#     writer = csv.writer(data)
#     writer.writerow([1, 'Red', 'A'])
#     writer.writerow([2, 'Green', 'B'])
#     writer.writerow([3, 'White', 'A'])

# with open('grades.csv', mode='r', newline='') as records:
#     reader = csv.reader(records)
#     # Print the header out
#     print(f'{"ID":<3}{"Name":<8}{"Grade":<6}')
    
#     for student in reader:
#         student_id, name, grade = student
#         print(f'{student_id:<3}{name:<8}{grade:<6}')




# df = pd.read_csv('accounts.csv', 
#                  names = ['account', 'name', 'balance'])
# print(df)
# df.to_csv('accounts_form_dataframe.csv', index=False)


titanic = pd.read_csv('https://vincentarelbundock.github.io/' + 
                     'Rdatasets/csv/carData/TitanicSurvival.csv')
pd.set_option('precision', 2)
titanic.columns = ['name', 'survived', 'sex', 'age', 'class']

# print(titanic.head())
# print(titanic.tail())
print(titanic.describe())
print((titanic.survived == 'yes').describe())