from collections import deque

class Stack:
    def __init__(self):
      self.container = deque()

    def push(self,val):
       self.container.append(val)
      
    def pop(self):
       return self.container.pop()

    def peek(self):
       return self.container[-1]

    def is_empty(self):
      return len(self.container)==0

    def size(self):
       return len(self.container)


def reverse_string(str):
  s = Stack()

  for i in str:
     s.push(i)
     
  if s.size() <= 1:
     print('str')

  str = ''

  while s.size() > 0:
     str += s.pop()

  return str


def is_match(ch1, ch2):
    match = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match[ch1] == ch2


def is_balanced(str):
    s = Stack()
    for ch in str:
        if ch=='(' or ch=='{' or ch == '[':
            s.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if s.size()==0:
                return False
            if not is_match(ch,s.pop()):
                return False

    return s.size()==0

str = 'Hello World'
print(str)

str = reverse_string(str)
print(str)

str = '({[Hello World]})'
print(is_balanced(str))

