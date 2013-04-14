import RPi.GPIO as GPIO

class Setup:
    def setAllOut():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

class Lights:      
    #Lights or shuts a led depending on the given six element array
    def __processLedArray(leds):
        if leds[0]:
            GPIO.output(17, True)
        else:
            GPIO.output(17, False)
        if leds[1]:
            GPIO.output(18, True)
        else:
            GPIO.output(18, False)
        if leds[2]:
            GPIO.output(27, True)
        else:
            GPIO.output(27, False)
        if leds[3]:
            GPIO.output(22, True)
        else:
            GPIO.output(22, False)
        if leds[4]:
            GPIO.output(23, True)
        else:
            GPIO.output(23, False)
        if leds[5]:
            GPIO.output(24, True)
        else:
            GPIO.output(24, False)

        #Lights up all leds
    def LightUpAll():
        Setup.setAllOut()
        __processLedArray([1,1,1,1,1,1])
        
    #Basic running light without pwm
    def BasicRunningLight(self):
        Setup.setAllOut()
        leds = [0,0,0,0,0,0]
               
    

Lights.LightUpAll()
