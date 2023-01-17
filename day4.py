# ex 7-4

things = ['mozzarealla', 'cinderella', 'salmonella']

things[-2] = things[-2].title()
print(things)
things[0] = things[0].upper()
print(things)
print(f'delete {things.pop()} from things')

# for thing in things:
#     print(thing.title())