import time


"PĘTLA//////////////////////////////////////////////////////"
def sumuj_do(liczba):
    suma = 0

    for liczba in range (1, liczba + 1):
        suma += liczba
        
    return suma    




"LISTA//////////////////////////////////////////////////////"
def sumuj_do2(liczba):
     return sum([liczba for liczba in range(1, liczba + 1)])




"ZBIÓR//////////////////////////////////////////////////////"
def sumuj_do3(liczba):
     return sum({liczba for liczba in range(1, liczba + 1)})




"GENERATOR//////////////////////////////////////////////////////"
def sumuj_do4(liczba):
     return sum((liczba for liczba in range(1, liczba + 1)))




"SUMA_CIĄGU_ARYTM///////////////////////////////////////////"    
def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba



"TIMER_DLA_FUNKCJI//////////////////////////////////////////""""
def finish_timer(start):
    end = time.perf_counter()
    return end - start
"""


"TIMER_FUNKCJA_W_FUNKCJI////////////////////////////////////"
def function_perf(func, argument):
    start = time.perf_counter()
    func(argument)
    end = time.perf_counter()
    return end - start
    




"""
print("Ten program sumuje wszystkie liczby od 1 do wartości, którą wpiszesz.")

koniec = int(input("Podaj końcową wartość: "))
"""


"start = time.perf_counter()"
print(sumuj_do(25665555))
t1 = function_perf(sumuj_do, 25665555)

print(sumuj_do2(25665555))
t2 = function_perf(sumuj_do2, 25665555)

print(sumuj_do3(25665555))
t3 = function_perf(sumuj_do3, 25665555)

print(sumuj_do4(25665555))
t4 = function_perf(sumuj_do4, 25665555)

print(sumuj_do5(25665555))
t5 = function_perf(sumuj_do5, 25665555)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)



