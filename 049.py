#           sort() method = lists
#           sort() function = iterables

#camps = ("Clarisse", "Percy", "Travis", "Connor")
# camps.sort(reverse=True)

#sorted_camps = sorted(camps)
#for i in sorted_camps: 
#    print(i)


students = (("Harry Potter", "EE", 17),
            ("Hermione Granger", "O", 17),
            ("Rony Weasley", "A", 17),
            ("Luna Lovegood", "O", 16))
grade = lambda grades:grades[1]
age = lambda age:age[2]
#students.sort(key=grade, reverse=True)
sorted_students = sorted(students,key=age)
for i in sorted_students:
    print(i)