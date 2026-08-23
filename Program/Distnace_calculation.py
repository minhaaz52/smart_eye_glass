import RPi.GPIO as GPIO
import time
from espeak import espeak

TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)

while True:
    print("Distance measurement in progress")
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)   # wait for 10 micro seconds
    GPIO.output(TRIG, False)
    
    while (GPIO.input(ECHO)==0):  # wait till echo is low
        pulse_start=time.time()
    
    while (GPIO.input(ECHO)==1):   # wait till echo is high
        pulse_end=time.time()
    
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    print("Distance :",distance,"cm")
    
    espeak.set_voice("f3")
    espeak.synth("Obstacle is nearby")
    espeak.synth(str(round (distance,1)))
    espeak.synth("centimeters")
    
    
    time.sleep(5)