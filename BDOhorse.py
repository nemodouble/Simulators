import random
import matplotlib.pyplot as plt

maxTrierCount = 100000
successStack = []
hightry = 0;
for trierCount in range(1, maxTrierCount):
    successProbality = 0.01
    tryCount = 1
    while True:
        if random.random() < successProbality:
            print(str(trierCount) + "번째 환장마피해자 " + str(tryCount) + "트 성공")
            successStack.append(tryCount)
            if tryCount > hightry:
                hightry = tryCount
            tryCount = 1
            successProbality = 0.01
            break
        else:
            print(str(trierCount) + "번째 환장마피해자 " + str(tryCount) + "트 실패")
            successProbality += 0.002
            tryCount += 1
    print()
AVG = sum(successStack) / len(successStack)
#deviation =
print("성공스택 평균 : " + str(AVG))
print("최대스택 : " + str(hightry))

successStack.sort()
for i in range(1, len(successStack)):
    if successStack[i] > 60:
        print("상위" + str(i/maxTrierCount*100) )
        break;
plt.hist(successStack, bins=20)
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
plt.show()
