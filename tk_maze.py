#!/usr/bin/env python3
from tkinter import *
from PIL import Image, ImageTk
import mazemaking

w = 50
h = 30
ply_x = 1
ply_y = 1

def mov(y_shift,x_shift):
	global ply_x 
	global ply_y
	global w
	global h
	global maze
	if maze[ply_x+x_shift][ply_y+y_shift]:
		ply_x += x_shift
		ply_y += y_shift
		player.place(x=ply_x*10,y=ply_y*10)
	if (ply_x == w-2) and (ply_y == h-2):
		print("You won!")
		quit()
	return

def key_handler(event):
	if event.keysym == "Right":
		mov(0,1)
	elif event.keysym == "Left":
		mov(0,-1)
	elif event.keysym == "Up":
		mov(-1,0)
	elif event.keysym == "Down":
		mov(1,0)
	
entrance = (ply_x,ply_y)
mexit = (w-2,h-2)
maze = mazemaking.mazeMaker(h,w,entrance,mexit)

window = Tk()
window.geometry("600x300")
window.title("TkMaze")

#Keystrokes handler
window.bind("<Key>",key_handler)

#Draw the maze
maze_window = Frame(window, bd=0, bg="#000000", height=h*10, width=w*10)
maze_window.place(x=10,y=10)
maze_window.pack(side="left")

tile_file = Image.open("tile.png")
tile_render = ImageTk.PhotoImage(tile_file)
tiles = []

for i1,columns in enumerate(maze):
	for i2,row in enumerate(columns):
		if not(row):
			tiles.append(Label(maze_window,image=tile_render,bd=0))
			tiles[len(tiles)-1].place(x=i1*10,y=i2*10)

player_file = Image.open("player.png")
player_render = ImageTk.PhotoImage(player_file)
player = Label(maze_window,image=player_render,bd=0,bg="#000000")
player.place(x=ply_x*10,y=ply_y*10)

end_file = Image.open("end.png")
end_render = ImageTk.PhotoImage(end_file)
end = Label(maze_window,image=end_render,bd=0,bg="#000000")
end.place(x=(w-2)*10,y=(h-2)*10)

#Draw the buttons
button_window = Frame(window, bd=0, height=300, width=200)
button_window.place(x=500,y=0)

up_button = Button(button_window, text="↑", width=1, height=1, command = lambda: mov(-1,0))
down_button = Button(button_window, text="↓", width=1, height=1, command = lambda: mov(1,0))
left_button = Button(button_window, text="←", width=1, height=1, command = lambda: mov(0,-1))
right_button = Button(button_window, text="→", width=1, height=1, command = lambda: mov(0,1))
up_button.place(x=35,y=100)
down_button.place(x=35,y=200)
left_button.place(x=10,y=150)
right_button.place(x=60,y=150)


window.mainloop()
