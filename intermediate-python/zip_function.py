x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

for a,b in zip(x,y):
    print(a,b)

print([i for i in zip(x,y,z)])
[print(i) for i in zip(x,y,z)]
[print(a,b,c) for a,b,c in zip(x,y,z)]
