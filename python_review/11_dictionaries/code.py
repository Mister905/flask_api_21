friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages["Greg"] = 88

print(friend_ages["Rolf"])

print(friend_ages["Anne"])

print(friend_ages["Greg"])


friends = [
    {"name": "George", "age": 46},
    {"name": "Patty", "age": 23},
    {"name": "Seymore", "age": 57}
]

print(friends[0])

print(friends[2]["name"])


student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
    
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class.")
    
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))