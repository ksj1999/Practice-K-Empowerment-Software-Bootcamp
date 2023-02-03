def insert_data(idx, pokemon):
    """
    선형 리스트의 idx위치에 원소 삽입
    :param idx: int
    :param pokemon: str
    :return: void
    """
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return
    pokemons.append(None)
    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None
    pokemons[idx] = pokemon


def delete_data(idx):
    """
    선형 리스트 idx 위치의 원소 삭제
    :param idx: int
    :return: void
    """
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None

    # self 3-1
    # for _ in range(len_pokemons - idx):
    #     pokemons.pop()
    for i in range(idx + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None

    pokemons.pop()


def add_data(pokemon):
    """
    선형 리스트의 맨 뒤에 원소 삽입
    :param pokemon: str
    :return: void
    """
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon


pokemons = []

if __name__ == "__main__":
    while True:
        menu = input("1: 추가, 2: 삽입, 3: 삭제, 4: 종료--> ")
        if (menu == '1'):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif (menu == '2'):
            idx = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(idx, data)
            print(pokemons)
        elif (menu == '3'):
            idx = int(input("삭제할 위치--> "))
            delete_data(idx)
            print(pokemons)
        elif (menu == '4'):
            print(pokemons)
            # exit()
            break
        else:
            print("menu에서 고르세요")
            continue