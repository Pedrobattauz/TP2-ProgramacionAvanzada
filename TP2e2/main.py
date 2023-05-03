# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:54:05 2023

@author: pedro
"""

import numpy as np
import random,math
import matplotlib.pyplot as plt
# from funciones import aw_manzana
# , aw_papa, aw_zanahoria, aw_verduras,aw_frutas, aw_total,aw_kiwi,

class DetectorAlimento:
    """clase que representa un conjunto de sensores de la cinta transportadora
    para detectar el tipo de alimento y su peso.
    """
    def _init_(self):
        self.alimentos = ["kiwi", "manzana", "papa", "zanahoria", "undefined"]
        self.peso_alimentos = np.round(np.linspace(0.05, 0.6, 12),2)
        self.prob_pesos = np.round(self.__softmax(self.peso_alimentos)[::-1], 2)

    def __softmax(self, x):
        """función softmax para crear vector de probabilidades 
        que sumen 1 en total
        """
        return (np.exp(x - np.max(x)) / np.exp(x - np.max(x)).sum())

    def detectar_alimento(self):
        """método que simula la detección del alimento y devuelve un diccionario
        con la información del tipo y el peso del alimento.
        """
        n_alimentos = len(self.alimentos)
        alimento_detectado = self.alimentos[random.randint(0, n_alimentos-1)]
        peso_detectado = random.choices(self.peso_alimentos, self.prob_pesos)[0]
        return {"alimento": alimento_detectado, "peso": peso_detectado}
    
if __name__ == "_main_":
    
    n=int(input('Ingrese la cantidad de alimentos:'))
    random.seed(1)
    sensor = DetectorAlimento()
    lista_pesos = []
    for _ in range(n):
        lista_pesos.append(sensor.detectar_alimento()["peso"])
    # plt.hist(lista_pesos, bins=12)
    # plt.show()
    # lista_alimentos = []
    # for _ in range(n):
    #     lista_alimentos.append(sensor.detectar_alimento()["alimento"])
    # print(lista_pesos)
    # print(lista_alimentos)