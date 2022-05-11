#Creamos la funcion objetivo Z
def funObjt(x1,x2,th):
    Z = (1.20*x1 +1.16*x2 - th*(2*x1**2 + x2**2 + (x1 + x2**2)))
    return float(Z)
#Retornamos el resultado de la funcion en tipo de dato flotante

th = float(input("Valor de theta: "))

#crear x1, x2 y x iniciados en 0
x1 = x2 = x = 0

#Tuplas de los puntos y resultados evaluados en la funcion objetivo
lista_Res = []

#Crear dos ciclos for para recorrer 
for x1 in range(6):
    for x2 in range(6):
        if((x1 + x2) <= 5):
            x = (x1,x2) #Guardaremos los puntos y 
                                              #el resultado que nos da evaluando 
                                              #x1 y x2 en la funcion objetivo
            lista_Res.append((x,funObjt(x1, x2, th))) 
   
a = max(lista_Res)
print("--------------------------------------")
print("En el intervalo de x1,x2 F[0,5] la funcion esta maximizada en...")
print("--------------------------------------")
print("Los puntos evaluados ", a[0] )
print("--------------------------------------")
print( "El resultado de la evaluacion de estos puntos ", a[1])