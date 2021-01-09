#!/usr/bin/env python
# coding: utf-8

# In[6]:



import numpy as np
import pandas as pd
df_2015=pd.read_csv(r'C:\Users\DELL\Downloads\2015-building-energy-benchmarking.csv')
df_2016=pd.read_csv(r'C:\Users\DELL\Downloads\2016-building-energy-benchmarking.csv')


# In[7]:


print(df_2015)


# In[8]:


print(df_2016)


# In[9]:


set(df_2015)-set(df_2016)


# In[11]:


set(df_2016)-set(df_2015)


# In[12]:


df_2015.isnull().sum().sort_values(ascending=False)


# In[13]:


df_2015.describe()


# In[15]:


df_2015.describe().transpose()


# In[16]:


df_2015["ENERGYSTARScore"].fillna( '68', inplace = True)


# In[17]:


df_2015.isnull().sum().sort_values(ascending=False)


# In[18]:


df_2015["City Council Districts"].fillna( '1', inplace = True)


# In[19]:


df_2015.isnull().sum().sort_values(ascending=False)


# In[ ]:




