import random
import matplotlib.pyplot as plt

maxTrierCount = 10000
successStack = []
for trierCount in range(1, maxTrierCount):
    successProbality = 0.01
    tryCount = 1
    while True:
        if random.random() < successProbality:
            print(str(trierCount) + "번째 환장마피해자 " + str(tryCount) + "트 성공")
            successStack.append(tryCount)
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

successStack.sort()
for i in range(1, len(successStack)):
    if successStack[i] > 37:
        print("상위" + str(i/maxTrierCount*100) )
        break;
plt.hist(successStack)
plt.show()