wynik = 0
i = 0

n = int(input("Podaj ilość liczb do sumowania: "))

while i < n:
    
    x = int(input("Podaj liczbę: "))
    wynik += x
    i += 1

print("Wynik dodawania", n, "liczb to:", wynik)
            
