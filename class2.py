"""class Animal:
    def speak(self):
        print("Animal is speaking ")
class Dog(Animal):
    def bark(self):
        print("dog barking")
d=Dog()
d.bark()
d.speak()"""

"""def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(n1, n2):
    for number in range(n1, n2 + 1):
        if is_prime(number):
            print(number)

# Example usage:
n1 = 1
n2 = 10
print("Prime numbers between", n1, "and", n2, "are:")
print_primes_in_range(n1, n2)"""

"""d=lambda p:p*5
t=lambda p:p*2
x=7
x=d(x)
x=t(x)
print(x)
nums=[6,16,26,36,46,56]
result=list(map(lambda x:x*2+2-4,nums))
print(result)
t=[1,2,3,4,5,6,7,8,9]
result=filter(lambda v:v%2!=0,t)
print(list(result))"""

"""dict={}
dict['one']='This is one'
dict[2]="This is two"
tinydict={"name":'Sakshi','Code':2212,"dept":'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())"""
"""This is one
This is two
{'name': 'Sakshi', 'Code': 2212, 'dept': 'sales'}
dict_keys(['name', 'Code', 'dept'])
dict_values(['Sakshi', 2212, 'sales'])"""

"""
a=['abc','pqr','www']
print(a)
print(a[1])
print(len(a))
print(type(a))
d={6:"six"}
d[5]="five"
d[10]='ten'
print("dictionary",d)
del d[10]
print("dictionary",d)

 OUTPUT
['abc', 'pqr', 'www']
pqr
3
<class 'list'>
dictionary {6: 'six', 5: 'five', 10: 'ten'}
dictionary {6: 'six', 5: 'five'}"""

"""
from os import walk
dir_path = r'Desktop'
res=[]
for(dir_path,dir_names,file_names)in walk(dir_path):
    res.extend(file_names)
print(res)"""

"""import os.path
path='Desktop'
norm_path=os.path.normpath(path)
print(norm_path)"""

"""def split_string (string):
    list_string=string.split(' ')
    return list_string
def join_string(list_string):
    string='-'.join(list_string)
    return string
if __name__=='__main__':
    string='Hey this is my file'
    list_string=split_string(string)
    print(list_string)
    new_string=join_string(list_string)
    print(new_string)

    OUTPUT

    ['Hey', 'this', 'is', 'my', 'file']
    Hey-this-is-my-file 
    """


