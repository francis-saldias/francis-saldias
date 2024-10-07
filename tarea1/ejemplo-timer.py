#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplo de calculo de tiempo de demora usando el módulo datetime
y la función sleep del módulo time

@author: José Urzúa jose@urzua.cl
"""
# Ejemplo de uso de calculo de tiempo de procesamiento

# importamos módulo datetime
from datetime import datetime
from time import sleep


# obtenemos el datetime actual y lo almacenamos en variable start
start = datetime.now()
print("Hola mundo!")
# Acá debería ir todo el procesamiento de su programa
# - obtener definicion para primera pregunta, preguntar, recibir respuesta,
# comparar, etc

# simulamos una demora de 2 segundos
sleep(2)

# obtenemos el datetime actual y lo almacenamos en variable end
end = datetime.now()

# calculamos la demora en segundos
demora = (end - start).total_seconds()

print("Demora:", demora)