import matplotlib.pyplot as graf
 
#Función gráficas
def gráfica(tiem1, tiem2, tiem3, tiem4, tiem5):
    fig, ax = graf.subplots()
    ax.set_xlabel("Tiempo promedio")
    ax.set_ylabel("Procesos")  
    ax.plot([tiem1, tiem2, tiem3, tiem4, tiem5], [25, 50, 100, 150, 200])
    graf.show()

print("Indique el número de la opción de gráfica que desea visualizar: \n1. Intervalo de 10. \n2. Intervalo de 5. \n3. Intervalo de 1.")
op = int(input())

if op == 1:
    gráfica(4.27, 4.01, 4.61, 4.1, 4.48)
elif op == 2: 
    gráfica(3.37, 5.01, 6.13, 6.12, 6.31)
elif op == 3:
    gráfica(29.33, 61.87, 114.45, 168.16, 213.36)
else:
    print("Opción ingresada no es válida...")

