with open('test_data.csv', 'r', encoding="utf8") as f:
    f.readline()
    i = 0
    arr=[]
    for line in f:
        print(type(line))
        x = line.split(",")
        print(type(x))
        print(x)
        arr.append(x)
        i += 1
    print (arr[0])