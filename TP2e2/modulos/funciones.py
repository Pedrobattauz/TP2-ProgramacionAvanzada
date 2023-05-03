

# -- coding: utf-8 --
"""
Created on Mon May  1 11:56:08 2023

@author: pedro
"""
import math

def aw_manzana(lista_nombre,lista_peso):
    for i in range(len(lista_nombre)):
        if lista_nombre[i]=='manzana':
            m=lista_peso[i]
            Manzana=0.97*((0.066*m)*2)/(1+(0.066*m)*2)
            AwManzana=[]
            AwManzana.append(Manzana)
    aw_manzana_promedio=sum(AwManzana)/len(AwManzana)
    return round(aw_manzana_promedio,2)

def aw_kiwi(lista_nombre,lista_peso):
    for i in range(len(lista_nombre)):
        if lista_nombre[i]=='kiwi':
            m=lista_peso[i]
            Kiwi=0.96*(1-(math.e)*-0.055*m)/(1+(math.e)*-0.055*m)
            AwKiwi=[]
            AwKiwi.append(Kiwi)
    aw_kiwi_promedio=sum(AwKiwi)/len(AwKiwi)
    return round(aw_kiwi_promedio,2)

def aw_papa(lista_nombre,lista_peso):
    for i in range(len(lista_nombre)):
        if lista_nombre[i]=='papa':
            m=lista_peso[i]
            Papa=0.66*math.atan(0.055*m)
            AwPapa=[]
            AwPapa.append(Papa)
    aw_papa_promedio=sum(AwPapa)/len(AwPapa)
    return round(aw_papa_promedio,2)

def aw_zanahoria(lista_nombre,lista_peso):
    for i in range(len(lista_nombre)):
        if lista_nombre[i]=='zanahoria':
            m=lista_peso[i] 
            Zanahoria=0.96*(1-math.e**(-0.1*m))
            AwZanahoria=[]
            AwZanahoria.append(Zanahoria)
    aw_zanahoria_promedio=sum(AwZanahoria)/len(AwZanahoria)
    return round(aw_zanahoria_promedio,2)

def aw_verduras(lista_nombres,lista_pesos):
    for i in range(len(lista_nombres)):
        AwVerduras=[]
        if lista_nombres[i]=='papa':
            m=lista_pesos[i]
            Papa=0.66*math.atan(0.055*m)
            AwVerduras.append(Papa)
        if lista_nombres[i]=='zanahoria':
            m=lista_pesos[i]
            Zanahoria=0.96*(1-math.e**(-0.1*m))
            AwVerduras.append(Zanahoria)
    aw_verduras_promedio=sum(AwVerduras)/len(AwVerduras)
    return aw_verduras_promedio
            
        
            
            
def aw_frutas(lista_nombres,lista_pesos):
    for i in range(len(lista_nombres)):
        AwFrutas=[]
        if lista_nombres[i]=='kiwi':
            m=lista_pesos[i]
            Kiwi=0.96*(1-(math.e)*-0.055*m)/(1+(math.e)*-0.055*m)
            AwFrutas.append(Kiwi)
        if lista_nombres[i]=='manzana':
            m=lista_pesos[i]
            Manzana=0.97*((0.066*m)*2)/(1+(0.066*m)*2)
            AwFrutas.append(Manzana)
    aw_frutas_promedio=sum(AwFrutas)/len(AwFrutas)
    return aw_frutas_promedio

def aw_total(lista_nombres,lista_pesos):
    AwTotal=[]
    for i in range(len(lista_nombres)):
        if lista_nombres[i]=='manzana':
            m=lista_pesos[i]
            Manzana=0.97*((0.066*m)*2)/(1+(0.066*m)*2)
            AwTotal.append(Manzana)
        elif lista_nombres[i]=='kiwi':
            m=lista_pesos[i]
            Kiwi=0.96*(1-(math.e)*-0.055*m)/(1+(math.e)*-0.055*m)
            AwTotal.append(Kiwi)
        elif lista_nombres[i]=='papa':
            m=lista_pesos[i]
            Papa=0.66*math.atan(0.055*m)
            AwTotal.append(Papa)
        elif lista_nombres[i]=='zanahoria':
            m=lista_pesos[i] 
            Zanahoria=0.96*(1-math.e**(-0.1*m))
            AwTotal.append(Zanahoria)
    aw_total=sum(AwTotal)/len(AwTotal)
    return aw_total
    