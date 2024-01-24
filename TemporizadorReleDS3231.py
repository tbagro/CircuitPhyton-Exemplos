import time
import adafruit_ds3231
import board
import busio
from digitalio import DigitalInOut, Direction

# Configuração do objeto I2C usando os pinos configurados RP2040
i2c = busio.I2C(board.GP7, board.GP6)
rtc = adafruit_ds3231.DS3231(i2c)

# Configuração do relé
rele = DigitalInOut(board.GP4)
rele.direction = Direction.OUTPUT

# Lookup table para nomes dos dias (impressão mais amigável).
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
current_time = rtc.datetime

# Configure o tempo de desligamento do relé para 11:00
# O preenchimento segue o formato (year, month, day, hour, minute, second, weekday, yearday, isdst)
# Definimos apenas os campos necessários, e -1 indica campos que devem ser ignorados.

# Preencha com o ano, mês e dia atual

# Define o horário para ligar o relé (10:00)
ligar_horario = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 17, 20, 0, 0, -1, -1))

# Define o horário para desligar o relé (11:00)
desligar_horario = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 17, 28, 0, 0, -1, -1))

# Loop principal
while True:
    # Obtém a data e hora atual
    t = rtc.datetime
    
    # Converte o horário atual para uma tupla
    hora_atual = (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, 0, -1, -1)

    print(
        "The date is {} {}/{}/{}".format(
            days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year
        )
    )
    print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))

    # Verifica se o horário atual está entre o horário de ligar e desligar
    if ligar_horario <= hora_atual < desligar_horario:
        rele.value = True
        print("Relé ligado às 10:00")
    else:
        rele.value = False
        print("Relé desligado")

    # Aguarda por um segundo antes de verificar novamente
    time.sleep(1)
