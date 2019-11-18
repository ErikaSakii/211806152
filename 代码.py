txt1 = open("text.txt",'r') #打开文件
hackers = [] #建立用于放异常用户的列表
for line in txt : 
a = line.strip().split(' ') #把文件里的数据 按行分开
count = 0 #计用户发送数据包的次数
t = 0 
for b in a : #循环计数
if b in hackers :
continue
b = a[t]
t += 1
count += 1
if count >= 100
hackers.append(b) 
c = len(hackers) #异常用户个数
txt2 = open("text.txt",'w') #写入txt2 
txt2.write(count + '\n')
for d in hackers :
txt2.write(d + '\n')
txt2.close() 
