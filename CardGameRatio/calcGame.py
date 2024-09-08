
def calc_game_probability(game, target_prob):
    game_prob_sum_list = dict()
    for i in range(game + 1) :
        game_prob_sum_list[i] = 0

    game_probability(game, target_prob, game_prob_sum_list, 1, 0)
    return game_prob_sum_list 

def game_probability(game, target_prob, game_prob_sum_list, game_prob, game_hit_sum):
    if game <= 0:
        game_prob_sum_list[game_hit_sum] += game_prob
        return None
    #当たる分岐
    game_probability(game - 1, target_prob, game_prob_sum_list, game_prob * target_prob, game_hit_sum + 1)
    #外れる分岐
    game_probability(game - 1, target_prob, game_prob_sum_list, game_prob * (1 - target_prob), game_hit_sum)
        
#target枚以上当たる確率の計算
def calc_target_over(prob_sum_list, target):
    target_over_pro = 0
    n = len(prob_sum_list) - 1
    while n >= target :
        target_over_pro += prob_sum_list[n]
        n -= 1
    return target_over_pro