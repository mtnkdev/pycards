def replace(filename, old, new):
    f = open(filename, "r")
    data = f.read()
    f.close()
    data = data.replace(old, new)
    f = open(filename, "w")
    f.write(data)
    f.close()


def replaceAll(filename):
    replace(filename, "STYLE.", "STYLE.")
    replace(filename, "SKILL.", "SKILL.")
    replace(filename, "CATEGORY.", "CATEGORY.")
    replace(filename, "from pysollib.gametype import STYLE, SKILL", "from pysollib.gametype import STYLE, SKILL")
    replace(filename, "from pysollib.gametype import STYLE, SKILL", "from pysollib.gametype import STYLE, SKILL")


import os

count = 0
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
##    for subdirname in dirnames:
##        print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    #count = 0
    for filename in filenames:
        print(os.path.join(dirname, filename))
        #count = 0        
        if filename[len(filename)-1] == 'y':
            print filename
            replaceAll(os.path.join(dirname, filename))
