'''Rock, Paper, knife Minigame...

Display: Welcome to the game prompt>, "Choose your weapon!"

1. Get user input - user chooses(types) either 'rock', 'paper' or 'knife'
    # player_turn = this needs if elif else input check - user can type rock, Rock, or R or r etc
2. Program assigns 'its move' i.e randomly picks 1 of the 3 options (r,p or s)
    # cpu_choice = B # "random choice"

3. Program COMPARES the two results (calculation/comparison operator) using IF ELSE statement (function)
4. Display 'Win, Lose or Draw' Result (based on defined rules) print result

Outcomes: 'Player wins', 'Player loses', 'CPU wins', 'CPU loses', or 'DRAW'
PoI: 'Player Wins' == 'CPU Loses' and 'Player Loses' == 'CPU Wins'

TODO:
- replace all globals with func attributes
-

'''
import random
from random import choice
import sys
import time
# init sound and timer modules
import rpk_sounds as sm
import bam_intro as bam
import ktimer as kt
# flash text!
from termcolor import colored, cprint


# globals (how do I avoid using them again??) - add them as funct attr (cpu_turn.cpu_weapon)
weapons = ["rock", "paper", "knife"]
cpu_weapon = ''
user_weapon = ''
round = 1
score = 0
# last_chosen = str()
# switch = 0

#print("last_chosen:", last_chosen)

def result():
    # blast
    global cpu_weapon
    global user_weapon
    global score
    play_again = True

    # outcomes
    if play_again:
        # DRAW
        if user_weapon == cpu_weapon:
            sm.insert_coin()
            print("DRAW! Try again friend!")
            time.sleep(0.5)
            print("Score:",score)
        # WIN 1
        elif user_weapon == "paper" and cpu_weapon == "rock":
            sm.peak_up()
            print("Paper wrapped Rock! YOU WIN!")
            time.sleep(0.5)
            #sm.life_up()
            score = score + 10
            sm.one_up()
            print("Score:",score)
        # WIN 2
        elif user_weapon == "knife" and cpu_weapon == "paper":
            sm.peak_up()
            print("knife stabbed Paper! YOU WIN!")
            score = score + 10
            time.sleep(0.5)
            #sm.one_up()
            sm.life_up()
            print("Score:",score)
        # WIN 3
        elif user_weapon == "rock" and cpu_weapon == "knife":
            sm.peak_up()
            print("Rock blunted knife! YOU WIN!")
            score = score + 10
            time.sleep(0.5)
            #sm.one_up()
            sm.life_up()
            print("Score:",score)
        # LOSE 1
        elif user_weapon == "rock" and cpu_weapon == "paper":
            sm.lose_up()
            print("Paper wrapped Rock! YOU LOSE!")
            score = 0
            print("Score:",score)
        # LOSE 2
        elif user_weapon == "paper" and cpu_weapon == "knife":
            sm.lose_up()
            print("knife stabbed Paper! YOU LOSE!")
            score = 0
            print("Score:",score)
        # LOSE 3
        elif user_weapon == "knife" and cpu_weapon == "rock":
            sm.lose_up()
            print("Rock blunted knife! YOU LOSE!")
            score = 0
            print("Score:",score)

    # play_again?
    play_again = input("\nYou wanna play some more?!! (y or n): ")
    # conditional
    if play_again == 'y':
        # play again
        sm.shell_up()
        #global last_chosen
        global round
        round += 1
        #print('last_chosen:', last_chosen)
        new_game()
    else:
        # quit
        sm.gong_up()
        print("OK, maybe next time!")
        time.sleep(2)
        sys.exit()

def battle_time():
    print("Battle starts in: ")
    # countdown music?
    #sm.countdown()
    kt.kart_timer()
    time.sleep(1)

    global cpu_weapon, user_weapon
    cprint("\n<<< BATTLE RESULTS IN!!! >>>\n", 'green')
    #print("\n<<< BATTLE RESULTS IN!!! >>>\n")
    print("CPU chose:",cpu_weapon)
    print("PLAYER chose:",user_weapon,'\n')
    time.sleep(0.5)
    result()

# The Players turn
def player_turn():
    # player up
    #sm.player_up()
    sm.gong_up()
    time.sleep(0.5)
    # Set user_choice to empty string (lower case)
    user_choice = str().lower()

    while user_choice not in ["rock", "paper", "knife"]: # 'r', 'p', 'k' ?

        user_choice = input("Choose your weapon: ")
        # if word == True
        if (user_choice == "rock"):
            sm.rock_up()
            #sm.punch_up()
            #return data[word]
            print("You selected Rock.")
            time.sleep(0.8)
            # if selected - continue to final else
            continue

        elif (user_choice == "paper"):
            sm.paper_up()
            #sm.punch_up()
            print("You selected Paper.")
            time.sleep(0.8)
            continue

        elif (user_choice == "knife"):
            sm.knife_up()
            #sm.punch_up()
            print("You selected knife.")
            time.sleep(0.8)
            continue

        else:
            # bump
            #sm.bump_up()
            sm.error_up()
            # add a try again input for loop
            print("You have not selected correctly, try again.")
    # final else
    else:
        # stop the loop and finalise players weapon
        global user_weapon
        # assign user_choice as weapon
        user_weapon = user_choice
        time.sleep(0.5)
        #sm.ready_up()
        #sm.gong_up()
        sm.kom_dun()
        #print("OK, you have selected: "+ user_weapon+'\n')
        print("\nthat can mean only one thing...\n")
        time.sleep(2)

        # play battle horn
        #sm.battle_up() NO metallica please
        sm.fight_up()
        #print("BATTLE TIIIIME!!")
        cprint("BATTLE TIIIIME!!", 'red', attrs=['blink'])
        time.sleep(0.5)
        sm.punch_up()
        time.sleep(0.3)
        sm.punch2_up()
        time.sleep(0.5) # 2 if audio (battle_up)

        # call battle
        battle_time()

# CPU picks a weapon!
def cpu_selects():

    global cpu_weapon
    sm.insert_coin()
    # switch the weapon var to a choice
    cpu_weapon = random.choice(weapons)

    #return choice(weapon)
    print("CPU has chosen.\n")
    # DEBUG VERSION
    #print("CPU has chosen.\n"+cpu_weapon +'\n')
    time.sleep(2)
    #switch = 1
    # call Players turn
    player_turn()

# start new game
def start_program():
    # play intro
    sm.coin_up()
    # Intro Welcome to Minigame
    bam.bam_timer()

start_program()

def new_game():
    # global last_chosen
    # print(last_chosen)
    global score
    # global round #??
    # only show the score from round 2? Why?
    if round > 1:
        print("\nScore:",score)

    # allow time for player to read / wait before game starts
    start_pause = ''
    # why cant I get this to work?
    # while start_pause != '':
    start_pause = input("press ENTER to start a new round\n")
    if start_pause in '':
        sm.power_up()
        print("Round",round,"...")
        time.sleep(0.3)
        #print(" >>> START! <<< \n")
        cprint(">>> START! <<< \n", 'green')
        time.sleep(1)
        print("CPU is choosing a weapon ...")
        sm.cpu_up()
        time.sleep(2)
        # call CPU turn
        cpu_selects()
    # else:
    #     # user didn't press enter
    #     sm.error_up()
    #     # add a try again input for loop
    #     print("You have not pressed ENTER you crazy fool, try again.")

new_game()
