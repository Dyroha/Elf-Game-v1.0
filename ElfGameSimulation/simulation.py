import random
import math

ELF_COST = 25

class Character:
    def __init__(self):
        self.startingElves = 10
        self.elves = self.startingElves
        self.money = 0
        self.run_earnings = []
        self.level = 1

    def __repr__(self):
        return type(self).__name__ + ", " + str(self.money) + ", elves = " + str(self.elves)
    
    def buyElves(self, day):
        #calculate how much money an elf will make for the days it'll be working
        daysLeft = 24-day
        elfmakes = daysLeft * 7
        elfprofit = elfmakes - ELF_COST

        if elfprofit > 0:
            maxElves = math.floor(self.money / ELF_COST)
            cost = maxElves * ELF_COST
            self.money -= cost
            self.elves += maxElves

    def levelUp(self):
        self.level += 1
    
    def nextRun(self):
        self.run_earnings.append(self.money)
        self.money = 0
        self.elves = self.startingElves
        self.level = 1

    def getAverageEarnings(self):
        return sum(self.run_earnings) / len(self.run_earnings)
    
    def rollDice(self, number = 2, sides = 6, take = 2):
        dice = [random.randint(1,sides) for x in range(number)]
        dice = sorted(dice)
        total = sum(dice[:take+1])
        return total

    def assignElves(self, weather):
        #default all in nearby wood
        self.money += self.elves * self.rollDice()
    
    def reset(self):
        self.nextRun()
        self.run_earnings = []
    
'''
    Specific Characters:
'''

class Lumberjack(Character):
    def __init__(self):
        Character.__init__(self)
        self.startingElves = 6
        self.elves = self.startingElves
    
    def buyElves(self, day):
        #calculate how much money an elf will make for the days it'll be working
        daysLeft = 24-day
        elfmakes = daysLeft * (8.46 if self.level < 3 else 9.34)
        elfprofit = elfmakes - ELF_COST

        if elfprofit > 0:
            maxElves = math.floor(self.money / ELF_COST)
            cost = maxElves * ELF_COST
            self.money -= cost
            self.elves += maxElves

    def rollDice(self):
        if self.level < 3:
            return super().rollDice(3,6,2)
        else:
            return super().rollDice(4,6,2)
        
class OneManBand(Character):
    def __init__(self):
        Character.__init__(self)
        self.startingElves = 10
        self.elves = self.startingElves

    def assignElves(self, weather):
        #default an additional 1 in the Boreal Forest weather doesn't matter
        e = self.elves - 1
        if self.level == 2:
            self.money += 10 + self.rollDice()
            e -= 1
        elif self.level == 3:
            self.money += 2 * (30 + self.rollDice())
            self.money += 2 * (10 + self.rollDice())
            e -= 4
        self.money += 10 + self.rollDice()
        self.money += e * self.rollDice()
        
class Cosy(Character):
    def __init__(self):
        Character.__init__(self)
        self.startingElves = 5
        self.elves = self.startingElves

    def buyElves(self, day):
        #calculate how much money an elf will make for the days it'll be working
        daysLeft = 24-day
        elfmakes = daysLeft * (9.8 if self.level < 3 else 10.97)
        elfprofit = elfmakes - ELF_COST

        if elfprofit > 0:
            maxElves = math.floor(self.money / ELF_COST)
            cost = maxElves * ELF_COST
            self.money -= cost
            self.elves += maxElves

    def assignElves(self, weather):
        #default all sent to nearby forest
        if self.level == 3:
            self.money += self.elves * self.rollDice(number=3, sides=8)
        else:
            self.money += self.elves * self.rollDice(sides=8)

class WinterWitch(Character):
    def __init__(self):
        Character.__init__(self)
        self.startingElves = 13
        self.elves = self.startingElves
        self.wintermagic = 0
        self.zombies = 0

    def nextRun(self):
        Character.nextRun(self)
        self.wintermagic = 0
        self.zombies = 0

    def assignElves(self, weather):
        #default assign 1 to Taiga
        e = self.elves
        if e > 1 and self.level > 1:
            e -= 1
            if weather:
                self.money += 30 + self.rollDice()
            else:
                self.elves -= 1
                #resurrect immediately if possible
                if self.wintermagic > 0:
                    self.zombies += 1
                    # print("made zombie")
                    self.wintermagic -= 1
                self.wintermagic += 2

        self.money += self.rollDice() * e + self.rollDice() * self.zombies


class ReindeerWrangler(Character):
    rcost = 50

    def assignElves(self, weather):
        rmoney = 0
        if self.money > self.rcost and ((self.level == 1 and self.rcost < (17 * 4)) or (self.level == 2 and self.rcost < (17 * 6)) or (self.level == 3 and self.rcost < (37 * 9))):
            self.money -= self.rcost
            self.rcost += 5
            if self.level == 1:
                rmoney = 4 * (10 + self.rollDice())
            elif self.level == 2:
                rmoney = 6 * (10 + self.rollDice())
            else:
                rmoney = 9 * (30 + self.rollDice())
        
        self.money += self.elves * self.rollDice() + rmoney
    

    def nextRun(self):
        Character.nextRun(self)
        self.rcost = 50

