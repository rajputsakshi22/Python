num = int(input("Enter the number : "))
prime = True
for i in range(2,num):
  if(num%i == 0):
       prime = False
       break
if prime:
     
     print("The number is prime number")
else:
    print("The number is not prime")