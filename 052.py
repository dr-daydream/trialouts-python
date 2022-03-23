# list comprehension

grades = [100, 90, 80, 70, 60, 50, 40, 30, 0]
# approveds = list(filter(lambda hs: hs >= 60, grades))
# approveds = [i for i in grades if i >= 60 ]
approveds = [i if i >= 60 else "FAILURE" for i in grades]
print(approveds)