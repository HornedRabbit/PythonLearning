"SUMA_WSZYSTKICH_ARGUMENTÓW////////////////////////////"

def count(*numbers):
    suma = 0
    for item in numbers:
        suma += item 
    return suma

print(count(2,4,1,2,4,5,10))
