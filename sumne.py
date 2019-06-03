def sortIndex():
    indexfile = open('index.txt', 'r')
    content=[]
    for line in indexfile:
        content.append(line)
    content.sort()
    indexfile.close()
    indexfile = open('index.txt', 'w')
    for rec in content:
        indexfile.write(rec)
sortIndex()
