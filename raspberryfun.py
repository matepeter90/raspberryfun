import RPi.GPIO as GPIO
from time import sleep
import alsaaudio
import struct

class Lights:
    """Class for playing with leds"""

    def __init__(self):
        """Initialize leds"""
        #Setup.setAllOut()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

    def __enter__(self):
        """Shut all led"""
        self.__processLedArray([0,0,0,0,0,0])
        return self
    
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
        try:
            while(True):
                self.__processLedArray([1,1,1,1,1,1])
        except KeyboardInterrupt:
            pass
        GPIO.cleanup()
        
    def BasicRunningLight(self,time = 1.0):
        """Basic running light without pwm, running in one direction
        :param time: sleep between led change
        """
        if time is not float and time <= 0:
            print("Error: Invalid time")
            return
        leds = [0,0,0,0,0,0]
        index = 0
        state = 1
        try:
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
        except KeyboardInterrupt:
            pass
        GPIO.cleanup()

    def BasicTwoWayRunningLight(self,time = 1,tail = 2):
        """Basic two way running light without pwm, running
        from one end to the other with tail
        :param time: float sleep between led change
        :param tail: int tail size between 1 or 5
        """
        if time is not float and time <= 0:
            print("Error: Invalid time")
            return
        if tail < 1 or tail > 5:
            print("Error: Invalid tail size: %s" % tail)
            return
        leds = [0,0,0,0,0,0]
        index = 0
        #First it starts from right side
        direction = "right"
        #Cooldown is used when it reached the end, but it has to wait for the tail
        cooldown = False
        try:
            while(True):
                if direction == "right":
                    #Shuts the light which is not part of the tail anymore
                    if index-tail >= 0:
                        leds[index-tail] = 0
                    #Lights the next led if we are not at the end
                    if not cooldown:
                        leds[index] = 1;
                    index += 1
                    #If it reached the end it will wait for the tail
                    if index == 6:
                        cooldown = True
                    #If tail reached the end it switches direction
                    if index == 5 + tail:
                        direction = "left"
                        cooldown = False
                        #it leaves the last led ON, so it has to continue with the led next to it
                        index = 4
                elif direction == "left":
                    #Shuts the light which is not part of the tail anymore
                    if index+tail <= 5:
                        leds[index+tail] = 0
                    #Lights the next led if we are not at the end
                    if not cooldown:
                        leds[index] = 1;
                    index -= 1
                    #If it reached the end it will wait for the tail
                    if index == -1:
                        cooldown = True
                    #If tail reached the end it switches direction
                    if index == 0 - tail:
                        direction = "right"
                        cooldown = False
                        #it leaves the last led ON, so it has to continue with the led next to it
                        index = 1
                self.__processLedArray(leds)
                sleep(time)
        except KeyboardInterrupt:
            pass
        GPIO.cleanup()

    def music(self, filename):
        """plays wav file"""
        out = alsaaudio.PCM()
        out.setchannels(2)
        out.setrate(44100)
        out.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        f = open(filename, 'rb')
        counter = 0
        data = f.read(320)
        while data:
            out.write(data)
            if counter == 20:
                data = struct.unpack('<H',data[0:2])[0]
                if data > 60000:
                    self.__processLedArray([0,0,0,0,0,0])
                elif data > 50000:
                    self.__processLedArray([1,0,0,0,0,0])
                elif data > 40000:
                    self.__processLedArray([1,1,0,0,0,0])
                elif data > 30000:
                    self.__processLedArray([1,1,1,0,0,0])
                elif data > 20000:
                    self.__processLedArray([1,1,1,1,0,0])
                elif data > 10000:
                    self.__processLedArray([1,1,1,1,1,1])
                counter = 0
            counter += 1
            data = f.read(320)




        
    def __exit__(self, type, value, traceback):
        GPIO.cleanup()
