# Use open function to read the content of a file..


#f=open('sample.txt','r')
f=open('sample.txt') # by default the mode are 
#data = f.read()
data = f.read(5) # this line read only 5 letters
print(data)
f.close()