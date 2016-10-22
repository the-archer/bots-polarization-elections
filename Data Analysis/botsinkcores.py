#getting stats of how many bots/humans/unknowns are in kcores

import cPickle as pickle 
import networkx as nx 

kcores = pickle.load(open('kcores.p', 'rb'))
userbot = pickle.load(open('userbotscore.p', 'rb'))


frac = {}

for core in range(10, 101, 10):
	G = kcores[core]
	print core
	frac[core] = {}
	frac[core]['total'] = len(G.nodes())
	bot = 0
	user = 0
	noinfo = 0
	for node in G.nodes():
		if node not in userbot:
			noinfo += 1
			continue
		if userbot[node]['score'] >= 0.5:
			bot += 1
		else:
			user += 1
	frac[core]['bot'] = bot
	frac[core]['user'] = user
	frac[core]['noinfo'] = noinfo
	print frac[core]

pickle.dump(frac, open('corestats.p', 'wb'))
