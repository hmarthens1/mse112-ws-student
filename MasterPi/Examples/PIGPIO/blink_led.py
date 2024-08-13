import RPi.GPIO as GPIO
import time

# Set the numbering scheme to BOARD
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin where the LED is connected (using BOARD numbering)
LED_PIN = 11  # GPIO 17 corresponds to pin 11 in BOARD numbering

# Set the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Blink the LED
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        time.sleep(1)                    # Wait for 1 second
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off
        time.sleep(1)                    # Wait for 1 second
except KeyboardInterrupt:
    # Clean up on Ctrl+C
    GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED off
    GPIO.cleanup()                  # Clean up GPIO settings
    print("Program terminated")