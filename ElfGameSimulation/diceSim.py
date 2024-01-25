import random
from inspect import signature
from statistics import *

WEATHER_ROLLS = [((1,6), lambda x: x == 6),
                 ((2,6), lambda x,y: x == y),
                 ((1, 100), lambda x: pow(x,0.5)%1 == 0),
                 ((1,20), lambda x: pow(2,1/x)%1 == 0),
                 ((1,6), lambda x: x != 6),
                 ((2,6), lambda x,y: x < y),
                 ((2,6), lambda x,y: x+y == 7),
                 ((1,20), lambda x: x%2 == 0),
                 ((1,20), lambda x: x%2 == 1),
                 ((1,20), lambda x: x in (1,6,15,20)),
                 ((1,100), lambda x: x in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)),
                 ((1,20),lambda x: x%5 == 0),
                 ((2,6), lambda x,y: x+y >= 5),
                 ((2,6), lambda x,y: x+y >= 6),
                 ((2,6), lambda x,y: x+y >= 7),
                 ((2,6), lambda x,y: x+y >= 8),
                 ((2,6), lambda x,y: x+y >= 9),
                 ((2,6), lambda x,y: x+y >= 10),
                 ((2,6), lambda x,y: x+y >= 11)]

def rollDice(number, sides):
    return [random.randint(1,sides) for x in range(number)]

def goodWeather(dice, f):
    return f(*dice[:len(signature(f).parameters)+1])


def simRolls():
    results = []
    RUNS = 10000
    for i in range(len(WEATHER_ROLLS)):
        r = 0
        for j in range(RUNS):
            roll = WEATHER_ROLLS[i]
            number,sides = roll[0]
            func = roll[1]
            dice = rollDice(number,sides)
            # print(dice, goodWeather(dice, func))
            if goodWeather(dice, func):
                r += 1
        results.append(r/RUNS)

    print(sum(results)/len(results))

twod6 = {
    '2': 2.78,
    '3': 5.56,
    '4': 8.33,
    '5': 11.11,
    '6': 13.89,
    '7': 16.67,
    '8': 13.89,
    '9': 11.11,
    '10': 8.33,
    '11': 5.56,
    '12': 2.78
}

muffins = []
def td6work():
    for i in range(len(twod6)-1):
        k = sum(list(twod6.values())[i:])
        print(int(list(twod6.keys())[i]), k)
        muffins.append(k)
    print(mean(muffins[5:]))

if __name__ == "__main__":
    print(len(WEATHER_ROLLS))
    simRolls()