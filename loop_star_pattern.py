''' pattern 1
n = 4
for i in range(4):
    print(" * " * (i+1))
    
    o/p
    *
    **
    ***
    ****
    '''
# pattern 2
''' 
n = 3 
for i in range(3):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (n-i-1))

op
    *
  * * * 
* * * * *'''
# pattern 3
'''n = 3
for i in range(3):
    print("*" * (n-i-1),end="")
    print("*" * (1*i-1),end="")
    print("*" * (n-i-1)) 

op
****
**
*
'''

