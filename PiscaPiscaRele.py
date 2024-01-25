# ### Pisca-pisca cronometrado equivalente (t = ton = toff)
# 
# O projeto do de algorítimo em circuitphyton, envolve a interação de um relé, e um temporizador para criar um pisca-pisca cronometrado. 
# Ao ser ligado, o relé fecha o contato após 1 segundo;
# O temporizador inicia a contagem do tempo em UNIXTIME, de ligado (ton);
# 	Após o término do tempo de ligado, o relé abre o contato, desativando a saída.
#  O temporizador então inicia a contagem do tempo de desligado (toff), 
# 	 Ao final do tempo de desligado, o ciclo reinicia, alternando entre os estados de ligado e desligado do relé
# Em caso de falta de energia, os valores de toff, precisam ser armazenados para que não ocorra  acionamentos antes do necessário;
# 
# Esse processo ocorre de maneira contínua, proporcionando um pisca-pisca cronometrado pelo circuito. (loop infinito)
# 
# os intervalos  de tempo de ton e toff serão ser entre contados em UNIXTIME:
# Tempo (t)................................. : 0.1sec, - 999 horas
 
import time
import board
import digitalio

# Configuração do relé
relay_pin = board.GP4  # Substitua GP4 pelo pino conectado ao relé
relay = digitalio.DigitalInOut(relay_pin)
relay.direction = digitalio.Direction.OUTPUT

# Tempo de ligado (ton) e tempo de desligado (toff) em segundos
ton = 1  # 1 segundo # intervalo de 1 seg - 999 horas
toff = 5  # 1 segundo # intervalo de 1 seg - 999 horas

# Inicializa o temporizador
start_time = time.monotonic()

# Função para realizar o pisca-pisca cronometrado
def piscapisca(ton, toff):
    global start_time  # Usa a variável global para armazenar o tempo de início

    while True:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time

        if elapsed_time < ton:
            # Ligado
            print("Ligado - Tempo:", elapsed_time, "segundos")
            relay.value = True
        elif elapsed_time < ton + toff:
            # Desligado
            print("Desligado - Tempo:", elapsed_time, "segundos")
            relay.value = False
        else:
            # Reinicia o ciclo
            start_time = current_time

# Execute a função para começar o pisca-pisca cronometrado
try:
    piscapisca(ton, toff)

except KeyboardInterrupt:
    # Lidar com interrupção do teclado (Ctrl+C)
    relay.value = False
