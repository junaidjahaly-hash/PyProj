import json
with open ("files/r1/students.json", "r") as f:
    students=json.load(f)
    print(students)