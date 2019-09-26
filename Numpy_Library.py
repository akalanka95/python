#!/usr/bin/env python
# coding: utf-8

# # NumPy Arrays
# 

# In[2]:


my_list = [1,2,3]
my_list


# In[5]:


import numpy as np

arr = np.array(my_list)
arr


# In[7]:


my_mat =[[1,2,3],[3,4,5]]
np.array(my_mat)


# In[12]:


np.arange(0,11)


# In[14]:


np.arange(0,11,2)


# In[16]:


np.zeros(4)


# In[19]:


np.zeros((2,3))


# In[22]:


np.ones((3,4))


# In[26]:


## evenly space 10 numbers
np.linspace(0,5,10)


# In[28]:


## Identity Matrics
np.eye(4)


# In[30]:


##within 0 and 1
np.random.rand(5)


# In[31]:


np.random.rand(5,3)


# In[33]:


np.random.randn(3)


# In[34]:


np.random.randint(1,100)


# In[35]:


np.random.randint(1,100,10)


# In[38]:


arr = np.arange(25)
arr


# In[40]:


ranarr = np.random.randint(0,50,10)
ranarr


# In[42]:


arr.reshape(5,5)


# In[46]:




# In[48]:


ranarr.max()


# In[49]:


ranarr.min()


# In[50]:


ranarr.argmax()


# In[52]:


arr.shape


# In[53]:


arr.dtype


# In[ ]:




