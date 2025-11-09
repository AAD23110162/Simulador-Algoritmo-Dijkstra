"""Generador de HTML para visualizar los pasos de Dijkstra.

Genera un HTML estático que puede subirse a GitHub Pages.
"""
import json
from typing import Dict, Any


def write_html(graph: Dict[str, Any], steps: Any, source: str, dest: str, output_path: str):
    nodes = []
    edges = []
    for n in sorted(graph.keys()):
        nodes.append({'id': n, 'label': str(n)})
    # edges from adjacency
    for u in graph:
        for v, w in graph[u]:
            edges.append({'from': u, 'to': v, 'label': str(w), 'weight': w})

    data = {
        'nodes': nodes,
        'edges': edges,
        'steps': steps,
        'source': source,
        'dest': dest,
    }

    # Insertaremos los datos como JSON reemplazando el token __DATA_TOKEN__
    html = '''<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Visualización Dijkstra</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; }}
    #network {{ width: 100%; height: 70vh; border-bottom: 1px solid #ddd; }}
    #controls {{ padding: 10px; display:flex; gap:8px; align-items:center; }}
    button {{ padding: 6px 10px; }}
    #info {{ padding: 8px; font-size: 14px; }}
  </style>
  <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
</head>
<body>
  <div id="network"></div>
  <div id="controls">
    <button id="prev">Anterior</button>
    <button id="next">Siguiente</button>
    <button id="play">Reproducir</button>
    <button id="pause">Pausa</button>
    <span> Paso: <span id="stepIndex">0</span> / <span id="stepMax">0</span></span>
  </div>
  <div id="info"></div>

  <script>
    const data = __DATA_TOKEN__;
    const container = document.getElementById('network');
    const nodes = new vis.DataSet(data.nodes.map(n=>({id:n.id, label:n.label, color:{background:'#ffffff'}})));
    const edges = new vis.DataSet(data.edges.map(e=>({from:e.from, to:e.to, label:e.label, arrows:'to'})));
    const network = new vis.Network(container, {nodes, edges}, {physics:{stabilization:true}});

    const steps = data.steps;
    const stepIndexEl = document.getElementById('stepIndex');
    const stepMaxEl = document.getElementById('stepMax');
    const info = document.getElementById('info');
    let idx = 0;
    let timer = null;

    function render(i){
      if(i < 0) i = 0;
      if(i >= steps.length) i = steps.length - 1;
      const s = steps[i];
      stepIndexEl.textContent = i;
      stepMaxEl.textContent = steps.length - 1;
      // Update node labels to show distances
      const dists = s.distances || {};
      const visited = new Set(s.visited || []);
      const current = s.current;
      nodes.forEach(n => {
        const dist = (dists[n.id] === null || dists[n.id] === undefined) ? '∞' : dists[n.id];
        nodes.update({id: n.id, label: n.id + ' (' + dist + ')'});
        if (n.id === current) {
          nodes.update({id:n.id, color:{background:'#ffeb3b'}});
        } else if (visited.has(n.id)) {
          nodes.update({id:n.id, color:{background:'#b2fab4'}});
        } else {
          nodes.update({id:n.id, color:{background:'#ffffff'}});
        }
      });
      // Show info
      let html = `<b>Acción:</b> ${s.action}`;
      if(s.relaxed){ html += `<br><b>Detalles:</b> ${JSON.stringify(s.relaxed)}` }
      html += `<br><b>Visitados:</b> ${s.visited.join(', ')}`;
      info.innerHTML = html;
    }

    document.getElementById('next').addEventListener('click', ()=>{ idx = Math.min(idx+1, steps.length-1); render(idx); });
    document.getElementById('prev').addEventListener('click', ()=>{ idx = Math.max(idx-1, 0); render(idx); });
    document.getElementById('play').addEventListener('click', ()=>{ if(timer) return; timer = setInterval(()=>{ idx++; if(idx>=steps.length){ clearInterval(timer); timer=null; } render(idx); }, 700); });
    document.getElementById('pause').addEventListener('click', ()=>{ if(timer){ clearInterval(timer); timer=null; }});

    // Inicializar
    render(0);
  </script>
</body>
</html>

'''

  # Reemplazar token por JSON seguro
  data_json = json.dumps(data)
  html = html.replace('__DATA_TOKEN__', data_json)

  with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

  print(f"Visualización escrita en: {output_path}")


if __name__ == '__main__':
  # Test rápido cuando se ejecuta directamente
  print('Este módulo genera un HTML. Usa create_html.write_html(graph, steps, source, dest, output_path)')
