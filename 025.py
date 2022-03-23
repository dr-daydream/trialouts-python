#   *args
#   * == arguments

def pirate(*result):
    sum = 0
    result = list(result)
    result[9] = 80
    for i in result:
        sum += i
    return sum

print(pirate(33,16,9,2,3,4,5,6,6,66))