class Meteorologist(Character):
    COST = 7
    def __init__(self):
        Character.__init__(self)
        self.abilityCost = self.COST
        self.predictionpoints = 0
    
    def assignElves(self, weather):
        # print(self.predictionpoints)
        if weather:
            self.predictionpoints += 1

        if not weather and self.predictionpoints >= self.abilityCost and self.level > 1:
            self.predictionpoints -= self.abilityCost
            self.money += self.elves * (30 + self.rollDice())
            self.abilityCost -= 1
        elif not weather:
            if self.predictionpoints >= 2 and self.level < 3:
                self.predictionpoints -= 2
                self.abilityCost -= 1
                self.predictionpoints += 1
                # print("used", self.abilityCost)
            self.money += self.elves * self.rollDice()
        else:
            self.money += self.elves * self.rollDice()

    def nextRun(self):
        Character.nextRun(self)
        self.predictionpoints = 0
        self.abilityCost = self.COST


CARDS = {
    1: (0, "The Fool", "money", lambda elf: - elf.elves * 17),
    2: (2.4, "The Magician", "money", lambda elf: elf.rollDice() * elf.elves * 2),
    3: (4.5,"The High Priestess", "money", lambda elf: elf.rollDice() * (elf.elves-10) + (30 + elf.rollDice()) * 10),
    4: (10,"The Empress", "elves", lambda : 10),
    5: (0, "THe Emperor", "nothing", lambda : None),
    6: (2, "The Hierophant", "money", lambda elf: 10 * elf.elves),
    7: (7, "The Lovers", "elves", lambda: 2),
    8: (2.5, "The Chariot", "money", lambda elf: (elf.rollDice()+10) * 9),
    9: (5, "Strength", "money", lambda elf: 10 * elf.elves),
    10: (0, "The Hermit", "nothing", lambda : None),
    11: (0, "Wheel of Fortune", "money", lambda elf: 1000 if random.random() > 0.5 else -500),
    12: (7.5, "Justice", "all", {"elves":2, "money":100}),
    13: (6, "The Hanged Man", "money", lambda elf: (10 + elf.rollDice()) * elf.elves),
    14: (-1,"Death", "elves", lambda : -5),
    15: (4, "Temperance", "money", lambda elf: (10 + elf.rollDice()) * elf.elves),
    16: (0, "The Devil", "nothing", lambda : None),
    17: (-1, "The Tower", "nothing", lambda : None),
    18: (6, "The Star", "money", lambda elf: 30 * elf.elves),
    19: (0, "The Moon", "nothing", lambda : None),
    20: (0, "The Sun", "nothing", lambda : None),
    21: (0, "The World", "nothing", lambda : None)
}

class Mystic(Character):
    def __init__(self):
        Character.__init__(self)
        self.cardsPulled = []

    def levelUp(self):
        Character.levelUp(self)
        self.pullCards()

    def pullCards(self):
        card1 = random.choice(list(CARDS.values()))
        card2 = random.choice(list(CARDS.values()))
        while True:
            good = True
            if card1 in self.cardsPulled:
                card1 = random.choice(list(CARDS.values()))
                good = False
            if card2 in self.cardsPulled or card1 == card2:
                card2 = random.choice(list(CARDS.values()))
                good = False

            if good:
                break
        
        cardUsed = 0
        #compare cards
        if card1[0] == -1:
            self.useCard(card1)
            cardUsed += 1

        if card2[0] == -1:
            self.useCard(card2)
            cardUsed += 2
        
        if card1[0] > card2[0] and cardUsed not in (1,3):
            self.useCard(card1)
        elif cardUsed not in (2,3):
            self.useCard(card2)
        
        #add both to cardsPulled
        self.cardsPulled.append(card1)
        self.cardsPulled.append(card2)

    def useCard(self, card):
        if card[2] == "money":
            self.money += card[3](self)
        elif card[2] == "elves":
            self.elves += card[3]()
        elif card[2] == "all":
            self.elves += card[3]["elves"]
            self.money += card[3]["money"]

    def nextRun(self):
        Character.nextRun(self)
        self.cardsPulled = []
        
class Simulation:
    day = 0
    lastday = 24

    def __init__(self, shopdays, characters):
        self.characters = characters
        self.leveldays = [7,14]
        self.shopdays = shopdays

    def runSimulation(self, runs):
        for i in range(runs):
            for j in range(self.lastday):
                weather = self.rollWeather()
                for c in self.characters:
                    if j in self.shopdays:
                        c.buyElves(j)
                    if j in self.leveldays:
                        c.levelUp()
                    #get money if good weather
                    c.assignElves(weather)
                # print(j, [x for x in self.characters])
            
            self.nextRun()

        return self.characters
    
    def rollWeather(self):
        return random.random() > 0.7
    
    def nextRun(self):
        for c in self.characters:
            c.nextRun()

def resetElves(elves):
    for elf in elves:
        elf.reset()

if __name__ == "__main__":
    elves = [Character(), Lumberjack(), OneManBand(), Cosy(), WinterWitch(), ReindeerWrangler(), Meteorologist(), Mystic()]
    sim = Simulation([7,14,21], elves)
    print([(type(x).__name__, x.getAverageEarnings()) for x in sim.runSimulation(1)])
    # resetElves(elves)