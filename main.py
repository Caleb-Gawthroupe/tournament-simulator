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
        self.rank = random.randint(1,100)
        self.name = "".join(first+" "+last)


def sort_round(bracket):
    bracket = sorted(bracket, key=lambda x: x.rank)
    print(rank_bracket(bracket))
    return bracket


def create_boxers():
    initial = [] 
    size = int(input("How many players are competing? "))
    # add the size ammount of boxers to the initial bracket
    for i in range(size):
        initial.append(Boxer())
    # Sort the initial list based on the boxers rank
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


def fight(boxer1, boxer2, sim_speed):
    print(str(boxer1.name) + "(" + str(boxer1.rank) + ")" " vs " + str(boxer2.name) + "(" + str(boxer2.rank)+ ")")
    time.sleep(sim_speed)
    outcome = random.randint(0,200)+(boxer2.rank-boxer1.rank) # Determine the outcome of the fight, favour towards the better boxer
    if outcome > 100:
        print(str(boxer2.name)+" wins!")
        return boxer2
    else:
        print(str(boxer1.name)+" wins!")
        return boxer1
    
    
def sim_bracket(tournament, sim_speed):
    next_round = [] # Create empty list of opponents for the next round
    if len(tournament)%2 != 0:
        next_round.append(tournament[-1])
        print(str(tournament[-1])+" gets a by")
        tournament.pop(-1)
    while len(tournament) > 0: # Loop while there are still fights to be played
        next_round.append(fight(tournament[0],tournament[-1],sim_speed))
        tournament.pop(0)
        tournament.pop(-1)
        time.sleep(sim_speed)
    return next_round 
    

def main():
    tournament = create_boxers()
    sim_speed = float(input("Simulation Speed? (0 Fastest) "))
    while len(tournament) > 1:
        # List out the current bracket
        print(name_bracket(tournament))
        tournament = sim_bracket(tournament, sim_speed) # Simulate the current round
        
    
main()