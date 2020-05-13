#!/usr/bin/env python3
# -*- coding: utf-8 -*.
"""
2D game engine
"""

import pygame
import mazemaking

class Player(pygame.sprite.Sprite):
	def __init__(self,x,y,res,disp,color,wall_color,exit_color):
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(x*res-(res/2),y*res-(res/2),2,2)
		self.disp = disp
		self.color = color
		self.wall_color = wall_color
		self.exit_color = exit_color
		self.won = False

	def update(self):
		keystate = pygame.key.get_pressed()
		x = self.rect.x
		y = self.rect.y
		if keystate[pygame.K_LEFT]:
			x -=2
		if keystate[pygame.K_RIGHT]:
			x +=2
		if keystate[pygame.K_UP]:
			y -=2
		if keystate[pygame.K_DOWN]:
			y +=2
		if self.checkWall(self.disp,x,y):
			self.rect.x = x
			self.rect.y = y
		pygame.draw.rect(self.disp,self.color,self.rect)

	def checkWall(self,disp,x_check,y_check):
		wall = disp.get_at((x_check,y_check))
		if wall == self.wall_color:
			return False
		elif wall == self.exit_color:
			self.won = True
			return True
		else:
			return True
		
		

def gameApp(start_x,start_y,end_x,end_y,res,disp,player_color,wall_color,exit_color):
	loop = True
	playtime = 0.0
	milliseconds = 0.0
	player = Player(start_x,start_y,res,disp,player_color,wall_color,exit_color)
	while loop:
		milliseconds = clock.tick(20)
		playtime += milliseconds /1000.0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False
		if player.won:
			print("You won in "+str(int(playtime))+" seconds.")
			loop = False
		player.update()
		pygame.display.flip()
	return
		
def drawMaze(maze,disp,room_color,exit_x,exit_y,exit_color,res):
	for col in enumerate(maze):
		for row in enumerate(col[1]):
			if row[1] == True:
				pygame.draw.rect(disp,room_color,pygame.Rect(row[0]*res,col[0]*res,res,res))
	pygame.draw.rect(disp,exit_color,pygame.Rect(exit_y*res,exit_x*res,res,res))
	pygame.display.flip()
	return
	
if __name__=="__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-x','--width', metavar='width', default=80, type=int, help='width')
	parser.add_argument('-y','--height', metavar='height', default=60, type=int, help='height')
	parser.add_argument('-b','--size', metavar='size', default=10, type=int, help='block size')
	parser.add_argument('-s','--start', metavar=("start Y","start X"), default=(1,1), type=int, nargs=2, help='start x y')
	parser.add_argument('-e','--exit', metavar=("exit Y","exit X"), default=(58,78), type=int, nargs=2, help='exit x y')
	parser.add_argument('-l','--wallcolor', metavar=("wall R","wall G","wall B"), default=(80,80,80), type=int, nargs=3, help='wall R G B')
	parser.add_argument('-p','--playercolor', metavar=("player R","player G","player B"), default=(180,90,0), type=int, nargs=3, help='player R G B')
	parser.add_argument('-t','--exitcolor', metavar=("exit R","exit G","exit B"), default=(0,180,0), type=int, nargs=3, help='exit R G B')
	parser.add_argument('-r','--roomcolor', metavar=("room R","room G","room B"), default=(20,20,20), type=int, nargs=3, help='room R G B')
	args = parser.parse_args()
	maze = mazemaking.mazeMaker(args.width,args.height,(args.start[0],args.start[1]),(args.exit[0],args.exit[1]))
	pygame.init()
	screen = pygame.display.set_mode((args.width*args.size,args.height*args.size))
	screen.fill((args.wallcolor[0],args.wallcolor[1],args.wallcolor[2]))
	pygame.display.set_caption("A-maze-ing")
	drawMaze(maze,screen,(args.roomcolor[0],args.roomcolor[1],args.roomcolor[2]),args.exit[0],args.exit[1],(args.exitcolor[0],args.exitcolor[1],args.exitcolor[2]),args.size)
	clock = pygame.time.Clock()
	gameApp(args.start[0]+1,args.start[1]+1,args.exit[0],args.exit[1],args.size,screen,(args.playercolor[0],args.playercolor[1],args.playercolor[2]),(args.wallcolor[0],args.wallcolor[1],args.wallcolor[2]),(args.exitcolor[0],args.exitcolor[1],args.exitcolor[2]))
	pygame.quit()
