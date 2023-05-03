# -*- coding: utf-8 -*-
"""
@author:gina y pedro
"""

from modulos.curso import Curso 
from modulos.departamento import Departamento 

from modulos.estudiante import Estudiante
from modulos.profesor import Profesor
from modulos.universidad import Universidad 

#Creo el profesor
profe=Profesor("Juan","Benitez", "444444")

#Se crea el departamento Informatica
dptoI=Departamento("Informàtica", profe)

#Creo la universidad
miUniversidad=Universidad(dptoI)


#Creo el estudiante 
alumno = Estudiante("Pedro","Aries", "55555")

#Pedro se inscribe a la universidad 
miUniversidad.AgregarEstudiante(alumno)



#se crea el profesor Jose Benito 
profe2=Profesor("Jose","Benito", "5555")

#Se agrega profesor al departamento Informatica 
dptoI.agregarProfesor(profe2) 


#Se crea el curso Programacion Avanzada
progra_Avanzada= Curso("Programacion Avanzada", profe2, dptoI)

#Jose Benito enseña en Programacion Avanzanda
profe2.enseñar(progra_Avanzada)

#Pedro, el alumno, asiste a Programacion Avanzada 
alumno.asistir(progra_Avanzada)

