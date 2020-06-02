#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools


# In[16]:


result=["".join(i) for i in itertools.permutations("add")]


# In[17]:


result


# In[18]:


def palindrome_check(words):
    for i in words:
        if i[0::]==i[::-1]:
            print(i,"-->>it's a palindrome")
        else:
            print(i,"-->>it's not a palindrome")


# In[23]:


palindrome_check(result)


# In[ ]:




