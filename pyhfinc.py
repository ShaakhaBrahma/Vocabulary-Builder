def writeIndex():
    datafile = open('dictionary.txt', 'r+')
    indexfile = open('index.txt', 'w+')
    line = datafile.readline()
    while line:
        offset = datafile.tell()
        offset-=len(line)
        offset=offset.__str__()
        word = line.split('|')[0]
        rec = word+'|'+offset+'\n'
        indexfile.write(rec)
        line=datafile.readline()
writeIndex()





