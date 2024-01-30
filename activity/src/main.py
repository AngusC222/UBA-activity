import matplotlib.pyplot as plt
from datetime import datetime
from discord import fetchMessages
import asyncio

def createObject(data):
    reactions = []
    
    for objectID in range(len(data)):
        if "ACTIVITY CHECK" in data[objectID]["content"]:
            reactions.append({
                "timeStamp": data[objectID]["timestamp"],
                "count": data[objectID]["reactions"][0]["count"]
            })

    return reactions

def plotLineGraph(reactions, path=None):
    timestamps = [datetime.fromisoformat(reactionObject["timeStamp"]) for reactionObject in reactions]
    counts = [reactionObject["count"] for reactionObject in reactions]

    plt.figure(figsize=(16, 9))
    plt.plot(timestamps, counts, marker='o')
    plt.xlabel('Timestamp')
    plt.ylabel('Reaction Count')
    plt.title('Activity Over Time')
    
    if path:
        plt.savefig(path, bbox_inches='tight')
    else:
        plt.show()

plotLineGraph(createObject(asyncio.run(fetchMessages())), "./img/graph.png")
