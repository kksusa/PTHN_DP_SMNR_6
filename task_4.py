import random
import check_module


# Функция генерации абсолютно любых неповторяющихся позиций ферзей
def generate_pos():
    pos_list = []
    while len(pos_list) < 9:
        num1 = random.randint(1, 8)
        num2 = random.randint(1, 8)
        if not pos_list:
            pos_list.append((num1, num2))
        else:
            check_ = True
            for j in pos_list:
                if (num1, num2) == j:
                    check_ = False
                    break
            if not check_:
                continue
            else:
                pos_list.append((num1, num2))
    return pos_list


# Функция более корректной генерации позиций ферзей, где вертикальные и горизонтальные ряды содержат не более одного
# ферзя
def gen_pos_right():
    pos_list = []
    second_pos = [1, 2, 3, 4, 5, 6, 7, 8]
    for k in range(1, 9):
        num = random.choice(second_pos)
        pos_list.append((k, num))
        second_pos.remove(num)
    return tuple(pos_list)


count = 1
hashes = []
MAX_COUNT = 4  # число отображения верных координат ферзей без пересечения (макс. 92, что и вводится для получения всех
# возможных вариантов)
while count <= MAX_COUNT:
    variant = gen_pos_right()
    if check_module.check_queen_cut(variant):
        if not hashes:
            hashes.append(hash(variant))
        else:
            check = True
            for i in hashes:
                if hash(variant) == i:
                    check = False
                    break
            if not check:
                continue
            else:
                hashes.append(hash(variant))
        print(f'{count}: {variant}')
        count += 1
