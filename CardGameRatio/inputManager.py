#初期値入力とチェック
def input_nums():
    deck = 0
    hit = 0
    check = 0
    is_error_num = True
    while is_error_num :
        try:
            deck = input('デッキ枚数 >>')
            deck = int(deck)
            hit = input('当たりの枚数 >>')
            hit = int(hit)
            check = input('めくる枚数 >>')
            check = int(check)
        except ValueError:
            print('ValueError:整数以外が入力されました。')
            continue
        
        if deck <= 0 or hit <= 0 or check <= 0 :
            print('エラー：０以下の値が入力されています。入力できる数は１以上です')
            continue
        if hit > deck :
            print('エラー：当たりの数がデッキ枚数より多くなっています')
            continue
        if check > deck :
            print('エラー：めくる枚数がデッキ枚数より多くなっています')
            continue
        if check > 25 :
            print('エラー：めくる枚数が制限(25枚)より多くなっています')
            continue
        is_error_num = False

    return deck, hit, check

def input_games(check):
    game = 0
    target = 0
    is_error_num = True
    while is_error_num :
        try:
            game = input('ゲーム数 >>')
            game = int(game)
            target = input('毎ゲームの目標当たり数 >>')
            target = int(target)
        except ValueError:
            print('ValueError:整数以外が入力されました。')
            continue

        if target > check:
            print('エラー：目標当たり数がめくる枚数より多くなっています')
            continue
        if game <= 0:
            print('エラー：ゲーム数が0以下になっています')
            continue
        if game > 25:
            print('エラー：ゲーム数が制限(25回)を超えています')
            continue

        is_error_num = False
    return game, target