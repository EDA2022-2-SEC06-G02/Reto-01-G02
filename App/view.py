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
def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
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

catalog = None

def loadData(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description = controller.loadData(control)
    return show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description

control = newController()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        print("Cargando información de los archivos ....")
        show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description = loadData(control)
        print('Películas cargadas: ' + str(title))

    elif int(inputs[0]) == 2:
        pass

    else:
        continue
sys.exit(0)
