with open('test_data.csv', 'r', encoding="utf8") as f:
    f.readline()
    i = 0
    arr=[]
    for line in f:
        x = line.split(",")
        for y in x:
            print(y)
        arr.append(x)
        i += 1
    j = 0
    #print (arr)