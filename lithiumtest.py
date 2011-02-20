#! /usr/bin/env python

#   Lithium Hunter

#
#   Copyright (C) 2010  Callum Stott 
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


import random
import sqlite3

#these functions prompt for input at command line and loop until accepted

def proMon(strTr, strTxt, strErr):#accepts only one string
	prompt = raw_input(strTxt + "...")
	while (prompt != strTr):
		print strErr
		prompt = raw_input(strTxt + "...")

def proLs(strLs, strTxt, strErr):#will accept any string from an array of strings, returns accepted input
	prompt = raw_input(strTxt  + "...")
	while (prompt not in strLs):
		print strErr
		prompt = raw_input(strTxt + "...")
	return prompt

#set up db
conn = sqlite3.connect("scores")
c = conn.cursor()
c.execute("Create Table scores (score NUMERIC, name TEXT)")
	
#intro text
print "       _____ _______ _     _ _____ _     _ _______"      
print "|        |      |    |_____|   |   |     | |  |  |"
print "|_____ __|__    |    |     | __|__ |_____| |  |  |"
print "_     _ _     _ __   _ _______ _______  ______"
print "|_____| |     | | \  |    |    |______ |_____/"
print "|     | |_____| |  \_|    |    |______ |    \_"
print ""
print ""


print "Welcome to Lithium Hunter"
print "Concept by Colin Bramwell, Alexander Robinson and Tom Mckenna"
print "Coded by Callum Stott"
print ""

#ask user to start
name = raw_input("Type your name to begin your journey...")

#start game
intro = 0

while (True):
	
	#tutorial
	if (intro == 0):

		print ""
		print "Congratulations! You have entered into the lucrative business of Lithium Mining."
		print "The greatest of all alkali metals."
		print "I am you friendly guide... your... assistant you might say and"
		print "my name is Lalapagaduweewee."
		print "As I'm sure you learnt when you were but a small waffle, lithium" 
		print "mining is all about moderation."
		print "I'll also remind you that as you learnt in kinderarteggfan school, the" 
		print "optimum amount of lithium is 468 lithiums."
		print "Anymore and you will wake up in your bed all vumberscoobed and with" 
		print "no lithium to speak of!"
		print "NOW! PAY ATTENTION!"
		print "To mine lithium simply type in an 'l' to your lithium command" 
		print "terminal sysgerafific..."
		print ""		
		print "Try this now:"	
			
		proMon("l","Type an 'l' to mine lithium","This game is about lithium." +
				"You can't get lithium without typing an 'l' can you? Try again.")
	
		print ""
		print ""
		print "Well done! You are truly a lithium miner."
		print "Now, every time you mine lithium, you will get an amount of lithium." 
		print "This amount will be between hugtry or beecletee."
		print "This of course means you will get somewhere between 1 and 20 lithiums."
		print "REMEMBER:"
		print "If you get more than 468 lithiums, you will wake up in your bed with no lithiums!"
		print "ENJOY!"
		intro = 1

	lithiums = int(0)
	
	#game loop
	while (lithiums < 468):

		proMon("l","Type an 'l' to mine lithium","This game is about lithium." +
			"can't get lithium without typing an 'l' can you? Try again.")

		lithiums = lithiums + int(random.uniform(1,20))
		print "You have " + str(lithiums) + " lithiums"

	if (lithiums == 468):
		print "You have the best amount of lithium! YOU WIN!"
		print ""
		string = "Insert Into scores values ('%d', '%s')" % \
			(468, name)
		c.execute(string)
		conn.commit

	else:
		print "You have woken up in your bed with no lithiums. You lose"
		print ""

	useIn = proLs(["yes","no"],"Would you like to play again?","Type 'yes' or 'no' dumbass!")

	if (useIn == "yes"):
		print ""

	else:	
		print ""
		print "Bai bai! Happy lorgyhumming!"
		break

