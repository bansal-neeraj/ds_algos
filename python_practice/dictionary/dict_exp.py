# plus + can NOT be used to add two dictionaries, unlike list
a = {
    1:'abc',
    2:[7,8,9]
}

b = {
    2:'def'
}

# c = a + b   NOT ALLOWED

a_list = [1,2,3]
b_list = [3,4,5]

c_list = a_list + b_list
print(c_list)

# update a dictionary with another dictionary
print(a)
a.update(b)

print(a)