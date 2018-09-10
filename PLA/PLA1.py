import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(2)

means = [[-1, 0], [1, 0]]
cov = [[.3, .2], [.2, .3]]
N = 10
X0 = np.random.multivariate_normal(means[0], cov, N).T
X1 = np.random.multivariate_normal(means[1], cov, N).T
# print X0
# print X1

X = np.concatenate((X0, X1), axis = 0)
y = np.concatenate((np.ones((1, N)), -1*np.ones((1, N))))
# Xbar 
# Xbar = np.concatenate((np.ones((1, 2*N)), X), axis = 1)
print y
# # xong phan khoi tao du lieu 

# #---------------------------------------------------------
# def perdict(w,x):
# 	return np.sign(x.dot(w))
# def pla(x,y,w_iniy):
# 	w = w_iniy
# 	while True:
# 		pred = perdict(w,x)
# 		mis_idxs = np.where(np.equal(pred,y)==False)[0]
# 		num_mis = mis_idis.share[0]
# 		if num_mis == 0:
# 			return w
# 		random_id = np.random.choice(mis_idis,1)[0]
# 		w = w +y[random_id]*x[random_id]
# w_init = np.random.randn(Xbar.shape[1])
# w = pla(Xbar,y,w_init)
# print w			

