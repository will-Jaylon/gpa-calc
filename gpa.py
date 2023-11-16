# function to calculate grade points based on letter grade
def get_grade_points(letter_grade):
    if letter_grade == 'A+':
        return 4.3
    elif letter_grade == 'A':
        return 4.0
    elif letter_grade == 'A-':
        return 3.7
    elif letter_grade == 'B+':
        return 3.3
    elif letter_grade == 'B':
        return 3.0
    elif letter_grade == 'B-':
        return 2.7
    elif letter_grade == 'C+':
        return 2.3
    elif letter_grade == 'C':
        return 2.0
    elif letter_grade == 'C-':
        return 1.7
    else: 
        return None
    
 # function to caculate GPA
def calculate_gpa(courses):
    total_credit_hours = 0
    weighted_grade_points = 0

    for course in courses:
        credit_hours = course['credit_hours']
        letter_grade = course['letter_grade']
        
        grade_points = get_grade_points(letter_grade)
        #skip the course if grade points could not be determined
        if grade_points is None:
            continue

        total_credit_hours += credit_hours 
        weighted_grade_points += grade_points * credit_hours
    if total_credit_hours == 0:
        return 0
    gpa = weighted_grade_points / total_credit_hours
    return gpa

# main part of program
courses = []
num_courses = int(input("Enter the number of courses: "))

# collect information for each program 
for i in range(num_courses):
    print(f"\nCourse {i + 1}:")
    course_name = input("Enter course name: ")
    letter_grade = input("Enter letter grade: ")
    credit_hours = int(input("Enter credit hours: "))

    # create a dictionary for the course and add it to the list of courses
    course = {
        'name': course_name,
        'letter_grade': letter_grade,
        'credit_hours': credit_hours
    }
    courses.append(course)

#calculate the GPA
gpa = calculate_gpa(courses)

#display the GPA
print("\nGPA: {:.2f}".format(gpa))