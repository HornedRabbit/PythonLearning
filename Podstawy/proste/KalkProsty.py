operator = input("Wybierz działanie : \
+ dodawanie, - odejmowanie, / dzielenie, * mnożenie,\
 // dzielenie z resztą, ** potęgowanie: ")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if (operator == "+"):
    print(a, "+", b, "=", a + b)
    
elif (operator == "-"):
    print(a, "-", b, "=", a - b)
    
elif (operator == "/"):
    if(b == 0):
        print("Nie można dzielić przez 0")
    else:
        print(a, "/", b, "=", a / b)

elif (operator == "*"):
    print(a, "*", b, "=", a * b)

elif (operator == "//"):
    print(a, "/", b, "=", a // b, "oraz", a % b, "reszty")

elif (operator == "**"):
    print(a, "^", b, "=", a ** b)
    
else:
    print("Nie wybrałeś poprawnego działania")
    
