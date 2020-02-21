#!/usr/env python3
# -*- coding: utf-8 -*.
"""
test program
"""

import pygame

def gameApp():
	loop = True
	playtime = 0.0
	milliseconds = 0.0
	while loop:
		milliseconds = clock.tick(20)
		playtime += milliseconds /1000.0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					loop = False
		pygame.display.set_caption("A-maze-ing")
		pygame.display.flip()
		
	
	

if __name__=="__main__":
	pygame.init()
	screen = pygame.display.set_mode((800,600))
	background = pygame.Surface(screen.get_size())
	background.fill((255,80,0))
	background = background.convert()
	screen.blit(background,(0,0))
	clock = pygame.time.Clock()
	gameApp()
	pygame.quit()
