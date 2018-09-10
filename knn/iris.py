import numpy as np

def chinh_dau_vao(x) :
	tt = []
	for i in x :
		#x0,x1,x2,x3,x4 = float(i[0]),float(i[1]),float(i[2]),float(i[3]),i[4]
		t = [float(i[0]),float(i[1]),float(i[2]),float(i[3])]
		tt.append(t)
	return tt	

		


def khoang_cach_x_z(z,x):
	x2 = np.sum(x*x)
	z2 = np.sum(z*z)

	return x2+z2 - 2*x.dot(z)

try:
	f = open('data_iris.txt')
except:
	print 'file loi dmm'
	exit()


x = []
for line in f :
	x_t = line.split(',')
	x.append(x_t)
	
z = [6.9,3.1,5.4,2.1]
z = np.array(z)
kq = []
kqq,itt,minarr=1,1,100
for i in range(150)	:
	arr = np.array(chinh_dau_vao(x)[i]).astype(np.float32)
	tam = khoang_cach_x_z(z,arr)
	kq.append(tam)
	if tam < minarr :
		minarr = tam
		kpp= tam
		itt = i
kxx = raw_input('nhap k:')
kxx= int(kxx)		
print kxx
kq = np.array(kq)		
k1=np.argsort(kq)
for i in range(kxx):
	print(x[k1[i]][4])
	 

