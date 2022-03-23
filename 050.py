# filther 
# filter (function, iterable)

friends = [("Rachel", 23),
          ("Monica", 18),
          ("Phoebe", 22),
          ("Joey", 19),
          ("Ross", 25),
          ("Chandler", 21)]

age = lambda data:data[1] >= 21
drinkin_buddies = list(filter(age, friends))
for i in drinkin_buddies:
    print(i)