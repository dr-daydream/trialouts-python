# threading = flow of exec

# multithreading

import threading 
import time 

def acordar():
    time.sleep(5)
    print("Você dormiu!")
def cafe():
    time.sleep(5)
    print("Você bebeu café.")
def estudar():
    time.sleep(2)
    print("Você terminou de estudar.")

x = threading.Thread(target=acordar, args=())
x.start()

y = threading.Thread(target=cafe, args=())
y.start()

z = threading.Thread(target=estudar, args=())
z.start()

x.join()
y.join()
z.join()

# acordar()
# cafe()
# estudar()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())