
from time import sleep
from picamera import PiCamera
camera = PiCamera(resolution=(1280, 720), framerate=30)
# Wait for the automatic gain control to settle
sleep(2)
camera.awb_mode = 'fluorescent'
# Finally, take several photos with the fixed settings
camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])
