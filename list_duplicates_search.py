DATA_LIST = ['a', 'b', 'c', 'a', 'c', 'c', 'b', 'a', 'c', 'a', 'a']
l = {}

for d in DATA_LIST:
    if d not in l:
        l.update({d: 1})
    else:
        l.update({d: l.get(d) + 1})

print l
