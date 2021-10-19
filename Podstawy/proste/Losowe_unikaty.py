import random

"//////////////////////////////////"


def choose_random_uniques(ammount, total_ammount):
    cont = []
    while (len(cont) < ammount):
        add = random.randint(0, total_ammount)
        if (add not in cont):
            cont.append(add)

    return cont


"//////////////////////////////////"

def choose_random_uniques_2(ammount, total_ammount):
    cont = random.sample(range(total_ammount + 1), ammount)
    return cont

"Obie funkcje choose mają taką samą końcową funkcjonalność"



print(choose_random_uniques_2(10,49))
                
    
