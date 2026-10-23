
stud_name = input("Enter a Student Name: ")

subject_python = int(input("Enter The Marks In Python: "))
subject_SQL = int(input("Enter The Marks In SQL: "))
subject_Maths = int(input("Enter The Marks In Maths: "))


if not (0 <= subject_python <= 100 and
        0 <= subject_SQL <= 100 and
        0 <= subject_Maths <= 100):

    print("Invalid marks! Each subject mark must be between 0 and 100.")

else:
    total_marks = subject_python + subject_SQL + subject_Maths
    average_marks = total_marks / 3

    # Calculate grade
    if average_marks < 60:
        grade = "F"
    elif average_marks < 70:
        grade = "D"
    elif average_marks < 80:
        grade = "C"
    elif average_marks < 90:
        grade = "B"
    else:
        grade = "A"

  
    print("\n" + "_" * 40)
    print("       STUDENT MARKS REPORT")
    print("_" * 40)

    print("Student Name:", stud_name)
    print("Python Marks:", subject_python)
    print("SQL Marks:", subject_SQL)
    print("Maths Marks:", subject_Maths)
    print("Total Marks:", total_marks, "/ 300")
    print("Average:", round(average_marks, 2), "/ 100")
    print("Grade:", grade)

    print("_" * 40)
