import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.metrics import plot_confusion_matrix
#plot count label in data
def count_label(data):
    x_1 = np.arange(2)
    plt.bar(x_1,data['Label'].value_counts(),color='g')
    plt.xticks(x_1,[0,1])
    plt.xlabel("label")
    plt.ylabel("distribution")
    plt.title('data distribution')
    plt.legend(["label"],bbox_to_anchor =(0.75, 1.2))
    plt.show()
#apply tsne
def apply_tsne(data_sample):
    data_tsne=TSNE(n_components=2,random_state=0)
    data__tsne = data_tsne.fit_transform(data_sample)
    plt.plot(data__tsne)
#apply tsne with show label
def apply__tsne(data_sample):
    data_tsne=TSNE(n_components=2, random_state=0).fit_transform(data_sample.iloc[:,0:-1])
    train_ts=pd.DataFrame(data_sample.iloc[:,-1])
    train_ts['tsne-2d-one'] = data_tsne[:,0]
    train_ts['tsne-2d-two'] = data_tsne[:,1]
    plt.figure(figsize=(16,10))
    sns.scatterplot(
        x="tsne-2d-one", y="tsne-2d-two",
        hue="Label",
        palette=sns.color_palette("hls", 2),
        data=train_ts,
        legend="full",
        alpha=0.3)
#plot confusuin_matrix of catBoost model
def conf_matrix(model,x_test,y_test):
    plot_confusion_matrix(model, x_test, y_test)  

