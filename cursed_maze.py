#!/usr/bin/env python3

import curses
import mazemaking
import signal,sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-x','--width',metavar='width',default=30,type=int,help='width')
parser.add_argument('-y','--height',metavar='height',default=20,type=int,help='height')
parser.add_argument('-s','--start',metavar=('start Y','start X'),default=(1,1),type=int,nargs=2,help='start x y')
parser.add_argument('-e','--exit',metavar=('exit Y','exit X'),default=(28,18),type=int,nargs=2,help='exit x y')
parser.add_argument('-c','--cursor',metavar='cursor',default='@',type=str,help='cursor')
parser.add_argument('-o','--objective',metavar='objective',default='$',type=str,help='exit token')

args = parser.parse_args()


character = args.cursor
exit_symbol = args.objective
h = args.height
w = args.width
entrance = args.start
mexit = args.exit
maze = mazemaking.mazeMaker(w,h,entrance,mexit)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(True)
wpos = entrance[0]
hpos = entrance[1]

def endcurses():
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()

def signal_handler(sig,frame):
	endcurses()
	quit()

signal.signal(signal.SIGINT, signal_handler)

try:
	for i1,column in enumerate(maze):
		for i2,row in enumerate(column):
			if row == True:
				stdscr.addch(i1,i2," ")
			else:
				stdscr.addch(i1,i2,"░")
except:
	endcurses()
	print("Terminal window too small")
	quit()

stdscr.addch(entrance[0],entrance[1],character)
stdscr.addch(mexit[0],mexit[1],exit_symbol)
stdscr.refresh()

while True:
	c = stdscr.getch()
	if c == curses.KEY_DOWN:
		direction = (1,0)
	elif c == curses.KEY_RIGHT:
		direction = (0,1)
	elif c == curses.KEY_UP:
		direction = (-1,0)
	elif c == curses.KEY_LEFT:
		direction = (0,-1)
	elif c == ord("q"):
		break
	else:
		continue
	if maze[hpos+direction[0]][wpos+direction[1]] == True:
		stdscr.addch(hpos,wpos," ")
		hpos = hpos + direction[0]
		wpos = wpos + direction[1]
		stdscr.addch(hpos,wpos,character)
		stdscr.refresh()
	if (hpos == mexit[0]) and (wpos == mexit[1]):
		break

endcurses()
