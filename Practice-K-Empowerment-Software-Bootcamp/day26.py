from operator import itemgetter


def make_index(array, position):
    """

    :param array:
    :param position:
    :return:
    """
    before_array = list()
    index = 0
    for data in array:
        before_array.append((data[position], index))
        index += 1

    sorted_array = sorted(before_array, key=itemgetter(0))
    return sorted_array


def search_book(ary, fData):
    """
    :param ary:
    :param fData:
    :return:
    """
    pos = -1
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        if fData == ary[mid][0]:
            return ary[mid][1]
        elif fData > ary[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return pos


book_array = [['어린왕자', '쌩떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'],
              ['신곡', '단테'], ['돈키호테', '세르반테스'], ['동물농장', '조지오웰'],
              ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅'], ['이것이 자바다', '신용권']]
name_index = []
author_index = []

print(book_array)
name_index = make_index(book_array, 0)
print(name_index)
author_index = make_index(book_array, 1)
print(author_index)

find_name = '신곡'
find_position = search_book(name_index, find_name)
if find_position != -1:
    print(f"{find_name}의 작가는 {book_array[find_position][1]}입니다.")
else:
    print(f"{find_name} 책은 없습니다.")

find_name = '신용권'
find_position = search_book(author_index, find_name)
if find_position != -1:
    print(f"{find_name}의 도서는 {book_array[find_position][0]}입니다.")
else:
    print(f"{find_name} 작가는 없습니다.")