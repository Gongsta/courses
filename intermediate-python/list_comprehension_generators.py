#Returns list
a = [i for i in range(5)]
print(a)

#Returns generator object
a = (i for i in range(5))
print(a)


input_list = [5,6,4,3,2,2,4,25,6,7,7,77]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

#Wont require to save thing in memory
xyz = (i for i in input_list if div_by_five(i))
for i in xyz:
    print(i)
#Same thing as [print(i) for i in xyz]

#1 Liner for loops
[[print(i, ii) for ii in range(5)] for i in range(5)]
print(xyz)


xyz = [[[i, ii] for ii in range(5)] for i in range(5)]
print(xyz)



def simple_gen():
    yield "Oh"
    yield "hello"
    yield "there"

for i in simple_gen():
    print(i)


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo:{}'.format((c1, c2, c3)))
        break


