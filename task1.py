student={'Alice':85,'Jay':90,'Aakash':60}
name=input("Enter the student's name: ")
if name in student:
    print(f"{name}'s marks: {student[name]}")
else:
    print("Student not found")
