#輸入對應資料
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
#創造一個空白列表
list3 = []
#將list各項依序相加，並使用append加入list3(空列表)
for i in range(len(list1)):
    v1 = list1[i]+list2[i]
    list3.append(v1)
#輸出list3
print(list3)
