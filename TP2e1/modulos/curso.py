# -*- coding: utf-8 -*-
"""

@author:gina y pedro
"""

class Curso:
    def __init__(self, p_nombre_curso, p_profesor, p_dpto):
        self.nombre_curso = p_nombre_curso
        self.profesor_a_cargo= p_profesor
        self.estudiantes_curso= []
        self.dpto= p_dpto
        
        
    def agregar_estudiante(self, Estudiante):
        self.estudiantes_curso.append(Estudiante)
        
    