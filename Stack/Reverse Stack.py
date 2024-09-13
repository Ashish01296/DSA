class Stack:
    def __init__(self):
        self.stack = []
        self.index = -1

    
    def push(self,data):
        self.stack = [data] + self.stack
        self.index += 1
    

    def reverse(self):
        self.stack.reverse()
     
    

    def pop(self):
        self.stack.pop(0)
        self.index-=1




st = Stack()

st.push(10)
st.push(20)
st.push(30)
st.pop()


st.reverse()
print(st.stack)