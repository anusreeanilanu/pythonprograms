f=open("file1.txt","r")
f1=open("oddfile.txt","w")
cont=f.readlines()
for i in range(0,len(cont)):
    if i%2!=0:
        f1.write(cont[i])
f1.close()
f1=open('oddfile.txt','r')
cont1=f1.read()
print(cont1)
f.close()
f1.close()
        
        
