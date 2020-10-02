names = ["John", "Mom", "Dad", "Jeff"]
print("\n".join(names))


import os
filename = "README.md"
location_of_files = "./"
with open(os.path.join(location_of_files, filename)) as f:
    print(f.read())


who = "Gary"
how_many = 12
print("{} bought {} apples".format(who, how_many))
print("{0} bought {0} apples".format(who, how_many))
print("{1} bought {0} apples".format(who, how_many))




