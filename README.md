# Elf Game v1.0
 Simulation of a board game I created over christmas 2023
 All done in python. Sheets using HTML and CSS.
#### Python packages used
pandas, matplotpy, statistics, math, random, inspect

## About the game
The game is simple where you roll dice to collect wood however the weather will stop you depending on dice rolls as well.
Each character has separate attributes and actions which I made character sheets for in the character sheets folder.
I will not get into how the game is played in this. This upload is mainly to show the basic simulation I made and the stats collected from running it to balance the character's abilities.

## Simulation
I started by creating a basic Character class with common attributes and functions across all the different characters and then used inheritance to create additional Characters.
I created a basic usually "safe" method of wood collection for each character to balance around and used this for the simulation.

Each game was run a number of times to find the average outcome of wood collection for each character.

## Statistics and Graphing
I then used the data collected from the simulation to graph each character's outcomes and find the mean, median and standard deviation in each one trying to keep the s.d lower so as to reduce randomness of outcome and keep the averages close to one another to "balance" the characters.

Some characters work with more dice or have random abilities they access so their s.d is bound to be larger than the less stochastic characters.

### Final thoughts
As this is the first version of the game. I played it with my family over the holidays and got feedback from them and myself for improvements and changes to the gameplay. I will then use this to create improvements and continue the product lifecycle as and when I have time. This will be a long project if completed and entirely done on my own time so I do not expect regular updates.
