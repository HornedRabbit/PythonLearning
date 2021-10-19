import random
from enum import Enum

Encounter = Enum("Encounter", ["nothing", "chest"])
encountersDictionary = {
                            Encounter.nothing: 0.4,
                            Encounter.chest: 0.6
                        }
encounterList = list(encounterDictionary.keys())
encounterProbability = list(encounterDictionary.values())



Chest_rarity =  Enum("Chest rarity", ["green", "orange", "purple", "gold"])
chest_rarityDictionary = {
                            Chest_rarity.green: 0.75,
                            Chest_rarity.orange: 0.2,
                            Chest_rarity.purple: 0.04,
                            Chest_rarity.gold: 0.01
                        }

chest_rarityList = tuple(chest_rarityDictionary.keys())
chest_rarityPossibility = tuple(chest_rarityDictionary.values())



chest_rewardDictionary = {
                            chest_rarityList[reward]: (reward + 1) * (reward + 1) * 1000
                            for reward in range (len(chest_rarityList))
                        }
