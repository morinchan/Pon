# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:46:31 2017

@author: rin
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.mixture import GaussianMixture

def Best_GaussianMixture(X_all):
    
    aic = []   
    min_aic = float('inf')
    n_components = range(1,10)
    covariance_tpye = ['spherical','tied','diag','full']
    
    for cv in covariance_tpye:
        for n in n_components:
            model_gm = GaussianMixture(n_components = n, covariance_type=cv)
            model_gm.fit(X_all)
            aic.append(model_gm.aic(X_all))
            if aic[-1] < min_aic:
                min_aic = aic[-1]
                Best_GaussianMixture = model_gm
    return Best_GaussianMixture
    

if __name__ == '__main__':
    X_train = pd.read_csv('F:/py/data_science_london/train.csv', 
                    header = None).as_matrix()
    #same as y = pd.read_csv()[0].as_matrix()
    y = pd.read_csv('F:/py/data_science_london/trainlabels.csv', 
                    header = None).as_matrix().ravel() 
    X_test = pd.read_csv('F:/py/data_science_london/test.csv', 
                      header = None).as_matrix()
    X_all = np.r_[X_train, X_test]                  
    
    model_gm = Best_GaussianMixture(X_all)
    model_gm.fit(X_all)
    
    X = model_gm.predict_proba(X_train)
    
    '''
    model_rf = RandomForestClassifier(n_estimators=1000, bootstrap=False, 
                                    random_state=None, verbose=1)
    param_grid = dict()
    model_gs = GridSearchCV(model_rf, param_grid=param_grid, 
                          verbose=3, cv=10).fit(X, y)
                          
    model_gs_best = model_gs.best_estimator_.fit(X, y)    
    print(model_gs.best_estimator_.score(X, y))
    scores = cross_val_score(model_gs_best, X, y, cv=10,scoring='accuracy')
    print(scores.mean(), scores.min())        
    #0.98,0.95 for randomforest
                          
    '''
    
    #SVM
    
    param_grid = dict()
    svm = SVC()
    model_svm = GridSearchCV(svm,param_grid=param_grid,
                             verbose=3,cv=5).fit(X,y)     
                             
    svm_score = cross_val_score(model_svm, X, y, cv=5,
                                scoring='accuracy')
    #print(svm_score.mean(), svm_score.min())                     
    #0.995 0.985
                                
    X_t = model_gm.predict_proba(X_test)
    y_pred = model_svm.best_estimator_.predict(X_t)    
        
    submit = []
    for i in range(9000):
        submit.append([i+1, y_pred[i]])
    submit = pd.DataFrame(submit)
    submit.to_csv('F:/py/data_science_london/submit.csv',
                  index=False, header=['Id','Solution'])
     
    
        
    
    
    


