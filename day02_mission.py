import random

small = random.choice([True, False])
print(small)
green = random.choice([True, False])
print(green)

# small = False
# green = False

if small:
    if green:
        print('완두콩입니다')
    else:
        print('체리')
else:
    if green:
        print('수박')
    else:
        print('호박')



# import random
#
# guess = random.randint(1, 10)
# secret = random.randint(1, 10)
#
# diff = secret - guess
#
# if diff > 0:
#     print("too high")
#
# elif diff < 0:
#     print("too low")
#
# else:
#     print("just right")
