# Функция проверки на пересечение ферзей
def check_queen_cut(pos_list):
    for i in range(8):
        for j in range(i + 1, 8):
            if pos_list[i][0] == pos_list[j][0] or pos_list[i][1] == pos_list[j][1] or \
                    pos_list[i][0] + pos_list[i][1] == pos_list[j][0] + pos_list[j][1] or \
                    abs(pos_list[i][0] - pos_list[j][0]) == abs(pos_list[i][1] - pos_list[j][1]):
                return False
    return True
