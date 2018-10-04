import random
secret = random.randint(1,5)
temp = input("请输入：")
guess = int(temp)
while guess != secret:
    temp = input("错啦，再输入:")
    guess = int(temp)
    if guess>secret:
        print("大了")
    else:
        if guess<secret:

           print("小了")
        else:
            print("正确")


print("游戏结束")