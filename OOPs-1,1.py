class Parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name= name
        self.age= age

blu = Parrot("Blu",10)
woo = Parrot("Woo",15)

print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))