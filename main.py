
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

def updated():
    print 'Update'
    for s in ss:
        s.on()

m.on_device_updated_on = updated

registry.register(m)

env.wait()
