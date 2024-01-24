import time
import TM1637
import board
import busio
import adafruit_ds3231
i2c = busio.I2C(board.GP7, board.GP6)

# Lookup table for names of days (nicer printing).
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Inicialize o objeto DS3231
rtc = adafruit_ds3231.DS3231(i2c)

if __name__ == "__main__":
  CLK = board.GP4
  DIO = board.GP3
  display = TM1637.TM1637(CLK, DIO)
  time.sleep(5)
  while True:
    t = rtc.datetime
    display.numbers(t.tm_hour,t.tm_min)
    time.sleep(60-(t.tm_sec%60))
