import re


x = re.fullmatch(r"[A-Z]*",'ADEFYUOP')

print(x.span())

y = re.fullmatch(r"[L]{3}",'PPALLPLLL')
print(y)

pattern = re.compile(r'[L]{3}')
m = pattern.search('PPALLPLLL')
print(m)
