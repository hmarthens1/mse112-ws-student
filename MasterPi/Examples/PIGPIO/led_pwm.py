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

# Initialize the duty cycle
duty_cycle = 0

# Function to update the LED brightness
def update_led_brightness():
    global duty_cycle
    pi.set_PWM_dutycycle(LED_PIN, duty_cycle)  # Set PWM duty cycle for the LED

    duty_cycle += 5
    if duty_cycle > 255:
        duty_cycle = 0

# Blink the LED using PWM
try:
    while True:
        update_led_brightness()
        time.sleep(0.3)  # Wait for 20 milliseconds
except KeyboardInterrupt:
    # Clean up on Ctrl+C
    pi.set_PWM_dutycycle(LED_PIN, 0)  # Turn LED off
    pi.stop()  # Stop the pigpio library
    print("Program terminated")
