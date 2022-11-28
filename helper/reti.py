# -*- coding: utf-8 -*-
import helper.escri as escri
import helper.err as err
import helper.sonido as sonido
def retirar_medicamento(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo):
    msj1 = '!Alerta¡ el medicamento acaba de agotarse'
    msj2 = 'El medicamento está agotado'
    code = 100
    while code!=0:
        code=input('Ingrese 0 para salir al menú princial o el código de un medicamento para seguir retirando medicamentos:')
        y,code = err.error_menu(code)
        if y == True:
            z = err.error_codigo(cod_medicamento,code)
            if z == True:
                idx = cod_medicamento.index(code)
                if cantidad_medicamento[idx]>0:
                    cantidad_medicamento[idx]-=1
                    sonido.alerta_sonora(idx,riesgo)
                    escri.escritura_datos(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo)
                    print('\nEl medicamento retirado es:'+nombre_medicamento[idx]+'\nLa cantidad ahora es:',cantidad_medicamento[idx])
                    if riesgo[idx] == 'Alto':
                        print('\nEstá retirando un medicamento que se considera de alto riesgo \nverifique las dosis a suministrar')
                    if cantidad_medicamento[idx]==0:
                        print(msj1)
                else:
                    print(msj2)     
            if code ==0:
                print('Guardando los cambios...espere')
                escri.escritura_datos(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo)
                print('Volviendo al menu inicial')
    return nombre_medicamento,cantidad_medicamento,cod_medicamento