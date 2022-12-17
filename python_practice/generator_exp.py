dig = {
    2: 'abc',
    3: 'def',
    4: 'ghi'

}

gen_list = [(x for x in dig[int(i)]) for i in '234']

print(gen_list)
