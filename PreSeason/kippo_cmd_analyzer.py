#!/usr/bin/env python

# builds a stochastic model of ssh honeypot activity from 
# kippo logs.
# yields a dot graph to be processed by graphviz.

import sys

def main():
    res = {}
    for arg in sys.argv[1:]:
        with open(arg, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if 'CMD: ' in line:
                    # 2013-09-07 00:53:02-0400 [SSHChannel session (0) on SSHService ssh-connection on HoneyPotTransport,24486,42.96.165.163] CMD: ethtool eth0
                    line = line.split()
                    ki = line.index('CMD:')-1
                    key = ','.join(line[ki].split(',')[1:])
                    ci = line.index('CMD:')+1
                    cmd = line[ci]
                    if cmd in ('curl', 'wget',): cmd = 'download'
                    cmds = res.get(key, [])
                    cmds.append(cmd)
                    res[key] = cmds
    # now res looks like this (keyed by sessions, then list of cmds run):
    # {'24486,42.96.165.163': ['ls', 'id', 'ps'], 
    #  '24485,111.123.19.24': ['uname',] , }

    # now to analyze the lists and determine the likelihood of
    # executing a certain command next, e.g. uname -> wget = 0.9

    #print 'CMDFREQ'
    cmdfreq = {}
    for cmds in res.values():
        for cmd in cmds:
            cmdfreq[cmd] = cmdfreq.get(cmd, 0) + 1
    cmdfreq['start'] = len(res.keys())
    #print cmdfreq

    #print 'TRANSITIONS'
    transitions = {}
    for session in res.values():
        #print 'session', session
        key = 'start|%s' % session[0]
        transitions[key] = transitions.get(key, 0) + 1
        for i in xrange(len(session)-1):
            key = '%s|%s' % (session[i], session[i+1])
            transitions[key] = transitions.get(key, 0) + 1
        key = '%s|end' % session[-1]
        transitions[key] = transitions.get(key, 0) + 1

    #print 'CHANCES'
    chances = {}
    for transition, n in transitions.iteritems():
        #print 'transition, n', transition, n
        root = transition.split('|')[0]
        chances[transition] = float(n)/float(cmdfreq[root])

    print 'digraph kippo {'
    print '\toverlap=scale;'
    print '\tnode [shape = doublecircle]; "start" "end";'
    print '\tnode [shape = circle];'
    for transition in transitions.keys():
        a,b = transition.split('|')
        print '\t"%s" -> "%s" [label="%0.2f"];' % (a, b, chances[transition])
    print '}'

if __name__ == '__main__':
    main()