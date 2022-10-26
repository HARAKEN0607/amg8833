list = [[20, 30, 40, 50], [15, 25, 35, 45]]

for n in range(0, 2, 1):
    temp_arrange = list[n]

    for d in range(0, 4, 1):
        temp = temp_arrange[d]
        if temp > 30:
            print("異常温度を検知しました。  検知温度：" + str(temp) + '℃')


