import RPi.GPIO as GPIO
from time import sleep

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for each segment (a to g) and the common pin
segments = [2, 3, 4, 14, 15, 17, 18]
common_pin = 27

# Setup GPIO pins
GPIO.setup(segments, GPIO.OUT)
GPIO.setup(common_pin, GPIO.OUT)

# Function to display a digit on the 7-segment display
def display_digit(digit):
    # Define the mapping of segments to each digit
    digit_segments = {
        0: [1, 1, 1, 1, 1, 1, 0],  # 0
        1: [0, 1, 1, 0, 0, 0, 0],  # 1
        2: [1, 1, 0, 1, 1, 0, 1],  # 2
        3: [1, 1, 1, 1, 0, 0, 1],  # 3
        4: [0, 1, 1, 0, 0, 1, 1],  # 4
        5: [1, 0, 1, 1, 0, 1, 1],  # 5
        6: [1, 0, 1, 1, 1, 1, 1],  # 6
        7: [1, 1, 1, 0, 0, 0, 0],  # 7
        8: [1, 1, 1, 1, 1, 1, 1],  # 8
        9: [1, 1, 1, 1, 0, 1, 1],  # 9
    }

    # Turn on/off each segment based on the digit's mapping
    for segment, state in zip(segments, digit_segments[digit]):
        GPIO.output(segment, state)

# Function to turn off all segments
def turn_off_segments():
    for segment in segments:
        GPIO.output(segment, 0)

# Example: Display the number 7 on the 7-segment display
try:
    GPIO.output(common_pin, 1)  # Turn on the common pin (common anode)
    display_digit(7)
    sleep(2)  # Display for 2 seconds

finally:
    turn_off_segments()
    GPIO.output(common_pin, 0)  # Turn off the common pin

    # Cleanup GPIO settings
    GPIO.cleanup()
