class CSStudent:

    stream = "cse"

    def __init__(self,roll):
        self.roll= roll

    def set_address(self,address):
        self.address = address

    def get_address(self):
        return self.address  

add = CSStudent(101)
add.set_address("Pune,Mahrastara")
print(add.get_address())

a= CSStudent(101)
b= CSStudent(102)

print(a.stream)
print(b.stream)
print(a.roll)

print(CSStudent.stream)