#!/usr/bin/env python
# coding: utf-8

# ## Question A)

# In[83]:


#On importe les bibliothèques nécessaires
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import random as rd
import seaborn as sns

n = [10, 100, 1000] #liste pour les différents nombre de sauts

for n in n: 
    #La simulation pour n sauts
    x = list() #Liste des 50 positions finales
    m = 50 #Nombre de fois que l'on fait tourner la simulation
    delta_x = list() #Une liste cotenant les n mouvements pour une simulation
    
    for i in range(m): #i va de 0 à 49
        possibilites = [-1, 1] #Les possibilités présentes pour la particules
        probabilites = [0.5, 0.5] #Les probabilités de chacune des possibilités
        delta_x = np.random.choice(possibilites, n, p=probabilites) #On réitère le choix n fois
        x.append(sum(delta_x)) 

    #On calcul la moyenne des 50 simulations pour n sauts
    moyenne = 1/m * sum(x)

    #Calcul de l'écart- type
    x = np.array(x) #On transforme la liste en un object mieux manipulable mathématiquement
    ecart_type = (sum((x - moyenne)**2 * 1/(m - 1)) )**(1/2)
    
    #Théoriquement les valeurs devraient se rappocher de 
    p = 0.5
    E = 0
    sigma = (2 * n * p *(1 - p) / m) ** (1/2)
    
    print('Nombre de sauts', '\t', 'Moyenne', '\t','Moyenne théorique','\t', 'Écart- type', '\t',  'Écart- type théorique')
    print("---------------", '\t', "--------", '\t', "-----------------", '\t', "-----------", '\t', "---------------------")
    print('{:.0f}'.format(n), '\t\t\t', '{:.4f}'.format(moyenne), '\t', '{:.4f}'.format(E), '\t\t', '{:.4f}'.format(ecart_type), '\t', '{:.4f}'.format(sigma))
    
    #On trace l'histogramme
    sns.set() #Une meilleur allure pour les histogrmmes
    _ = plt.hist(x, bins = 15)
    _ = plt.xlabel('Position finale')
    _ = plt.ylabel('Nombre de particules')
    _ = plt.title('Histogramme des valeurs de X')
    plt.show()



# ## Question B)

# In[63]:


print('Nombre de sauts', '\t', 'Moyenne', '\t', 'Écart- type', '\t', 'Écart- type / n^(1/2)')
print("---------------", '\t', "--------", '\t', "-----------", '\t', "--------------------")

n = [10, 100, 1000] #liste pour les différents nombre de sauts

for n in n:
    #La simulation pour n sauts
    x = list() #Une liste des m positions finales
    m = 50 #Nombre de fois que l'on fait tourner la simulation
    for i in range(m):
        delta_x = list() #Les n sauts de la particule pour la simulation i
        for i in range(n): #i va de 0 à 49
            delta_x.append(rd.uniform(-1, 1))
        x.append(sum(delta_x))

    #On calcul la moyenne des m simulations pour n sauts
    moyenne = 1/m * sum(x)

    #Calcul de l'écart- type
    x = np.array(x) #On transforme la liste en un object mieux manipulable mathématiquement
    ecart_type = (sum((x - moyenne)**2 * 1/(m - 1)) )**(1/2)

    print('{:.0f}'.format(n), '\t\t\t', '{:.4f}'.format(moyenne), '\t', '{:.4f}'.format(ecart_type), '\t', '{:.4f}'.format(ecart_type / n**(1/2)))


# ## Question C)

# In[79]:


print('Nombre de sauts', '\t', 'Moyenne', '\t', 'Écart- type', '\t', 'Écart- type / n**(1/2)')
print("---------------", '\t', "--------", '\t', "-----------", '\t', "--------------------")
n = [10, 100, 1000] #Liste pour les différents nombres de sauts

for n in n:
    #La simulation pour n sauts
    R = list() #Les des m positions finals 
    m = 50 #Nombre de fois que l'on fait tourner la simulation
    for i in range(m): #Boucle pour les m simulations
        #Les n sauts de la particule pour la simulation i
        delta_x = list() 
        delta_y = list() 
        delta_z = list() 
        for i in range(n): #Boucle pour les n sauts
            delta_x.append(rd.uniform(-1, 1))
            delta_y.append(rd.uniform(-1, 1))
            delta_z.append(rd.uniform(-1, 1))
        
        #Position finale de la particule dans les trois directions
        x = sum(delta_x) 
        y = sum(delta_y)
        z = sum(delta_z)
        R.append((x**2 + y**2 + z**2)**(1/2))
        
    #On calcul la moyenne de la simulation pour n sauts
    moyenne = 1/m * sum(R)

    #Calcul de l'écart- type
    R = np.array(R) #On transforme la liste en un object mieux manipulable mathématiquement
    ecart_type = (sum((R - moyenne)**2 * 1/(m - 1)) )**(1/2)    
        
    print('{:.0f}'.format(n), '\t\t\t', '{:.4f}'.format(moyenne), '\t','{:.4f}'.format(ecart_type),'\t', '{:.4f}'.format(ecart_type / n ** (1/2)))


# ## Question D)

# In[ ]:


import random as rd
# On crée une classe atome
class atome:
    """Une classe qui représente un atome"""
    
    r = []
    for i in range (3):
        r.append(rd.randrange(0, 100))
    v = []
    for i in range (3):
        v.append(rd.randrange(0, 100))
        
    def __init__(self):
        """Le constructeur de la classe"""
        #On crée un vecteur pour la position aléatoire
        r = []
        for i in range (3):
            r.append(rd.randrange(0, 100))
            
        #On crée un vecteur pour la position aléatoire
        v = []
        for i in range (3):
            v.append(rd.randrange(0, 100))
            
        self.position = r
        self.vitesse = v


# In[ ]:


#Générer 10 atomes aléatoirement et les mettre dans un dictionnaire
conteneur_atomes = dict()
for i in range(1, 11):
    conteneur_atomes["Atome_" + str(i)] = atome()

