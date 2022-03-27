import os
def food_file(name,mode):
    with open(name,mode,encoding='UTF-8') as file:
        food_file.__name__ = os.path.join(os.getcwd(), name)
        food= {}
        for line in file:
            food_name = line.strip()
            ing_count = int(file.readline())
            food_block = []
            for ing in range(ing_count):
                ingrs = {}
                ingr = file.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                food_block.append(ingrs)
            file.readline()
            food[food_name] = food_block
    return food

def get_shop_list_by_dishes(dishes, person_count):
    ing_list = {}
    for dish in dishes:
        if dish in food_good:
            for ing in food_good[dish]:
                need_ing = {}
                if ing['ingredient_name'] not in ing_list:
                    need_ing['measure'] = ing['measure']
                    need_ing['quantity'] = ing['quantity'] * person_count
                    ing_list[ing['ingredient_name']] = need_ing
                else:
                    ing_list[ing['ingredient_name']]['quantity'] = ing_list[ing['ingredient_name']]['quantity'] + \
                                                                   ing['quantity'] * person_count
    return ing_list
food_good = food_file('dz.txt', 'r')
def result():
    print(food_file('dz.txt','r'))
    print(get_shop_list_by_dishes(dishes=['Омлет','Сырники'], person_count=2))
result()