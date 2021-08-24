#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Python Stuff
import datetime

# Model stuff
from sklearn                        import metrics, svm
from sklearn.linear_model           import LinearRegression
from sklearn.linear_model           import LogisticRegression
from sklearn.tree                   import DecisionTreeClassifier
from sklearn.tree                   import DecisionTreeRegressor
from sklearn.neighbors              import KNeighborsClassifier
from sklearn.discriminant_analysis  import LinearDiscriminantAnalysis
from sklearn.naive_bayes            import GaussianNB
from sklearn.svm                    import SVC


# In[26]:


def choose_model(): #hard choice...
    #return svm.SVR()                                 #doesnt work
    return LinearRegression()                        # 1342.07
    #return LogisticRegression()                      #doesn't work
    #return DecisionTreeClassifier()                  #1378.01
    #return KNeighborsClassifier()                    #no go
    #return LinearDiscriminantAnalysis()              #eh...
    #return GaussianNB ()                             #noop
    #return SVC()                                     #doesn't work
    #return DecisionTreeRegressor(random_state = 0)   #1255.48


# In[ ]:




