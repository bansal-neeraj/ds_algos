# to check time difference between append and comprehension for list
"""
List comprehension is twice as fast as an append , and also faster than dictionary and set comprehension
"""
import timeit,dis

def list_via_append():
    """create a list using append """
    a = []
    for i in range(5000):
        a.append(i)


def list_via_comp():
    a = [x for x in range(5000)]


def dict_via_comp():
    a_dict = {x:'123' for x in range(5000)}
    # print(a_dict)


def set_via_comp():
    a_set = {x: '123' for x in range(5000)}
    # print(type(a_set))


if __name__ == '__main__':
    print('append',timeit.timeit("list_via_append()",setup="from __main__ import list_via_append",number=1000))
    print('list comp',timeit.timeit("list_via_comp()",setup="from __main__ import list_via_comp",number=1000))
    print('dict comp',timeit.timeit("dict_via_comp()",setup="from __main__ import dict_via_comp",number=1000))
    # print('set comp',timeit.timeit("set_via_comp()",setup="from __main__ import set_via_comp",number=1000))

    # print(dis.dis(list_via_append))
    # print(dis.dis(list_via_comp))