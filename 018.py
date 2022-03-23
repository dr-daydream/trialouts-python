#cabins.py

cabins = {'Zeus':'Cabin 1',
          'Hera':'Cabin 2',
          'Poseidon':'Cabin 3',
          'Demeter':'Cabin 4',
          'Ares':'Cabin 5',
          'Athena':'Cabin 6',
          'Apollo':'Cabin 7',
          'Artemis':'Cabin 8',
          'Hephaestus':'Cabin 9',
          'Aphrodite':'Cabin 10',
          'Hermes':'Cabin 11',
          'Dionysus':'Cabin 12',
          'Hades':'Cabin 13',
          'Iris':'Cabin 14'}
cabins.update({'Hypnos':'Cabin 15'})

#cabins.clear()
#cabins.update({'Zeus':'Jupiter'})
#cabins.pop('Iris')
#print(cabins['Hades'])
#print(cabins.get('Hypnos'))
#print(cabins.keys())
#print(cabins.values())
#print(cabins.items())

for key,value in cabins.items():
    print(key, value)