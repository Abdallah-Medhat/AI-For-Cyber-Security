#import Libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score,accuracy_score,classification_report
from catboost import CatBoostClassifier
from pathlib import Path
import pickle
from src.visualization import visualize
def train_model(path_data):
    #read data
    df_data=pd.read_csv(path_data)
    df_data_copy = df_data.copy()
    #count label
    visualize.count_label(df_data)
    #preprocessing data
    df_data=df_data.drop(['timestamp','longest_word','sld'], axis=1)
    #sample from data
    data_sample=df_data.sample(n=2000,random_state=0)
    #plot data in 2D after using tsne
    visualize.apply_tsne(data_sample)
    #plot data with label in 2D after using tsne
    visualize.apply__tsne(data_sample)
    x=df_data.iloc[:,0:-1]
    y=df_data.iloc[:,-1]
    #split data to training and testing
    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,random_state=0)
    #fitting and predicting CatBoostClassifier
    clf_c=CatBoostClassifier(iterations=1000,verbose=0,learning_rate=0.01,random_state=0)
    clf_c.fit(x_train, y_train)
    y_pred_c=clf_c.predict(x_test)
    print("f1 score for catBoost",f1_score(y_test, y_pred_c))
    print("accuracy for catBoost",accuracy_score(y_test, y_pred_c))
    print(classification_report(y_test, y_pred_c))
    visualize.conf_matrix(clf_c,x_test,y_test)
    #save model
    project__dir=Path(__file__).resolve().parents[1]
    pickle.dump(clf_c, open(str(project__dir)+'\\catboost_.sav','wb'))
    

