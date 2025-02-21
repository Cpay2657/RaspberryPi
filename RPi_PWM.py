"""
Simple PWM signal based on the output of the Fly Sky FS-IA6B RC Rx (50 Hz PWM, DC Range: 1ms-2ms)
Written by Christopher Payne
Date: 21 Feb. 2025
"""
import RPi.GPIO as GPIO
import time

PWM_PIN = 18
PWM_FREQ = 50
PWM_MAX = 10
PWM_MID = 7.5
PWM_MIN = 5
PWM_STOP = PWM_MID

GPIO.setmode(GPIO.BCM)

GPIO.setup(PWM_PIN, GPIO.OUT)

pwm = GPIO.PWM(PWM_PIN, PWM_FREQ)

pwm.start(0)

try:
    while True:
        
        pwm.ChangeDutyCycle(PWM_MIN)
        print(f"Min DC: {PWM_MIN}%")
        time.sleep(3)
        
        pwm.ChangeDutyCycle(PWM_MID)
        print(f"Mid DC: {PWM_MID}%")
        time.sleep(3)
        
        pwm.ChangeDutyCycle(PWM_MAX)
        print(f"MAX DC: {PWM_MAX}%")
        time.sleep(3)
        
        
except KeyboardInterrupt:
    pwm.ChangeDutyCycle(PWM_STOP)
    print(f"Stopping Motor DC: {PWM_STOP}%")
    time.sleep(1)
    print("Closing program")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO are clean")