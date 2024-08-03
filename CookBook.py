with open('recipes.txt', encoding='UTF-8') as f:
    data = f.read()
cook_book = {}
rec = []
ingrid = []
name = ['ingredient_name', 'quantity', 'measure']
for recipes in data.split('\n\n'):
    rec = recipes.split('\n')
    for i in range(2, 2 + int(rec[1])):
        ingrid.append(dict(zip(name, rec[i].split(' | '))))
        ingrid[i-2]['quantity'] = int(ingrid[i-2]['quantity'])
    cook_book[rec[0]] = ingrid
    ingrid = []


def pretty():
    for key, item in cook_book.items():
        print(f'{key}:')
        for i in range(len(item)):
            print(f'{item[i]}')


def get_shop_list_by_dishes(list, n):
    shop_list = {}
    for i in list:
        if i in cook_book:
            for k in range(len(cook_book[i])):
                key = cook_book[i][k][name[0]]
                ind1 = cook_book[i][k][name[1]] * n
                ind2 = cook_book[i][k][name[2]]
                if shop_list.get(key):
                    shop_list[key][name[1]] += ind1
                else:
                    shop_list[key] = {name[1]: ind1, name[2]: ind2}
        else:
            print('Нет рецепта!')
    for key, item in shop_list.items():
        print(f'{key}: {item}')


pretty()
print()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print()
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)