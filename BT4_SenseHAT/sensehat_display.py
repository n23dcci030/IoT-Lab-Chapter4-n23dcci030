from sense_emu import SenseHat
import time

sense = SenseHat()

y=[255,255,0]
b=[0,0,0]
r=[255,0,0]

smiley= [
	b,r,r,b,b,r,r,b,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	b,r,r,r,r,r,r,b,
	b,b,r,r,r,r,b,b,
	b,b,b,r,r,b,b,b,
	b,b,b,b,b,b,b,b,
	b,b,b,b,b,b,b,b,
]

sense.set_pixels(smiley)
print('Bieu tuong da hien thi.')
time.sleep(5)
sense.clear()
