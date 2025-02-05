class parrot:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,sing):
        print("{} sings {}".format(self.name, sing))

    
    def dance(self):
        print("{} is now dancing".format(self.name))    


blu = parrot("Blu",10)

blu.sing("'Happy'")
blu.dance()

