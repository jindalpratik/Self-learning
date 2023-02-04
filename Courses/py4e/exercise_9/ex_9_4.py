fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Not a correct file name.')
    exit()
di = {}
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    li = line.split()
    di[li[1]] = di.get(li[1], 0) + 1
# print(di)
max = 0
index = 0
for i in di:
    if di[i] > max:
        index = i
        max = di[i]
print(index , di[index])