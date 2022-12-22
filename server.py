#AUTOR: Antonio Gaitán Mansilla
import requests
import random
import json
import time

#id y valor del agente
serverInfo = {"id": 0,"valor": 9}

#Nos va a indicar cuando los valores de todos los agente sean iguales
finish = False

#Rango maximo del random que genera el agente
randomRange = 10


#Funcion que hace una petición GET para obtener el id del agente
def join_request():
    res = requests.get('http://127.0.0.1:5000/agentAssign')
    if res.status_code == 200:
        serverInfo['id'] = json.loads(res.content)
    print("Servidor numero:" ,serverInfo['id'])


#Función que hace un POST al servidor del random del agente
def send_random():
    serverInfo['valor'] = random.randint(1,randomRange)
    requests.post('http://127.0.0.1:5000/random',json =serverInfo)

#Función que hace un POST al servidor para indicar que el agente deja el servidor
def send_leave():
    requests.post('http://127.0.0.1:5000/agentLeave',json =serverInfo)


#Funció que hace un GET al servidor para obtener:
    #0 - si no todos los valores son iguales, entonces el flasg finish = False
    #1 - si todos los valores son iguales, encontes el flag finish = True
def request_all():
    res = requests.get('http://127.0.0.1:5000/randomBool')
    value = json.loads(res.content)
    global finish
    if(value == 0):
        finish = False
    else:
        finish = True

join_request()   

#Bucle que  que se realiza tanta veces como es necesario hasta
#que los ultimos valores enviados por los 3 agentes resultan iguales
while True:

    #time.sleep(5)
    send_random()
    request_all()
    if(finish == True):
        print("TODOS IGUALES")
        print("Agente dejando servidor")
        send_leave()
        break
    print("Generando nuevo random")
    send_random()

finish = False


