# Define the list of dictionaries
students = [
    {
        "name": "john",
        "mark": 450,
    },
    {
        "name": "david",
        "mark": 490,
    },
    {
        "name": "guru",
        "mark": 455,
    }
]

# Sort the list of dictionaries by the "mark" key in descending order
students.sort(key=lambda x: x["mark"], reverse=True)

# Assign ranks to students
for i, student in enumerate(students, start=1):
    if i == 1:
        student["rank"] = "Rank 1"
    elif i == 2:
        student["rank"] = "Rank 2"
    elif i == 3:
        student["rank"] = "Rank 3"

# Print the sorted list of dictionaries with ranks
for student in students:
    print(f"{student['name']} - {student['mark']} marks - {student['rank']}")

