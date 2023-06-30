class Stack:
    def __init__(self):
        self.stack = []
        self.max_size = 3 
        self.top = -1 
    def push(self, el):
        if self.top >= self.max_size -1:
            raise Exception("Stack Overflow") 
        self.stack.append(el)
        self.top +=1
        print("Pushed:",el, "Top:", self.top)
    def pop(self):
        if self.top <= -1:
            raise Exception("Stack Empty")
        popped_el= self.stack.pop()
        self.top -=1
        print("Popped:", popped_el,"Top: ", self.top)
        return popped_el
    
    def __str__(self):
        print("Stack Elements:")
        s = ""
        for i in reversed(self.stack):
           s += str(i)+"\n" 
        return s



s = Stack()
s.push(3)
s.push(5)
s.push(7)
print(s)
s.pop()
s.pop()
s.pop()
s.pop()
print(s)

