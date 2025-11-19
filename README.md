# Simulador del Algoritmo de Dijkstra
**Autor:** Alejandro Aguirre Díaz.   
**Descripción:** Este repositorio contiene un simulador didáctico del algoritmo de Dijkstra para encontrar caminos más cortos en grafos ponderados.     
**Última modificación:** Martes 11 de noviembre del 2025.   

## ¿Qué es?

El algoritmo de Dijkstra es un método para calcular las distancias mínimas desde un nodo origen a todos los demás nodos en un grafo ponderado con pesos no negativos.

- Tipo: algoritmo de grafos, voraz (greedy).
- Entrada: grafo (nodos y aristas con peso >= 0) y nodo fuente s.
- Salida: distancias mínimas dist[v] para cada vértice v y, opcionalmente, un arreglo de predecesores prev[v] para reconstruir caminos mínimos.
- Restricciones: no admite pesos negativos (usar Bellman–Ford en ese caso). Si el grafo está desconectado, algunas distancias permanecerán en infinito (sin camino).

Complejidad típica:
- Con una heap binaria: O((V + E) log V).
- Con montículo de Fibonacci: O(E + V log V).

Contrato mínimo:
- Entrada: lista de nodos y lista de aristas (u, v, w) con w >= 0.
- Salida: distancias y prev para reconstrucción de caminos.

Nota: este repositorio contiene una implementación didáctica en Python que permite ver paso a paso cómo funciona Dijkstra (`dijkstra_simulator.py`) y ejemplos para probarlo (`sample_graph.json`).

## ¿Para qué sirve?

El objetivo fundamental de Dijkstra es encontrar rutas de coste mínimo en problemas modelables como grafos con pesos no negativos. Sus usos prácticas incluyen:

- Navegación: calcular distancia o tiempo mínimo entre ubicaciones (p. ej. en mapas).
- Enrutamiento de redes: protocolos de encaminamiento interior (p. ej. OSPF) usan Dijkstra para calcular tablas de rutas.
- Logística y transporte: optimización de rutas de reparto y planificación de flotas.
- Juegos y simulaciones: búsqueda de caminos óptimos en mapas de juego.

Además, Dijkstra es una construcción básica que aparece dentro de soluciones más complejas (A*, contraction hierarchies, multi‑criterio routing) usadas en sistemas de producción.

## ¿Cómo se implementa en el mundo?

En entornos reales Dijkstra se emplea como bloque base, pero normalmente se adapta o se combina con técnicas adicionales para alcanzar los requisitos de rendimiento y escalabilidad:

- Motores de mapas: se usan variantes como A* (heurística admisible) para búsquedas punto a punto y técnicas de preprocesado (contraction hierarchies, multi‑level routing) para acelerar consultas en grafos de carreteras a escala.
- Sistemas de networking: los protocolos IGP ejecutan Dijkstra periódicamente para construir árboles de enrutamiento en cada router.
- Logística: Dijkstra puede formar parte de pipelines que calculan rutas óptimas dentro de optimizadores más amplios (restricciones de capacidad, ventanas horarias, costeo múltiple).

Prácticas industriales comunes:

- Preprocesado y indexación para consultas rápidas.
- Uso de heurísticas (A*) cuando existe una función estimada del coste restante.
- Caching de rutas frecuentes y particionado del grafo para escalabilidad.
- Monitoreo de latencias y pruebas automatizadas para asegurar exactitud tras cambios en la topología.

## ¿Cómo lo implementarías en tu vida?

Aplicaciones personales sencillas donde Dijkstra es útil:

- Planificar rutas diarias: modelar ubicaciones como nodos y tiempos/ distancias entre ellas como pesos para encontrar la secuencia más eficiente.
- Optimizar decisiones personales con coste asociado: transformar opciones en estados/nodos y transiciones con coste; Dijkstra da la secuencia de menor coste.
- Aprendizaje y enseñanza: usar ejemplos pequeños para entender colas de prioridad, relax de aristas y reconstrucción de caminos.

