# # subway = [10, 20, 30]
# #
# # subway = ['you', 'joe', 'kim']
# # print(subway.index('kim'))
# #
# # subway.append('haha')
# # print(subway)
# #
# # subway.insert(1, 'jung')
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
# # # print(subway.pop())
# # # print(subway)
# # # print(subway.pop())
# # # print(subway)
# #
# # subway.append('you')
# # print(subway)
# # print(subway.count('you'))
# #
# # num_list = [5, 2, 4, 3, 1]
# # num_list.sort()
# # print(num_list)
# #
# # num_list.reverse()
# # print(num_list)
# # num_list.clear()
# # print(num_list)
# num_list = [5, 2, 4, 3, 1]
# mix_list = ['joe', 1, True]
# print(mix_list)
#
# num_list.extend(mix_list)
# print(num_list)
#
## print(cabinet[3])
# print(cabinet[100])
#
# print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet.get(5, 'use'))

# print(3 in cabinet)
# print(5 in cabinet)

cabinet = {'A3':'you', 'B100':'kim'}
print(cabinet['A3'])
print(cabinet['B100'])

print(cabinet)
cabinet['A3'] = 'kill'
cabinet['c20'] = 'joe'
print(cabinet)

del cabinet['A3']
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()
print(cabinet)