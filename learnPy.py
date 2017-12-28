class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

my_dog=Dog("my_dog",13)

print("My dog's name is "+my_dog.name.title()+".")

your_dog=Dog("your dog",1)
print("Your dog's name is "+your_dog.name.title()+".")

a={}
a['root']="a"
print(a['root'])

from collections import OrderedDict

myfavoratelanguage=OrderedDict()
myfavoratelanguage['tool']=12
print(myfavoratelanguage['tool'])


file_name="my_language.txt"

with open(file_name,'a') as fileobj:
    fileobj.write("\nI love python!")


try:
    print(5/0)
except ZeroDivisionError:
    print("you cannot divide by zero")


x=[1,2,3]
y=[4,5,6]

for a,b in [x,y]:
    print(a)
    print("and")
    print(b)

