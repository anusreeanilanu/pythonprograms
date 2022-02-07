file_obj = open('sample1.txt','r+')
condition = True
while condition:
    line = file_obj.readline()
    words = line.split(" ")
    if(len(words)>5):
        x = words[0]
        if(x[0].isupper()):
            print(line)
    if not line:
        condition = False
        print("end of the file")
