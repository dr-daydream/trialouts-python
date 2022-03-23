# daemon thread

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logado por: ",count, "segundos.")
x = threading.Thread(target=timer, daemon=True)
x.start()

resposta = input("Você deseja sair?")