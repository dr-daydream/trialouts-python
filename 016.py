# tuple

student = ("Percy Jackson", 12, "Demigod")

print(student.count("Percy Jackson"))
print(student.index("Demigod"))

for x in student:
    print(x)

if "Demigod" in student:
    print("Go to the Camp!")