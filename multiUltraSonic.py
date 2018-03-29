import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#sensor1
GPIO.setup(16,GPIO.OUT) #Trigger
GPIO.setup(18,GPIO.IN)  #Echo
#sensor2
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.IN)
#sensor3
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.IN)
#sensor4
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.IN)
#sensor5
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.IN)

triggerList = [16,8,36,35,13]
echoList = [18,10,38,37,15]

def distanceMeasurement(GPIO_TRIGGER,GPIO_ECHO):

    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    
    for i in range(0,len(echoList)): 
        channel = GPIO.wait_for_edge(echoList[i], GPIO_RISING)
        if channel is None:
            print('RISING_ERROR')
        else:
            startTime = time.time()
            sssss
    for j in range(0,len(echoList)): 
        channell = GPIO.wait_for_edge(echoList[j], GPIO_FALLING)
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
           for i in range(5):
               if i == 0:
                   recoveredDistance1 = distanceMeasurement(16,18)
                   print ("sensor1: ",recoveredDistance1,"cm")
               elif i == 1:
                   recoveredDIstance2 = distanceMeasurement(8,10)
                   print ("sensor2: ",recoveredDistance2,"cm")
               elif i == 2:
                   recoveredDIstance3 = distanceMeasurement(36,38)
                   print ("sensor3: ",recoveredDistance3,"cm")
               elif i == 3:
                   recoveredDIstance4 = distanceMeasurement(35,37)
                   print ("sensor4: ",recoveredDistance4,"cm")
               elif i == 4:
                   recoveredDIstance5 = distanceMeasurement(13,15)
                   print ("sensor5: ",recoveredDistance5,"cm" )   
           time.sleep(1)
    except KeyboardInterrupt:
        print ("Measurement stopped by user")
        GPIO.cleanup()


