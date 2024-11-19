#create a pattern
#1   1
#12 21
#12321
#n=3
#for i in range(1,n+1):
 #   for j in range(1,i+1):
  #      print(j,end=' ')
   # for j in range (i+1,n*2-i):
    #    print(' ',end=' ')
    #for j in range(i,0,-1):
     #   print(j,end=' ')
#print()
# 1 21 321 pattern
'''n=4
for i in range(1,4):
    for j in range(i,0,-1):
        print(j,end=' ')
        
    print()'''  


    # 1-12-123-1234 Pattern up to n lines

'''n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1, i+1 , 2 , i-1):
        print(j, end="")
    print()  '''
 

n = 3
for i in range(1, n + 1):
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end=' ')
    
    # Print spaces
    for j in range(2 * (n - i)):
        print(' ', end=' ')
    
    # Print decreasing numbers
    for j in range(i, 0, -1):
        #if j != n:  # To avoid printing an extra space at the end
            print(j, end=' ')
    print()  # Move to the next line
