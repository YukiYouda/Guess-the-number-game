import random

n = int(input("最小値を入力してください : "))
m = int(input("最大値を入力してください : "))

answer_num = random.randint(n, m)

for i in range(5):
    user_answer = int(input("数字を推測してください : "))
    int
    if answer_num == user_answer:
        print("正解です")
        break
    else:
        print("不正解です")
