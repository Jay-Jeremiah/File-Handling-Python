#open the file 
file1 = open("Intro.txt","r")

#read lines 
print(file1.readline())

#Looping through the file line by line
for x in file1:
    print (x)

#close the file 
file1.close()