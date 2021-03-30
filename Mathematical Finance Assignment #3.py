#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


y1= np.array([[7/10,2/10,1/10,0],[1/10,5/10,2/10,2/10],[1/10,3/10,3/10,3/10],[0,0,0,1]])
y2=np.matmul(y1,y1)
y3=np.matmul(y2,y1)
print(y3)


# In[9]:


import scipy.linalg

scipy.linalg.fractional_matrix_power(y1,1/6)


# In[10]:


scipy.linalg.fractional_matrix_power(y1,100)


# In[ ]:




