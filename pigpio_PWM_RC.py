"""
Simple PWM signal based on the output of the Fly Sky FS-IA6B RC Rx (50 Hz PWM, DC Range: 1ms-2ms)
Written by Christopher Payne
Date: 21 Feb. 2025

Notes:

The "pigpio" library has been shown to work in ROS 2. - C.P. 23 Feb. 2025
"""
import pigpio
import time

PWM_PIN = 18
PWM_FREQ = 50
PWM_MAX = 100
PWM_MID = 75
PWM_MIN = 50
PWM_STOP = PWM_MID

pi = pigpio.pi()

if not pi.connected:
    exit(0)

pi.set_PWM_frequency(PWM_PIN, 50) # Default RC frequency is 50 Hz

# Set the range of the PWM:
# (e.g. if range is 1000, 100 is 10%, 75 is 7.5%, and 50 is 5%.)
pi.set_PWM_range(PWM_PIN, 1000)

# Set the PWM to 0% DC (off)
pi.set_PWM_dutycycle(PWM_PIN, 0)

# Wait for 3 seconds
time.sleep(3)

try:
    while True:
        
        pi.set_PWM_dutycycle(PWM_PIN, PWM_MAX)
        print(f"DC: {PWM_MAX}")
        time.sleep(3)

        pi.set_PWM_dutycycle(PWM_PIN, PWM_MID)
        print(f"DC: {PWM_MID}")
        time.sleep(3)

        pi.set_PWM_dutycycle(PWM_PIN, PWM_MIN)
        print(f"DC: {PWM_MIN}")
        time.sleep(3)
        
except KeyboardInterrupt:

    pi.set_PWM_dutycycle(PWM_PIN, PWM_STOP)
    print("\nStopping Motor")
    print(f"PWM_STOP: {PWM_STOP}")
    time.sleep(1)
    print("Closing program")
    
finally:
    
    print("\ntidying up")
    pi.set_PWM_dutycycle(PWM_PIN, 0)
    print("\nSetting PWM to 0 DC (off)")
    pi.stop()
    print("\nStopping PWM")
    