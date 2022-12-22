#AUTOR: Antonio Gaitán Mansilla
#Based on: https://realpython.com/api-integration-in-python/
from flask import Flask, request, jsonify
import random
import data
app = Flask(__name__)

#Capacidad para los agentes con un status que nos indica si está ocupada o no
agents =[
    {"Server": 1,"status":"OFF"},
    {"Server": 2,"status":"OFF"},
    {"Server": 3,"status":"OFF"}
]

#Datos de cada servidor con un id que indica su respectivo id y el último valor 
#que este ha enviado.
data = [
    {"id": 1,"random":0},
    {"id": 2,"random":1},
    {"id": 3,"random":2}
]

#Petición GET que nos devuelve en formato JSON 'data'
@app.get("/random")
def get_random_numbers():
    return jsonify(data)

#Petición post que permite modificar el valor 'random' de alguno 
#de los servidores.
@app.post("/random")
def asign_random():
    if request.is_json:
        update = request.get_json()
        for key in data:
            if(key['id'] == update['id']):
                key['random'] = update ['valor']
                break
    return  'done' 
    
#Petición GET que nos devuelve en formato JSON 'agents'
@app.get("/agents")
def get_server_status():
    return jsonify(agents)

#Petición GET que devuelve el id con el que se va a identificar
#el agente
@app.get("/agentAssign")
def get_server_assign():
    cont = 1
    for key in agents:
        if(key['status'] == "OFF"):
            key['status'] = "ON"
            return jsonify(cont)
        cont += 1
    return {"error": "No hay más espacio"}, 415

#Petición POST que indica que un agente abandona el servidor
@app.post("/agentLeave")
def server_leave():
    if request.is_json:
        update = request.get_json()
        for key in agents:
            if(key['Server'] == update['id']):
                key['status'] = "OFF"
                break
        return 'done'
    return {"error": "No es un json"}, 415

#Peticion GET que devuelve 1- si los random son iguales 0 - si no todos los random son iguales
@app.get("/randomBool")
def compare_values():
    aux = 0
    cont = 0
    for key in data:
        if(cont == 0):
            aux = key['random']
        if(key['random'] != aux):
            return jsonify(0)
        cont += 1
    return jsonify(1)


if __name__ == '__main__':
    app.run(debug= True, port=5000)

# Save the file as: app.py  #or: export FLASK_APP=app.py
# Run: python -m flask run

