#!/usr/bin/env python
# coding: utf-8

# In[46]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt


# In[47]:


APMC = pd.read_csv("APMC.csv" , index_col='APMC')


# In[48]:


APMC.head(14)


# In[41]:


years = APMC.columns.str.strip('unit_price1')


# In[42]:


APMC.columns = years.astype(string)


# In[43]:


APMC.Year['Haryana'].plot()


# In[44]:


APMC.T.plot()
plt.ylabel('Unit_price1')


# In[45]:


APMC_Gujarat = APMC.loc['Gujarat']
APMC_Haryana = APMC.loc['Haryana']

plt.plot(years, APMC_Gujarat, 'b-', label='Gujarat')
plt.plot(years, APMC_Haryana, 'g-', label='Haryana')



plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('Unit Prices($)')


# In[ ]:




