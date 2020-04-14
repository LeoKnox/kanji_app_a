with open('test_data.csv', 'r', encoding="utf8") as f:
    f.readline()
    for line in f:
        print (line)