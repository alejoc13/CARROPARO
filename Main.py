# -*- coding: utf-8 -*-
import helper.carga as carga #importar la carga de datos
import helper.invent as invent #modulo del iventario en sus distintos formatos
import helper.reti as reti #modulo de retirado de medicamentos
import helper.abast as abast #modulo de abastecimiento del carro
import helper.err as err #control de errores de escrituras cuando se ejecuta el codigo,evita qeu el codigo se caiga
import helper.inf as inf #encargado de dar la información de nombre,codigo,riesgo de cada medicamento(siempre todos)
import helper.escri as escri #escritura y modificación de los archivos de medicamentos
def run():
    print('Cargando los datos del sistema, por favor espere\n')
    print('Bienvenido al sistema de control de medicamentos \nPor favor, elija una opción para continuar:')
    nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo = carga.carga_datos()
    a = 0
    while a!=6:
        a=input('1)Retiro de medicamentos \n2)Ingreso de medicamentos \n3)Consulta de inventario \n4)Información \n5)Registro \n6)Salir del sistema \nElegir:')
        v,a = err.error_menu(a)
        if v == True:
            if a == 1:
                print('\nBienvenido al modo de retiro de medicamentos')
                nombre_medicamento,cantidad_medicamento,cod_medicamento = reti.retirar_medicamento(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo)
            if a==2:
                print('\nBienvenido al sistema de abastecimiento del carro')
                nombre_medicamento,cantidad_medicamento,cod_medicamento = abast.entrada_medicamento(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo)
            if a==3:
                print('\nBienvenido al sistema de inventario del carro')
                invent.inventario(nombre_medicamento,cantidad_medicamento,cod_medicamento)
            if a==4:
                print('\nCargando la información disponible \nEspere un momento...\n')
                inf.info_sistema(cod_medicamento,nombre_medicamento,riesgo)
            if a==5:
                print('\nBienvenido al sistema de modificación del resgistro \nEspere un momento...\n')
                nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo = escri.registro(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo)
                escri.escritura_datos(nombre_medicamento,cantidad_medicamento,cod_medicamento,riesgo)
            if a>7 or a<0:
                print('\nLas opciones son números del 1 al 6')
        else:
            print('\nLas opciones validas a ingresar son los numeros 1,2,3,4,5 ó 6. No los nombres de las opciones')
    print('\nTenga un buen turno')

if __name__=="__main__":
    run()