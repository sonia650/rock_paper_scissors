import random
from ascii import simpson

def computer_random():
    c = ["rock", "paper", "scissors"]
    computer = random.choice(c)
    return computer


def player_moves():
    print ("Please play one of the following")
    player1 = raw_input(" Rock, Paper, Scissors:\n").lower()
    return player1 


def find_winner(player1,computer):
    if player1 == "scissors":
        if computer == "scissors":
            return "Computer picked scissors too!\nLOL, Tie!"
        elif computer == "rock":
            return "Computer chose rock.....\n YOU LOSE BABY"
        elif computer == "paper":
            return "Computer chose paper....\nYOU WIN BABY!"
        else:
            return "DO YOU EVEN KNOW HOW TO PLAY?"

    elif player1 == "paper":
        if computer == "paper":
            return "Seriously, It\'s a Tie!"
        elif computer == "rock":
            return "Computer chose rock.....YOU WIN BOO"
        elif computer == "scissors":
            return "Computer chose scissors, You LOSE!"
        else: 
            return "wtf is going on?"

    elif player1 == "rock":
        if computer == "rock":
            return "Computer picked Rock Too! UGH, Tie!"
        elif computer == "paper":
            return "Computer chose paper....YOU\'RE A LOSER"
        elif computer == "scissors":
            return "Computer chose scissors, You win"
        else: 
            return "WTF ARE YOU DOING"

def options():
      print "Please choose from the following:"
      print "1 - Play Again"
      print "2 - Quit"
      choices = int(raw_input())
      return choices


def main():
    raw_input("\nAre you ready to play?\n")
    print simpson 
    raw_input('''\nWe're going to play Rock, Paper, Scissors\n 
                    \nSimpsons Edition\n
                    PRESS ENTER TO PLAY''')   
  
    print '''\nRULES OF THE GAME:
    
    \n1)Rock Breaks Scissors, 
    \n2)Scissors Cuts Paper, 
    \n3)Paper Covers Rock\n'''

    choices = 1
    while True:
     if choices == 1: 
        player1_move = player_moves()
        computer_move = computer_random()
        print find_winner(player1_move,computer_move)
        
     elif choices == 2:
         print "BYE FELICIA!"
         break
     choices = options()

    

    
    

 
if __name__ == '__main__':
    main()
