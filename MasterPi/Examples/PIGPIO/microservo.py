import pigpio
import time

servo_pin = 18

# Initialize pigpio
pwm = pigpio.pi()

# Set up GPIO pin for the servo
pwm.set_mode(servo_pin, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo_pin, 100)  # Set PWM frequency to 50 Hz
pwm.set_PWM_range(servo_pin, 20000)   # Set PWM range (20,000 us for 100% duty cycle)

# Move servo from 0 to 180 degrees
for angle in range(0, 181, 10):
    pulse_width = int(1000 + angle * 10)  # Convert angle to pulse width
    pwm.hardware_PWM(servo_pin, 50, pulse_width)
    time.sleep(0.5)

# Move servo back from 180 to 0 degrees
for angle in range(180, -1, -10):
    pulse_width = int(1000 + angle * 10)  # Convert angle to pulse width
    pwm.hardware_PWM(servo_pin, 50, pulse_width)
    time.sleep(0.5)

# Stop the servo
pwm.set_servo_pulsewidth(servo_pin, 0)

# Clean up
pwm.stop()
