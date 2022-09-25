#輸入對應元素，形成名為numbers的列表
numbers = [1, 2, 3, 4, 5, 6, 7]
#創造一個一樣的list，用於待會計算
list1 =  [1, 2, 3, 4, 5, 6, 7]
#創造一個空的列表
list2 = []
#將list各項依序相乘，並使用append加入list2(空列表)
for i in range(len(numbers)):
    v1 = numbers[i]*list1[i]
    list2.append(v1)
#輸出list2
print(list2)