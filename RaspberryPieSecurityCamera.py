#------------------
#Security Camera
#------------------
from gpiozero import MotionSensor
from time import sleep
from picamera import PiCamera
from signal import pause
import datetime
import SendingEmailWithAttachments



#Order of variebles for email sender:sender, password, recipient, subject ,body, filename

start_monitering = datetime.time(16,00,00)#starts recording at 4PM
stop_monitering = datetime.time(20,10,00)#stops recording at 8.10AM
current_time = datetime.datetime.now()
camera = PiCamera()
PIR = MotionSensor(21)#asigns the gpio pin(21) as motion sensor
current_time_formatted = current_time.strftime("%d-%m-%Y_%H:%M")#formats current time so it can be displayed as a string

sender = ("sender@gmail.com")
reciever = ("reciever@gmail.com")
password = ("Enter in the security key for ur gmail account")
subject = ("Motion Detected")
body = ("Motion has been detected at"+current_time_formatted)


def start_recording():
    print("Recording")
    global filename
    filename = ("/home/pi/Alt4/Video" + current_time_formatted + ".h264")#where u want file saved to and as
    camera.start_recording(filename)#starts recording and saves a .h264 file

def stop_recording():
    if camera.recording:
        print("Stopped recording")
        camera.stop_recording()#stops recording

        SendingEmailWithAttachments.send_email(sender, password, reciever, subject ,body, filename)

if current_time.time() >= start_monitering or current_time.time() <= stop_monitering:#checks if it should be recording now
    PIR.when_motion = start_recording#starts recording
    PIR.when_no_motion = stop_recording#stops recording
else:
    print("Cameras inactive")

pause()#keeps code running sorta like a while loop
