import re

#with open('test_data.csv', 'r', encoding="utf8") as f:
with open('List-of-1000-Kanji-converted2.csv', 'r', encoding="utf8") as f:
    f.readline()
    z = str(f)
    i = 0
    arr=[]
    for line in f:
        x = line.split(",")
        #for y in x:
            #print(y)
        if (len(x) == 3):
            arr.append(x)
        i += 1
    j = 0
    print(arr[0][0])
    #print (arr)
    db_data = []
    for y in range(0, len(arr)):
        #print ("-- {}".format(arr[y]))
        item = {
            'translation': arr[y][0],
            'kanji': arr[y][1],
            'pronunciation': arr[y][2],
            #'kana': arr[y][3]
        }
        db_data.append(item)
    #db_data = {"translate":arr[0][0]}
    #print (db_data)
    f2 = open('kanji_db.csv', 'x', encoding="utf8")
    f2.write(str(db_data))