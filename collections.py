from collections import deque

d = deque('hello')
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())
