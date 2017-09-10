'''

Scale-free networks
===================

'''

import networkx as nx
import matplotlib.pyplot as plt
import random



for n in range(20):
    G = nx.barabasi_albert_graph(20,1)

    plt.subplot(5,4,n+1)
    nx.draw(G, node_size=5)


plt.show()
