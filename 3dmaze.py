#!/usr/bin/env python3

import pygame
from pygame.locals import *
import mazemaking

xPos = 1
yPos = 1
xOut = 18
yOut = 28

dirs = [
	(((0,0,0),(1,0,-1)),((1,1,1),(1,0,-1)),((2,2,2),(1,0,-1)),((3,3,3),(1,0,-1))),		 #SOUTH
	(((-1,0,1),(0,0,0)),((-1,0,1),(1,1,1)),((-1,0,1),(2,2,2)),((-1,0,1),(3,3,3))), 		 #WEST
	(((0,0,0),(-1,0,1)),((-1,-1,-1),(-1,0,1)),((-2,-2,-2),(-1,0,1)),((-3,-3,-3),(-1,0,1))),	 #NORTH
	(((1,0,-1),(0,0,0)),((1,0,-1),(-1,-1,-1)),((1,0,-1),(-2,-2,-2)),((1,0,-1),(-3,-3,-3)))	 #EAST
]

direction = 1

maze = mazemaking.mazeMaker(30,20,(xPos,yPos),(xOut,yOut))

pygame.init()
width = 1024
height = 768
black = ((0,0,0))
white = ((255,255,255))

area = pygame.display.set_mode((width,height))

skewX = 100
skewY = 200

a1 = (0,height)
a2 = (width,height)
wa1 = (0,height-skewY*2)
wa2 = (width,height-skewY*2)
ea1 = (a1[0],wa1[1])
ea2 = (a2[0],wa2[1])

b1 = (a1[0]+skewX,a1[1]-skewY)
b2 = (a2[0]-skewX,a2[1]-skewY)
wb1 = (b1[0],b1[1]-skewY*1.75)
wb2 = (b2[0],b2[1]-skewY*1.75)
eb1 = (0,wb1[1])
eb2 = (width,wb2[1])

c1 = (b1[0]+skewX,b1[1]-skewY)
c2 = (b2[0]-skewX,b2[1]-skewY)
wc1 = (c1[0],c1[1]-skewY*1.5)
wc2 = (c2[0],c2[1]-skewY*1.5)
ec1 = (0,wc1[1])
ec2 = (width,wc2[1])

d1 = (c1[0]+skewX/2,c1[1]-skewY/2)
d2 = (c2[0]-skewX/2,c2[1]-skewY/2)
wd1 = (d1[0],d1[1]-skewY*1.5)
wd2 = (d2[0],d2[1]-skewY*1.5)
ed1 = (0,wd1[1])
ed2 = (width,wd2[1])

def drawMaze(vis):
	area.fill(black)

	#0th row - nearest


	if setWall(vis[0],wa1,wb1,wa2,wb2):
		return
	drawRoom(a1,a2,b1,b2,wb1,wb2)
	setExit(vis[0][0],wa1,ea1,wb1,eb1)
	setExit(vis[0][2],wa2,ea2,wb2,eb2)

	#1st row

	if setWall(vis[1],wb1,wc1,wb2,wc2):
		return
	drawRoom(b1,b2,c1,c2,wc1,wc2)
	setExit(vis[1][0],wb1,eb1,wc1,ec1)
	setExit(vis[1][2],wb2,eb2,wc2,ec2)

	#2nd row

	if setWall(vis[2],wc1,wd1,wc2,wd2):
		return
	drawRoom(c1,c2,d1,d2,wd1,wd2)
	setExit(vis[2][0],wc1,ec1,wd1,ed1)
	setExit(vis[2][2],wc2,ec2,wd2,ed2)

	#4th row - farthest
	if not vis[3][1]:
		pygame.draw.line(area,white,wd1,wd2)
	else:
		pygame.draw.line(area,black,wd1,wd2)
	return
	
def drawRoom(sx,dx,sxFar,dxFar,sxFarUp,dxFarUp):
	pygame.draw.line(area,white,sxFar,dxFar) 	#floor
	pygame.draw.line(area,white,sx,sxFar)   	#left floor
	pygame.draw.line(area,white,dx,dxFar)   	#right floor
	pygame.draw.line(area,white,sxFar,sxFarUp) 	#left wall
	pygame.draw.line(area,white,dxFar,dxFarUp)	#right wall
	return

def setExit(test,wall,wallE,wallUp,wallUpE):
	if test:
		pygame.draw.line(area,white,wall,wallE)
		pygame.draw.line(area,white,wallUp,wallUpE)
	return

def setWall(walls,sx,sxW,dx,dxW):
	colorW1 = black
	colorW2 = black
	colorC = black
	blocked = False
	if not walls[1]:
		colorC = white
		blocked = True
	if not walls[0] and not blocked:
		colorW1 = white
	if not walls[2] and not blocked:
		colorW2 = white

	pygame.draw.line(area,colorW1,sx,sxW)
	pygame.draw.line(area,colorW2,dx,dxW)
	pygame.draw.line(area,colorC,sx,dx)
	
	return blocked

def parseMaze(mazeParse,xPos,yPos,direction):
	pattern = dirs[direction]
	parsed = []
	for i1 in range(0,4):
		parsed.append([])
		for i2 in range(0,3):
			parsed[i1].append(checkBounds(mazeParse,xPos+pattern[i1][0][i2],yPos+pattern[i1][1][i2]))
	return parsed

def checkBounds(mazeCheck,x,y):
	if x < 0 or x > len(mazeCheck)-1 or y < 0 or y > len(mazeCheck[0])-1:
		return False
	else:
		return mazeCheck[x][y]

def drawMap(maze,rowPos,colPos,dirc):
	for posX,column in enumerate(maze):
		for posY,row in enumerate(column):
			if row == True:
				if posX==rowPos and posY==colPos:
					if dirc == 0:
						print("↓",end='')
					elif dirc == 1:
						print("→",end='')
					elif dirc == 2:
						print("↑",end='')
					elif dirc == 3:
						print("←",end='')
				else:
					print(" ",end='')
			else:
				print("░",end='')
		print("")

pygame.event.clear()
visual = parseMaze(maze,xPos,yPos,direction)
drawMaze(visual)
pygame.display.update()
while True:
	keyPress = pygame.event.wait()
	if keyPress.type == QUIT:
		pygame.quit()
		exit()
	elif keyPress.type == KEYDOWN:
		if keyPress.key == K_UP	and visual[1][1]:
			if direction == 0:
				xPos +=1
			elif direction == 1:
				yPos +=1
			elif direction == 2:
				xPos -=1
			elif direction == 3:
				yPos -=1
		elif keyPress.key == K_LEFT:
			direction += 1
			direction = direction%4	
		elif keyPress.key == K_RIGHT:
			direction -= 1
			direction = direction%4
		elif keyPress.key == K_m:
			drawMap(maze,xPos,yPos,direction)
		visual = parseMaze(maze,xPos,yPos,direction)
		drawMaze(visual)
		pygame.display.update()
