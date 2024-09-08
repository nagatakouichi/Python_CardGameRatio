import inputManager
import calcDraw
import calcGame
import calcExpectedValue

def main():
    is_calc_deck = True
    while is_calc_deck :
        deck, hit, check = inputManager.input_nums()
        prob_sum_list = calcDraw.calc_draw_probability(deck, hit, check)
        #期待値
        expected_value = calcExpectedValue.calc_excepted_value(prob_sum_list)
        #画面表示
        print('')
        print(f'当たりの期待値：{round(expected_value, 2)}枚')
        for key in prob_sum_list.keys():
            hit_percent = round(prob_sum_list[key] * 100, 2)
            print(f'{key}枚当たる確率：{hit_percent}%')
        print('')
        input_code = input('デッキ・当たり・めくる枚数を変更するときは[d]を、複数ゲーム時の確率計算に移る場合は[g]を入力してください。それ以外が入力されると終了します。>>')
        if input_code == 'd' :
            continue
        elif input_code != 'g' :
            break
        
        #複数ゲーム時の確率
        is_calc_game = True
        while is_calc_game :
            game, target = inputManager.input_games(check)
            target_over_pro = calcGame.calc_target_over(prob_sum_list, target)
            target_hit_percent = round(target_over_pro * 100, 2)
            print(f'{target}枚以上当たる確率：{target_hit_percent}%')
            game_prob_sum_list = calcGame.calc_game_probability(game, target_over_pro)
            game_expected_value = calcExpectedValue.calc_excepted_value(game_prob_sum_list)
            #期待値
            print(f'当たりを引くゲームの期待値：{round(game_expected_value, 2)}ゲーム')
            #画面表示
            for key in game_prob_sum_list.keys():
                game_hit_percent = round(game_prob_sum_list[key] * 100, 2)
                print(f'{target}枚当たるゲームが{key}回の確率：{game_hit_percent}%')

            #再計算確認
            print('')
            code = input('デッキ・当たり・めくる枚数を変更するときは[d]を、ゲーム数・目標当たり数を変更するときは[g]を入力してください。それ以外が入力されると終了します。>>')
            if code == 'd' :
                is_calc_game = False
            elif code == 'g' :
                continue
            else:
                is_calc_game = False
                is_calc_deck = False    
    
main()

