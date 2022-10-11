class Node():
    """節點"""
    def __init__(self, name=None, birthday=None, gender=None, heigh=None, weight=None, degree=None, next=None):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.heigh = heigh
        self.weight = weight
        self.degree =degree
        self.next = next

    def showinfo(self):
        print(self.name, self.birthday, self.gender, self.heigh, self.weight, self.degree)

class Linked_list():
    def __init__(self):
        self.head = None

    def append(self, Newname, Newbirthdat, Newgender, Newheight, Newweight, Newdegree):
        new_data = Node(Newname, Newbirthdat, Newgender, Newheight, Newweight, Newdegree)
        if self.head is None:
            self.head = new_data
        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        last_ptr.next = new_data

    def insert(self, index, Newname, Newbirthdat, Newgender, Newheight, Newweight, Newdegree):
        node = self.head
        current = self.head
        previous = None
        count = 0
        if index == 0:
            self.head = Node(Newname, Newbirthdat, Newgender, Newheight, Newweight, Newdegree, node)
        else:
            while count != index:
                count += 1
                previous = current
                current = current.next
            new_node = Node(Newname, Newbirthdat, Newgender, Newheight, Newweight, Newdegree, previous.next)
            previous.next = new_node

    def delete(self, dataname, all=False):
        current = self.head
        previous = None
        while current:
            if current.name == dataname:
                if previous:
                    previous.next = current.next
                    current.next = current
                else:
                    self.head = current.next
                if not all:
                    return
            else:
                previous = current
                current = current.next

    def index(self, name):
        node = self.head
        count = 0
        while node:
            if node.name == name:
                print(f'{name} 在第 {count} 個')
            count += 1
            node = node.next

    def showAll(self):
        """列印連結串列"""
        ptr = self.head
        while ptr:
            print(ptr.name, ptr.birthday, ptr.gender, ptr.heigh, ptr.weight, ptr.degree)
            ptr = ptr.next

    def sort(self, head):
        if not head: return head
        if not head.next: return head

        mid = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next
        mid.next, mid = None, mid.next
        return self.mergeTwoLists(self.sort(head), self.sort(mid))

    def mergeTwoLists(self, l1, l2):
        root = head = Node(0)
        while l1 and l2:
            if l1.name < l2.name:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return root.next

    def getSize(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        print(f'總共 {count} 個')

    def isExist(self, name, birthday, gender, heigh, weight, degree):
        node = self.head
        while node:
            if node.name == name and node.birthday == birthday and node.gender == gender and\
                    node.heigh == heigh and node.weight == weight and node.degree == degree:
                print(f'{name} 存不存在: True')
                break
            else:
                node = node.next
        else:
            print(f'{name} 存不存在: False')

link = Linked_list()

# 初始鏈結串列
print('新增串列:')
link.head = Node('Dennis', 911007, 1, 170, 65, 'good')
link.append('Sandy', 911021, 1, 165, 78, 'nice')
link.append('Junwe', 920315, 2, 180, 72, 'nice')
link.append('Eric', 920426, 1, 167, 56, 'bad')
link.showAll()
print('-' * 100)

# 新增
print('指定位子新增:')
link.insert(0, 'Max', 930405, 2, 154, 45, 'bad')
link.showAll()
print('-' * 100)

# 刪除
print('刪除:')
link.delete('Max')
link.showAll()
print('-' * 100)

# 尋找位子
link.index('Eric')
print('-' * 100)

# 排列
link.sort(link.head)
print('排列後:')
link.showAll()
print('-' * 100)

# 總數
link.getSize()
print('-' * 100)

# 存不存在
link.isExist('Eric', 920426, 1, 167, 56, 'bad')
print('-' * 100)
