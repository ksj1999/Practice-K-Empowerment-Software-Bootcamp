import random

guess = random.randint(1, 10)   #1에서 10사이의 정수가 임의로 발생
secret = random.randint(1, 10)
diff = secret - guess
if diff > 0:
    print('too high')
elif diff == 0:
    print('just right')
else:
    print('too low')