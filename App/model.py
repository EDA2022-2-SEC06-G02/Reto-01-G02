"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from gettext import Catalog
from turtle import title
import time
from datetime import date
from datetime import datetime
from App.controller import representacionDatos
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ns
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(entero):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    estructura = representacionDatos(entero)
    catalog = {
        "Amazon": lt.newList(estructura, cmpfunction = compare_name),
        "Disney": lt.newList(estructura, cmpfunction = compare_name),
        "Hulu": lt.newList(estructura, cmpfunction = compare_name),
        "Netflix": lt.newList(estructura, cmpfunction = compare_name),
        "TV_Shows": lt.newList(estructura, cmpfunction = compare_name),
        "Movies": lt.newList(estructura, cmpfunction = compare_name),
        "All": lt.newList(estructura, cmpfunction = compare_name)
                }

    return catalog

# Funciones para agregar informacion al catalogo

def addAmazon(catalog, title):
    type = title['type']
    title['platform'] = 'Amazon'
    lt.addLast(catalog['All'], title)
    lt.addLast(catalog['Amazon'], title)
    if type == 'TV Show':
        lt.addLast(catalog['TV_Shows'], title)
    else:
        lt.addLast(catalog['Movies'], title)
    
    return catalog

def addDisney(catalog, title):
    type = title['type']
    title['platform'] = 'Disney'
    lt.addLast(catalog['All'], title)
    lt.addLast(catalog['Disney'], title)
    if type == 'TV Show':
        lt.addLast(catalog['TV_Shows'], title)
    else:
        lt.addLast(catalog['Movies'], title)
    return catalog

def addHulu(catalog, title):
    type = title['type']
    title['platform'] = 'Hulu'
    lt.addLast(catalog['All'], title)
    lt.addLast(catalog['Hulu'], title)
    if type == 'TV Show':
        lt.addLast(catalog['TV_Shows'], title)
    else:
        lt.addLast(catalog['Movies'], title)
    return catalog

def addNetflix(catalog, title):
    type = title['type']
    title['platform'] = 'Netflix'
    lt.addLast(catalog['All'], title)
    lt.addLast(catalog['Netflix'], title)
    if type == 'TV Show':
        lt.addLast(catalog['TV_Shows'], title)
    else:
        lt.addLast(catalog['Movies'], title)
    return catalog

# Funciones para creacion de datos

def SortList(lista, sort, cmpfunction):
    if sort != 1 or sort!= 2 or sort != 3 or sort != 4 or sort != 5:
        return sa.sort(lista, cmpfunction)
    
    else:
        if sort  == 1:
            return ss.sort(lista, cmpfunction)
        
        elif sort  == 2:
            return ns.sort(lista, cmpfunction)
        
        elif sort  == 3:
            return sa.sort(lista, cmpfunction)
        
        elif sort == 4:
            return ms.sort(lista, cmpfunction)
        
        elif sort == 5:
            return qs.sort(lista, cmpfunction)

def sublist(tamaño, catalog):
        suball = lt.subList(catalog['All'], 1, tamaño)
        return suball
        

def RepresentacionDatos(entero):
    if entero == 1:
        return 'SINGLE_LINKED'
    elif entero == 2:
        return 'ARRAY_LIST'
    else: 
        return None

# Funciones de consulta

def requerimiento1(catalog, fecha1, fecha2, sort):
    movies = catalog['Movies']
    x = lt.newList('SINGLE_LINKED')
    start_time = getTime()
    for movie in lt.iterator(movies):
        if int(movie['release_year']) >= fecha1 and int(movie['release_year']) <= fecha2:
            lt.addLast(x, movie)
    respuesta = SortList(x, sort, compare_year)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)     
    return respuesta, delta_time

