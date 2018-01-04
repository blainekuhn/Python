"""This is a Rock-Paper-Scissors game"""

from random import randint
from time import sleep

choices = ["R", "P", "S"]
ulost = "You Lost!"
uwin = "You Win!"

c_choice = choices[randint(0,2)]
u_choice = raw_input("Please enter 'R', 'P', or 'S': ").upper()

def get_winner(c, u):
    if u not in choices:
        print "Please enter a valid choice"
        u = raw_input("Please enter 'R', 'P', or 'S': ").upper()
        get_winner(c, u)
    elif c == u:
        print "It's a tie."
        print "The computer also had '%s'." % c
    elif c == "P" and u == "R":
        print ulost
        print "The computer had '%s'." % c
    elif c == "R" and u == "S":
        print ulost
        print "The computer had '%s'." % c
    elif c == "S" and u == "P":
        print ulost
        print "The computer had '%s'." % c
    else:
        print uwin
        print "The computer had '%s'." % c

get_winner(c_choice, u_choice)
