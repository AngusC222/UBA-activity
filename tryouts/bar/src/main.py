import matplotlib.pyplot as plt
from datetime import datetime
from discord import fetchMessages
import json
import asyncio
import re

def createObject(data):
    grenadierGuardsTryouts = 0
    royalMilitaryPolice = 0
    educationTrainingService = 0
    unitedKingdomSpecialForces = 0
    theParachuteRegiment = 0
    royalGurkhaRifles = 0
    royalArmyMedics = 0
    
    for objectID in range(len(data)):
        try:
            grenadierGuardsTryouts = grenadierGuardsTryouts + int(re.search(r'\*\*Grenadier Guards:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1))
            royalMilitaryPolice = royalMilitaryPolice + int(re.search(r'\*\*Royal Military Police:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1))
            educationTrainingService = educationTrainingService + int(re.search(r'\*\*Education & Training Service:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1))
            unitedKingdomSpecialForces = unitedKingdomSpecialForces + int(re.search(r'\*\*United Kingdom Special Forces:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1))
            theParachuteRegiment = theParachuteRegiment + int(re.search(r'\*\*The Parachute Regiment:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1))
            royalGurkhaRifles = royalGurkhaRifles + int(re.search(r'\*\*Royal Gurkha Rifles:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1))
            royalArmyMedics = royalArmyMedics + int(re.search(r'\*\*Royal Army Medics:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1))
        except:
            print("Not a Total Regimental Tryouts Hosted post")

    return [["Grenadier Guards", "Royal Military Police", "Education & Training Service", "United Kingdom Special Forces", "The Parachute Regiment", "Royal Gurkha Rifles", "Royal Army Medics"], [grenadierGuardsTryouts, royalMilitaryPolice, educationTrainingService, unitedKingdomSpecialForces, theParachuteRegiment, royalGurkhaRifles, royalArmyMedics]]

def plotLineGraph(tryouts, path=None):
    plt.figure(figsize=(16, 9))
    plt.xticks(rotation=45)

    plt.xlabel('Lifetime Tryouts Hosted')
    plt.ylabel('Regiment Name')
    plt.title('Lifetime Tryouts Hosted')

    plt.bar(tryouts[0], tryouts[1])

    if path:
        plt.savefig(path, bbox_inches='tight')
    else:
        plt.show()

plotLineGraph(createObject(asyncio.run(fetchMessages())), "./img/graph.png")
