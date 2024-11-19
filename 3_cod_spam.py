from operator import truediv


text = input("Enter the Text \n")

if("make a lot of money" in text):
    spam = True
elif("Buy Now" in text):
    spam = True
elif("Click This" in text):
    spam = True
elif(" Subscribe This" in text):
    spam = True
else:
    spam = False
if(spam):
    print("This text is spam")
else:
    print("This is not spam ")