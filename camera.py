from picamera import PiCamera
from time import sleep
from time import time

while 1 :
	with PiCamera() as camera:
		camera.resolution = (2592,1944)
		camera.framerate = 15
		sleep(5)
		camera.capture('/home/pi/Desktop/image%s.jpg' % int(time()))
	sleep(294)	
