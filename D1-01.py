import random
secret = random.randint(1,10)
print('---------我爱郝斌培训班----')
temp = input("不妨猜一下郝斌现在心里想的是哪个数字：")
guess = int(temp)
while guess != secret:
    temp = input("你猜错了，请重新猜过：")
    guess = int(temp)
    if guess == secret:
        print ("哈哈猜对啦")
        print ("嘿嘿，你真伟大")
    else:
        if guess > secret:
            print("你猜的有点大")
        else:
            print("你猜的有点小")
print("游戏结束")    
  
