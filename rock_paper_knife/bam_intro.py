'''
a BAM timer - adds ROCK! (bam!) PAPER (bam!) KNIFE! (bam!) each second until 0 (of 3)

add boom sound to each

print('\nWelcome to Glitchy\'s:\n > ROCK <\n >> PAPER <<\n >>> KNIFE! <<<\n "The action packed battle game!"')
'''
import sys, time
import pyfiglet
from pyfiglet import Figlet
import rpk_sounds as sm
import rpk_ascii as asc
from termcolor import colored, cprint

#sm.glitchy_up()
sm.presents_up()

def bam_timer():
    #print("\n\r$$$ Glitchy Games Presents: $$$")
    cprint("\n\r$$$ Glitchy Games Presents: $$$\n", 'green')
    time.sleep(1)
    _TIME = 4
    while _TIME > 0:
        m, s = divmod(_TIME, 60)
        h, m = divmod(m, 60)
        m, s = divmod(s, 3600)
        #print(f"\r{int(s)}".rjust(5))
        _TIME -= 1
        time.sleep(1)
        # add each print line (per second)
        if _TIME == 3:
            sm.rock_up()
            #print("\t> ROCK ! <")
            cprint("\t> ROCK ! <", 'cyan')
        elif _TIME == 2:
            sm.paper_up()
            #print("\n\t>> PAPER ! <<")
            cprint("\n\t>> PAPER ! <<", 'yellow')
        elif _TIME == 1:
            sm.knife_up()
            #print("\n\t>>> KNIFE!!! <<<")
            cprint("\n\t>>> KNIFE!!! <<<", 'red')
    else:
        #add ascii
        asc.ascii()
        # show hook line
        sm.chug_up()
        print('\n >> "The action packed BATTLE game! <<"\n')
        #time.sleep(1)
