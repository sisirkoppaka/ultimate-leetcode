class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack_1 = Stack()
        stack_2 = Stack()
        stack_3 = Stack()
        
        s_lst = list(s)
        
        for element in s_lst:
            if element in ['(',')']:
                if element == '(':
                    stack_1.push(element)
                else:
                    try:
                        if stack_1.pop() != '(':
                            return False
                    except:
                        return False
            elif element in ['{','}']:
                if element == '{':
                    stack_1.push(element)
                else:
                    try:
                        if stack_1.pop() != '{':
                            return False                        
                    except:
                        return False
            elif element in ['[',']']:
                if element == '[':
                    stack_1.push(element)
                else:
                    try:
                        if stack_1.pop() != '[':
                            return False                         
                    except: 
                        return False
                    
        if stack_1.isEmpty() and stack_2.isEmpty() and stack_3.isEmpty():
            return True
        else:
            return False
        