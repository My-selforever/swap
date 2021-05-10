fi = open("file1.txt","r")
fil = open("file2.txt","r")

firead = fi.read()
filread = fil.read()

fiw = open("file1.txt","w")
filw = open("file2.txt","w")



fiw.write(filread)
filw.write(firead)