# zip (*iterables)

usernames = ["Gatsby", "Aethelwulf", "Raegon"]
passwords = ("346223", "abc321", "gu3st")
logs_date = ["1/1/2022", "3/5/2021", "5/9/2021"]

users = zip(usernames,passwords,logs_date)
for i in users:
    print(i)

#users = dict(list(zip(usernames, passwords)))
#print(type(users))

#for key,value in users.items():
#    print(key+" : "+value)