#確率計算（再帰関数）
def calc_draw_probability(deck, hit, check):
    prob_sum_list = dict()
    for i in range(check + 1) :
        prob_sum_list[i] = 0
    draw_probability(deck, hit, check, prob_sum_list, 1, 0)
    return prob_sum_list   

def draw_probability(deck, hit, check, prob_sum_list, hit_prob, drawing_hit_sum):
    if check <= 0 :
        prob_sum_list[drawing_hit_sum] += hit_prob
        return None
    #当たる分岐
    draw_probability(deck - 1, hit - 1, check - 1, prob_sum_list, hit_prob * hit / deck, drawing_hit_sum + 1)
    #外れる分岐
    draw_probability(deck - 1, hit, check -1, prob_sum_list, hit_prob * (1 - hit / deck), drawing_hit_sum)