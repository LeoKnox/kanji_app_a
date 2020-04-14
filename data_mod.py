with open('test_data.csv', 'r', encoding="utf8") as f:
    f.readline()
    i = 0
    for line in f:
        if i%6:
            print(line)
            i += 1
        else:
            i += 1
        #x = line.split(",")