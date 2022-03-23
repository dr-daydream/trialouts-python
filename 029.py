# exception

try:
    numerador = int(input("Digite um número para divisão: "))
    denominador = int(input("Digite um número para ser dividido: "))
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print(e)
    print("Não dá pra dividir por zero, lerdão!")
except ValueError as e:
    print(e)
    print("Só números, Einstein.")
except Exception as e:
    print(e)
    print("Deu merda, amigo.")
else:
    print(resultado)
finally:
    print("Não tem jeito, vai rodar. Wink-wink!")