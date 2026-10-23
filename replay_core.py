import sys,json,math
from pathlib import Path
import networkx as nx
sys.path.insert(0,str(Path(__file__).parent/'code'))
from forge_local import simulate
if __name__ == '__main__':
    rows=[]
    for seed in [20260726,20261013,1,2,3,4,5,6]:
        s=simulate(k=4,q=2,generations=2,block_size=6,closure_mode='face_cycle',seed=seed)
        r={'seed':seed,'cells':len(s.active),'L':sum(c.typ=='L' for c in s.active),'S':sum(c.typ=='S' for c in s.active),'vertices':len(s.spatial_graph),'edges':s.spatial_graph.number_of_edges(),'max_degree':max(dict(s.spatial_graph.degree()).values()),'connected':nx.is_connected(s.spatial_graph),'causal_acyclic':nx.is_directed_acyclic_graph(s.causal_graph)}
        assert (r['cells'],r['L'],r['S'],r['vertices'],r['edges'],r['max_degree'])==(108,72,36,460,1470,69)
        assert r['connected'] and r['causal_acyclic']
        rows.append(r)
    Path('replay_result.json').write_text(json.dumps({'runs':rows,'full_generation4_campaign_repeated':False},indent=2))
    print(json.dumps({'passed':True,'seeds':len(rows)}))
