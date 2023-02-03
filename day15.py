def find_and_add(pokeymon, pcount):
    findPok = -1
    for i in range(len(pokeinfo)):
        pair = pokeinfo[i]
        if pcount >= pair[1]:
            findPok = i
            break
    if findPok == -1:
        findPok = len(pokeinfo)

    insert_data(findPok, (pokeymon, pcount))


def insert_data(position, pokey):
    if position < 0 or position > len(pokeinfo):
        print("out of range")
        return

    pokeinfo.append(None)
    pokeylen = len(pokeinfo)

    for i in range(pokeylen - 1, position, -1):
        pokeinfo[i] = pokeinfo[i - 1]
        pokeinfo[i - 1] = None

    pokeinfo[position] = pokey


pokeinfo = []

if __name__ == "__main__":

    while True:
        data = input("추가할 포켓몬--> ")
        count = int(input("체력--> "))
        find_and_add(data, count)
        print(pokeinfo)
