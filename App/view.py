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
default_limit = 1000
sys.setrecursionlimit(default_limit*100)

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
ordenamiento = None

def loadData(control, archivo):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    amazon, disney, hulu, netflix = controller.loadData(control, archivo)

    return amazon, disney, hulu, netflix

def SortList(lista):
    
    return controller.SortList(lista)

def sublist(tamaño, catalog):
    return controller.sublist(tamaño, catalog)

def representacionDatos(entero):
    
    return controller.representacionDatos(entero)

def requerimiento1(catalog, fecha1, fecha2, sort):
    
    return controller.requerimiento1(catalog, fecha1, fecha2, sort)

def requerimiento2(catalog, fecha1, fecha2, sort):
    
    return controller.requerimiento2(catalog, fecha1, fecha2, sort)

def requerimiento3(catalog, actor, sort):
    
    return controller.requerimiento3(catalog, actor, sort)

def requerimiento4(catalog, genero, sort):
    return controller.requerimiento4(catalog, genero, sort)

def requerimiento6(catalog, top, sort):
    return controller.requerimiento6(catalog, top, sort)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = int(input('Seleccione una opción para continuar\n'))
    if inputs == 1:
        print('1. single linked list')
        print('2. Array list')
        entero = int(input('ingrese la estructura que desee usar: '))
        if entero == None:
            ent = 1
        else:
            ent = entero
        control = newController(ent)
        archivo=input("Ingrese el sufijo del archivo a cargar: ")
        opcion=int(input("Escriba '1' para cargar archivo en catálogo o '2' para sublista: "))
        if opcion==1:
            print("Cargando información de los archivos ....")
            print("Cargando información de los archivos ....")
            amazon, disney, hulu, netflix = loadData(control, archivo)
            catalog = control['model']
            print('Titulos de Amazon cargados: ' + str(amazon))
            print('Titulos de Disney cargados: ' + str(disney))
            print('Titulos de Hulu cargados: ' + str(hulu))
            print('Titulos de Netflix cargados: ' + str(netflix))
            total = amazon+disney+hulu+netflix
            print('Total de titulos cargados: '+ str(total))
        if opcion==2:
            tamaño=int(input("Escriba el tamaño de la sublista: "))
            if tamaño > total:
                print('Esa mondá no sirve. Deme un tamaño más pequeño.')
            else:
                suball = sublist(tamaño, catalog)
                for i in lt.iterator(suball):
                    print(i['title'])
            
    elif inputs== 2:
        fecha1= int(input("Ingrese fecha 1: "))
        fecha2= int(input("Ingrese fecha 2: "))
        respuesta = requerimiento1(catalog, fecha1, fecha2, ordenamiento)
        x = 1
        print('title - release_year - duration - platform - director - cast')
        for i in lt.iterator(respuesta[0]):
            if x <= 3 or x > lt.size(respuesta[0])-3:
                print(i['title'],'-', i['release_year'],'-', i['duration'],'-', i['platform'],'-', i['director'],'-', i['cast'])
            x += 1
        print(str(respuesta[1])+' milisegundos.')
    
    elif inputs == 3:
        fecha1= (input("Ingrese fecha 1: "))
        fecha2= (input("Ingrese fecha 2: "))
        respuesta = requerimiento2(catalog, fecha1, fecha2, ordenamiento)
        x = 1
        print('title - dete_added - release_year - duration - platform - director - cast')
        for i in lt.iterator(respuesta[0]):
            if x <= 3 or x > lt.size(respuesta[0])-3:
                print(i['title'],'-', i['date_added'],'-', i['release_year'],'-', i['duration'],'-', i['platform'],'-', i['director'],'-', i['cast'])
            x += 1
        print(str(respuesta[1])+' milisegundos.')
        
    elif inputs== 4:
        actor = (input("Ingrese el nombre de un actor: "))
        respuesta = requerimiento3(catalog, actor, ordenamiento)
        x = 1
        print('title - type - dete_added - release_year - duration - platform - director - cast')
        for i in lt.iterator(respuesta[0]):
            if x <= 3 or x > lt.size(respuesta[0])-3:
                print(i['title'],'-', i['date_added'],'-', i['type'],'-', i['release_year'],'-', i['duration'],'-', i['platform'],'-', i['director'],'-', i['cast'])
            x += 1
        print(str(respuesta[1])+' milisegundos.')
    
    elif inputs== 5:
        genero= input("Ingrese el nombre del género que quiere buscar: ")
        respuesta= requerimiento4(catalog, genero, ordenamiento)
        x = 1
        print("title - type - dete_added - release_year - duration - platform - director - cast")
        for i in lt.iterator(respuesta[0]):
            if x<= 3 or x>lt.size(respuesta[0])-3:
                print(i['title'],'-', i['date_added'],'-', i['type'],'-', i['release_year'],'-', i['duration'],'-', i['platform'],'-', i['director'],'-', i['cast'])
            x += 1
        print(str(respuesta[1])+' milisegundos.')
    
    elif inputs==6:
        director=input("Ingrese el director: ")
        respuesta= requerimiento6(catalog, director, ordenamiento)
        x=1
        print("Types" + "-" + "Count")
        for i in lt.iterator(respuesta[0]):
            print("movies", i['type'].count("Movie"), "\ntv_shows", i['type'].count("TV Show"))
        print("Service_name" + "-" + "Movie")
        for i in lt.iterator(respuesta[0]):
            print("Netflix "+"- ", i['platform'].count("Netflix"), "\nAmazon ","- ", i['platform'].count("Amazon"), "\nHulu ","- ", i['platform'].count("Hulu"), "\nDisney ","- ",i['platform'].count("Disney"))
        print("Listed_in"+"-"+"Count")
        lista=[]
        for i in lt.iterator(respuesta[0]):
            if x<= 3 or x>lt.size(respuesta[0])-3:
                lista=i['listed_in'].split(",")
                for l in range(len(lista)):
                    print(lista[l], i['listed_in'].count(lista[l]))
            x += 1
        x=1
        print("title - release_year - director - stream_service - type - duration - cast - country - rating - listed_in - description")
        for i in lt.iterator(respuesta[0]):
            if x<= 3 or x>lt.size(respuesta[0])-3:
                print(i['title'],'-', i['release_year'],'-', i['director'],'-', i['platform'],'-', i['type'],'-', i['duration'],'-', i['cast'],'-', i['country'],'-', i['rating'],'-', i['listed_in'], '-', i['description'])
            x += 1
        print(str(respuesta[1])+' milisegundos.')
    
    elif inputs == 10:
        print('1. shell')
        print('2. insertion')
        print('3. selection')
        print("4. merge")
        print("5. quick")
        ordenamiento = int(input('ingrese el ordenaiento que desee usar: '))

    elif inputs== 0:
        sys.exit(0)

    else:
        continue
sys.exit(0)