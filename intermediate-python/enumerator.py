example = ["right", "left", "up", "down"]
for i, j in enumerate(example):
    print(i, j)

#List comprehension version of the loop
[print(i,j) for i, j in enumerate(example)]

new_dict = dict(enumerate(example))
print(new_dict)

