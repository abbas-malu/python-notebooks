class Stack():
    """
    Creating and implementing stack in python
    """
    def __init__(self, *a):
        """
        Initialing Stack    
        """
        if len(a)==1:
            if type(a[0])==tuple or type(a[0]==list) or type(a[0]==str):
                self.stk = [i for i in a[0]]
        else:
            self.stk = list(a)
    def __str__(self):
        return str(self.stk)+str(f'stack{len(self.stk)}')
    def __len__(self):
        return len(self.stk)
    def push(self,item):
        self.stk.append(item)
        # return self.stk
    def pop(self):
        popped = self.top
        self.stk.pop(self.top)
        return popped
    @property
    def top(self):
        return len(self.stk)-1
    @property
    def peek(self):
        return self.stk[len(self.stk)-1]
    
if __name__ == "__main__":
    print('Creating and implemeting stack in python')