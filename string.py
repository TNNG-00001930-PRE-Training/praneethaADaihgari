#print even length words

string="python is a programming language"
l1=string.split(" ")
for i in l1:
    if len(i)%2==0:
        print(i)