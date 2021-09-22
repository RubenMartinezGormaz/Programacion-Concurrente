#!/usr/bin/env python
# coding: utf-8

# # SECOND PYTHON PROGRAM

# 1. Cuantos cores/cpu tiene su equipo

# In[2]:


import os


# In[3]:


os.cpu_count()


# 2. Cuantos cores / cpu's físicos tiene su equipo

# In[7]:


print("Mi equipo tiene " + str(os.cpu_count()) + " físicos")


# 3. Cuantos cores / cpu's lógicos tiene su equipo

# In[20]:


print("Mi pc tiene " + str(os.cpu_count() * 2 ) + " lógicos")


# 4. Cree una función con el objetivo de mantener su cpu activa al menos 10 seg (que no haga nada la función)

# In[24]:


os.getpid()


# In[22]:


def ten():
    while True:
        pass


# In[26]:


def ten():
    for i in range(1000):
        pass


# 5. Qué versión de Phyton tienes instalada ?

# In[28]:


import platform as lian


# In[29]:


lian.python_version()


# 6. El bus de su maq. es de 32 o 64?

# In[30]:


lian.architecture()


# 7. Cree una función que imprima del 1 al 10

# In[46]:


def to_ten():
    for i in range(10):
        print(i)


# 8. Ejecute concurrentemente 20 veces la función antes mencionada

# In[47]:


import threading as th


# In[48]:


th.Thread(target=to_ten).start()


# 9. Cuantos hilos estan activos

# In[45]:


th.active_count()


# In[ ]:




