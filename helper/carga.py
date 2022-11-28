# -*- coding: utf-8 -*-
import csv
def carga_datos(): 
    a = open('datos.csv','r')
    t =  []
    for i in csv.reader(a):
        t.append(i)
    nombre_medicamento = t[0]
    cantidad_medicamento =t[2]        
    cod_medicamento = t[4]
    riesgo = t[6]
    for i in range(len(cod_medicamento)):
        cantidad_medicamento[i]=int(cantidad_medicamento[i])
        cod_medicamento[i]=int(cod_medicamento[i])
    a.close()
    return nombre_medicamento, cantidad_medicamento,cod_medicamento,riesgo