def requerimiento2(catalog, fecha1, fecha2, sort):
    movies = catalog['TV_Shows']
    x = lt.newList('SINGLE_LINKED')
    fecha1 = datetime.strptime(fecha1, '%Y-%m-%d')
    fecha2 = datetime.strptime(fecha2, '%Y-%m-%d')
    start_time = getTime()
    for i in lt.iterator(movies):
        if i['date_added'] != '':
            fecha = datetime.strptime(i['date_added'], '%Y-%m-%d')
            if fecha >= fecha1 and fecha <= fecha2:
                lt.addLast(x, i)
    ordenado = SortList(x, sort, compare_date)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time) 
    return ordenado, delta_time   
    
def requerimiento3(catalog, actor, sort):
    all = catalog['All']
    x = lt.newList('SINGLE_LINKED')
    start_time = getTime()
    for i in lt.iterator(all):
        actores = i['cast'].split(', ')
        if actor in actores:
            lt.addLast(x, i)
    ordenado = SortList(x, sort, compare_title)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time) 
    return ordenado, delta_time

def requerimiento4(catalog, genero, sort):
    all = catalog['All']
    x = lt.newList('SINGLE_LINKED')
    start_time = getTime()
    for i in lt.iterator(all):
        generos = i['listed_in'].split(', ')
        if genero in generos:
            lt.addLast(x, i)
    ordenado = SortList(x, sort, compare_title)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return ordenado, delta_time

def requerimiento5(catalog, country, sort):
    all = catalog["All"]
    x = lt.newList("SINGLE_LINKED")
    start_time = getTime()
    
    for i in lt.iterator(all):
        countries = i["country"]
        if country in countries:
            lt.addLast(x, i)
    
    ordenado = SortList(x, sort, compare_title)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    
    return ordenado, delta_time

def requerimiento6(catalog, director, sort):
    all = catalog['All']
    x = lt.newList('SINGLE_LINKED')
    start_time = getTime()
    for i in lt.iterator(all):
        if director == i["director"]:
            lt.addLast(x, i)
    respuesta = SortList(x, sort, compare_date)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return respuesta, delta_time

def requerimiento7(catalog, sort):
    all = catalog["All"]
    x = lt.newList("SINGLE_LINKED")
    start_time = getTime()

    for i in lt.iterator(all):
        generos = i["listed_in"].split(", ")
        for j in generos:
            counted = generos.count(j)
            lt.addLast(x, counted)
    
    respuesta = SortList(x, sort, compare_number)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)

    return respuesta, delta_time 


def AmazonSize(catalog):
    
    return lt.size(catalog['Amazon'])

def DisneySize(catalog):
    
    return lt.size(catalog['Disney'])

def HuluSize(catalog):
    
    return lt.size(catalog['Hulu'])

def NetflixSize(catalog):
    
    return lt.size(catalog['Netflix'])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compare_number(n1, n2):
    if n1 == n2:
        return 0

    elif n1 > n2:
        return 1
    
    else:
        return -1


def compare_name(author1, author2):
    if author1['title'].lower() == author2['title'].lower():
        return 0
    elif author1['title'].lower() > author2['title'].lower():
        return 1
    return -1

def compare_year(title1, title2):
    if int(title1['release_year']) == int(title2['release_year']):
        if title1['title'] == title2['title']:
            return title1['duration'] < title2['duration']
        return title1['title'] < title2['title']
    return int(title1['release_year']) < int(title2['release_year'])

def compare_title(title1, title2):
    if title1['title'] == title2['title']:
        if title1['release_year'] == title2['release_year']:
            return title1['duration'] < title2['duration']
        return title1['release_year'] < title2['release_year']
    return title1['title'] < title2['title']

def compare_date(title1, title2):
    fecha1 = datetime.strptime(title1['date_added'], '%Y-%m-%d')
    fecha2 = datetime.strptime(title2['date_added'], '%Y-%m-%d')
    if fecha1 == fecha2:
        if title1['title'] == title2['title']:
            return title1['duration'] < title2['duration']
        return title1['title'] < title2['title']
    return fecha1 < fecha2

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed