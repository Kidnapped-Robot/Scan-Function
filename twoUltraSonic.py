import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
#Configuration

#sensor1
GPIO.setup(16,GPIO.OUT) #Trigger
GPIO.setup(18,GPIO.IN)  #Echo
#sensor2
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.IN)


def distanceMeasurement(GPIO_TRIGGER,GPIO_ECHO):

    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    while GPIO.input(GPIO_ECHO) == 0:
        startTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        endTime = time.time()

            
    pulseDuration = endTime - startTime
    distance = (pulseDuration * 34300)/2
   
    return distance


#main Loop
if __name__ == '__main__':
    try:
        while True:
           for i in range(2):
               if i == 0:
                   recoveredDistance1 = distanceMeasurement(16,18)
                   print ("sensor1: ",recoveredDistance1,"cm")
               elif i == 1:
                   recoveredDIstance2 = distanceMeasurement(13,15)
                   print ("sensor2: ",recoveredDistance2,"cm")
               
           time.sleep(1)
    except KeyboardInterrupt:
        print ("Measurement stopped by user")
        GPIO.cleanup()
