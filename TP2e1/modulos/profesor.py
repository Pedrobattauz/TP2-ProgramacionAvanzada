# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:43:27 2022

@author: matia
"""
from persona import Persona
class Profesor(Persona) :
    def __init__(self,p_nom_p, p_ape_p, p_dni):
        super().__init__(p_nom_p, p_ape_p, p_dni)
        self.ListaCursosACargo=[]
   
    def get_nombre(self):
        return self.nombre
    
    def enseñar(self,curso):
        self.ListaCursosACargo.append(curso)