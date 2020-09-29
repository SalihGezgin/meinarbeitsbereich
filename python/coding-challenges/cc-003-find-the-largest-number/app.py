# Write a python code that finds the largest number among the 5 numbers given by the user as input
number = input("Please enter 5 numbers to learn the largest number among them \n").split(" ")
maxnumber = 0
for i in number:
    for n in number:
        if int(i) > maxnumber and int(i) > int(n):
            maxnumber = int(i)
print (maxnumber)