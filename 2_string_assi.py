letter=''' Dear <|NAME|>,
Greatings from ABC .i am so happy to tell you about your selection
You are Selected !!!!
Have a great day ahead !!!
Thanks And Regards,
XYZ
Date:<|DATE|>
'''
name = input("Enter Your Name \n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print("\n")
print(letter)