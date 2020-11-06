"""Să se calculeze sumele: 	s1=1+2+3+…+n
			s2=1*2+2*3+3*4+…+(n-1)*n
			s3=1+1*2+1*2*3+…+1*2*3*…*n
			s4=12+22+32+…+n2
			s5=1/2+2/3+3/4+…+n/(n+1)
			s6=1+2+22+23+24+…+2n"""
n=int(input("dati un numar:"))
s1=0
for i in range(1,n+1):
    s1+=i
print("s1=",s1)

n=int(input("dati un numar:"))
s2=0
for i in range(1,n+1):
    s2+=(i-1)*i
print("s2=",s2)

n=int(input("dati un numar:"))
s3=1
pr=1
for i in range(2,n+1):
	pr*=i
	s3+=pr
print("s3=",s3)

n=int(input("dati un numar:"))
s4=0
for i in range(1,n+1):
	s4+=(10*i+2)
print("s4=",s4)

n=int(input("dati un numar:"))
s5=0
for i in range(1,n+1):
	s5+=n/(n+1)
print("s5=",s5)

n=int(input("dati un numar:"))
s6=3
for i in range(2,n+1):
	m=str(i)
	s6+=int(str('2'+m))
print("s6=",s6)