def get_grades():
    grades_input = input("Enter grades separated by commas: ")
    try:
        grades = [int(grade.strip()) for grade in grades_input.split(',')]
        print("Grades:", grades)
    except ValueError as e:
        print("One or more of the values you entered cannot be converted to an integer:", e)

get_grades()
