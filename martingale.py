import random

money = 128

player_num = 0
winner = 0
drawer = 0
loser = 0

money_sum = 0
max_player_num = 100000
while player_num < max_player_num:
    player_num += 1
    game_num = 0
    bet = 2
    while 258 >= money >= 0:
        game_num += 1
        if random.random() <= 0.5:
            money += bet
            bet = 2
            # print(str(game_num) + " / 승리 /  현재 금액 : " + str(money) + " / 배팅액 : " + str(bet))
        else:
            money -= bet
            bet *= 2
            # print(str(game_num) + " / 패배 /  현재 금액 : " + str(money) + " / 배팅액 : " + str(bet))
        if game_num > 100:
            break
    if money > 128:
        winner += 1
        print(str(player_num) + "번 / 승리 / 승리자 : " + str(winner))
        # print("\n\n")
    elif money == 128:
        drawer += 1
        print(str(player_num) + "번 / 무승 / 무승자 : " + str(drawer))
        # print("\n\n")
    else:
        loser += 1
        print(str(player_num) + "번 / 패배 / 패배자 : " + str(loser))
        # print("\n\n")
    money_sum += money
    bet = 2
    game_num = 0
    money = 128

print("승리자 " + str(winner) + " / 패배자 " + str(loser) + " / 무승부 " + str(drawer))
print("종료 금액 평균 : " + str(money_sum/max_player_num))
