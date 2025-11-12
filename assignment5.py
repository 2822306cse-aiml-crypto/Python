student_marks = {
    "Ravi": 85,
    "Neha": 92,
    "Amit": 78,
    "Priya": 88,
    "Rahul": 95
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")
