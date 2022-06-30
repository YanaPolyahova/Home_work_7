from pprint import pprint
import os

file_name = "cook_book_file.txt"

def cook_book_reader(file_name):
    with open(file_name, encoding='utf-8') as file_obj:
        resalt = {}
        for line in file_obj:
            dish_name = line.strip()
            resalt[dish_name] = []
            for item in range(int(file_obj.readline())):
                ingredients = file_obj.readline()
                ingredients_list = ingredients.split(sep=" | ")
                ingredient_dict = dict()
                ingredient_dict['ingredient_name'] = ingredients_list[0].strip()
                ingredient_dict['quantity'] = int(ingredients_list[1])
                ingredient_dict['measure'] = ingredients_list[2].strip()
                resalt[dish_name].append(ingredient_dict)
            file_obj.readline()
        return resalt

cook_book = cook_book_reader(file_name)
pprint(cook_book)

print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    for dish in dishes:
        if dish in cook_book:
            for ings in cook_book[dish]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in shop_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    shop_list[ings['ingredient_name']] = meas_quan_list
                else:
                    shop_list[ings['ingredient_name']]['quantity'] = shop_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count
        else:
            print(f' \n "Такого блюда нет в списке!" \n ')
    return shop_list

pprint(get_shop_list_by_dishes(dishes=['Фахитос'], person_count= 4))

print()

def rewrite_file(path1=None, path2=None, path3=None):
    if path1 or path2 or path3 is None:
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = '3.txt'
        output_file = "general_file.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open(output_file, 'w', encoding='utf-8') as f_total:

            if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)

    return

rewrite_file(path1='4.txt', path2='2.txt', path3='3.txt')

