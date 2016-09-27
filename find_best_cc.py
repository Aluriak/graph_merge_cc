"""See README for problem definition"""


from collections import defaultdict
from matplotlib import pyplot as mpl
import networkx as nx


def extract_aligned_graph(input_file:str, show=False) -> nx.Graph:
    grapha_id, graphb_id = None, None
    output = nx.Graph()
    graph_id = {}  # graph id: nx.Graph()
    aligned = {}
    graphs = set()  # {graph id}
    nodes = defaultdict(set)  # {graph id:{node id}}
    edges = defaultdict(set)  # {graph id:{(node id, node id)}}
    with open(input_file) as fd:
        for line in fd:
            line = line.strip()
            if not line: continue  # empty line

            if line.startswith('graph('):
                graph_id[line[len('graph('):].strip(').')] = nx.Graph()
            elif line.startswith('node('):
                node, graph = line[len('node('):].strip(').').split(',')
                graph_id[graph].add_node(node)
            elif line.startswith('edge('):
                source, target, graph = line[len('edge('):].strip(').').split(',')
                graph_id[graph].add_edge(source, target)
            elif line.startswith('align('):
                na, ga, nb, gb = line[len('align('):].strip(').').split(',')
                assert ga in graph_id
                assert gb in graph_id
                assert grapha_id is None or grapha_id == ga
                assert graphb_id is None or graphb_id == gb
                grapha_id = ga
                graphb_id = gb
                aligned[na] = nb
                output.add_node(na)
    # construction of merged graph

    # print('ALIGNED:', aligned)
    graph1, graph2 = graph_id[grapha_id], graph_id[graphb_id]

    # filter out unmerged nodes
    graph1 = graph1.subgraph(output.nodes())
    graph2 = graph2.subgraph(aligned[n] for n in output.nodes())

    # add an edge of graph1 in merged graph only if present in graphb
    graph2_edges = frozenset(graph2.edges())
    # print('G2 EDGES:', graph2_edges)
    for src, trg in graph1.edges():
        if (aligned[src], aligned[trg]) in graph2_edges:
            output.add_edge(src, trg)
        if (aligned[trg], aligned[src]) in graph2_edges:
            output.add_edge(src, trg)
    if show:
        nx.draw_networkx(graph2, show=True)
        mpl.show()
    return output


def best_cc(graph:nx.Graph) -> frozenset:
    return sorted(nx.connected_components(graph), key=len, reverse=True)


if __name__ == "__main__":
    data = 'toy.lp'
    data = 'toy2.lp'
    data = 'alpha.lp'

    ccs = best_cc(extract_aligned_graph(data, show=False))
    print('CC:', len(ccs))
    print('BIGGER:', ', '.join(n.strip('"') for n in ccs[0]))
