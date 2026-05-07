#Diseña un algoritmo recursivo que imprima todos los elementos de un arreglo

#A) Escribe el caso base: cuando i == 0
#B) Escribe el caso recursivo: i - 1
#C) Encuentra la ecuación de recurrencia
#D) Encuentra la complejidad del algoritmo usando la ecuación de recurrencia

def imp_arr(arr, i):
    if i < 0:
        return
        
    print(arr[i])
    
    imp_arr(arr, i - 1)

arr = [10, 20, 30, 40, 50]
imp_arr(arr, len(arr) - 1)