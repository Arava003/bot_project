lst = ['1qqq', '1', '1', '1', '1', '1', '1']
x1 = 0
y1 = 0
print(lst[1:])
for i in lst[1::2]:
    x1 += float(i)
    y1 += float(lst[lst.index(i) + 1])
    print(x1, y1)