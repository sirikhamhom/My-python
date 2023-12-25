from machine import Pin
import time
    
segments = (4, 5, 6, 7, 9, 10, 11)
digits = (12, 14, 0, )

for segment in segments:
    Pin(segment, Pin.OUT)
    
for ditgit in digits:
    Pin(digit, Pin.OUT)

num = {
    ' ': (0, 0, 0, 0, 0, 0, 0, 0),
    '0': (1, 1, 1, 1, 1, 1, 0, 0),
    '1': (0, 1, 1, 0, 0, 0, 0, 0),
    '2': (1, 1, 0, 1, 1, 0, 1, 0),
    '3': (1, 1, 1, 1, 0, 0, 1, 0),
    '4': (0, 1, 1, 0, 0, 1, 1, 0),
    '5': (1, 0, 1, 1, 0, 1, 1, 0),
    '6': (1, 0, 1, 1, 1, 1, 1, 0),
    '7': (1, 1, 1, 0, 0, 0, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1, 0),
    '9': (1, 1, 1, 1, 0, 1, 1, 0),
    }

def seg():
    for digit in range(4):
        for i 
        
seg()
while(1):
    for i in range(len(Numbers)):
        for j in range(len(segments)):
            pin[j].value(char[i][j])
        time.sleep(i)