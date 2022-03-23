# dictionary comprehension

# fahrenheit p celsius

#cities_F = {'NYC': 32, 'Boston': 75, 'LA': 100, 'Chicago': 50}
#cities_C = {key: round((value-32)*(5/9)) for (key,value) in cities_F.items()}
#print(cities_C)

# ---------------------------------------------------------------------------------

#       magic_centers = {'New York': 100, 'Boston': 75, 'Indianopolis': 50, 'California': 80}
#       battle_centers = { key: () for (key, value) in magic_centers()}

# ---------------------------------------------------------------------------------

#clima = {'NYC': 'nevando', 'Boston': 'ensolarado', 'LA':'ensolarado','Chicago':'nublado'}
#clima_ensolarado = {key: value for (key,value) in clima.items() if value == 'ensolarado'}
#print(clima_ensolarado)

# ---------------------------------------------------------------------------------

#desc_cities = {key:('Quente' if value >= 40 else 'Frio') for (key,value) in cities.items()}
#print(desc_cities)

def check_temp(value):
    if value >= 70:
        return 'Calorzão'
    elif 69 >= value >= 40:
        return 'Quente'
    else:
        return 'Frio'

cities = {'NYC': 32, 'Boston': 75, 'LA': 100, 'Chicago':50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)