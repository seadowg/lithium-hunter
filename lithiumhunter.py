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


class LithiumHunter(object):
    
  MAX_LITHIUMS = 468
  
  def __init__(self, window):
    """ window is the main curses window to draw the CLI """
    # game vars
    self._lithiums = 0
    
    # screen vars
    self._maxY, self._maxX = window.getmaxyx()
    titleWin = window.derwin(8, self._maxX, 0, 0)
    self._inputWin = window.derwin(2, self._maxX, 10, 0)
    self._graphWin = window.derwin(3, self._maxX, 13, 0)
    self._graphColour = 1
    
    # draw the title
    titleCenter = int( (self._maxX-51)/2 )
    titleWin.addstr(0, titleCenter, "       _____ _______ _     _ _____ _     _ _______")
    titleWin.addstr(1, titleCenter, "|        |      |    |_____|   |   |     | |  |  |")
    titleWin.addstr(2, titleCenter, "|_____ __|__    |    |     | __|__ |_____| |  |  |")
    titleWin.addstr(3, titleCenter, "  _     _ _     _ __   _ _______ _______  ______  ")
    titleWin.addstr(4, titleCenter, "  |_____| |     | | \  |    |    |______ |_____/  ")
    titleWin.addstr(5, titleCenter, "  |     | |_____| |  \_|    |    |______ |    \_  ")
    titleWin.addstr(6, titleCenter, "            Welcome to Lithium Hunter             ")
    titleWin.refresh()
  
  def _setGraphColour(self, colour):
    if colour == "red":
      curses.init_pair(self._graphColour, curses.COLOR_RED,     curses.COLOR_BLACK)
    elif colour == "green":
      curses.init_pair(self._graphColour, curses.COLOR_GREEN,   curses.COLOR_BLACK)
    elif colour == "amber":
      curses.init_pair(self._graphColour, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    else:
      raise AttributeError("Invalid colour")
  
  def _retryOrQuit(self, y=1, x=2):
    while True:
      self._inputWin.addstr(y, x, "(R)etry or (Q)uit ?")
      key = self._inputWin.getkey()
      if key in "rR":
        return True
      elif key in "qQ":
        return False
      else:
        curses.flash()
  
  def getName(self):
    #name = raw_input("Type your name to begin your journey...")
    pass
  
  def tutorial(self):
    """
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

  def mainGame(self):
    
    self._lithiums = 0
    self._inputWin.clear()
    self._inputWin.refresh()
    self._graphWin.clear()
    self._graphWin.refresh()
    
    while True:
      
      # get the input
      self._inputWin.addstr(1, 2, "Type an 'l' to mine lithium")
      self._inputWin.refresh()
      key = self._inputWin.getkey()
      
      # error check
      if key in "lL":
        self._lithiums += int( random.uniform(1,20) )
      elif key in "Cc":
        self._lithiums = LithiumHunter.MAX_LITHIUMS
      elif key in "EeQq":
        return False
      else:
        self._inputWin.addstr(0, 1, "This game is about lithium. can't get lithium without typing an 'l' can you? Try again.")
        continue
      
      ## draw progress bar
      self._graphWin.clear()
      self._graphWin.border(0)
      if self._lithiums > LithiumHunter.MAX_LITHIUMS:
        self._setGraphColour("red")
      elif self._lithiums == LithiumHunter.MAX_LITHIUMS:
        self._setGraphColour("green")
      else:
        self._setGraphColour("amber")
      graphLen = int( self._lithiums * ((self._maxX-2)/(LithiumHunter.MAX_LITHIUMS+0.0)) )
      if graphLen > self._maxX-2:
        graphLen = self._maxX-2
      for i in range(1, graphLen):
        self._graphWin.addch( 1, i, curses.ACS_BLOCK, curses.color_pair(self._graphColour) )
      self._graphWin.refresh()

      
      # clear screen
      self._inputWin.clear()
      
      if self._lithiums > LithiumHunter.MAX_LITHIUMS:
        self._inputWin.addstr(0, 1, "You have woken up in your bed with no lithiums. You lose")
        return self._retryOrQuit()
      elif self._lithiums == LithiumHunter.MAX_LITHIUMS:
        self._inputWin.addstr(0, 1, "You have the best amount of lithium! YOU WIN!")
        return self._retryOrQuit()
      else:
        self._inputWin.addstr(0, 1, "You have {0} lithiums".format(self._lithiums) )
      
if __name__ == "__main__":
  # Initialize curses
  stdscr = curses.initscr()
  curses.noecho()
  curses.cbreak()
  stdscr.keypad(1)
  try:
    curses.start_color()
  except:
    pass
  
  # run the game
  try:
    game = LithiumHunter(stdscr)
    game.getName()
    game.tutorial()
    while game.mainGame():
      pass
    msg = "Bai bai! Happy lorgyhumming!"
  
  # pick up any errors
  except KeyboardInterrupt:
    msg =  "Next time press q to exit" # TODO not working ??
  except Exception as e:
    msg =  "Sorry somthing went wrong"
    msg += "\t({0})".format(e)
  
  # allways reset the screen
  finally:
    # Set everything back to normal
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
  
  # final message
  print msg
  print
  print "Concept by Colin Bramwell, Alexander Robinson and Tom Mckenna"
  print "Coded by Callum Stott and Guy Taylor"
  print

