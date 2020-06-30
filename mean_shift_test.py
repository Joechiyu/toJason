#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
from sklearn.cluster import MeanShift


def main():
	x=np.load('./wnet/A2/plant005_emb.npy')


	# In[2]:


	test= np.reshape(x, (512*512,8))


	# In[3]:
	print("Hello world!")

	clustering= MeanShift().fit(test)
	clustering.labels_

	print(clustering.labels_)

	#f= open('/work/scratch/yuchi/mean_shift/result.txt')
	#f.write("test")
	#f.close()


if __name__ == "__main__":
	main()



# In[ ]:




