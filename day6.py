# ex 9-2

cnts = 0

def get_odds():
    for num in range(10):
        if num % 2:
            yield num

odds = get_odds()
for i in odds:
    cnts += 1
    if cnts ==3:
        print(i)