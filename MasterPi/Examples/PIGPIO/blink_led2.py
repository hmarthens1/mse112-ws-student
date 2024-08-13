import pigpio
import time

# Initialize the pigpio library and connect to the pigpiod daemon
pi = pigpio.pi()

# Check if the connection to pigpiod was successful
if not pi.connected:
    print("Failed to connect to pigpio daemon")
    exit()

# Define the GPIO pin where the LED is connected
LED_PIN = 17

# Set the LED pin as an output
pi.set_mode(LED_PIN, pigpio.OUTPUT)

# Blink the LED
try:
    while True:
        pi.write(LED_PIN, 1)  # Turn LED on
        time.sleep(1)         # Wait for 1 second
        pi.write(LED_PIN, 0)  # Turn LED off
        time.sleep(1)         # Wait for 1 second
except KeyboardInterrupt:
    # Clean up on Ctrl+C
    pi.write(LED_PIN, 0)  # Turn LED off
    pi.stop()             # Stop the pigpio library
    print("Program terminated")
