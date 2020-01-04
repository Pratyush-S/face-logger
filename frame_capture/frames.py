from picamera import PiCamera
from time import sleep

camera =PiCamera()

for i in range(5):
	sleep(5)
	camera.capture('/home/pi/face-logger/frame_capture/image%s.jpg'%i)

camera.stop_preview()
