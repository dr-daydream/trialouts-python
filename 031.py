# reading a file

try:
    with open('C:\\Users\\mrd4y\\Dropbox\\PC\\Documents\\Testingbot\\.env.tx') as file:
        print(file.read())
# print(file.closed)
except FileNotFoundError:
    print("Não deu pra achar, camarada.")