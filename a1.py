fo=open("Lorem.txt")
print("reading:")
print(fo.read()) #reading complete file
fo.close()

fo=open("Lorem.txt")
print("reading:")
print(fo.read(5)) #reading first five characters
fo.close()

fo=open("Lorem.txt")
ch=fo.read(1)
c=0
while ch:
    if ch in ["a","e","i","o","u","A","E","I","O","U"]:
        c+=1
    ch=fo.read(1)
print("Total number of vowels: ",c)

fo=open("Lorem.txt")
ch=fo.read(1)
c=1
while ch:
    if ch=="\n":
        c+=1
    ch=fo.read(1)
print("Total number of lines: ",c)

fo=open("Generated.txt","w")
fo.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc pharetra")
fo.close()

fo=open("Generated.txt","a")
fo.write("\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc pharetra")
fo.close()

'''
count number of words
count the words starting with t
'''