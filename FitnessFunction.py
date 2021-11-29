#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritos Evolutivos
Alumno: Tu Nombre
Profesor: Dr. Asdrúbal López Chau
Descripción: Función de aptitud para el problema de adivina contraseña
Regresa el número de coincidencias entre el objetivo y el individuo.
Futuro: Regresa la posición de las coindicencias

Created on Wed Sep  1 14:50:23 2021

@author: asdruballopezchau
"""

from Individuo import Individuo
import numpy as np
class FitnessFunction:
    inovaciones = 0#Variables de Clase
    def __init__(self, objetivo):
        '''Función objetivo para el problema "Adivina contraseña".
        objetivo: Una cadena
        '''
        self.objetivo = objetivo
        
    def fitness(self, individuo):
        FitnessFunction.inovaciones
        coincidencias = 0
        i = 0
        #futuro = np.zeros(len(self.objetivo)) # Siguiente versión
        for letra in individuo.genes:
            if self.objetivo[i] == letra:
                coincidencias += 1
                
                #  futuro[i] = 1. # Siguiente versión
            self.inovaciones += 1
            i += 1
        return coincidencias
            