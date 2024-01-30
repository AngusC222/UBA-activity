import matplotlib.pyplot as plt
from datetime import datetime
from discord import fetchMessages
import asyncio
import re

def createObject(data):
    tryouts = []
    
    for objectID in range(len(data)):
        try:              
            tryouts.append([{
                "timeStamp": data[objectID]["timestamp"],
                "tryouts": {
                    "total": int(re.search(r'A Total of \*\*(\d+)\*\* regimental tryouts', data[objectID]["embeds"][0]["description"]).group(1)),
                    "Grenadier Guards": int(re.search(r'\*\*Grenadier Guards:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1)),
                    "Royal Military Police": int(re.search(r'\*\*Royal Military Police:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1)),
                    "Education & Training Service": int(re.search(r'\*\*Education & Training Service:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1)),
                    "United Kingdom Special Forces": int(re.search(r'\*\*United Kingdom Special Forces:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1)),
                    "The Parachute Regiment": int(re.search(r'\*\*The Parachute Regiment:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1)),
                    "Royal Gurkha Rifles": int(re.search(r'\*\*Royal Gurkha Rifles:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1)),
                    "Royal Army Medics": int(re.search(r'\*\*Royal Army Medics:\*\* \*(\d+)\*', data[objectID]["embeds"][0]["description"]).group(1)),
                }
            }])
        except:
            print("Was not a tryout record")
        print(tryouts)

    return tryouts

def plotLineGraph(tryouts, path=None):
    timeStamps = [datetime.fromisoformat(day["timeStamp"]) for tryout in tryouts for day in tryout]
    totalAmount = [day["tryouts"]["total"] for tryout in tryouts for day in tryout]
    GrenadierGuardsAmount = [day["tryouts"]["Grenadier Guards"] for tryout in tryouts for day in tryout]
    RoyalMilitaryPoliceAmount = [day["tryouts"]["Royal Military Police"] for tryout in tryouts for day in tryout]
    EducationAndTrainingServiceAmount = [day["tryouts"]["Education & Training Service"] for tryout in tryouts for day in tryout]
    UnitedKingdomSpecialForcesAmount = [day["tryouts"]["United Kingdom Special Forces"] for tryout in tryouts for day in tryout]
    TheParachuteRegimentAmount = [day["tryouts"]["The Parachute Regiment"] for tryout in tryouts for day in tryout]
    RoyalGurkhaRiflesAmount = [day["tryouts"]["Royal Gurkha Rifles"] for tryout in tryouts for day in tryout]
    RoyalArmyMedicsAmount = [day["tryouts"]["Royal Army Medics"] for tryout in tryouts for day in tryout]

    plt.figure(figsize=(16, 9))

    plt.plot(timeStamps, totalAmount, marker='o', label='Total')
    # colours may not match regiments
    plt.plot(timeStamps, EducationAndTrainingServiceAmount, marker='o', label='Education & Training Service', color='darkblue')
    plt.plot(timeStamps, UnitedKingdomSpecialForcesAmount, marker='o', label='United Kingdom Special Forces', color='black')
    plt.plot(timeStamps, RoyalMilitaryPoliceAmount, marker='o', label='Royal Military Police', color='red')
    plt.plot(timeStamps, TheParachuteRegimentAmount, marker='o', label='The Parachute Regiment', color='brown')
    plt.plot(timeStamps, RoyalGurkhaRiflesAmount, marker='o', label='Royal Gurkha Rifles', color='indigo')
    plt.plot(timeStamps, RoyalArmyMedicsAmount, marker='o', label='Royal Army Medics', color='lightcoral')
    plt.plot(timeStamps, GrenadierGuardsAmount, marker='o', label='Grenadier Guards', color='gold')

    plt.xlabel('Timestamp')
    plt.ylabel('Tryouts hosted')
    plt.title('Daily Tryouts Hosted Over Time')
    # plt.xticks(rotation=45)
    plt.legend()

    if path:
        plt.savefig(path, bbox_inches='tight')
    else:
        plt.show()

plotLineGraph(createObject(asyncio.run(fetchMessages())), "./img/graph.png")
