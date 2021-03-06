# -*- coding: utf-8 -*-
"""
Created on Mon Apr 8 17:37:57 2019

@author: Blake
"""

import pandas as pd
import numpy as np
data=pd.read_csv('golfstats1.csv')

X = data.drop('POINTS',1)   
y = data['POINTS']
# extract Titles from each column
names = list(X.columns.values)
import matplotlib.pyplot as plt

# Apply Standard Scaler to dataset
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X)
data_scaled = sc.fit_transform(X)

# Apply PCA
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(data_scaled)
explainedvariance = pca.explained_variance_ratio_
# PCA Projection to 2 dimensions
principalDf = pd.DataFrame(data = X,
                           columns =['PC1','PC2'])

finalDf = pd.concat([principalDf, data[['POINTS']]],axis = 1)

# Plot PCs
plt.grid()
pts = plt.scatter(X_pca[:,0], X_pca[:,1],c = y)
           
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(pts)

plt.title('2 Component PCA', fontsize=20)

#SVD(x) For testing linear dependency. if anything is close to zero, there is a linear dependency
# perform SVD and eliminate linearly dependent variables
u,s,vh = np.linalg.svd(X)

# Data looks good, should be able to run ANOVA now
from scipy.stats import f_oneway
anova = f_oneway(y,X_pca[:,0],X_pca[:,1])


data=pd.read_csv('golfstats1.csv')
from sklearn.preprocessing import StandardScaler
scaler_func = StandardScaler()

scaler_func.fit(data)
data_scaled = scaler_func.transform(data)

y = data_scaled[:,0]
X = data_scaled[:,1:]

from sklearn.linear_model import LinearRegression
# Perform multivariate regression
lin_reg = LinearRegression()
lin_reg.fit(X,y)
# Extract coefficient loadings
coefs = lin_reg.coef_
print(coefs)
# Find max coeff & index of that coef
max_c = np.max(coefs)
max_c_pos = np.argmax(coefs)
print(max_c)
print(max_c_pos)
# Convert coefs to list and concat
coef_str=list(coefs)
conc=np.c_[names,coef_str]
# print corresponding coefs 
print(conc)
r = lin_reg.score(X,y)
print(r)

