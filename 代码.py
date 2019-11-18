txt1 = open("text.txt",'r') 
hackers = []
for line in txt :
a = line.strip().split(' ')
count = 0
t = 0
for b in a :
b = a[t]
t += 1
count += 1
if count >= 100
hackers.append(b)
c = len(hackers)
txt2 = open("text.txt",'w')
txt2.write(count + '\n')
for d in hackers :
txt2.write(d + '\n')
txt2.close()
