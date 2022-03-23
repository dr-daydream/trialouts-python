# deleting files
import os
import shutil

origem = "C:\\Users\\mrd4y\\Desktop\\copyB"

try:
    os.remove(origem) # remove arquivo
    os.rmdir(origem) # remove diretorio
    shutil.rmtree(origem) # remove diretorio c/ arquivos
except FileNotFoundError:
    print("Não deu pra encontrar esse aí não.")
except PermissionError:
    print("Sem permissão pra deletar isso, rapaz.")
except OSError:
    print("Você não pode deletar esse arquivo com essa função.")
else:
    print(origem+ "foi  deletada.")