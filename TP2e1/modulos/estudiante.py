# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:43:40 2022

@author: matia
"""
from persona import Persona


class Estudiante(Persona):
    def __init__ (self,p_nom_p, p_ape_p, p_dni): 
        super().__init__(p_nom_p, p_ape_p, p_dni)
        self.listaCursos=[]

    
    def asistir(self, curso):
        for elemento in self.listaCursos: 
            if elemento in self.listaCursos: 
                break 
            else: 
                self.listaCursos.append(curso)