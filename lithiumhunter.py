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

import curses
import random

"""
  print "Welcome to Lithium Hunter"
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

"""

MAX_LITHIUMS = 468

def retryOrQuit(window, y=1, x=2):
  while True:
    window.addstr(y, x, "(R)etry or (Q)uit ?")
    key = window.getkey()
    if key in "rR":
      return True
    elif key in "qQ":
      return False
    else:
      curses.flash()

def main(window):
  
  maxY, maxX = window.getmaxyx()
  
  titleWin = window.derwin(8, maxX, 0, 0)
  
  titleCenter = int( (maxX-51)/2 )
  titleWin.addstr(0, titleCenter, "       _____ _______ _     _ _____ _     _ _______")
  titleWin.addstr(1, titleCenter, "|        |      |    |_____|   |   |     | |  |  |")
  titleWin.addstr(2, titleCenter, "|_____ __|__    |    |     | __|__ |_____| |  |  |")
  titleWin.addstr(3, titleCenter, "  _     _ _     _ __   _ _______ _______  ______  ")
  titleWin.addstr(4, titleCenter, "  |_____| |     | | \  |    |    |______ |_____/  ")
  titleWin.addstr(5, titleCenter, "  |     | |_____| |  \_|    |    |______ |    \_  ")
  
  titleWin.refresh()
  
  inputWin = window.derwin(2, maxX, 10, 0)
  graphWin = window.derwin(3, maxX, 13, 0)
  
  lithiums = 0
  
  while True:
    
    # get the input
    inputWin.addstr(1, 2, "Type an 'l' to mine lithium")
    inputWin.refresh()
    key = inputWin.getkey()
    
    # error check
    if key in "lL":
      pass
    elif key in "EeQq":
      return
    else:
      inputWin.addstr(0, 1, "This game is about lithium. can't get lithium without typing an 'l' can you? Try again.")
      continue
    
    # game
    inputWin.addstr(0, 0, " "*maxX)
    lithiums += int( random.uniform(1,20) )
    
    # clear screen
    inputWin.clear()
    
    if lithiums > MAX_LITHIUMS:
      inputWin.addstr(0, 1, "You have woken up in your bed with no lithiums. You lose")
      if retryOrQuit(inputWin):
        lithiums = 0
        inputWin.clear()
      else:
        return
    elif lithiums == MAX_LITHIUMS:
      inputWin.addstr(0, 1, "You have the best amount of lithium! YOU WIN!")
      if retryOrQuit(inputWin):
        lithiums = 0
        inputWin.clear()
      else:
        return
    else:
      inputWin.addstr(0, 1, "You have {0} lithiums".format(lithiums) )
    
    ## draw progree bar
    graphWin.clear()
    graphWin.border(0)
    graphWin.hline(1, 1, curses.ACS_BLOCK, int(lithiums * ((maxX-2)/(MAX_LITHIUMS+0.0))) )
    graphWin.refresh()
  
  inputWin.getkey()
    
if __name__ == "__main__":
  curses.wrapper(main)
  print
  print "Bai bai! Happy lorgyhumming!"
  print "Concept by Colin Bramwell, Alexander Robinson and Tom Mckenna"
  print "Coded by Callum Stott and Guy Taylor"
  print

