import pywhatkit
from time import sleep as delay
from time import  sleep
from datetime import datetime
import requests, json

trava = 0

while True:
    try:
        while True:
            delay(5)
            urlBanco = 'https://projetohandersonn-default-rtdb.firebaseio.com/.json'
            response = requests.get(urlBanco)
            if(response.status_code == 200):
                codeZap = response.json()['codZap']['code']
                nada, codeZap = codeZap.split('com/')
                horarios = response.json()['horarios']
                agora = datetime.now()
                print(f'Horário: {agora}, codeZap: {codeZap}, Horários: {horarios}')
                for key in horarios:
                    horario = horarios[key]
                    horas, minutos = horario.split(':')
                    print(f'Horas: {horas}, Minutos: {minutos}')
                    if(str(agora.hour) == horas and str(agora.minute) == minutos):
                        trava = 1
                        if(agora.day < 10):
                            stringDay = f'0{agora.day}'
                        else:
                            stringDay = str(agora.day)
                        if(agora.month < 10):
                            stringMes = f'0{agora.month}'
                        else:
                            stringMes = str(agora.month)

                        stringEnviar = f'*{stringDay}-{stringMes}-{agora.year}*: Sistema atuando *{agora.hour}h{agora.minute}min*.'
                        print(stringEnviar)
                        pywhatkit.sendwhats_image(codeZap, "image1.jpg", stringEnviar, 20, True, 3)

    except:
        print('except')

    finally:
        print('finally')
