#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[60]:


get_ipython().system('pip install pandas')
import pandas as pd


# In[61]:


#M2 T01
#Exercici 1
#Cal crear una llista que agrupi els mesos de l'any en trimestres, és a dir, una llista amb quatre llistes.


# In[62]:


listaT1 = ["Enero", "Febrero", "Marzo"]
listaT2 = ["Abril", "Mayo", "Junio"]
listaT3 = ["Julio", "Agosto", "Septiembre"]
listaT4 = ["Octubre", "Noviembre", "Diciembre"]

lista_anualidad = [listaT1, listaT2, listaT3, listaT4]
print(lista_anualidad)


# In[63]:


#Exercici 2


# In[64]:


#Crea un codi que permeti accedir al segon mes del primer trimestre.


# In[65]:


posicion_trimestre=0
x=lista_anualidad[posicion_trimestre]
print(x[1])


# In[66]:


#Crea un codi que permeti accedir els mesos del primer trimestre.


# In[67]:


print(lista_anualidad[0])


# In[68]:


#Crea un codi que permeti accedir a setembre i octubre.


# In[ ]:




