def searchInIndex(keyword):
    global result
    result=0
    indexf=open('index.txt','r')
    for line in indexf:
        if keyword in line:
            result = line.split('|')[1]
           # print(result)
            break
    indexf.close()
    datafile = open('dictionary.txt', 'r')
    if result==0:
        meaning="Word is not in file"
        return meaning
    datafile.seek(int(result))
    meaning = datafile.readline().split('|')[1]
    return meaning
