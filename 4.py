#創造列表
list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
#運用len()數出元素個數
v1 = len(list1)
#將項數除以2取整除數作為mid_index
a1 = v1 // 2
#列出mid_index前的元素
b1 = list1[:a1]
#列出mid_index後的元素
c1 = list1[a1:]


#運用len()數出元素個數
v2 = len(list2)
#將項數除以2取整除數作為mid_index
a2 = v2 // 2
#列出mid_index前的元素
b2 = list2[:a2]
#列出mid_index後的元素
c2 = list2[a2:]

#將各分割後元素作排列組合
q = b1+b2
q = [' '.join(q)]
qq = b1+c2
qq = [' '.join(qq)]
qqq = b2+c1
qqq = [' '.join(qqq)]
qqqq = b2+c2
qqqq = [' '.join(qqqq)]

#將內容整合並輸出
qqqqq = q + qq + qqq + qqqq
print(qqqqq)