import random

from prettytable import PrettyTable

myTeam = []
opponents1 = []
opps2 = []
opps3 = []
opps4 = []
opps5 = []
opps6 = []
opps7 = []
allPlayers = ["Virat Kohli", "MS Dhoni", "Rohit Sharma", "Jasprit Bumrah", "David Warner", "Avesh Khan", "Adam Zampa",
              "Cameron Green", "Rachin Ravindra", "Rajat Patidar", "Faf Du Plessis", "Mitchell Starc", "Pat Cummins",
              "Nathan Lyon", "Hardik Pandya", "Will Jacks", "Mohammed Siraj", "Yashasvi Jaiswal", "Kane Williamson",
              "Sam Curran", "Tom Curran", "Chris Gayle", "Sachin Tendulkar", "Wanindu Hasaranga", "KL Rahul",
              "Rishabh Pant", "Andre Russell", "Tim Southee", "Rashid Khan", "Ben Stokes", "Trent Boult", "Joe Root",
              "Kagiso Rabada", "Jonny Bairstow", "Jos Buttler", "Jason Holder", "Quinton de Kock", "Babar Azam",
              "Shai Hope", "Martin Guptill"]
myRatings = []
opponentRatings = []
allTeams = []
myPurse = 0
purse1 = 0
purse2 = 0
purse3 = 0
purse4 = 0
purse5 = 0
purse6 = 0
purse7 = 0
allPurses = [myPurse, purse1, purse2, purse3, purse4, purse5, purse6, purse7]


class Players:
    def __init__(self, name, speed, agility, strength, technique, awareness, endurance, team):
        self.name = name
        self.speed = speed
        self.agility = agility
        self.strength = strength
        self.technique = technique
        self.awareness = awareness
        self.endurance = endurance
        self.team = team

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def getAgility(self):
        return self.agility

    def getStrength(self):
        return self.strength

    def getTechnique(self):
        return self.technique

    def getAwareness(self):
        return self.awareness

    def getTeam(self):
        return self.team

    def getEndurance(self):
        return self.endurance

    def getRating(self):
        return round((self.speed + self.strength + self.agility * self.technique/(self.awareness + self.endurance)))

    def changeSpeed(self, amt):
        self.speed += amt

    def changeAgility(self, amt):
        self.agility += amt

    def changeStrength(self, amt):
        self.strength += amt

    def changeTechnique(self, amt):
        self.technique += amt

    def changeAwareness(self, amt):
        self.awareness += amt

    def changeEndurance(self, amt):
        self.endurance += amt


def makeYourTeam():
    global myTeam
    global allPlayers
    for x in range(5):
        myPlayers = random.choice(allPlayers)
        myTeam.append(Players(myPlayers, random.randint(70, 99), random.randint(70, 99), random.randint(70, 99),
                              random.randint(70, 99), random.randint(70, 99), random.randint(70, 99), myTeam))
        allPlayers.remove(myPlayers)


def performance(team):
    global myPurse
    global allTeams
    myPerformance = 0
    for x in team:
        myPerformance += x.getRating()
    print("Performance: ", myPerformance)
    allTeams.append(myPerformance)


def pickWinner():
    global myPurse
    global purse1
    global purse2
    global purse3
    global purse4
    global purse5
    global purse6
    global purse7
    global allTeams
    global allPurses
    winner = max(allTeams)
    if winner == allTeams[0]:
        print("You Win!")
        myPurse += 10
        purse1 += 5
        purse2 += 5
        purse3 += 5
        purse4 += 5
        purse5 += 5
        purse6 += 5
        purse7 += 5
    elif winner == allTeams[1]:
        print("Opponent 1 wins!")
        myPurse += 5
        purse1 += 10
        purse2 += 5
        purse3 += 5
        purse4 += 5
        purse5 += 5
        purse6 += 5
        purse7 += 5
    elif winner == allTeams[2]:
        print("Opponent 2 wins!")
        myPurse += 5
        purse1 += 5
        purse2 += 10
        purse3 += 5
        purse4 += 5
        purse5 += 5
        purse6 += 5
        purse7 += 5
    elif winner == allTeams[3]:
        print("Opponent 3 wins!")
        myPurse += 5
        purse1 += 5
        purse2 += 5
        purse3 += 10
        purse4 += 5
        purse5 += 5
        purse6 += 5
        purse7 += 5
    elif winner == allTeams[4]:
        print("Opponent 4 wins!")
        myPurse += 5
        purse1 += 5
        purse2 += 5
        purse3 += 5
        purse4 += 10
        purse5 += 5
        purse6 += 5
        purse7 += 5
    elif winner == allTeams[5]:
        print("Opponent 5 wins!")
        myPurse += 5
        purse1 += 5
        purse2 += 5
        purse3 += 5
        purse4 += 5
        purse5 += 10
        purse6 += 5
        purse7 += 5
    elif winner == allTeams[6]:
        print("Opponent 6 wins!")
        myPurse += 5
        purse1 += 5
        purse2 += 5
        purse3 += 5
        purse4 += 5
        purse5 += 5
        purse6 += 10
        purse7 += 5
    elif winner == allTeams[7]:
        print("Opponent 7 wins!")
        myPurse += 5
        purse1 += 5
        purse2 += 5
        purse3 += 5
        purse4 += 5
        purse5 += 5
        purse6 += 5
        purse7 += 10


