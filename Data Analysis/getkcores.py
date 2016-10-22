#Takes a networkX graph (after removing self loops) and generates k cores

import cPickle as pickle 
import networkx as nx 

G = pickle.load(open('nxGraph_noselfloops.p', 'rb'))
#kcores = pickle.load(open('kcores.p', 'rb'))
kcores = {}
for core in range(10, 101, 10):
	H = nx.k_core(G, k=core)
	kcores[core] = H
	print core
	print len(H.nodes())
	print len(H.edges())

pickle.dump(kcores, open('kcores.p', 'wb'))
