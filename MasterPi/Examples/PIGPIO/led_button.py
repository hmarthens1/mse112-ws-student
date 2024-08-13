import pigpio
import time

# Initialize the pigpio library and connect to the pigpiod daemon
pi = pigpio.pi()

# Check if the connection to pigpiod was successful
if not pi.connected:
    print("Failed to connect to pigpio daemon")
    exit()

# Define the GPIO pins for the LED and the button
LED_PIN = 17
BUTTON_PIN = 4

# Set the LED pin as an output and the button pin as an input with a pull-down resistor
pi.set_mode(LED_PIN, pigpio.OUTPUT)
pi.set_mode(BUTTON_PIN, pigpio.INPUT)
pi.set_pull_up_down(BUTTON_PIN, pigpio.PUD_DOWN)

# Function to read the button state and update the LED
def update_led():
    button_state = pi.read(BUTTON_PIN)  # Read the button state
    if button_state:
        pi.write(LED_PIN, 1)  # Turn LED on
    else:
        pi.write(LED_PIN, 0)  # Turn LED off

# Main loop to continuously check the button state and update the LED
try:
    while True:
        update_led()
        time.sleep(0.01)  # Check the button state every 10 milliseconds
except KeyboardInterrupt:
    # Clean up on Ctrl+C
    pi.write(LED_PIN, 0)  # Turn LED off
    pi.stop()  # Stop the pigpio library
    print("Program terminated")
