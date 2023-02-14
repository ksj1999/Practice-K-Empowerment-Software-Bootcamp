def find(ary):
    min = 0
    for i in range(1, len(ary)):
        if ary[min] > ary[i]:
            min = i
        return min

test = [55, 88, 33, 77]
minpos = find(test)
print(test[minpos])