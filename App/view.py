"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from turtle import title
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController(entero):
    """
    Se crea una instancia del controlador
    """
    control = controller.newController(entero)
    return control

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar las películas estrenadas en un periodo de tiempo")
    print("3- Listar las películas estrenadas en un periodo de tiempo")
    print("4- Encontrar contenido donde participa un actor")
    print("5- Encontrar contenido por un género especifico")
    print("6- Encontrar contenido producido en un país")
    print("7- : Encontrar contenido con un director involucrado")
    print("8- Listar el TOP de los géneros con más contenido")
    print("9- : Listar el TOP de los actores con más participaciones en contenido")
    print("10- Seleccionar estructura de la lista")
    print("0- : Salir")

catalog = None
entero = None

def loadData(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    amazon, disney, hulu, netflix = controller.loadData(control)

    return amazon, disney, hulu, netflix

def SortList(lista):
    
    return controller.SortList(lista)

def representacionDatos(entero):
    
    return controller.representacionDatos(entero)

def requerimiento1(catalog, fecha1, fecha2):
    
    return controller.requerimiento1(catalog, fecha1, fecha2)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        if entero == None:
            ent = 1
        else:
            ent = entero
        control = newController(ent)
        print("Cargando información de los archivos ....")
        print("Cargando información de los archivos ....")
        amazon, disney, hulu, netflix = loadData(control)
        catalog = control['model']
        print('Titulos de Amazon cargados: ' + str(amazon))
        print('Titulos de Disney cargados: ' + str(disney))
        print('Titulos de Hulu cargados: ' + str(hulu))
        print('Titulos de Netflix cargados: ' + str(netflix))
        print(catalog)

    elif int(inputs[0]) == 2:
        fecha1= int(input("Ingrese fecha 1: "))
        fecha2= int(input("Ingrese fecha 2: "))
        respuesta = requerimiento1(catalog, fecha1, fecha2)
        x = 1
        for i in lt.iterator(respuesta):
            if x <= 3 or x > lt.size(respuesta)-3:
                print(i['title'],',', i['release_year'])
            x += 1
            
    elif int(inputs[0]) == 9:
        print('1. single linked list')
        print('2. Array list')
        entero = int(input('ingrese la estructura que desee usar '))

    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        continue
sys.exit(0)