# -*- coding: utf-8 -*-
import helper.err as err
def inventario(nombre_medicamento,cantidad_medicamento,cod_medicamento):
    vac = 0
    a = 0
    print('Elija una opción:')
    while a !=4:
        a=input('1)Inventario General \n2)Stock medicamento específico \n3)Medicamentos agotados\n4)Regresar al menú inicial \nElegir:'  )
        v,a = err.error_menu(a)
        if v == True:
            if a ==1:
                print('\nMedicamento \tCantidad')
                for i in range(len(cantidad_medicamento)):
                    print(nombre_medicamento[i]+'\t ',cantidad_medicamento[i])
            if a==2:
                code=99
                while code!=0:
                    print('\nPor favor, ingrese el código del medicamento que desea consultar o 0 para regresar al menú de inventario:')
                    code=input('Digite el código:')
                    y,code = err.error_menu(code)
                    if y==True:
                        z= err.error_codigo(cod_medicamento,code)
                        if z==True:
                            idx=cod_medicamento.index(code) #indice del medicamento buscado
                            print('Medicamento \tCantidad')
                            print(nombre_medicamento[idx]+'\t ',cantidad_medicamento[idx])  
                        else:
                            if code==0:
                                print('\nRegresando al menú de inventario')
                            else:
                                print('\nOpción invalida')
                    else:
                        print('\nOpción invalida')
            if a==3:
                print('Se mostrarán los medicamentos agotados en este carro')
                print('Nombre \tCodigo\n')
                for i in range(len(nombre_medicamento)):
                    if cantidad_medicamento[i]==0:
                        print(nombre_medicamento[i]+'\t',cod_medicamento[i])  
                    else:
                        vac+=1 #contador de medicamentos que si tienen stock
                if vac ==len(nombre_medicamento): 
                    print('No hay medicamentos agotados')
            if a==4:
                print('\nRegresando al menú principal...')
        else:
            print('\nRegresando al menú de inventario...')