import numpy as np
def length(v):
	res=0
	for i in range(len(v)):
		res+=(v[i])**2
	res=res**0.5
	return res
def dot_product(v1,v2):
	if len(v1)!=len(v2):
		return
	res=0
	for i in range(len(v1)):
		res+=v1[i]*v2[i]
	return res
def cosine_similarity(v1, v2):
	res=dot_product(v1,v2)/(length(v1)*length(v2))
	return res
	