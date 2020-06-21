import collections

deck = collections.deque('\nhello\n')
# deck.append('\nhello\n')
for elem in deck:                   # iterate over the deque's elements
    print(elem.upper())


listy = ["\n","h","e","l","l","o","\n"]

for elem in listy:
    print(elem.upper())