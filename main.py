import gevent
from gevent.wsgi import WSGIServer

from ouimeaux.environment import Environment

from ouimeaux.subscribe import SubscriptionRegistry

registry = SubscriptionRegistry()

def on_switch(switch):
    print "Switch found!", switch.name

def on_motion(motion):
    print "Motion found!", motion.name

env = Environment(on_switch, on_motion)

env.start()

ms = env.list_motions()
ss = env.list_switches()

m = ms[0]

m = env.get_motion(ms[0])
ss = [env.get_switch(s) for s in ss]

print m
print ss

def call_back(v):
    print 'tete'
    print v

registry.register(m)
registry.on(m, 'BinaryState', call_back)

env.wait()
