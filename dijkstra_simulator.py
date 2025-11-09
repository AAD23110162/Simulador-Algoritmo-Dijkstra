#!/usr/bin/env python3
"""Simulador de Dijkstra (CLI)

Muestra paso a paso la ejecución de Dijkstra en consola y puede exportar
una visualización HTML para GitHub Pages.

Uso básico:
  python3 dijkstra_simulator.py --load sample_graph.json --source A --dest D --auto --export-html visualization.html

"""
import argparse
import heapq
import json
import math
import os
from typing import Dict, List, Tuple, Any


def load_graph(path: str) -> Dict[str, List[Tuple[str, float]]]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Expecting { "nodes": ["A","B"...], "edges": [["A","B",3], ...] }
    nodes = data.get('nodes', [])
    edges = data.get('edges', [])
    g: Dict[str, List[Tuple[str, float]]] = {n: [] for n in nodes}
    for u, v, w in edges:
        if u not in g:
            g[u] = []
        if v not in g:
            g[v] = []
        g[u].append((v, float(w)))
        # If the graph is undirected, also add reverse. We'll respect a flag later if needed.
    return g


def dijkstra_with_steps(graph: Dict[str, List[Tuple[str, float]]], source: str):
    dist: Dict[str, float] = {n: math.inf for n in graph}
    prev: Dict[str, Any] = {n: None for n in graph}
    dist[source] = 0.0
    visited = set()
    pq: List[Tuple[float, str]] = [(0.0, source)]

    steps = []

    def snapshot(action: str, current=None, relaxed=None):
        # Make serializable shallow copies
        return {
            'action': action,
            'current': current,
            'distances': {k: (v if v != math.inf else None) for k, v in dist.items()},
            'visited': list(sorted(visited)),
            'pq': list(pq),
            'relaxed': relaxed,
        }

    steps.append(snapshot('start', current=None))

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            steps.append(snapshot('pop_ignored', current=u))
            continue
        # Visiting u
        visited.add(u)
        steps.append(snapshot('visit', current=u))

        for v, w in graph.get(u, []):
            old = dist[v]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
                steps.append(snapshot('relax', current=u, relaxed={'edge': (u, v), 'new_dist': dist[v], 'old_dist': old}))
            else:
                steps.append(snapshot('no_relax', current=u, relaxed={'edge': (u, v), 'candidate': dist[u] + w, 'old_dist': old}))

    steps.append(snapshot('end', current=None))
    return {
        'steps': steps,
        'distances': {k: (v if v != math.inf else None) for k, v in dist.items()},
        'prev': prev,
    }


def reconstruct_path(prev: Dict[str, Any], source: str, dest: str):
    if dest not in prev:
        return None
    path = []
    cur = dest
    while cur is not None:
        path.append(cur)
        cur = prev.get(cur)
    path.reverse()
    if path and path[0] == source:
        return path
    return None


def print_step(step: Dict[str, Any], step_no: int):
    print(f"\n--- Paso {step_no}: {step['action']} ---")
    if step['current'] is not None:
        print(f"Nodo actual: {step['current']}")
    if step.get('relaxed'):
        print(f"Detalles relax: {step['relaxed']}")
    print("Distancias:")
    for n, d in sorted(step['distances'].items()):
        print(f"  {n}: {d}")
    print(f"Visitados: {', '.join(step['visited']) if step['visited'] else '(ninguno)'}")
    print(f"Cola (pq): {step['pq']}")


def export_html(graph, steps, source, dest, output_path):
    try:
        import create_html
    except Exception as e:
        print("No se pudo importar create_html.py: ", e)
        return False
    create_html.write_html(graph, steps, source, dest, output_path)
    return True


def main():
    parser = argparse.ArgumentParser(description='Simulador Dijkstra (paso a paso)')
    parser.add_argument('--load', '-l', help='Archivo JSON con grafo (nodes, edges)', required=True)
    parser.add_argument('--source', '-s', help='Nodo origen', required=True)
    parser.add_argument('--dest', '-d', help='Nodo destino (opcional)', default=None)
    parser.add_argument('--auto', '-a', help='Modo automático (no esperar Enter)', action='store_true')
    parser.add_argument('--export-html', help='Generar visualización HTML en archivo dado (ej: visualization.html)')

    args = parser.parse_args()

    graph = load_graph(args.load)
    if args.source not in graph:
        print(f"Nodo fuente {args.source} no está en el grafo. Nodos disponibles: {list(graph.keys())}")
        return

    result = dijkstra_with_steps(graph, args.source)
    steps = result['steps']

    # Console step-by-step
    for i, step in enumerate(steps):
        print_step(step, i)
        if not args.auto:
            inp = input('Presiona Enter para continuar, "q" para salir, "r" para run automático: ').strip().lower()
            if inp == 'q':
                break
            if inp == 'r':
                args.auto = True
                continue

    # Summary
    print('\n=== Resultado final ===')
    for n, d in sorted(result['distances'].items()):
        print(f"{n}: {d}")
    if args.dest:
        path = reconstruct_path(result['prev'], args.source, args.dest)
        if path:
            print(f"Camino {args.source} -> {args.dest}: {' -> '.join(path)}")
        else:
            print(f"No se encontró camino de {args.source} a {args.dest}")

    if args.export_html:
        ok = export_html(graph, steps, args.source, args.dest, args.export_html)
        if ok:
            print(f"HTML exportado a {args.export_html}")


if __name__ == '__main__':
    main()
