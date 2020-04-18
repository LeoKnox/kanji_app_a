def plus_one_digit(val):
    total = 0
    while not val < 10:
        total += val % 10
        val = val // 10
    total += val
    return total

def one_digit(val):
    if val == 0:
        return 0
    else:
        while not val < 10:
            val = plus_one_digit(val)
        return val

print (one_digit(738215793))
print (one_digit(123))
print (one_digit(585858))
print (one_digit(1))