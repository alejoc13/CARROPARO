# -*- coding: utf-8 -*-
import csv
import helper.err as err
def escritura_datos(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo):
    cad = [nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo]
    a = open('datos.csv','w')
    escri = csv.writer(a)
    escri.writerows(cad)
    a.close()
def registro(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo):
    a = 0
    while a !=3: 
        a = input('1)Para ingresar un medicamento al sistema \n2)Para eliminar un medicamento del sistema \n3)Para volver al menu inicial \nElegir:')
        v,a = err.error_menu(a)
        if  v == True: 
            if a ==1:
                y = False
                while y==False:  #control del nombre, valores alfanumericos, no solo numericos
                    n = input('Ingrese el nombre del medicamento:')
                    y,n = err.error_nombre(n)
                y = False
                while y==False: #control de codigo, solo numérico
                    c = input('Ingrese el codigo del medicamento:')
                    y,c = err.error_menu(c)
                    if y == False:
                        print('\nEl sistema solo reconoce codigos de medicamento numéricos') 
                g = 0
                while g!=1: #Control para el tipo de riesgo
                    r = input('ingrese el nivel de riesgo del medicamento:')
                    if r == 'Alto' or r == 'ALTO' or r== 'alto':
                        g = g+1
                        r = 'Alto'
                    if r == 'Bajo' or r == 'BAJO' or r== 'bajo':
                        g = g+1
                        r = 'Bajo'
                    if g !=1:
                        print('Las opciones validas para ingresar son: Alto o Bajo')
                conf=err.control_ingreso(c,cod_medicamento,n,nombre_medicamento)
                if conf==True:
                    n=n.capitalize()
                    nombre_medicamento.append(n)
                    cod_medicamento.append(c)
                    riesgo.append(r)
                    cantidad_medicamento.append(0)
                    print('\nLa cantidad del medicamento se iniciará como 0 \nSi desea aumentarlas hagalo desde el menú de abastesimiento')
                    print('\nMedicamento agregado')
            if  a == 2:
                code=input('Digite el código:')
                y,code = err.error_menu(code)
                if y==True:
                    z= err.error_codigo(cod_medicamento,code)
                    if z==True:
                        idx=cod_medicamento.index(code)
                        nombre_medicamento.pop(idx)
                        cod_medicamento.pop(idx)
                        cantidad_medicamento.pop(idx)
                        riesgo.pop(idx)
                        print('\nEliminando medicamento, por favor espere....\nMedicamento eliminado')
                    else:
                        print('\nResgresando al menú de registro,espere... ')
        else:
            print('\nLas opciones validas a ingresar son los numeros 1,2 ó 3. No los nombres de las opciones')
    print('\n Regresando al menú principal espere por favor')
    return nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo