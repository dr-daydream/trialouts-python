# move file

import os

onde = "copyB.txt"
para = "C:\\Users\\mrd4y\\Desktop\\copyB.txt"

try:
    if os.path.exists(para):
        print("Já tem esse bloco aqui.")
    else:
        os.replace(onde,para)
        print(onde +" foi movida.")
except FileNotFoundError:
    print(onde+" não foi encontrado.")