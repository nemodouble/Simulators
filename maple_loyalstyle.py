import random

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter

# 확률 설정
special_label_weapon_percentage = 0.025
special_label_cape_percentage = 0.03
special_label_shoes_percentage = 0.032
special_label_cloth_percentage = 0.032
special_label_head_percentage = 0.031

# 획득할 아이템 여부
want_special_label_weapon = True
want_special_label_cape = True
want_special_label_shoes = True
want_special_label_cloth = True
want_special_label_head = True

# 가격 설정
loyal_style_price = 2200

# 시뮬레이션 설정
simulating_count = 100000
do_print_log_each_simulation = False
total_spend_money_array = list(0 for i in range(0, simulating_count))

weapon_percentage_range = special_label_weapon_percentage
cape_percentage_range = weapon_percentage_range + special_label_cape_percentage
shoes_percentage_range = cape_percentage_range + special_label_shoes_percentage
cloth_percentage_range = shoes_percentage_range + special_label_cloth_percentage
head_percentage_range = cloth_percentage_range + special_label_head_percentage

for i in range(simulating_count):
    # 시뮬레이션 초기화
    total_spend_money = 0
    get_weapon = not want_special_label_weapon
    get_cape = not want_special_label_cape
    get_shoes = not want_special_label_shoes
    get_cloth = not want_special_label_cloth
    get_head = not want_special_label_head

    while not (get_weapon and get_cape and get_shoes and get_cloth and get_head):
        # 금액 지불
        total_spend_money += loyal_style_price

        # 뽑기 결과
        random_float = random.random()

        if random_float <= weapon_percentage_range:
            get_weapon = True
            if do_print_log_each_simulation:
                print("스라벨 무기 획득")

        elif random_float <= cape_percentage_range:
            get_cape = True
            if do_print_log_each_simulation:
                print("스라벨 망토 획득")

        elif random_float <= shoes_percentage_range:
            get_shoes = True
            if do_print_log_each_simulation:
                print("스라벨 신발 획득")

        elif random_float <= cloth_percentage_range:
            get_cloth = True
            if do_print_log_each_simulation:
                print("스라벨 한벌옷 획득")

        elif random_float <= head_percentage_range:
            get_head = True
            if do_print_log_each_simulation:
                print("스라벨 머리 획득")

        else:
            if do_print_log_each_simulation:
                print("잡 로얄 획득")

        if total_spend_money < 0:
            break
    if do_print_log_each_simulation:
        print(str(total_spend_money) + "원 소모")
    else:
        print("\r진행 중 " + str(int(i / simulating_count * 100)) + "%", end='')
    total_spend_money_array[i] = total_spend_money

print("\n평균 " + str(sum(total_spend_money_array) / len(total_spend_money_array)) + "원 소모 ")

total_spend_money_array.sort()

# 유의미한 최대 숫자
max_value = 600000#total_spend_money_array[simulating_count-1]
plt.hist(total_spend_money_array, bins=20, range=[0, max_value], \
         weights=np.ones(len(total_spend_money_array))/len(total_spend_money_array))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.xticks(np.arange(0, max_value, int(max_value / 20)), rotation=90)
plt.show()
