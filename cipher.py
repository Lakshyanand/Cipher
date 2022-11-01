import string

dict1={}
data=""
file=open("cipher.txt","w")
for i in range(len(string.ascii_letters)):
    dict1[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict1)
    
with open("python.txt") as f:
    while(True):
        c=f.read(1)
        if not c:
            print("file is empty")
            break
        if c in dict1:
            data=dict1[c]
        else:
            data=c
        file.write(data)
        print(data)
file.close()