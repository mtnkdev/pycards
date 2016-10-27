import os

count = 0
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
##    for subdirname in dirnames:
##        print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    #count = 0
    for filename in filenames:
        #print(os.path.join(dirname, filename))
        #count = 0        
        if filename[len(filename)-1] == 'y' and filename != "lineCounter.py":
            f = open(os.path.join(dirname,filename), "r")
            text = f.readlines()
            for line in text:
                if line.count('create('):
                    print filename
                    print line
                count += 1
##                if len(line) > 0 and line[0] != '#':
##                    count += 1
##            if count != 0:
##                print filename
##                print count            
print count
