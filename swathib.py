x= open("input0.txt",'r').read().split('\n')
x.pop(0)
l=[]
k=[]
d={}
for a in x:
	p=a.split(": ")
	l.append(p)
for a in l:
	if a[0] not in d:
		d[a[0]]=a[1]
for x in d.values():
	k.append(int(x))
k.sort()
no=int(input("Enter number of employees:"))
j=[]
for x in range(len(k)-no):
	j.append(k[x+no-1]-k[x])
a=sorted(j)
s=j.index(a[0])
c=(k[s:s+no])

f = open("output.txt", "w")
f.write("Here the goodies that are selected for distribution are:\n")
for k,v in d.items():
	if int(v) in c:
		f.write(k+": "+v+"\n")
f.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(a[0]))
f.close()