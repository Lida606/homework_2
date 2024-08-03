sizes = []
size = []
for t in range(1, 4):
    file = str(t) + '.txt'
    with open('text/' + file, encoding='UTF-8') as f:
        sizes.append(len(f.readlines()))
for i, v in enumerate(sizes):
    size.append([v, i])
size.sort()
for t in range(3):
    file = str(size[t][1] + 1) + '.txt'
    data = ''
    with open('text/' + file, encoding='UTF-8') as f:
        data = f.read()
    with open('Union.txt', 'a', encoding='UTF-8') as f:
        f.write(file)
        f.write('\n')
        f.write(str(size[t][0]))
        f.write('\n')
        f.write(data)
        f.write('\n')
