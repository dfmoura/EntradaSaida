for x in range(1, 50):
    print(repr(x).ljust(2), repr(x*x).center(3), end=' ')
    print(repr(x*x*x).rjust(4))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))
