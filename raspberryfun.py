import RPi.GPIO as GPIO
from time import sleep

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
    #Class for playing with leds

    def __init__(self):
        #Initialize leds
        Setup.setAllOut()
    
    def __processLedArray(self,leds):
        """Lights or shuts leds depending on the given six element array
           eg. [0,0,1,0,0,0] lights up third led and shuts the others
        :param leds: led array
        """
        if leds[0] == 1:
            GPIO.output(17, True)
        else:
            GPIO.output(17, False)
        if leds[1] == 1:
            GPIO.output(18, True)
        else:
            GPIO.output(18, False)
        if leds[2] == 1:
            GPIO.output(27, True)
        else:
            GPIO.output(27, False)
        if leds[3] == 1:
            GPIO.output(22, True)
        else:
            GPIO.output(22, False)
        if leds[4] == 1:
            GPIO.output(23, True)
        else:
            GPIO.output(23, False)
        if leds[5] == 1:
            GPIO.output(24, True)
        else:
            GPIO.output(24, False)

    
    def LightUpAll(self):
        #Lights up all leds
        self.__processLedArray([1,1,1,1,1,1])
        
    def BasicRunningLight(self,time = 1):
        """Basic running light without pwm
        :param time: sleep between led change
        """    
        leds = [0,0,0,0,0,0]
        index = 0
        state = 1
        while(True):
            leds[index] = state;
            index += 1
            if index == 6:
                index = 0
                if state == 1:
                    state = 0
                else:
                    state = 1
            self.__processLedArray(leds)
            sleep(time)
            
            

program = Lights()
program.BasicRunningLight(0.05)
