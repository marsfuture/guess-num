import random
r = random.randint(1, 100)
count = 0
while True:
    number = input('請輸入數字: ')
    number = int(number)
    count += 1 # 是 count = count + 1 的快寫法
    if number == r:
        print('終於猜對了')
        print('你猜了', count, '次')
        break
    elif number > r:
        print('比答案大')
    else :
        print('比答案小')
    print('你猜了', count, '次') #寫在if架構之後，可以減少程式重複次數

