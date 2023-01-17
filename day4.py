# dictionary

students = {'name':'kiminha', 'age': 23, 'eyes': [0.9, 1.1]}
# for k in students.keys():
# for k in students():
for k, v in students.items():
    #print(k)
    print(f'{k} : {v}')
print(f'이름은 {students["name"]}, 나이는 {students["age"]}세', end=' ')
print(f'시력은 좌: {students["eyes"][0]}, 우: {students["eyes"][1]}')

