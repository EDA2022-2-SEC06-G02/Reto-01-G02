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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'show_id': None,
               'type': None,
               'title': None,
               'director': None,
               'cast': None,
               'country': None,
               'date_added': None,
               'release_year': None,
               'rating': None,
               'duration': None,
               'listed_in': None,
               'description': None}

    catalog['show_id'] = lt.newList('ARRAY_LIST')

    catalog['type'] = lt.newList('SINGLE_LINKED')
                               
    catalog['title'] = lt.newList('SINGLE_LINKED')
                                
    catalog['director'] = lt.newList('ARRAY_LIST')

    catalog['cast'] = lt.newList('ARRAY_LIST')

    catalog['country'] = lt.newList('ARRAY_LIST')

    catalog['date_added'] = lt.newList('ARRAY_LIST')

    catalog['release_year'] = lt.newList('ARRAY_LIST')

    catalog['rating'] = lt.newList('ARRAY_LIST')

    catalog['duration'] = lt.newList('ARRAY_LIST')

    catalog['listed_in'] = lt.newList('ARRAY_LIST')

    catalog['description'] = lt.newList('ARRAY_LIST')

    return catalog