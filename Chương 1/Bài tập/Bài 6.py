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
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
        else:
            print("Nội dung stack (từ đáy → đỉnh):", self.stack)
s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.print()
s.pop()
s.print()
