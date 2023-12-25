from machine import ADC, Pin
import time

# Define the ADC pin
adc_pin = Pin(25, Pin.IN)

# Create ADC object
adc = ADC(25)

while True:
    analog_value = adc.read()
    print("Analog Value:", analog_value)
    time.sleep(0.1)
