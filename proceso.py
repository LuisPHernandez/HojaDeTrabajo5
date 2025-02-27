import random
import simpy

# Se crea la semilla de random
random.seed(42)

# Se crea el ambiente de simulación
env = simpy.Environment()

# Variables globales
RAM_CAPACITY = 100 
CPU_SPEED = 3
INTERVALO_LLEGADA = 10
NUM_PROCESOS = 25 

# Se crean los recursos
RAM = simpy.Container(env, init=RAM_CAPACITY, capacity=RAM_CAPACITY)
CPU = simpy.Resource(env, capacity=1)

# Se define la función que simula el camino de un proceso
def proceso(env, name, RAM, CPU, memoria_necesaria, instrucciones_totales):
    # Estado new
    print(f'{name} llega al sistema en tiempo {env.now}')
    
    yield RAM.get(memoria_necesaria)
    print(f'{name} obtiene {memoria_necesaria} unidades de memoria en tiempo {env.now}')
    
    # Estado ready
    while instrucciones_totales > 0:
        with CPU.request() as req:
            yield req
            print(f'{name} comienza a ejecutarse en tiempo {env.now}')
            
            # Estado running
            instrucciones_ejecutadas = min(CPU_SPEED, instrucciones_totales)
            yield env.timeout(1) 
            instrucciones_totales -= instrucciones_ejecutadas
            print(f'{name} ejecuta {instrucciones_ejecutadas} instrucciones, le quedan {instrucciones_totales} en tiempo {env.now}')
            
            if instrucciones_totales == 0:
                # Estado terminated
                print(f'{name} termina en tiempo {env.now}')
                yield RAM.put(memoria_necesaria)
                print(f'{name} libera {memoria_necesaria} unidades de memoria en tiempo {env.now}')
                break
            else:
                # Decidir si va a waiting o ready
                if random.randint(1, 2) == 1:
                    # Estado waiting
                    print(f'{name} va a estado waiting en tiempo {env.now}')
                    yield env.timeout(random.randint(1, 2))
                    print(f'{name} regresa a estado ready en tiempo {env.now}')
                else:
                    # Estado ready
                    print(f'{name} regresa a estado ready en tiempo {env.now}')

# Se define la función que genera los procesos
def generador_procesos(env, RAM, CPU, intervalo, num_procesos):
    proceso_id = 0
    while proceso_id < num_procesos:
        yield env.timeout(random.expovariate(1.0 / intervalo))
        
        # Generar un nuevo proceso
        proceso_id += 1
        memoria_necesaria = random.randint(1, 10)
        instrucciones_totales = random.randint(1, 10)
        env.process(proceso(env, f'Proceso {proceso_id}', RAM, CPU, memoria_necesaria, instrucciones_totales))

# Iniciar el generador de procesos
env.process(generador_procesos(env, RAM, CPU, INTERVALO_LLEGADA, NUM_PROCESOS))

# Ejecutar la simulación
env.run()