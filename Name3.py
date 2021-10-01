# Add each character, and it's ordinal, of user's text input, to two lists

s = input("Enter value: ")  # this line requires Python 3.x, use raw_input() instead of input() in Python 2.x

l1=[c for c in s]   

l2=[ord(c) for c in s]

print(l1)

print(l2)
