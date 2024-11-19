myDict ={
    "Pankha" : "Fan",
    "Pen" : "Pen",
    "Dabba" : "Box",
    "Vastu" :"Items"
}
print("Option are",myDict.keys())
a = input("Enter the Hindi Word\n")

#print("The meaning of your word is :",myDict[a])

#Below line will not throw the error if the key is not present in the dictionry

print("The meaning of your word is :",myDict.get(a))