def makeOpps(team):
    global allPlayers
    for x in range(5):
        myPlayers = random.choice(allPlayers)
        team.append(Players(myPlayers, random.randint(70, 99), random.randint(70, 99), random.randint(70, 99),
                            random.randint(70, 99), random.randint(70, 99), random.randint(70, 99), team))
        allPlayers.remove(myPlayers)


def improveMyStats():
    global myPurse
    stat = int(input("What stat do you want to improve Speed(1), Agility(2), Strength(3), Technique (4), Awareness "
                     "(5), or Endurance (6)"))
    print("Which player's stats do you want to improve?")
    print(myTeam[0].getName(), "(1)", myTeam[1].getName(), "(2)", myTeam[2].getName(), "(3)", myTeam[3].getName(),
          "(4)", myTeam[4].getName(), "(5)")
    whichPlayer = int(input())
    if stat == 1 and myPurse >= 15:
        myTeam[whichPlayer - 1].changeSpeed(1)
        myPurse -= 15
    elif stat == 2 and myPurse >= 5:
        myTeam[whichPlayer - 1].changeAgility(1)
        myPurse -= 5
    elif stat == 3 and myPurse >= 10:
        myTeam[whichPlayer - 1].changeStrength(1)
        myPurse -= 10
    elif stat == 4 and myPurse >= 10:
        myTeam[whichPlayer - 1].changeTechnique(1)
        myPurse -= 10
    elif stat == 5 and myPurse >= 5:
        myTeam[whichPlayer - 1].changeAwareness(1)
        myPurse -= 5
    elif stat == 6 and myPurse >= 10:
        myTeam[whichPlayer - 1].changeEndurance(1)
        myPurse -= 5
    else:
        print("You can't improve stats because you don't have enough money")
        print("Play more games to try to earn more money")


def ImproveOppStats(team, purse):
    stat = random.randint(1, 5)
    whichPlayer = random.randint(0, 4)
    if stat == 1 and purse >= 15:
        team[whichPlayer].changeSpeed(1)
        purse -= 15
        print("The other team improved the speed of", team[whichPlayer].getName())
    elif stat == 2 and purse >= 5:
        team[whichPlayer].changeAgility(1)
        purse -= 5
        print("The other team improved the agility of", team[whichPlayer].getName())
    elif stat == 3 and purse >= 10:
        team[whichPlayer].changeStrength(1)
        purse -= 10
        print("The other team improved the strength of", team[whichPlayer].getName())
    elif stat == 4 and purse >= 10:
        team[whichPlayer].changeTechnique(1)
        purse -= 10
        print("The other team improved the technique of", team[whichPlayer].getName())
    elif stat == 5 and purse >= 5:
        team[whichPlayer].changeAwareness(1)
        purse -= 5
        print("The other team improved the awareness of", team[whichPlayer].getName())
    elif stat == 6 and purse >= 10:
        team[whichPlayer].changeEndurance(1)
        purse -= 10
        print("The other team improved the endurance of", team[whichPlayer].getName())


def randomEvents(pickTeam):
    probability = random.randint(1, 25)
    whichPlayer = random.randint(0, 4)
    if probability == 5:
        print(pickTeam[whichPlayer].getName(), "had a hamstring injury, so his speed was lowered by 2")
        pickTeam[whichPlayer].changeSpeed(-2)
    elif probability == 7:
        print(pickTeam[whichPlayer].getName(), "got the flu, so his agility was lowered by 2")
        pickTeam[whichPlayer].changeAgility(-2)
    elif probability == 16:
        print(pickTeam[whichPlayer].getName(), "got a concussion, so his awareness was lowered by 2")
        pickTeam[whichPlayer].changeAwareness(-2)


