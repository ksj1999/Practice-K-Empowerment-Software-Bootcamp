

def insert_data(index, pokemon):
    if index < 0 or index > len(pokemons):
        print("out of range.")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, index, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[index] = pokemon  # 지정한 위치에 친구 추가


def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("out of range.")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None

    for i in range(idx + 1, len_pokemons):
        # pokemons[i - 1] = pokemons[i]
        pokemons[i] = None

    for i in range(idx, i):
        pokemons.pop()


if __name__=="__main__":
    pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "이상해"]
    #insert_data(3, '어니부기')
    delete_data(1)
    print(pokemons)
    #delete_data(5)
    insert_data(6, '거북왕')
    print(pokemons)


