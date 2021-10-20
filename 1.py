# 猜拳游戏
import random

times=0
win=0
lose=0
dic={"石头":0,"剪刀":1,"布":2}
print("我们开始游戏吧，游戏三局两胜\n请输入 石头、剪刀、布 中的一个：")
while win<2 and lose<2:
    times+=1
    s=input()
    usr=dic[s]
    bot=random.randint(0,2)
    if usr-bot==-1 or usr-bot==2:
        print(f"你赢了第{times}局比赛")
        win+=1
    elif usr-bot==1 or usr-bot==-2:
        print(f"你输了第{times}局比赛")
        lose+=1
    elif usr-bot==0:
        print(f"平局重赛")
        times-=1
if win==2:
    print(f"你赢了比赛")
elif lose==2:
    print(f"你输了比赛")
