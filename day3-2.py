# 6-3 문제

guess_me = 5
for number in range(1, 10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    else:
        print("oops")
        break
    number += 1

