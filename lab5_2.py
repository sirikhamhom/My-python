#Include the library files
from machine import ADC, Pin,PWM
from time import sleep

led = PWM(Pin(12))#Include the LED pin
potentiometer = ADC(25)#Include the potentiometer pin
led.freq(1000)#Set the frequency

while True:
    value = potentiometer.read_u16()#Get the values
    print(value)#Print value on the shell
    led.duty_u16(value)#Turn the LED ON and OFF
    sleep(0.2)#Set the delay time
