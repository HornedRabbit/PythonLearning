wynik = 0

i = 0

while i < 3:
    x = int(input("Podaj parzystą liczbę dodatnią: "))
    if ( (x > 0) and (x % 2 == 0)):
        wynik += x
    else:
        print("Miała być dodatnia parzysta, spróbuj jeszcze raz.")
        continue
    i += 1

print("Wynik sumowania:", wynik)    

