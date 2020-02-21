#!/usr/bin/env python3

import curses
import mazemaking
#TODO from signal import signal, SIGINT

def showCursedMaze(maze):
        for i1,column in enumerate(maze):
                for i2,row in enumerate(column):
                        if row == 1:
                                stdscr.addch(i1,i2," ")
                        elif row == -1:
                                stdscr.addch(i1,i2,"█")
                        elif row == 2:
                                stdscr.addch(i1,i2,"☺")
                        elif row == 3:
                                stdscr.addch(i1,i2,"$")
                        else:
                                stdscr.addch(i1,i2,"░")

h = 120
w = 30
entrance = (2,2)
mexit = (27,117)
maze = mazemaking.mazeMaker(h,w,entrance,mexit)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(True)
wpos = entrance[0]
hpos = entrance[1]

showCursedMaze(maze)

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
	if maze[hpos+direction[0]][wpos+direction[1]] == 1:
		maze[hpos][wpos] = 1
		stdscr.addch(hpos,wpos," ")
		maze[hpos+direction[0]][wpos+direction[1]] == 2
		hpos = hpos + direction[0]
		wpos = wpos + direction[1]
		stdscr.addch(hpos,wpos,"☺")
		stdscr.refresh()
	elif maze[hpos+direction[0]][wpos+direction[1]] == 3:
		break

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
