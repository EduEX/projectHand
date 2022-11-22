import pywhatkit
from time import  sleep
from datetime import datetime

trava = 0

while True:
    agora = datetime.now()
    sleep(0.1)
    print(agora)
    if(agora.hour == 0 and agora.minute == 1 and trava == 0):
        trava = 1
        stringEnviar = f"*{agora.day}/{agora.month}/{agora.year}*: Sistema atuando ás *{agora.hour}h{agora.minute}min*."
        pywhatkit.sendwhats_image("+558598569832", "teste.png", stringEnviar, 15, True, 3)