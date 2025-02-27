import random
import simpy
import statistics

# Se crea la semilla de random
random.seed(42)

# Se crea el ambiente de simulación
env = simpy.Environment()

# Variables y listas
#CapacidadDeRam = 100 
#VelCPU = 3
#IntervalosDeLlegada = 10
#CantProcesos = 25 
MedicionTiempo = []

#Cambios para solo ingresar los datos y que siga funcionando igual el programa
print("Ingrese los siguientes datos de cantidades como enteros \nProcesos que desea trabajar:")
CantProcesos = int(input())

print("Intervalos:")
IntervalosDeLlegada = int(input())

print("Memoria:")
CapacidadDeRam = int(input())

print("Velocidad del CPU:")
VelCPU = int(input())
#

# Se crean los recursos
RAM = simpy.Container(env, init=CapacidadDeRam, capacity=CapacidadDeRam)
CPU = simpy.Resource(env, capacity=1)

# Se define la función que simula el camino de un proceso
def proceso(env, name, RAM, CPU, memoriaUtil, cantidadInstrucciones):
    """Simula un proceso en el sistema"""
    
    # Registrar el tiempo de llegada
    TiempoInicial = env.now
    print(f'{name} tiempo de llegada {TiempoInicial}')
    
    # Estado new, espera por memoria
    yield RAM.get(memoriaUtil)
    print(f'{name} obtiene {memoriaUtil} unidades de memoria {env.now}')
    
    # Estado ready, espera por CPU
    while cantidadInstrucciones > 0:
        with CPU.request() as req:
            yield req  # Esperar turno en CPU
            print(f'{name} Se empieza a ejecutar {env.now}')
            
            # ejecuta hasta VelCPU
            ejecucionDeIstrucciones = min(VelCPU, cantidadInstrucciones)
            yield env.timeout(1) 
            cantidadInstrucciones -= ejecucionDeIstrucciones
            print(f'{name} ejecuta {ejecucionDeIstrucciones} instrucciones, le quedan {cantidadInstrucciones} en tiempo {env.now}')
            
            if cantidadInstrucciones == 0:
                #Registrar el tiempo de finalización
                tiempoFinal = env.now
                tiempoTotal = tiempoFinal - TiempoInicial
                MedicionTiempo.append(tiempoTotal) 
                
                # Estado final o terminado
                print(f'{name} termina en tiempo {env.now}')
                yield RAM.put(memoriaUtil)  
                print(f'{name} libera {memoriaUtil} unidades de memoria en tiempo {env.now}')
                break
            else:
                # Estado waiting o listo
                if random.randint(1, 2) == 1: 
                    print(f'{name} va a estado waiting en tiempo {env.now}')
                    yield env.timeout(random.randint(1, 2))  
                    print(f'{name} regresa a estado ready en tiempo {env.now}')
                else:
                    print(f'{name} regresa a estado ready en tiempo {env.now}')

# Se define la función que genera los procesos
def generador_procesos(env, RAM, CPU, intervalo, CantProcesos):
    proceso_id = 0
    while proceso_id < CantProcesos:
        yield env.timeout(random.expovariate(1.0 / intervalo))
        
        # Generar un nuevo proceso
        proceso_id += 1
        memoriaUtil = random.randint(1, 10)
        cantidadInstrucciones = random.randint(1, 10)
        env.process(proceso(env, f'Proceso {proceso_id}', RAM, CPU, memoriaUtil, cantidadInstrucciones))

# Iniciar el generador de procesos
env.process(generador_procesos(env, RAM, CPU, IntervalosDeLlegada, CantProcesos))

# Ejecutar la simulación
env.run()

# Ejecutar la simulación
env.run()

# Calcular estadísticas después de la simulación
if MedicionTiempo:
    promedio = sum(MedicionTiempo) / len(MedicionTiempo)
    desviacion = statistics.stdev(MedicionTiempo) if len(MedicionTiempo) > 1 else 0 
    
    print("\nResultados:")
    print(f"Tiempo promedio cuando se ejecuta: {promedio:.2f}")
    print(f"DesVest del proceso ejecutado: {desviacion:.2f}")
