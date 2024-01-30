# UBA activity monitor

![Discord: aaa2.](https://img.shields.io/badge/Discord-aaa2.-white?labelColor=blue&style=flat&logo=discord&logoColor=white) [![Roblox: SlRANGUS](https://img.shields.io/badge/Roblox-SlRANGUS-white?labelColor=Grey&style=flat&logo=roblox&logoColor=white&link=https://www.roblox.com/users/557148823/profile)](https://www.roblox.com/users/557148823/profile)

> A script that creates a line graph of activity in the UBA server

## Activity Over Time

### How does this work?

1. The discord.py file retrieves all the messages from the #activity channel on the Discord.
2. the timestamps and reaction count is extracted from all the *"Activity check posts*.
3. The script then generates a line graph with timestamps on the X-axis and reaction counts on the Y-axis
4. Then the graph is saved to the graph.png file.

### Example:

<div align="center"><img alt="Example Graph Of Activity Over Time" src="./activity/img/graph.png"></div>

<p align="center">as of 22/01/2024</p>

## Daily Tryouts Hosted Over Time

### How does this work?

1. The discord.py file retrieves all the messages from the #regimental channel on the Discord.
2. The main.py then searches all the *"Total Regimental Tryouts Hosted* posts for the amount of tryouts being hosted by each regiment and in total using regex. 
3. Each regiment is given its own line in the graph with an extra total line added for the total tryouts hosted in a day and time stamps are then put into a line graph with reactions as the Y axis and time stamp as the X axis.
4. the graph is then saved to the graph.png file.

### Example:

<div align="center"><img alt="Example Graph Of Tryouts Hosted Over Time" src="./tryouts/line/img/graph.png"></div>

<p align="center">as of 30/01/2024</p>

## Lifetime Tryouts Hosted

### How does this work?

1. The discord.py file retrieves all the messages from the #regimental channel on the Discord.
2. The main.py then searches all the *"Total Regimental Tryouts Hosted* posts for the amount of tryouts being hosted by each regiment using regex.
3. Each regiment is given its own individual bar in the bar graph.
4. the graph is then saved to the graph.png file.

### Example:

<div align="center"><img alt="Example Chart Of Lifetime Tryouts Hosted" src="./tryouts/bar/img/graph.png"></div>

<p align="center">as of 30/01/2024</p>
