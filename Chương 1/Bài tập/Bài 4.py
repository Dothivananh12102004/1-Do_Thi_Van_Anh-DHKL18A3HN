class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.capacity
    
    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm!")
        else:
            self.stack.append(value)
            print(f"Đã push {value} vào stack")
    
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng, không thể pop!")
            return None
        else:
            value = self.stack.pop()
            print(f"Đã pop {value} ra khỏi stack")
            return value
s = Stack(3)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.pop()
s.pop()
s.pop()
s.pop()

