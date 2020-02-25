import pyb
import machine
import ssd1306
import mazemaking

pscl = machine.Pin('D15',machine.Pin.OUT_PP)
psda = machine.Pin('D14',machine.Pin.OUT_PP)
i2c = machine.I2C(scl=pscl,sda=psda)
oled = ssd1306.SSD1306_I2C(128,32,i2c)
oled.fill(0)

def refreshPixel(x,y,v):
        oled.pixel(x*2,y*2,v)
        oled.pixel(x*2+1,y*2+1,v)
        oled.pixel(x*2+1,y*2,v)
        oled.pixel(x*2,y*2+1,v)


maze = mazemaking.mazeMaker(16,64,(2,2),(62,14))
for x,column in enumerate(maze):
	for y,row in enumerate(column):
		refreshPixel(x,y,not row)
oled.show()

yaxis = pyb.ADC(pyb.Pin("A0"))
xaxis = pyb.ADC(pyb.Pin("A1"))

yvalue = 0
xvalue = 0

lasty = 0
lastx = 0

yPos = 2
xPos = 2

blink = False

while True:
	pyb.delay(100)
	refreshPixel(xPos,yPos,blink)
	oled.show()
	blink = not blink

	yvalue = yaxis.read()
	xvalue = xaxis.read()

	if (yvalue < 1000) and (lasty != 1):
		if maze[xPos][yPos-1]:
			refreshPixel(xPos,yPos,0)
			yPos -= 1
		lasty = 1
	elif (yvalue > 3000) and (lasty != -1):
		if maze[xPos][yPos+1]:
			refreshPixel(xPos,yPos,0)
			yPos += 1
		lasty = -1
	elif (yvalue >= 1000) and (yvalue <=3000):
		lasty = 0

	if (xvalue < 1000) and (lastx != -1):
		if maze[xPos-1][yPos]:
			refreshPixel(xPos,yPos,0)
			xPos -= 1
		lastx = -1
	elif (xvalue > 3000) and (lastx != 1):
		if maze[xPos+1][yPos]:
			refreshPixel(xPos,yPos,0)
			xPos += 1
		lastx = 1
	elif (xvalue >= 1000) and (xvalue <= 3000):
		lastx = 0
