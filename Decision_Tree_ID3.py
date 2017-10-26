# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def createDataset(filepath):
        
    data = pd.read_csv(filepath, encoding='gbk', sep='    ')
    labels = data.columns[:-1]
    
    return data, labels


def cal_entropy(data):
    
    labelcounts = data[u'好瓜'].value_counts()
    numEntries = len(data)
    numlabel = len(labelcounts)    
    ent = 0.0    
    
    for i in range(numlabel):
        ent -= labelcounts[i]/numEntries * np.log2(labelcounts[i]/numEntries)
        
    return ent

def split_data(data, axis, value):  
    
    labels = data.columns
    data = data.values
    # Have no idea how to realize this step in DataFrame tpye
    row_index = data[:,axis] == value
    subData = np.array(data[row_index,:])
    subData = pd.DataFrame(subData)
    subData.columns = labels
    
    return subData
  
def choose_BestFeature(data, labels):
    
    baseEnt = cal_entropy(data)
    num_features = len(labels)
    bestInfoGain = 0.0
    bestFeature = -1    
    
    for i in range(num_features):
        
        values = pd.unique(data[labels[i]])  # values in each feature
        featEnt = 0
        
        for value in values:
            subData = split_data(data, i, value)
            prob = len(subData) / float(len(data))
            featEnt += prob * cal_entropy(subData) 
        infoGain = baseEnt - featEnt
    # the difference between ID3 and C4.5 is that ID3 calculate infoGain while C4.5 calculate infoGateRatio      
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature
    
def get_mostlabel(labellist):
    
    labeldict = {}
    for i in labellist:
        labeldict[i] = label_dict.get(i,0) + 1
    sorted_label = sorted(labeldict.items(), key=lambda item:item[1])

    return sorted_label[0][0]


def createTree(data, labels):
    
    label_list = data.iloc[:,-1]
    if len(label_list.value_counts()) == 1:
        return label_list.values[0]
    if all([len(data[i].value_counts()) == 1 for i in labels]):
        return get_mostlabel(label_list)
    
    bestFeat = choose_BestFeature(data, labels)
    bestFeatLabel = labels[bestFeat]
    Tree = {bestFeatLabel:{}}
    
    labels = labels.drop(labels[bestFeat])
    
    values = pd.unique(data[bestFeatLabel])
    for value in values:
        subLabels = labels[:]
        Tree[bestFeatLabel][value] = createTree(split_data(data,bestFeat,value),subLabels)
    
    return Tree

if __name__ == '__main__':
    
    filepath = 'F:\\Mymaterial\\dataset\\Decision_Tree.txt'
    data, labels = createDataset(filepath)
    tree = createTree(data, labels)
    # tree is not right, something wrong in the final loop?


