# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 23:50:31 2019

@author: SaGaRueda
ITRA CALCULATION
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import exp

#data_path = 'dataset_3.csv'
#km,des,time, z = np.loadtxt('dataset_0.txt', unpack=True)
#data1 = pd.read_csv("gabi.txt") 
data2 = pd.read_csv("avg.txt") 

#v1 = np.array(data1["grade_adjusted_speed"])
#df = pd.DataFrame([data1] columns=['Name', 'Amount'])

df = pd.DataFrame([data2])# columns=['Name', 'Amount'])
v1 = df[0]
#Luego después se almacena todos los datos en un dataframe único.

plt.figure()
plt.plot(v1)#itra_data.distance,itra_data.Puntaje,'x')
"""
fig2, = plt.plot(time, z,'o')
fig3, = plt.plot(des, z,'*')

plt.xlabel('Variable')
plt.ylabel("Puntaje Itra")
plt.legend((fig1,fig2,fig3), ('Distancia [km]','Tiempo [min]','Desnivel [+m]'))   
plt.title("Puntaje ITRA")
plt.xlim((0,3000))
plt.ylim((500, 1000))
plt.grid()

"""
"""
f = open('dataset_0.txt')  # 'r' (read) is the default processing mode
itra = f.read()
f.close() 
print(itra)  
data = itra.split()
print(data)
"""