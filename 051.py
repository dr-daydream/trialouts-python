# reduce()

import functools 

tonystark = ["J","A","R","V","I","S"]
system = functools.reduce(lambda x, y,:x+y,tonystark)
print(system)

factorial = [50,3,20,1,10,5,9]
result = functools.reduce(lambda x, y,:x * y, factorial)
print(result)