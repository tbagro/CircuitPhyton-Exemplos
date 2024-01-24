import time
import board
import busio
import adafruit_ds3231

# Crie o objeto I2C usando os pinos configurados
i2c = busio.I2C(board.GP7, board.GP6)

# Inicialize o objeto DS3231
rtc = adafruit_ds3231.DS3231(i2c)

# Obtenha a hora atual do computador
current_time = time.localtime()

# Configure o RTC com a hora atual do computador
rtc.datetime = current_time

# Exiba a hora no RTC
print("RTC sincronizado com o computador. Hora atual:", rtc.datetime)
