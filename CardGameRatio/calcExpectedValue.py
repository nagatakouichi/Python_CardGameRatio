#期待値計算
def calc_excepted_value(prob_sum_list):
    sum = 0
    for key in prob_sum_list.keys():
        sum += key * prob_sum_list[key]
    return sum