# file detection

import os

pjo1 = "C:\\Users\\mrd4y\\Dropbox\\PC\\Documents\\Livros\\Rick Riordan\\Percy Jackson e os Olimpianos\\Vol. 1 - O Ladrão de Raios.pdf"
if os.path.exists(pjo1):
    print("Achouuuu!")
    if os.path.isfile(pjo1):
        print("Isso é arquivo.")
    elif os.path.isdir(pjo1):
        print("É pasta, família.")
else:
    print("Tá aí não, bro.")