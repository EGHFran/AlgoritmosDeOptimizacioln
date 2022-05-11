"""
------------------------------------------------------------******************
------------------------------******************************ln May 9 20:46:52*    
---------------****************     Francisca Fuentes Pérez                  * 
****************                                                             *
*                                                                            *
*                                                                            *   
******************************************************************************
"""
#Librerias
import numpy as np
from matplotlib import pyplot as plt 


#Validamos si el usuario nos entrega un entero o no
def validar(st):  
    crr = False
    num = 0
    while(not crr):
        try:
            print("Valor de", st)
            num = int(input(""))
            crr = True
        except ValueError:
            print('Eso no es un numero')   
    return num
 
    
 
#Validamos si el usuario nos entrego un valor de lambda correcto
def validarLmb():  
    crr = False
    while(not crr):
       try:
           lmb = float(input("Dame el valor de lambda: "))
           if lmb < 0 or lmb > 1:
               lmb = float(input("El valor de lambda debe ser entre [0, 1]"))
               crr = True
           else:
               break
       except ValueError:
           print("Eso no es un numero")   
    return lmb
     


#Funcion para evaluar x en una funcion matematica
def funcion(x, fun):
    z = eval(fun)
    return z



#Funcion para recorrer en un intervalo de lambda dado hasta 
# 1 con saltos de lambda dado para evaluarlos en la funcion 
# dada y determinar si es concava o convexa
def Con_Cov(xa, xb, lmb, fun):
    for i in np.arange(lmb, 1, lmb):
        izq = funcion((lmb * xa + (1 - lmb) * xb), fun)
        der = lmb * funcion(xa,fun) + (1-lmb) * funcion(xb, fun)
        
        if izq <= der:
            res = "Esta funcion es convexa"
        elif izq >= der:  
            res = "Esta funcion es concava"
        else:
            res = "Esta funcion es imposible de determinar"
    return print(res)    



def grafx(xa, xb, lmb, fun):
    #Graficamos la funcion
    y =  []
    x = [i for i in np.arange(-6, 6, step=lmb)]
    for i in x:
        y.append(funcion(i, fun))    
    #Graficamos en el rango xa, xb(Evaluacion de la funcion)
    x1 = []
    y1 = []
    for i in np.arange(xa,xb,step=lmb):
        x1.append(i)
        y1.append(funcion((lmb*i + (1 - lmb)*i), fun))
    #Graficamos que es la interpolacion 
    #lineal entre los puntos xa y xb
    x2 = np.linspace(xa,xb,2)
    y2 = np.interp(x2,x1,y1)
    #Graficar    
    plt.ion()
    plt.plot(x, y, label="F(x)", color="black")
    plt.plot(x1, y1,label="F(x) evaluada", color="blue")
    plt.plot(x2, y2, label="Interpolacion", color="red")
    plt.ylabel("F(x)")
    plt.xlabel("X")
    plt.title("Grafica F(x)")
    plt.legend(loc=1)
    plt.grid()
    plt.show()




#Funciones funcionando...    
#Validar numeros entregados por usuario
Xa = "Xa"    
xa = validar(Xa)
print("")
      
Xb = "Xb"    
xb = validar(Xb)
print("")

Lmb = "lambda entre [0, 1]"    
lmb = validarLmb()
print("")

#Pedir funcion por pantalla
fun = input("Dame la funcion como por ejemplo x+2 * 3x**2: ")

#Mostrar datos obtenidos por pantalla
print("---------------------------------")
print("DATOS: ")
print("---------------------------------")
print ('Xa: ', xa)
print("---------------------------------")
print ('Xb: ', xb)
print("---------------------------------")
print ('Lambda: ', lmb)
print("---------------------------------")

#¿Concava o convexa?
print("¿Que es esta funcion?")
Con_Cov(xa, xb, lmb, fun)
print("---------------------------------")
#Graficar todos los datos
print("GRAFICA:")
grafx(xa, xb, lmb, fun)
print("---------------------------------")