def printTeams():
    global myRatings
    opponent1_table = PrettyTable(["Name", "Speed", "Agility", "Strength", "Technique", "Awareness", "Rating"])
    opps2_table = PrettyTable(["Name", "Speed", "Agility", "Strength", "Technique", "Awareness", "Rating"])
    opps3_table = PrettyTable(["Name", "Speed", "Agility", "Strength", "Technique", "Awareness", "Rating"])
    opps4_table = PrettyTable(["Name", "Speed", "Agility", "Strength", "Technique", "Awareness", "Rating"])
    opps5_table = PrettyTable(["Name", "Speed", "Agility", "Strength", "Technique", "Awareness", "Rating"])
    opps6_table = PrettyTable(["Name", "Speed", "Agility", "Strength", "Technique", "Awareness", "Rating"])
    opps7_table = PrettyTable(["Name", "Speed", "Agility", "Strength", "Technique", "Awareness", "Rating"])
    my_table = PrettyTable(["Name", "Speed", "Agility", "Strength", "Technique", "Awareness", "Rating"])
    for x in opponents1:
        opponent1_table.add_row(
            [x.getName(), x.getSpeed(), x.getAgility(), x.getStrength(), x.getTechnique(), x.getAwareness(),
             x.getRating()])
    for x in opps2:
        opps2_table.add_row(
            [x.getName(), x.getSpeed(), x.getAgility(), x.getStrength(), x.getTechnique(), x.getAwareness(),
             x.getRating()])
    for x in opps3:
        opps3_table.add_row(
            [x.getName(), x.getSpeed(), x.getAgility(), x.getStrength(), x.getTechnique(), x.getAwareness(),
             x.getRating()])
    for x in opps4:
        opps4_table.add_row(
            [x.getName(), x.getSpeed(), x.getAgility(), x.getStrength(), x.getTechnique(), x.getAwareness(),
             x.getRating()])
    for x in opps5:
        opps5_table.add_row(
            [x.getName(), x.getSpeed(), x.getAgility(), x.getStrength(), x.getTechnique(), x.getAwareness(),
             x.getRating()])
    for x in opps6:
        opps6_table.add_row(
            [x.getName(), x.getSpeed(), x.getAgility(), x.getStrength(), x.getTechnique(), x.getAwareness(),
             x.getRating()])
    for x in opps7:
        opps7_table.add_row(
            [x.getName(), x.getSpeed(), x.getAgility(), x.getStrength(), x.getTechnique(), x.getAwareness(),
             x.getRating()])

    for y in myTeam:
        my_table.add_row(
            [y.getName(), y.getSpeed(), y.getAgility(), y.getStrength(), y.getTechnique(), y.getAwareness(),
             y.getRating()])

    print("My Team: ")
    print(my_table)
    print("Opponent 1 Team: ")
    print(opponent1_table)
    print("Opponent 2 Team: ")
    print(opps2_table)
    print("Opponent 3 Team: ")
    print(opps3_table)
    print("Opponent 4 Team: ")
    print(opps4_table)
    print("Opponent 5 Team: ")
    print(opps5_table)
    print("Opponent 6 Team: ")
    print(opps6_table)
    print("Opponent 7 Team: ")
    print(opps7_table)


def changeOpps(team):
    global allPlayers
    global opponents1
    for x in team:
        allPlayers.append(x.getName())
    team.clear()


def changeMyTeam():
    global allPlayers
    global opponents1
    for x in myTeam:
        allPlayers.append(x.getName())
    myTeam.clear()


def main():
    global myPurse
    global purse1
    global purse2
    global purse3
    global purse4
    global purse5
    global purse6
    global purse7
    global opponents1
    global myTeam
    done = False
    makeYourTeam()
    makeOpps(opponents1)
    makeOpps(opps2)
    makeOpps(opps3)
    makeOpps(opps4)
    makeOpps(opps5)
    makeOpps(opps6)
    makeOpps(opps7)
    while not done:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        choice = int(input("Change Opponent ratings(1), Play a Game (2), Change Your Team's ratings(3), View Purse(4),"
                           " Improve Stats(5), View Teams(6), Done? (7)"))
        if choice == 1:
            changeOpps(opponents1)
            changeOpps(opps2)
            changeOpps(opps3)
            changeOpps(opps4)
            changeOpps(opps5)
            changeOpps(opps6)
            changeOpps(opps7)
            makeOpps(opponents1)
            makeOpps(opps2)
            makeOpps(opps3)
            makeOpps(opps4)
            makeOpps(opps5)
            makeOpps(opps6)
            makeOpps(opps7)
        elif choice == 2:
            printTeams()
            performance(opponents1)
            performance(opps2)
            performance(opps3)
            performance(opps4)
            performance(opps5)
            performance(opps6)
            performance(opps7)
            randomEvents(myTeam)
            randomEvents(opponents1)
            randomEvents(opps2)
            randomEvents(opps3)
            randomEvents(opps4)
            randomEvents(opps5)
            randomEvents(opps6)
            randomEvents(opps7)
            pickWinner()
        elif choice == 3:
            changeMyTeam()
            makeYourTeam()
        elif choice == 4:
            print("My Purse: $", myPurse)
        elif choice == 5:
            improveMyStats()
            ImproveOppStats(opponents1, purse1)
            ImproveOppStats(opps2, purse2)
            ImproveOppStats(opps3, purse3)
            ImproveOppStats(opps4, purse4)
            ImproveOppStats(opps5, purse5)
            ImproveOppStats(opps6, purse6)
            ImproveOppStats(opps7, purse7)
            printTeams()
            myRatings.clear()
            opponentRatings.clear()
        elif choice == 6:
            printTeams()
        elif choice == 7:
            done = True


main()
