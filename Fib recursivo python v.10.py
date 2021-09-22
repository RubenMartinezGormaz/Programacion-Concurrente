#!/usr/bin/env python
# coding: utf-8

# Rubén Martínez Gormaz, exp 22037408 

# # First prg.

# ## Cree un prg que calcule la sec de fib de 30, 50, 80

# ### La formula que he usado es :

# In[18]:


from IPython import display


# In[19]:


display.Image("fibonacci-sequence.png")


# In[20]:


def fib(n):
    if n<=1:
        return n
    else: 
        return (fib(n-1) + fib(n-2))
    


# In[23]:


fib(40)

