#prime number for

# prime number

number = int(input("input number : "))

counts = 0

k = 1
for k in range(2, number):
    if number % k == 0:
        counts = counts + 1

if counts:   #0이면 소수라는 뜻
    print(f'{number}is not prime number.')

else:
    print(f'{number}is prime number!')





# # prime number while
#
# number = int(input("input number : "))
#
# counts = 0
#
# k = 1
# while k <= number:
#     if number % k == 0:
#         counts = counts + 1
#     k = k + 1
#
# if counts == 2:
#     print(f'{number}is prime number!')
#
# else:
#     print(f'{number}is not prime number.')