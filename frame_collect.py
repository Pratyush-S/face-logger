import time
import picamera
import subprocess

x=int(time.time())

cmd="raspistill -o as.jpg"

subprocess.call(cmd,shell=True)
