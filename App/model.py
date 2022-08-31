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
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {
        "Amazon": lt.newList('SINGLE_LINKED', cmpfunction=compare_name),
        "Disney": lt.newList('SINGLE_LINKED', cmpfunction=compare_name),
        "Hulu": lt.newList('SINGLE_LINKED', cmpfunction=compare_name),
        "Netflix": lt.newList('SINGLE_LINKED', cmpfunction=compare_name),
        "TV_Shows": lt.newList('SINGLE_LINKED', cmpfunction=compare_name),
        "Movies": lt.newList('SINGLE_LINKED', cmpfunction=compare_name),
        "All": lt.newList('SINGLE_LINKED', cmpfunction=compare_name)
                }

    return catalog

# Funciones para agregar informacion al catalogo

def addAmazon(catalog, title):
    type = title['type']
    lt.addLast(catalog['All'], title)
    lt.addLast(catalog['Amazon'], title)
    if type == 'TV Show':
        lt.addLast(catalog['TV_Shows'], title)
    else:
        lt.addLast(catalog['Movies'], title)
    return catalog

def addDisney(catalog, title):
    type = title['type']
    lt.addLast(catalog['All'], title)
    lt.addLast(catalog['Disney'], title)
    if type == 'TV Show':
        lt.addLast(catalog['TV_Shows'], title)
    else:
        lt.addLast(catalog['Movies'], title)
    return catalog

def addHulu(catalog, title):
    type = title['type']
    lt.addLast(catalog['All'], title)
    lt.addLast(catalog['Hulu'], title)
    if type == 'TV Show':
        lt.addLast(catalog['TV_Shows'], title)
    else:
        lt.addLast(catalog['Movies'], title)
    return catalog

def addNetflix(catalog, title):
    type = title['type']
    lt.addLast(catalog['All'], title)
    lt.addLast(catalog['Netflix'], title)
    if type == 'TV Show':
        lt.addLast(catalog['TV_Shows'], title)
    else:
        lt.addLast(catalog['Movies'], title)
    return catalog

# Funciones para creacion de datos

def SortList(lista):
    ordenado = sa.sort(lista, compare_title)
    return ordenado

# Funciones de consulta

def requerimiento1(catalog, fecha1, fecha2):
    movies = catalog['Movies']
    x = lt.newList('SINGLE_LINKED')
    
    for movie in lt.iterator(movies):
        if int(movie['release_year']) >= fecha1 and int(movie['release_year']) <= fecha2:
            lt.addLast(x, movie)
    
    respuesta = sa.sort(x, compare_title)      
    return respuesta

def requerimiento2(catalog, fecha1, fecha2):
    movies = catalog['TV_Shows']
    x = lt.newList('SINGLE_LINKED')
    
    for movie in lt.iterator(movies):
        if int(movie['release_year']) >= fecha1 and int(movie['release_year']) <= fecha2:
            lt.addLast(x, movie)
    
    respuesta = sa.sort(x, compare_title)      
    return respuesta
        


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

def compare_name(author1, author2):
    if author1['title'].lower() == author2['title'].lower():
        return 0
    elif author1['title'].lower() > author2['title'].lower():
        return 1
    return -1

def compare_title(title1, title2):
    if int(title1['release_year']) == int(title2['release_year']):
        if title1['title'] == title2['title']:
            return title1['duration'] < title2['duration']
        return title1['title'] < title2['title']
    return int(title1['release_year']) < int(title2['release_year'])