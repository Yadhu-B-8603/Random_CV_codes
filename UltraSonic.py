import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_ECHO_TOP = 18
GPIO_TRIGGER_TOP = 24
GPIO_TRIGGER_FRONT = 27
GPIO_ECHO_FRONT = 23

 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER_TOP, GPIO.OUT)
GPIO.setup(GPIO_ECHO_TOP, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_FRONT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_FRONT, GPIO.IN)
 
def distance(pin_trig,pin_echo):
    # set Trigger to HIGH
    GPIO.output(pin_trig, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(pin_trig, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(pin_echo) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(pin_echo) == 1:
        StopTime = time.time()
 

    TimeElapsed = StopTime - StartTime
    dist = (TimeElapsed * 34300) / 2
 
    return dist
 
if __name__ == '__main__':
    try:
        while True:
            count = 0
            dis_top = distance(18,24)
            dist_front_before_then = dist_front_then
            dist_front_then = dist_front_now
            dist_front_now = distance(27,23)
            if dis_top < 100:
                count += 1
                print(str(count))
                if dist_front_then > dist_front_before_then:
                    if dist_front_now > dist_front_then:
                        person_status = "+"
                        print(person_status)
            time.sleep(.1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        
        GPIO.cleanup()