# higher order function

#def loud(text):
#    return text.upper()

#def quiet(text):
#    return text.lower()

#def hello(fun):
#    text = fun("Hot damn")
#    print(text)

#hello(loud)
#hello(quiet)

def divisor(x):
    def dividendo(y):
        return y / x 
    return dividendo 

dividir = divisor(2)
print(dividir(32))