import machine
import ssd1306
import mazemaking

pscl = machine.Pin('D15',machine.Pin.OUT_PP)
psda = machine.Pin('D14',machine.Pin.OUT_PP)
i2c = machine.I2C(scl=pscl,sda=psda)

oled = ssd1306.SSD1306_I2C(128,32,i2c)

def createMaze(h=16,w=64):
	oled.fill(0)
	maze = mazemaking.mazeMaker(h,w,(2,2),(w-2,h-2))
	for x,column in enumerate(maze):
		for y,row in enumerate(column):
			if row == False:
				oled.pixel(x*2,y*2,1)
				oled.pixel(x*2+1,y*2+1,1)
				oled.pixel(x*2+1,y*2,1)
				oled.pixel(x*2,y*2+1,1)

	oled.show()

