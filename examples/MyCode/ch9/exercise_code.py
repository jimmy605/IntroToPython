import csv 
import json 

# Ch9 exercises
if __name__ == '__main__':
    print('running script')

# 9.1 - Writing grades to a plain text file
def grade_writer(filename) -> None:
    with open(filename, mode='w') as grades:
        sentinel = True 
        
        while sentinel:
            grade = input('Enter the grade (-1 to quit): ')
            if grade != '-1':
                grades.write(grade.strip() + '\n')
            else:
                sentinel = False 




# 9.2 - Reading grades from a plain text file
def read_grades(filename):
    with open(filename, mode='r') as grades:
        for grade in grades:
            g1, g2, g3 = [int(score) for score in grade.split()]
            total = sum([g1, g2, g3])
            count = 3
            average = total / count 
            
            print(f'Total score: {total}')
            print(f'Number of scores: {count}')
            print(f'Average score: {average}')
            print()




# 9.3 - Writing student records to a csv file
def data() -> list:
    """
    Ask for students name and results. Returns a list with this data.
    Note only for one student. Need to create a loop for multiple user inputs.
    """
    
    first_name, last_name = [input('First name: '), input('Last name: ')]
    exam1, exam2, exam3 = [input('Exam {} result: '.format(i)) for i in range(1, 4)]
    
    return [first_name, last_name, exam1, exam2, exam3]


def write_to_csv(func) -> None:
    """
    Ask for the output filename.
    Ask for number of students to input. 
    Input and write the data to a csv file.
    """
    
    filename = input('Enter the filename: ') + '.csv'
    students = int(input('Enter the number of students: '))
    
    with open(filename, mode='w', newline='') as data:
        for i in range(students):
            writer = csv.writer(data)
            writer.writerow(func())




# 9.4 - Reading student records from a csv file
def read_from_csv() -> str:
    """
    Ask for the input filename.
    Print a header for the data - first name, last name, exam 1-3.
    Iterate through each student and display the results.
    """
    
    filename = input('Enter the filename: ') + '.csv'
    # Header for the table
    print(f'{"First Name":^12}{"Last Name":^12}{"Exam 1":^8}{"Exam 2": ^8}{"Exam 3":^8}')
    
    with open(filename, mode='r', newline='') as students:
        reader = csv.reader(students)
        for stu in reader:
            print(f'{stu[0]:^12}{stu[1]:^12}{stu[2]:^8}{stu[3]:^8}{stu[4]:^8}')




# 9.5 - Creating a grade report from a csv file
def grade_report() -> str:
    
    """
    Returns a table with each persons exam results, their average exam score and the class average for each exam.
    """
    
    # Header for the table
    print(f'{"First Name":^12}{"Last Name":^12}{"Exam 1":^8}{"Exam 2": ^8}{"Exam 3":^8}{"Average":^8}')
    
    # Create a dict to store first names: [exam1, exam2, exam3, average], exam_average: [exam1, exam2, exam3]
    data = {}
    exams_total = [0, 0, 0]
    
    with open('grades2.csv', mode='r', newline='') as students:
        reader = csv.reader(students)
        
        for student in reader:
            first, last, exam1, exam2, exam3 = student 
            student_average = sum(int(exam) for exam in [exam1, exam2, exam3]) / 3
            print(f'{first:^12}{last:^12}{exam1:^8}{exam2:^8}{exam3:^8}{student_average:^8.2f}')
            
            exams_total[0] += int(exam1)
            exams_total[1] += int(exam2)
            exams_total[2] += int(exam3)
    
    exam_average = [exam // 3 for exam in exams_total]
    print()
    print(f'{" " * 24}{exam_average[0]:^8}{exam_average[1]:^8}{exam_average[2]:^8}')




# 9.6 - Writing a gradebook dictionary to a json file
def write_to_json(func) -> None:
    """
    Ask for the output filename.
    Ask for number of students to input. 
    Input and write the data to a json file.
    """

    filename = input('Enter the filename: ') + '.json'
    students = int(input('Enter the number of students: '))
    gradebook_dict = {'students':[]}
    
    # Take the input string from student and place into gradebook
    for i in range(students):
        first, last, exam1, exam2, exam3 = func()
        gradebook_dict['students'].append({f'{first} {last}': [int(exam1), int(exam2), int(exam3)]})
    
    with open(filename, mode='w') as data:
        json.dump(gradebook_dict, data)

write_to_json(data)