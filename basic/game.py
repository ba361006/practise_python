import random

# 死迴圈
while True:
    # 獲取電腦出拳的隨機數
    computer = random.randint(1, 3)
    # 獲取玩家出拳的數
    player = int(input("【1】：剪刀，【2】：石頭，【3】：布，請輸入你要出的拳頭："))
    # 玩家贏了
    if (computer == 1 and player == 2) or (computer == 2 or player == 3) or (computer == 3 and player == 1):
        print("恭喜你贏了電腦")
    # 平局
    elif computer == player:
        print("和電腦打成平手了，再接再厲")
    # 玩家輸了
    else:
        print("電腦贏了，繼續努力啊")