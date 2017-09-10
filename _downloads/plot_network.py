'''
Basic network using networkx
============================


'''


import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph()

nodes = ["p{}".format(i) for i in range(1,21)]

for n in nodes:
    G.add_node(n)

    if len(G.nodes())>1:
        pop = [i for i in G.nodes() if i!=n]
        sample = random.sample(pop, random.randint(1,len(pop)))

        for t in sample:
            G.add_edge(n,t)


print(G.nodes(), G.edges())
nx.draw(G)
plt.show()

plt.figure()
dist=nx.degree(G).values()
plt.hist(list(dist))
