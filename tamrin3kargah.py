# تعریف لیست دانشجویان
students = [
    {
        "name": "علی",
        "student_id": "1001",
        "grades": [18, 17, 19]
    },
    {
        "name": "سارا",
        "student_id": "1002",
        "grades": [14, 15, 13]
    },
    {
        "name": "رضا",
        "student_id": "1003",
        "grades": [9, 10, 8]
    }
]

# تابع محاسبه معدل دانشجو
def calculate_student_gpa(student):
    grades = student["grades"]
    if not grades:
        return 0
    return sum(grades) / len(grades)

# محاسبه معدل هر دانشجو و معدل کل کلاس
total_gpa = 0
print("معدل دانشجویان:\n")

for student in students:
    gpa = calculate_student_gpa(student)
    total_gpa += gpa
    print(f"{student['name']} - شماره دانشجویی: {student['student_id']} - معدل: {gpa:.2f}")

class_average = total_gpa / len(students)
print(f"\nمعدل کل کلاس: {class_average:.2f}\n")

# مقایسه معدل هر دانشجو با معدل کلاس
print("مقایسه با معدل کلاس:\n")
for student in students:
    gpa = calculate_student_gpa(student)
    if gpa > class_average:
        print(f"{student['name']} بالاتر از معدل کلاس است.")
    elif gpa < class_average:
        print(f"{student['name']} پایین‌تر از معدل کلاس است.")
    else:
        print(f"{student['name']} برابر با معدل کلاس است.")