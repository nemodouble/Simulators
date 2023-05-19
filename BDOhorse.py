import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter

# 값 받기
print("# 엔터 입력시 기본값 설정 #")
print("시뮬레이션 횟수(기본값:100000) : ", end='')
try:
    total_try_person_count = int(input())
except:
    total_try_person_count = 100000

print("시뮬레이션 출력(기본값:F) T/F: ", end='')
try:
    input_str = input()
    do_print_simulation = input_str == 'T' or input_str == 't'
except:
    do_print_simulation = False


success_try_count_list = []
high_try_count = 0

# 시뮬레이션
for try_person_index in range(1, total_try_person_count + 1):
    # 최초 성공 확률
    success_percentage = 0.01
    # 스택
    try_stack_count = 0
    while True:
        # 성공시
        if random.random() < success_percentage:
            # 시뮬레이션 출력
            if do_print_simulation:
                print(str(try_person_index) + "번째 환장마피해자 " + str(try_stack_count) + "트 성공")
            # 성공 횟수 저장
            success_try_count_list.append(try_stack_count)
            # 최대 스택일시 저장
            if try_stack_count > high_try_count:
                high_try_count = try_stack_count
            # 확률 및 스택 초기화
            try_stack_count = 0
            success_percentage = 0.01
            break
        # 실패시
        else:
            # 시뮬레이션 출력
            if do_print_simulation:
                print(str(try_person_index) + "번째 환장마피해자 " + str(try_stack_count) + "스택 실패")
            # 스택 및 성공확률 증가
            success_percentage += 0.002
            try_stack_count += 1
    if do_print_simulation:
        print()
    else:
        print("\r진행 중 " + str(int(try_person_index / total_try_person_count * 100)) + "%", end='')
success_try_count_list.sort()

# 평균 및 최대값 출력
AVG = sum(success_try_count_list) / len(success_try_count_list)
print("\n\n"
      "성공 스택 평균 : " + str(AVG))
print("최대 스택 : " + str(high_try_count))

# 퍼센트 확인
print("\n"
      "자신의 스택이 몇 퍼센트에 위치 하는지 확인")
print("스택 입력 : ", end='')
try:
    my_try = int(input())
    if my_try <= 0:
        raise Exception
    for i in range(1, len(success_try_count_list)):
        if success_try_count_list[i] > my_try:
            print("상위 " + str(i / total_try_person_count * 100) + "%")
            break
except Exception as e:
    print("예외 발생", e)

# 성공 스택 분포표 출력
plt.hist(success_try_count_list, bins=20, weights=np.ones(len(success_try_count_list))/len(success_try_count_list))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.xticks(np.arange(0, 100, 5))
plt.show()
