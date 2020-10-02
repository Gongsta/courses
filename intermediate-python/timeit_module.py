import timeit

print(timeit.timeit("1+3"))
print(timeit.timeit("1+3", number=500000))
print(timeit.timeit("2-2", number=500000))