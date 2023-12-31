import random
import time

class Boxer():
    def __init__(self):
        # Open the first and last name txt files and get first / last names
        with open("first_names.txt") as f:
            lines = f.readlines()
            first = random.choice(lines).strip("\n") # Strip the first name of any spaces or newlines
            first.strip(" ")
        with open("last_names.txt") as f:
            lines = f.readlines()
            last = random.choice(lines).strip("\n")  # Strip the last name of any spaces or newlines
            last.strip(" ")
        self.name = "".join(first+" "+last)
        self.agility = random.randint(1,33)
        self.power = random.randint(1,33)
        self.endurance = random.randint(1,33)
        self.rank = self.agility+self.power+self.endurance
        
class Player():
    def __init__(self):
        self.name = Player.create_name()
        self.agility = self.create_stat("Agility")
        self.endurance = self.create_stat("Endurance")
        self.power = self.create_stat("Power")
        self.rank = self.agility+self.power+self.endurance
        print(self.name+" ("+str(self.rank)+")")
        
    def create_name():
        confirm = ""
        while confirm != "y":
            name = input("\nBoxer's name? ")
            confirm = input("Is "+name+" right? (y/n) ")
        return name
    
    def create_stat(self, stat):
        s = 0
        while round(s) < 1 or round(s) > 33:
            s = int(input("(1-33) "+ stat+": "))
        return round(s)
        
        
        


def sort_round(bracket):
    bracket = sorted(bracket, key=lambda x: x.rank)
    return bracket


def create_boxers():
    initial = [] 
    size = int(input("How many boxers do you want to auto generate? "))
    # add the size ammount of boxers to the initial bracket
    for i in range(size):
        initial.append(Boxer())
    # Sort the initial list based on the boxers rank
    size = int(input("How many boxers do you want to create manually? "))
    for i in range(size):
        initial.append(Player())
    initial = sort_round(initial)
    return initial

def name_bracket(bracket):
    name_bracket = []
    for player in bracket:
        name_bracket.append(player.name)
    return name_bracket   

def rank_bracket(bracket):
    rank_bracket = []
    for player in bracket:
        rank_bracket.append(player.rank)
    return rank_bracket   


def sim_fight(boxer1, boxer2, sim_speed):
    outcome = random.randint(0,200)+(boxer2.rank-boxer1.rank) # Determine the outcome of the fight, favour towards the better boxer
    if outcome > 100:
        print(str(boxer2.name)+" wins!")
        return boxer2
    else:
        print(str(boxer1.name)+" wins!")
        return boxer1
    
def turn(b1,b2):
    attack = (b1.power+random.randint(0,32))-(b2.agility+random.randint(0,32)) # Function to determine wether they hit or missed
    if attack > 0:
        b2.endurance -= attack
        pre_announcements = ["That one lands from ", "Right hook from ", "Left jab connects by "]
        post_announcements = [" with the uppercut", " connects with that one", " with the one two"]
        if random.randint(0,1) == 0:
            print(pre_announcements[random.randint(0,len(pre_announcements)-1)]+b1.name)
        else:
            print(b1.name+post_announcements[random.randint(0,len(post_announcements)-1)])
        return attack
    else:
        pre_announcements = ["Big dodge by ", "Blocked By ", "Solid read from "]
        post_announcements = [" escapes the hit", " avoids the swing", " gets away"]
        if random.randint(0,1) == 0:
            print(pre_announcements[random.randint(0,len(pre_announcements)-1)]+b2.name)
        else:
            print(b2.name+post_announcements[random.randint(0,len(post_announcements)-1)])

    return 0

def watch_fight(boxer1, boxer2, sim_speed):
    time.sleep(sim_speed)
    # Set the turn to 0 or 1
    t = random.randint(0,1)
    # Loop while they both have endurance left
    while boxer1.endurance > 0 and boxer2.endurance > 0:
        if t == 1:
            turn(boxer1,boxer2) 
            time.sleep(sim_speed)
            t = 2
        else:
            turn(boxer2,boxer1)
            time.sleep(sim_speed)
            t = 1
    if boxer1.endurance > boxer2.endurance:
        print(boxer1.name+" wins!")
        return boxer1
    else:
        print(boxer2.name+" wins!")
        return boxer2
    
def sim_bracket(tournament, sim_speed):
    next_round = [] # Create empty list of opponents for the next round
    if len(tournament)%2 != 0:
        next_round.append(tournament[-1])
        print(str(tournament[-1].name)+" gets a by")
        tournament.pop(-1)
    while len(tournament) > 0: # Loop while there are still fights to be played
        # Print the name and rank of the matchup
        print(str(tournament[0].name) + "(" + str(tournament[0].rank) + ")" " vs " + str(tournament[-1].name) + "(" + str(tournament[-1].rank)+ ")")
        sim_style = input("Watch or Sim? ").lower() # Get the desired sim style and loop while it's invalid
        options = ["sim","watch"]
        while sim_style not in options:  
            print("Invalid Options [ Watch | Sim ]")
            sim_style = input("watch or Sim? ").lower()
        if sim_style == "watch":
            next_round.append(watch_fight(tournament[0],tournament[-1],sim_speed)) # Watch the fight
            time.sleep(sim_speed)
        else:
            next_round.append(sim_fight(tournament[0],tournament[-1],sim_speed)) # Sim the fight
        tournament.pop(0)
        tournament.pop(-1)
        
    return next_round 
    

def main():
    tournament = create_boxers()
    sim_speed = float(input("Simulation Speed? (0 Fastest) "))
    while len(tournament) > 1:
        # List out the current bracket
        print(name_bracket(tournament))
        tournament = sim_bracket(tournament, sim_speed) # Simulate the current round
        input("[Enter to Continue]") # Short pause until resume
        
    
main()
