# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:17:56 2020

@author: 57301
"""
def info_sistema(cod_medicamento,nombre_medicamento,riesgo):
    for i in range(len(riesgo)):
        a = [nombre_medicamento[i],cod_medicamento[i],riesgo[i]]
        print('Medicamento,Código,Clasificación')
        print(a)