# -*- coding: utf-8 -*-
import helper.escri as escri
import helper.err as err
def entrada_medicamento(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo):
    code = 100
    while code!=0:
        code=input('Ingrese 0 para salir al menú princial o el código de un medicamento para continuar abastesiendo:')
        y,code = err.error_menu(code)
        if y== True:
            z = err.error_codigo(cod_medicamento,code)
            if z==True:
                idx=cod_medicamento.index(code)
                cantidad_medicamento[idx]+=1
                escri.escritura_datos(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo)
                print('El medicamento que ingresó es:'+nombre_medicamento[idx]+'\nLa cantidad ahora es:',cantidad_medicamento[idx])
        if code==0:
            print('Guardando los cambios...espere')
            escri.escritura_datos(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo)
            print('Volviendo al menu inicial')
    return nombre_medicamento,cantidad_medicamento,cod_medicamento