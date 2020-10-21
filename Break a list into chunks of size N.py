#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_list = ['a', 'b', 'c', 'd', 
           'e','f', 'g', 'h', 
               'i','j', 'k','l','m'] 
  
# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# How many elements each 
# list should have 
n = 5
  
x = list(divide_chunks(my_list, n)) 
print (x) 


# In[ ]:




