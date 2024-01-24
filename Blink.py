import time
import board
from digitalio import DigitalInOut, Direction

# rele setup for onboard rele
rele = DigitalInOut(board.GP4)
rele.direction = Direction.OUTPUT

while True:

    rele.value = True
    print("led on")
    time.sleep(5)

    rele.value = False
    print("led off")
    time.sleep(2)
