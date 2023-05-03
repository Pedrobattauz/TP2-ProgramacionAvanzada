# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:03:59 2023

@author: pedro
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from modulos.funciones import aw_manzana, aw_kiwi, aw_papa, aw_zanahoria
from flask import Flask, render_template, request
app=Flask(__name__)

class DetectorAlimento:
    """clase que representa un conjunto de sensores de la cinta transportadora
    para detectar el tipo de alimento y su peso.
    """
    def __init__(self):
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
    

if __name__ == "__main__":
    n=0
    
      
    @app.route("/",methods=['GET', 'POST'])
    def raiz():
        global awm, awk, awp, awz, cantidad
        if request.method == 'POST':
            
         n = int(request.form['cantidad'])
         sensor = DetectorAlimento()
         lista_pesos = []
         
         for _ in range(n):
             lista_pesos.append(sensor.detectar_alimento()["peso"])
         lista_alimentos=[]
         for _ in range(n):
             
             lista_alimentos.append(sensor.detectar_alimento()["alimento"])
             awm=(aw_manzana(lista_alimentos,lista_pesos))
             awk=(aw_kiwi(lista_alimentos, lista_pesos))
             awp=(aw_papa(lista_alimentos, lista_pesos))
             awz=(aw_zanahoria(lista_alimentos,lista_pesos))
             
             return render_template("home.html", awm=awm, awk=awk, awp=awp, awz=awz, n=cantidad) 
         
         if request.method=='GET':
             
             return render_template("home.html")
    # # random.seed(1)
    # sensor = DetectorAlimento()
    # lista_pesos = []

    # plt.hist(lista_pesos, bins=12)
    # plt.show()
    # print(lista_pesos)
    # print(lista_alimentos)


    if __name__ =="__main__":
        
        app.run(debug=False)