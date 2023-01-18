# 9-2

def get_odds(first=0, last=10, step=1):
    number = first
    while number < last:
        if number % 2 == 1:
            yield number
        number += step
    else:
        number += step

ranger = get_odds(1, 11)
for x in ranger:
    print(x)
