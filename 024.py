#   scope

name = "Sancto"         # global (outside)

def thy():
    name = "Holy"       # local (inside)
    print(name)

thy()
print(name)