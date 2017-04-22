import pgn
from sys import argv
import os.path

name = argv[1]

if os.path.isfile(name):
    pass
elif os.path.isdir(name):
    pass
else:
    print name + " is not a file or directory."

    
pgn_text = open(name).read()
l = pgn.loads(pgn_text)

# the graph as a list of lines.
graph = []

for g in l:
    result = g.result
    if result == '1-0': 
        line = '"'+g.white+'"'+',0,'+'"'+g.black+'"'+',0\n'
        graph.append(line)
        graph.append(line)
    elif result == '0-1':
        line = '"'+g.black+'"'+',0,'+'"'+g.white+'"'+',0\n'
        graph.append(line)
        graph.append(line)
    else:
        line = '"'+g.white+'"'+',0,'+'"'+g.black+'"'+',0\n'
        graph.append(line)
        line = '"'+g.black+'"'+',0,'+'"'+g.white+'"'+',0\n'
        graph.append(line)


base = name.split('.')[0]
f = open(base + '.csv', 'w')
f.writelines(graph)
f.close()
