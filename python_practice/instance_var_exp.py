# instance and class attributes
class a:
    live_data = None


a_obj = a()
b_obj = a()

print(a_obj.live_data)
print(b_obj.live_data)

# a.live_data = 20
# print(id(a.live_data))
# print(id(a_obj.live_data))
# print(id(b_obj.live_data))
a.live_data = 50
print(id(a_obj.live_data))
print(a_obj.live_data)
print(b_obj.live_data)
a_obj.live_data = 45
print(a_obj.live_data)
print(b_obj.live_data)




