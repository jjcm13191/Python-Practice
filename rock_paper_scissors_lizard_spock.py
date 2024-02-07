#rock=1,paper=2,scissors=3,spock=4,lizard=5
import random
def name_to_number(name):
    if name == "rock": 
        return 1
    elif name == "paper": 
        return 2
    elif name == "scissors": 
        return 3
    elif name == "Spock": 
        return 4
    elif name == "lizard":
        return 5
    else:
        return "Wrong"
    
def number_to_name(number):
    if number == 1: 
        return "rock"
    elif number == 2: 
        return "paper"
    elif number == 3: 
        return "scissors"
    elif number == 4: 
        return "Spock"
    elif number == 5:
        return "lizard"
    else:
        return "Wrong"

computer_choice = random.randrange(1, 6)
 
def rpsls(a):
    print
    print "Player chooses " + a
    print "Computer chooses " + number_to_name(computer_choice)
 
    if a == "rock" and (computer_choice == 3 or computer_choice == 5):
        print "Player wins!"
    elif a == "paper" and (computer_choice == 1 or computer_choice == 4):
        print "Player wins!"
    elif a == "scissors" and (computer_choice == 2 or computer_choice == 5):
        print "Player wins!"    
    elif a == "Spock" and (computer_choice == 1 or computer_choice == 3):
        print "Player wins!"  
    elif a == "lizard" and (computer_choice == 2 or computer_choice == 4):
        print "Player wins!"  
        
    elif a == "rock" and (computer_choice == 2 or computer_choice == 4):
        print "Computer wins!"
    elif a == "paper" and (computer_choice == 3 or computer_choice == 5):
        print "Computer wins!"
    elif a == "scissors" and (computer_choice == 1 or computer_choice == 4):
        print "Computer wins!"
    elif a == "Spock" and (computer_choice == 2 or computer_choice == 5):
        print "Computer wins!"
    elif a == "lizard" and (computer_choice == 1 or computer_choice == 3):
        print "Computer wins!"
    else:
        print "Player and Computer tie!"
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
