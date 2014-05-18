#!/usr/bin/env python
from priodict import priorityDictionary
import dij
def make_link(G, node1, node2, value):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = value
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = value
    return G



if __name__ == "__main__":
    G = {}
    raw_data = [
                {"Wellington":{"Auckland":5}},
                {"Wellington":{"Hamilton":3}},
                {"Wellington":{"Rutorua":4}},
                {"Wellington":{"Christchurch":6}},
                {"Wellington":{"Turanga":8}},
                {"Auckland": {"Wellington": 5}},
                {"Auckland": {"Hamilton": 2}},
                {"Auckland": {"Rutorua":1}},
                {"Auckland": {"Turanga":2}}
            ]


    for meta in raw_data:
        make_link(G, ''.join(meta.keys()), meta.values()[0].keys()[0], meta.values()[0].values()[0])

    path = dij.shortestPath(G, "Wellington", "Turanga")

    value = 0
    for i in range(len(path) - 1):
        value += G[path[i]][path[i + 1]]
    print path
