# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:42:47 2022

@author: matia
"""

class Departamento:
    def __init__(self, p_nombre_dpto, p_director):
        self.nombre_dpto = p_nombre_dpto
        self.director = p_director
        self.lista_profesores=[]
    
    def agregarProfesor (self,profesor):
        self.lista_profesores.append(profesor)
  
    
    def asignarDirector (self, Profesor):
        self.director=Profesor
    