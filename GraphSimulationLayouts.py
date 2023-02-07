#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist('Downloads/facebook_combined.txt')
nx.info(G)


# In[3]:


nx.number_of_edges(G)


# In[4]:


nx.number_of_nodes(G)


# In[5]:


nx.is_directed(G)


# In[6]:


G1=nx.read_pajek('Downloads/football.net')


# In[7]:


nx.info(G1)


# In[8]:


G2=nx.read_pajek('Downloads/karate.paj')
nx.info(G2)


# In[18]:


G3=nx.read_gml('Downloads/karate.gml',label='id')
nx.draw(G3)


# In[9]:


G1=nx.read_pajek('Downloads/football.net')      #Diplay Directed Graph


# In[10]:


nx.draw_circular(G1)


# In[11]:


nx.draw_spectral(G1)


# In[12]:


nx.draw_random(G1)


# In[13]:


nx.draw_kamada_kawai(G1)


# In[15]:


nx.draw_spring(G1)


# In[16]:


nx.draw_shell(G1)


# In[19]:


nx.degree(G3)    #Degree of each Node 
    


# In[20]:


degrees = [val for (node, val) in G3.degree()]


# In[21]:


list(set(degrees))     #Unique Degrees of Nodes


# In[22]:


def plot_deg_dist(G):
    all_degrees=[val for (node, val) in G3.degree()]
    unique_degrees=list(set(all_degrees))
    count_of_degrees=[]
    for i in unique_degrees:
        x= all_degrees.count(i)
        count_of_degrees.append(x)
    plt.plot(unique_degrees,count_of_degrees,'yo-')
    plt.xlabel('Degrees')
    plt.ylabel('Number of Nodes')
    plt.title('Degree Distribution of Karate Network')
    plt.show()
    


# In[35]:


plot_deg_dist(G3)   #Degree Distribution Ploting for karate data set 


# In[23]:


nx.density(G3)


# In[ ]:




