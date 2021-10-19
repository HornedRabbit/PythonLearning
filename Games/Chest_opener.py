import random

#setting constants and data
possible_encounters = ["nothing", "chest"]
encounter_possibility = [40, 60]

chest_rarity = ["green", "orange", "purple", "gold"]
rarity_possibility = [75, 20, 4, 1]

spoils = {"green": 1000, "orange": 4000, "purple": 9000, "gold": 16000}
gold = 0
gameLength = 5


#Beginning of the "game" code######################################################

print("Hi, welcome to the retarded dungeon crawler.")
print("You can only move forward, or stay in your place.")
print("Moving forward will grant you a possibility of finding a chest with gold in it.")
print("Try to stomach it and find out how much gold you can accumulate, good luck!")

while (gameLength > 0): #Main Loop
    gameAnwser = input("Do you want to move forward?(yes/no): ") #Taking the player input
    
    if (gameAnwser == "yes"): #chosing to move forward
        encounter = random.choices(possible_encounters, encounter_possibility)[0] #randomising the encounter
        
        if (encounter == "chest"): #encounter "chest"
            chest = random.choices(chest_rarity, rarity_possibility)[0] #randomising the chest rarity
            gold = gold + spoils[chest] #adding up the chest reward to player spoils
            print("You have encountered a", chest, "chest and found", spoils[chest],"gold")
            print("Your total spoils are", gold, "gold.")
            
        elif (encounter == "nothing"): #encounter "nothing"
            print("You haven't found anything here")
        gameLength -= 1

    elif (gameAnwser == "no"): #chosing to stay in place
        print("You choose to stay in place.")
        gameLength -= 1

    else: #improper action
        print("You didn't choose proper action.")


#printing out the rewards
print("\nYou have reached the end of the game")
print("Your total spoils are", gold, "gold.")
