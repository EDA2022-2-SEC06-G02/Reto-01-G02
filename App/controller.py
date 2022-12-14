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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def newController(entero):
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog(entero)
    return control

def loadData(control, archivo):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    Amazon = loadAmazon(catalog, archivo)
    Disney = loadDisney(catalog, archivo)
    Hulu = loadHulu(catalog, archivo)
    Netflix = loadNetflix(catalog, archivo)
    return Amazon, Disney, Hulu, Netflix

    

def loadAmazon(catalog, archivo):
    """
    
    """
    titlesfile = cf.data_dir + 'Streaming/amazon_prime_titles-utf8-'+archivo+'.csv'
    input_file = csv.DictReader(open(titlesfile, encoding='utf-8'))
    for title in input_file:
        model.addAmazon(catalog, title)
    return model.AmazonSize(catalog)


def loadDisney(catalog, archivo):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    titlesfile = cf.data_dir + 'Streaming/disney_plus_titles-utf8-'+archivo+'.csv'
    input_file = csv.DictReader(open(titlesfile, encoding='utf-8'))
    for title in input_file:
        model.addDisney(catalog, title)
    return model.DisneySize(catalog)


def loadHulu(catalog, archivo):
    """
    Carga la información que asocia tags con libros.
    """
    titlesfile = cf.data_dir + 'Streaming/hulu_titles-utf8-'+archivo+'.csv'
    input_file = csv.DictReader(open(titlesfile, encoding='utf-8'))
    for title in input_file:
        model.addHulu(catalog, title)
    return model.HuluSize(catalog)


def loadNetflix(catalog, archivo):
    """
    Carga la información que asocia tags con libros.
    """
    titlesfile = cf.data_dir + 'Streaming/netflix_titles-utf8-'+archivo+'.csv'
    input_file = csv.DictReader(open(titlesfile, encoding='utf-8'))
    for title in input_file:
        model.addNetflix(catalog, title)
    return model.NetflixSize(catalog)


def sublist(tamaño, catalog):
    
    return model.sublist(tamaño, catalog)

def representacionDatos(entero):
    
    return model.RepresentacionDatos(entero)

def requerimiento1(catalog, fecha1, fecha2, sort):
    
    return model.requerimiento1(catalog, fecha1, fecha2, sort)

def requerimiento2(catalog, fecha1, fecha2, sort):
    
    return model.requerimiento2(catalog, fecha1, fecha2, sort)

def requerimiento3(catalog, actor, sort):
    
    return model.requerimiento3(catalog, actor, sort)

def requerimiento4(catalog, genero, sort):
    
    return model.requerimiento4(catalog, genero, sort)

def requerimiento5(catalog, country, sort):

    return model.requerimiento5(catalog, country, sort)

def requerimiento6(catalog, director, sort):
    
    return model.requerimiento6(catalog, director, sort)

def requerimiento7(catalog, sort):

    return model.requerimiento7(catalog, sort)