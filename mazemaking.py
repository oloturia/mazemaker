#!/usr/bin/env python3

import random

def mazeMaker(w,h,entrance,exit):
	cursor = [entrance[0],entrance[1]]	#cursor writing rooms
	track = [(entrance[0],entrance[1])]	#stack of rooms already written
	
	maze = []				#create matrix of 0
	for x in range(0,h):			#maze matrix, 0 = full, 1 = room, -1 = outer wall
		maze.append([])
		for y in range(0,w):
			maze[x].append(False)

	maze[entrance[0]][entrance[1]] = True
	maze[exit[0]][exit[1]] = True
	possibleDirections = [(1,0),(-1,0),(0,1),(0,-1)]
	direction = random.choice(possibleDirections)
	while len(track)>0:
		availDirections = list(possibleDirections)
		while (len(availDirections) > 0):
			direction = random.choice(availDirections)			#choose one direction
			newCursor = (cursor[0]+direction[0],cursor[1]+direction[1])	#place the cursor on the tile
			if (newCursor[0]+direction[0] < 0) or (newCursor[0]+direction[0] > h-1) or (newCursor[1]+direction[1] < 0) or (newCursor[1]+direction[1] > w-1): #check bounds
				availDirections.remove(direction)
			elif maze[newCursor[0]][newCursor[1]] == True:			#if the tile is already a room, skip
				availDirections.remove(direction)
			elif maze[newCursor[0]+direction[0]][newCursor[1]+direction[1]] == True:	#if the tile is full, but the tile after that is a room or outer wall, skip
				availDirections.remove(direction)
			else:
				senseWall = 0			#checks if the new tile has rooms around, if it has more than one (the tile cursor is moving from), skip
				for senseDirection in possibleDirections:
					if (maze[newCursor[0]+senseDirection[0]][newCursor[1]+senseDirection[1]]) == True:
						senseWall += 1
				if senseWall == 1: 		#if all the checks are correct, writes the room as 1 in the maze matrix
					track.append(cursor)	#store the track
					maze[newCursor[0]][newCursor[1]] = True
					cursor = newCursor
					break
				else:
					availDirections.remove(direction)
			if len(availDirections) == 0:		#if all directions are skipped, then go back 1 step, if there are no step left, the maze is completed
				cursor = track.pop()
	senseRoom = False
	distance = 1

	while not senseRoom:					#checks if exit tile connects with the rest of the maze
		for senseDirection in possibleDirections:	#sense the next room tile
			if (exit[0]+senseDirection[0]*distance < 1) or (exit[1]+senseDirection[1]*distance < 1) or (exit[0]+senseDirection[0]*distance > h-1) or (exit[1]+senseDirection[1]*distance > w-1) : 
				continue			#check that the search doesn't go out of bounds
			if (maze[exit[0]+senseDirection[0]*distance][exit[1]+senseDirection[1]*distance]) == True :
				senseRoom = True		#an empty room is detected, the distance and the direction are stored
				directionExit = list(senseDirection)
				break
		if senseRoom:
			for room in range(1,distance):		#dig from exit to the next room in a straight line
				maze[exit[0]+directionExit[0]*room][exit[1]+directionExit[1]*room] = True
		else:
			distance += 1				#if no room are sensed, then distance is increased
	
	return maze

def showMaze(maze):				#draw maze in ascii
	for columns in maze:
		for row in columns:
			if row == True:
				print(" ",end='')
			else:
				print("░",end='')
		print("")

if __name__=="__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-x', '--width', metavar='width', default=30, type=int, help='width')
	parser.add_argument('-y', '--height', metavar='height', default=20, type=int, help='height')
	parser.add_argument('-s', '--start', metavar=('start Y','start X'), default=(1,1), type=int, nargs=2, help='start x y')
	parser.add_argument('-e', '--exit', metavar=('exit Y','exit X'),default=(18,28), nargs=2, type=int, help='exit x y')
	args = parser.parse_args()	
	maze = mazeMaker(args.width,args.height,(args.start[0],args.start[1]),(args.exit[0],args.exit[1]))
	showMaze(maze)
