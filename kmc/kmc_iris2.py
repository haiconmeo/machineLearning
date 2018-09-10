import numpy as np
iris_x = []
def nhapfile(file):
	try :

		f =  open(file)
		for line in f:
			tam = line.split(',')
			iris_x.append(tam)
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
def dis(x,y):
	x2 = np.sum(x*x)
	y2 = np.sum(y*y)

	return x2+y2 - 2*x.dot(y)
def updateLabel(x,cen,li):

	for i in range((iris_x).shape[0]):
		k = []
		for j in range(3):
			k.append(dis(iris_x[i],cen[j]))
			manh = np.argsort(k)
			li[i]=manh[0]
	return li
def loadCentroid():
	return iris_x[np.random.choice(iris_x.shape[0],3,replace = False)]
def updateCentroid(cen,li) :
	
	cen2=np.zeros( (3,4) )
	jb0 = []
	jb1 = []
	jb2 = []
	for i in range(len(li)):
		if(li[i]==0):
			jb0.append(iris_x[i])
		if(li[i]==1):
			jb1.append(iris_x[i])
		if(li[i]==2) :
			jb2.append(iris_x[i])
	cen2[0] = np.mean(jb0,axis=0)
	cen2[1] = np.mean(jb1, axis=0)
	cen2[2] = np.mean(jb2, axis=0)
	# print cen2
	return cen2

def KMC(cen,li):
	i= 20
	while i!=0: 

		li = updateLabel(iris_x,cen,li)
		print cen
		cen = updateCentroid(cen,li)
		i-=1



nhapfile('data_iris.txt')
iris_x = biendoi(iris_x)
# print iris_x
# centroid =loadCentroid() #chose centroid
centroid =[]
centroid = loadCentroid()
# print loadCentroid() 
list = np.zeros(len(iris_x))
list=updateLabel(iris_x,centroid,list)
KMC(centroid,list)
# print updateCentroid(centroid,list)
# print centroid
