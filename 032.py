arabia = "\nLevaram tudo. :("
with open('aquelas.txt','w') as file:
#with open('aquelas.txt','a') as file:
    file.write(arabia)

with open('aquelas.txt') as file:
    print(file.read())