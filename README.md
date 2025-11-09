# Simulador del Algoritmo de Dijkstra

Este repositorio contiene un simulador didáctico del algoritmo de Dijkstra para encontrar caminos más cortos en grafos ponderados.

## ¿Qué es?

Es una pequeña herramienta en Python que permite ejecutar el algoritmo de Dijkstra paso a paso en la consola y, opcionalmente, exportar una visualización HTML estática que se puede publicar en GitHub Pages.

Incluye:
- `dijkstra_simulator.py` — ejecutable CLI que muestra cada paso, la cola de prioridad, las distancias y los nodos visitados.
- `create_html.py` — genera `visualization.html` (estático) con controles para avanzar/reproducir los pasos.
- `sample_graph.json` — grafo de ejemplo para probar rápidamente.

## ¿Para qué sirve?

Principalmente para aprendizaje y demostraciones:

- Visualizar cómo Dijkstra selecciona nodos y relaja aristas.
- Enseñar infraestructura de análisis de grafos en cursos o talleres.
- Generar una página estática (GitHub Pages) para mostrar la ejecución a un público no técnico.

## ¿Cómo se implementa en el mundo?

Dijkstra se usa en muchas aplicaciones reales:

- Sistemas de navegación (rutas más cortas en mapas, aunque para carreteras reales se usan variantes y heurísticas como A*).
- Redes y routing (calcular rutas en redes dirigidas o ponderadas).
- Planificación logística y optimización de costes.
- Juegos y simulaciones donde se necesita encontrar caminos óptimos en grafos.

Este repositorio demuestra la lógica básica y la trazabilidad (paso a paso) que suele ser útil en entornos educativos y de depuración.

## ¿Cómo lo implementarías en tu vida?

Algunas ideas personales para usar este simulador:

- Aprender estructuras de datos: practicar cómo funcionan colas de prioridad, relax de aristas y reconstrucción de caminos.
- Planificar rutas personales (pequeñas redes de ciudades o puntos) y experimentar con pesos (tiempo, distancia, coste).
- Enseñar a otros: usar la exportación HTML para mostrar el algoritmo en una presentación o en clase.

## ¿Cómo lo implementarías en tu trabajo o tu trabajo de ensueño?

En un entorno profesional o ideal:

- Integraría el motor de rutas en un servicio backend que exponga una API REST para recibir grafos y devolver rutas optimizadas.
- Conectar la visualización con datos reales (mapas, telemetría) para depurar y explicar decisiones de routing.
- Automatizar pruebas de regresión en rutas (por ejemplo, comprobar que cambios en la red no rompen caminos esperados).

## Cómo usar (rápido)

1) Ejecutar paso a paso (interactivo):

```bash
python3 dijkstra_simulator.py --load sample_graph.json --source A
```

Presiona Enter para avanzar entre pasos. Escribe `r` para ejecutar automáticamente el resto.

2) Ejecutar en modo automático y exportar HTML:

```bash
python3 dijkstra_simulator.py --load sample_graph.json --source A --dest D --auto --export-html visualization.html
```

Luego abre `visualization.html` en tu navegador o súbelo a GitHub Pages.

## Notas técnicas y contrato mínimo

- Entrada: archivo JSON con clave `nodes` (lista de ids) y `edges` (lista de tripletas [u,v,w]).
- Salida (con `--export-html`): archivo HTML estático con pasos y controles.
- El simulador es didáctico: no gestiona grafos enormes ni optimizaciones avanzadas (por ejemplo, tratamiento de aristas no dirigidas es explícito según el JSON).

## Siguientes pasos (mejoras posibles)

- Soporte para grafos no dirigidos con flag `--undirected`.
- Exportar imágenes o GIFs de la animación.
- Integrar más ejemplos y tests automáticos.

