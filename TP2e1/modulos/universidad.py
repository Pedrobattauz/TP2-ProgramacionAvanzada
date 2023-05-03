# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:43:46 2022

@author: matia
"""
from departamento import Departamento
class Universidad:
    def __init__ (self, p_departamentos): 
        self.listaDeDep = ["Informatica"]
        self.listaEstudiantes= []
        
        
        
    def AgregarEstudiante(self, Estudiante): 
        self.listaEstudiantes.append(Estudiante)
        
    def AgregarDepartamento (self, Departamento): 
        self.listaDeDep.append(Departamento)