firstfile = input("Enter the name of first file ")
secondfile = input("Enter the name of the second file ")

# opening both files in read only mode to read initial contents
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print(f1.read())
print(f2.read())

f1.close()
f2.close()