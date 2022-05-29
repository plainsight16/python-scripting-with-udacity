

names = [name.strip() for name in input("Enter names: ").split(",")]
print("names: ", names);

assignments = [int(assignment.strip()) for assignment in input(
    "Enter assignment count for each student: ").split(",")]

print(assignments)

grades = [int(grade.strip())
          for grade in input("Enter current grade for each student: ").split(",")]

potential_grades = [grade + (assignment * 2)
                    for grade, assignment in list(zip(grades, assignments))]

# message string to be used for each student
# HINT: use .format() with this string in your for loops

message = "Hi {0},\n\nThis is a reminder that you have {1} assignments left to \
submit before you can graduate. You're current grade is {2} and can increase \
to {3} if you submit all assignments before the due date.\n\n"

for i, name in enumerate(names):
    print(message.format(name, assignments[i], grades[i], potential_grades[i]))
