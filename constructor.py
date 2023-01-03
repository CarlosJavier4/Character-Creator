# Python3 + JSON

import json
import uuid
import time
from players import personajes

data = {}
data['personajes_creados'] = []

class Raza():
	valores = {'1': 'Humanos','2': 'Orcos'}

class ClaseHumano():
    tipoHumano = {
    	'1': 'Guerrero',
    	'2': 'Jinete',
    	'3': 'Mago'
    }
 
 # self.crearPersonaje(raza_seleccionada, clase_seleccionada)

class ClaseOrco():
    tipoOrco = {
    	'1': 'Guerrero',
    	'2': 'Chamán',
    	'3': 'Jinete'
    }

class Personaje():
    def __init__(self, nombre, raza, clase, vida, mana):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.vida = vida
        self.mana = mana
    def configurarPersonaje(self):
        print("""\n ¿Qué personaje deseas crear?\n
1) Humanos
2) Orcos""")
        raza_seleccionada = input('\n> ')
        if raza_seleccionada == '1':
            raza_seleccionada = Raza().valores[raza_seleccionada] # Identificar la raza
            print("""\n¿Qué clase de humano deseas crear?\n
1) Guerrero
2) Jinete
3) Mago """)
            clase_seleccionada = input("\n>")

            self.crearPersonaje(raza_seleccionada, ClaseHumano().tipoHumano[clase_seleccionada]) #Crear luego de dentificar el jugador humano
               
        elif raza_seleccionada == '2':
            raza_seleccionada = Raza().valores[raza_seleccionada]
            print("""\n¿Qué clase de orco deseas crear?\n
1) Guerrero
2) Chamán
3) Jinete """)
            clase_seleccionada = input("\n> ")
           
            self.crearPersonaje(raza_seleccionada, ClaseOrco().tipoOrco[clase_seleccionada]) # Crear luego de identificar el jugador orco

        else:
            print("\nHas introducido un comando inválido")

    def crearPersonaje(self, raza_seleccionada, clase_seleccionada):
        vida = personajes['Raza'][raza_seleccionada]['Clase'][clase_seleccionada]['Stats']['Vida']
        mana = personajes['Raza'][raza_seleccionada]['Clase'][clase_seleccionada]['Stats']['Mana']
        nombre = input("\nIntroduce el nombre de tu personaje > ")
        nuevo_pj = Personaje(
            nombre=nombre, raza=raza_seleccionada, clase=clase_seleccionada, vida=vida, mana=mana)
        datos = {
            "id": str(uuid.uuid4()),
            "Nombre": nuevo_pj.nombre,
            "Raza": nuevo_pj.raza,
            "Clase": nuevo_pj.clase,
            "Vida": nuevo_pj.vida,
            "Mana": nuevo_pj.mana
        }

        print("\nEl personaje \"{}\" ha sido creado".format(datos["Nombre"]))
        self.guardarPersonaje(datos)

    def guardarPersonaje(self, datos):
        data['personajes_creados'].append(datos)
        #pjs = data['personajes_creados']
        archivo = open('Personajes.json', 'w')
        json.dump(data, archivo, indent=4)

class Iniciar(Personaje):
    def __init__(self):
        self.configurarPersonaje()

Iniciar()
print(data['personajes_creados'])
