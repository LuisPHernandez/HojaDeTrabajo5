#------------------------------------
# Pedro Caso
# Luis Hernandez
# Tiffany Salazar 
# HDT5
# Algoritmos y Estructura de datos
# ----------------------------------- 

import matplotlib.pyplot as graf
 
#Función gráficas
def gráfica(tiem1, tiem2, tiem3, tiem4, tiem5):
    fig, ax = graf.subplots()
    ax.plot([25, 50, 100, 150, 200], [tiem1, tiem2, tiem3, tiem4, tiem5])
    #ax.plot([tiem1, tiem2, tiem3, tiem4, tiem5], [25, 50, 100, 150, 200]) 
    ax.set_title("Tiempo promedio vs procesos")
    ax.set_xlabel("Cant. procesos")
    ax.set_ylabel("Tiempo promedio")
    ax.grid()

    graf.show()

print("Indique el número de la opción de gráfica que desea visualizar: \n1. Intervalo de 10. \n2. Intervalo de 5. \n3. Intervalo de 1.")
op = int(input())

#con tiempos ya medidos (quitar # de comantario para visualizar otras gráficas)
if op == 1:
    #valores predeterminados
    gráfica(4.27, 4.01, 4.61, 4.1, 4.48)

    #al incrementar la memoria a 200
    #gráfica(4.27, 4.01, 4.61, 4.1, 4.48)

    #al incrementar velocidad del procesador a 6 instrucciones 
    #gráfica(1.71, 2.13, 2.07, 2.01, 1.98)

    #al incrementar a 2 procesadores
    #gráfica(2.84, 2.98, 3.38, 3.30, 3.27)

elif op == 2: 
    #valores predeterminados
    gráfica(3.37, 5.01, 6.13, 6.12, 6.31)

    #al incrementar la memoria a 200
    #gráfica(3.37, 5.01, 6.13, 6.12, 6.31)

    #al incrementar velocidad del procesador a 6 instrucciones 
    #gráfica(2.01, 2.33, 2.18, 2.42, 2.33)

    #al incrementar a 2 procesadores
    #gráfica(2.64, 3.19, 3.38, 3.35, 3.30)

elif op == 3:
    #valores predeterminados
    gráfica(29.33, 61.87, 114.45, 168.16, 213.36)

    #al incrementar la memoria a 200
    #gráfica(29.69, 69.28, 134.41, 192.44, 247.49)

    #al incrementar velocidad del procesador a 6 instrucciones 
    #gráfica(11.47, 24.11, 45.66, 62.02, 78.34)

    #al incrementar a 2 procesadores
    #gráfica(10.52, 14.75, 28.10, 41.67, 55.74)

else:
    print("Opción ingresada no es válida...")

exit()