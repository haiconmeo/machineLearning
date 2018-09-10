import numpy as np
x = []
def nhapfile(file):
	try :

		f =  open(file)
		for line in f:
			tam = line.split(',')
			x.append(tam)
	except :
		print 'loi roi'
		exit() 
			
	
	return 1	
def biendoi(x):
	tt = []
	for tam in x:
		k = [float(tam[0]),float(tam[1]),float(tam[2]),float(tam[3])]
		tt.append(k)
	tt = np.array(tt)	
	return tt
def khoang_cach(x,y):
	x2 = np.sum(x*x)
	y2 = np.sum(y*y)
	return x2+y2-2*x.dot(y)

def init_centroids(x,k):
	return biendoi(x)[np.random.choice(biendoi(x).shape[0],3)]
def gan_lable(x,cen,k):
	kq= []
	for i in range(x.shape[0]):
		att=[]
		for j in range(k):
			
			x1=khoang_cach(x[i],cen[j])
			att.append(x1)
		kk=np.argsort(att)	
		#print kk[0]
		#x[i][4]=kk[0]
		#print x
	return 1	
def stoppro(cen,newcen):
	if (cen-newcen)(cen-newcen) <=1e-3:
		return False
	return 	True

def update_cen(x,lable,k):
	cen = np.zeros((k,x.shape[1]))
	for i in range(k):
		xk =x[] 
		cen[k,:] = np.mean(xk, axis= 0)
	return cen	
def kmean(x,k):
	cen = init_centroids(x,3)
	#print cen
	# while stoppro(cen,newcen)::
	# 	pass
	gan_lable(x,cen,3)
	cen = update_cen(x)
	#print x
	return 1;	
		
nhapfile('data_iris.txt')
x= biendoi(x)
#print biendoi(x)
#print init_centroids(x,5)
#print x[np.random.choice(biendoi(x).shape[0],3)]
#print biendoi(x)[np.random.choice(biendoi(x).shape[0],3)]
#print type(biendoi(x))
#print init_centroids(x,3)
kmean(x,3)



