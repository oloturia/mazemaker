import machine
import ssd1306
import mazemaking

pscl = machine.Pin('D15',machine.Pin.OUT_PP)
psda = machine.Pin('D14',machine.Pin.OUT_PP)
i2c = machine.I2C(scl=pscl,sda=psda)

oled = ssd1306.SSD1306_I2C(128,32,i2c)

def createMaze(h=18,w=66):
	oled.fill(0)
	maze = mazemaking.mazeMaker(h,w,(2,2),(w-3,h-3))
	for x,column in enumerate(maze):
		for y,row in enumerate(column):
			if row == 0:
				oled.pixel((x-1)*2,(y-1)*2,1)
				oled.pixel((x-1)*2+1,(y-1)*2+1,1)
				oled.pixel((x-1)*2+1,(y-1)*2,1)
				oled.pixel((x-1)*2,(y-1)*2+1,1)

	oled.show()

