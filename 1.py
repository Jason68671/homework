#讓使用者自行輸入元素，並形成list1
list1 = list(input().split()) 
#將list1內之元素做顛倒排列
list1.reverse() 
#將空格加入列表並用做分隔
list1 = ' '.join(list1)
#輸出list1
print( list1 )