Pasos prácticos para uso personal:

1. Modelar el problema como grafo (definir nodos y pesos).
2. Normalizar unidades y limpiar datos (eliminar aristas inválidas).
3. Ejecutar Dijkstra y analizar distancias y rutas resultantes. Si hay muchos nodos, usar heurísticas o subconjuntos del grafo.

## ¿Cómo lo implementarías en tu trabajo o tu trabajo de ensueño?

En un contexto profesional, la implementación de soluciones de routing basadas en Dijkstra suele contemplar diseño de producto, rendimiento y operativa:

- Arquitectura: desplegar un servicio de routing (microservicio) que exponga una API para consultas de rutas y pueda acceder a una representación del grafo (almacenamiento persistente o en memoria).
- Escalabilidad: elegir algoritmos y estructuras (A*, contraction hierarchies, índices espaciales) según SLA; usar caching y particionado para consultas masivas.
- Robustez: permitir actualizaciones incrementales del grafo (cierres, cambios de peso), monitorización, y pruebas automatizadas que cubran rutas críticas.
- Experiencia de producto: combinar rutas óptimas con restricciones reales (ventanas horarias, capacidades, múltiples criterios) y exponer explicaciones/visualizaciones para usuarios finales.

Stack y herramientas típicas: motores como OSRM o GraphHopper para mapas; bibliotecas en C++/Rust/Go para rendimiento; despliegue en contenedores y pipelines de datos para ingestión y limpieza de mapas.

## Glosario técnico

- **Algoritmo voraz (greedy)**: estrategia que toma la mejor decisión local en cada paso esperando una solución global razonable.
- **Nodo / Vértice**: entidad del grafo que representa una posición o estado.
- **Arista / Arco**: conexión entre dos nodos; puede ser dirigida (u→v) o no dirigida (u↔v).
- **Peso (coste)**: valor numérico asociado a una arista que representa distancia, tiempo, coste, etc.
- **Cola de prioridad**: estructura que permite extraer el elemento de menor (o mayor) prioridad de forma eficiente; normalmente implementada con un heap.
- **Heap / Montículo**: implementación típica de una cola de prioridad (heap binario, montículo de Fibonacci, etc.).
- **Relajación (relax)**: operación que intenta mejorar la distancia conocida a un vértice v comprobando si pasar por u ofrece un coste menor.
- **Distancia provisional**: valor actual estimado de la distancia mínima desde la fuente a un nodo; puede actualizarse durante la ejecución.
- **Prev / Predecesor**: referencia al nodo anterior en el camino mínimo, utilizada para reconstruir la ruta final.
- **Infinito (∞)**: representación de una distancia no alcanzable desde la fuente (p. ej. `math.inf`).
- **Complejidad temporal**: medida del tiempo de ejecución en función del tamaño de la entrada (V = número de nodos, E = número de aristas).
- **Montículo de Fibonacci**: estructura de datos con mejores costes amortizados teóricos para algunas operaciones de cola de prioridad.
- **A***: algoritmo que extiende Dijkstra usando una heurística admisible para priorizar nodos hacia un objetivo (útil en búsquedas punto a punto).
- **Contraction Hierarchies (CH)**: técnica de preprocesado que crea atajos jerárquicos para acelerar búsquedas en grafos grandes.
- **Bellman–Ford**: algoritmo para caminos mínimos que admite pesos negativos y detecta ciclos de peso negativo.
- **Preprocesado**: operaciones realizadas sobre el grafo antes de aceptar consultas (indexación, contracción, etc.) para acelerar búsquedas posteriores.
- **Camino simple**: secuencia de nodos sin repetición; suele ser la solución esperada en rutas prácticas.


## Notas técnicas y contrato mínimo

- Entrada: archivo JSON con clave `nodes` (lista de ids) y `edges` (lista de tripletas [u,v,w]).
- El simulador es didáctico: no gestiona grafos enormes ni optimizaciones avanzadas (por ejemplo, tratamiento de aristas no dirigidas es explícito según el JSON).


