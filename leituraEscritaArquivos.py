f = open('teste.txt', 'w', encoding="utf-8").write("aaaaaaaaaaaaadfere"
                                                   "f3\ntestesteaaaaaaa"
                                                   "\njuvennnnnnnnnn")
b = open('teste.txt', 'r', encoding="utf-8").read()
print(b)
c = open('teste.txt', 'r', encoding="utf-8").readline()
print(c)
