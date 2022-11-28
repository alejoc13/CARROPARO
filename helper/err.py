# -*- coding: utf-8 -*-
def error_menu(a):
    try:  
        a = int(a)
        y=True
    except:
        print('\nPor favor, ingrese una opción válida')
        y=False
    return y,a
def error_codigo(cod_medicamento,code):
    try:
        cod_medicamento.index(code)
        z = True
    except:
        if code!=0:
            print("\nNo se encuentra este código en el archivo del carro")
            z=False
        if code==0:
            z=False
    return z
def error_nombre(n):
    try:  
        n = int(n)
        y=False
        print('\nLos nombres de medicamentos no son unicamente números')
    except:
        y=True
    return y,n
def control_ingreso(c,cod_medicamento,n,nombre_medicamento): #Control para que los medicamentos y codigos no se repitan.
    print('Comprobando los datos ingresados...espere un momento')
    nombres=[]
    n=n.upper()
    for nom in nombre_medicamento:
        nom=nom.upper()
        nombres.append(nom)
    a = n in nombres
    b = c in cod_medicamento
    conf = True
    if a == True:
        print('\nEl medicamento ya existe en el sistema')
        conf=False
    if b ==True:
        print('\nEL codigo ingresado ya está utilizado con otro medicamento')
        conf=False
    return conf 