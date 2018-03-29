import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#sensor1
GPIO.setup(16,GPIO.OUT) #Trigger
GPIO.setup(18,GPIO.IN)  #Echo
#sensor2
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.IN)
#sensor3
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.IN)


triggerList = [16,19,36]
echoList = [18,21,38]

def distanceMeasurement(GPIO_TRIGGER,GPIO_ECHO):

    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    
    for i in range(0,len(echoList)): 
        channel = GPIO.wait_for_edge(echoList[i], GPIO.RISING)
        if channel is None:
            print('RISING_ERROR')
        else:
            startTime = time.time()
            
    for j in range(0,len(echoList)): 
        channell = GPIO.wait_for_edge(echoList[j], GPIO.FALLING)
        if channell is None:
            print('FALLING_ERROR')
        else:
            endTime = time.time()    
        

   # while GPIO.input(GPIO_ECHO) == 0:
       # startTime = time.time()
    # while GPIO.input(GPIO_ECHO) == 1:
      #  endTime = time.time()

    pulseDuration = endTime - startTime
    distance = (pulseDuration * 34300)/2
   
    return distance



if __name__ == '__main__':
    try:
        while True:
           for i in range(3):
               if i == 0:
                   recoveredDistance1 = distanceMeasurement(16,18)
                   print ("sensor1: ",recoveredDistance1,"cm")
               elif i == 1:
                   recoveredDIstance2 = distanceMeasurement(8,10)
                   print ("sensor2: ",recoveredDistance2,"cm")
               elif i == 2:
                   recoveredDIstance3 = distanceMeasurement(36,38)
                   print ("sensor3: ",recoveredDistance3,"cm")
                
           time.sleep(1)
    except KeyboardInterrupt:
        print ("Measurement stopped by user")
        GPIO.cleanup()


