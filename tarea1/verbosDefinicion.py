#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo que carga en memoria un listado de verbos en inglés con su definición 
en español desde el archivo verbos-definicion.txt.
Provee las funciones para obtener de forma aleatoria una definición y para 
obtener el verbo correspondiente para una definición dada como argumento.

@author: José Urzúa jose@urzua.cl
"""

import random

verbosDefinicion = dict()
try:
    archivo = open("verbos-definicion.txt", "r", encoding="utf-8")
    for linea in archivo:
        datos = linea.split(":")
        verbosDefinicion[datos[1]] = datos[0]
    archivo.close()
except FileNotFoundError:
        print("[No se pudo abrir archivo verbos-definicion.txt]")
        
# generamos una copia del diccionario
# sobre esta copia se obtienen definicions y se eliminan para no repetir
copia = verbosDefinicion.copy()

# getDefinicion: none -> str
# obtiene una definicion de forma aleatoria del diccionario
# y la elimina para no retornarla en nuevas llamadas
def getDefinicion():
    indice = random.randint(0, len(copia)-1)
    definicion = (list(copia.keys()))[indice]
    del copia[definicion]
    return definicion

# getVerbo: str -> str
# retorna el verbo en inglés de una definicion dada como argumento
def getVerbo(definicion):
    return (verbosDefinicion[definicion]).strip().lower()