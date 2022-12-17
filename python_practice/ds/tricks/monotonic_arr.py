"""
Monotonic array - a stack in which elemnts are in a particular order

uses - can be used to create hash maps with some relation between the elements
following code creates a hash map where all elements in the list are keys and element greater on the right-hand side is
the value - leetcode - Q 496
"""

# code only works when elements are unique , if an element is repeated , earlier elemewnts are lost

# a = [1,2,3,4]
# a = [1, 3, 4, 2]
a = [2, 3, 5, 1, 0, 7, 3]

my_dict = {}
mono_stack = []

for i in a:
    if mono_stack:
        if i < mono_stack[-1]:
            mono_stack.append(i)
        else:
            while mono_stack and mono_stack[-1] < i:
                e = mono_stack.pop()
                my_dict[e] = i
            mono_stack.append(i)
    else:
        mono_stack.append(i)

while mono_stack:
    e = mono_stack.pop()
    my_dict[e] = -1


print(my_dict)
