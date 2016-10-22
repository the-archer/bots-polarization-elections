#takes userbotscore.p returns onlybots.p and onlyhumans.p 
import cPickle as pickle

uscores = pickle.load(open('userbotscore.p', 'rb'))
bots = set()
humans = set()
for user in uscores:
	if uscores[user]['score'] >= 0.5:
		bots.add(user)
	else:
		humans.add(user)

pickle.dump(bots, open('onlybots.p', 'wb'))
pickle.dump(humans, open('onlyhumans.p', 'wb'))


