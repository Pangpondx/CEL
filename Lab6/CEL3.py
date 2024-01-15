import RPi.GPIO as GPIO
LED = 18
SW = 22
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
try :
    while True :
        if GPIO.wait_for_edge (SW, GPIO.RISING):
            if count == 0:
              GPIO.output (LED, True)       
              print(f"LED => ON ")
              count = count + 1
            elif count == 1:
              GPIO.output (LED, False)         
              print(f"LED => OFF ")    
              count = count - 1
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye...")   
