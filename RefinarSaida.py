year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}\n'.format(yes_votes, percentage))

s = 'Bom dia!'
print(f'{str(s)}\n')
print(f'{repr(s)}\n')
b = str(1/7)
print(b)

x = 10*3.25
y = 200 * 200
z = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...\n'
print(z)

cabelo = 'cabelo, liso\n'
cabelos = repr(cabelo)
print(cabelos)

print(repr((x, y, ('spam', 'eggs'))))
