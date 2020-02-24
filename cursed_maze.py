#!/usr/bin/env python3

import curses
import mazemaking
#TODO from signal import signal, SIGINT


h = 20
w = 30
entrance = (1,1)
mexit = (28,18)
maze = mazemaking.mazeMaker(h,w,entrance,mexit)

#TODO check terminal size
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(True)
wpos = entrance[0]
hpos = entrance[1]


for i1,column in enumerate(maze):
	for i2,row in enumerate(column):
		if row == True:
			stdscr.addch(i1,i2," ")
		else:
			stdscr.addch(i1,i2,"░")

stdscr.addch(entrance[0],entrance[1],"☺")
stdscr.addch(mexit[0],mexit[1],"$")
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
		stdscr.addch(hpos,wpos,"☺")
		stdscr.refresh()
	if (hpos == mexit[0]) and (wpos == mexit[1]):
		break

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
