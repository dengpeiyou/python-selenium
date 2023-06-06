f=open(r"e:\aa\bbb.txt",'r')
s1=f.read()
print(s1[:10])
print(s1[10:])
s2=s1[:10]+ "中国"+s1[10:]
f.close()

f=open(r"e:\aa\bbb.txt",'w')
f.write(s2)
f.close()
