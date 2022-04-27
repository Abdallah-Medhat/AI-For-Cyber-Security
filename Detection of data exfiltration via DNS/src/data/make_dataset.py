# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from kafka import KafkaConsumer
from src.features import build_features
from src.models import predict_model
from src.models import train_model
import pandas as pd
# @click.command()
# @click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
def make_dataset(x):
    df=pd.DataFrame(columns=["domain","FQDN_count","subdomain_length","upper","lower","numeric","entropy","special","labels","labels_max","labels_average","longest_word","sld","len","subdomain","label_pred","confidence_score"])
    df["domain"]=[x]
    df["FQDN_count"]=[build_features.FQDN_count(x)]
    df["subdomain_length"]=[build_features.subdomain_length(x)]
    df["upper"]=[build_features.upper(x)]
    df["lower"]=[build_features.lower(x)]
    df["numeric"]=[build_features.numeric(x)]
    df["entropy"]=[build_features.entropy(x)]
    df["special"]=[build_features.special(x)]
    df["labels"]=[build_features.labels(x)]
    df["labels_max"]=[build_features.labels_max(x)]
    df["labels_average"]=[build_features.labels_average(x)]
    df["longest_word"]=[build_features.longest_word(x)]
    df["sld"]=[build_features.sld(x)]
    df["len"]=[build_features.len_domaind_subdomain(x)]
    df["subdomain"]=[build_features.subdomain(x)]
    return df
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    #train model
    train_model.train_model(input_filepath)
    #load model
    project_dirr=Path(__file__).resolve().parents[1]
    loaded_model=pickle.load(open(str(project_dirr)+'\\catboost_.sav','rb'))
    #consumer and predict model record by record
    consumer = KafkaConsumer(
    'ml-raw-dns',
    bootstrap_servers = ['localhost:9092'],
    auto_offset_reset = 'earliest',
    enable_auto_commit = False,
)   
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    list_data=[]
    j=0
    for i in consumer:
        data=make_dataset(i.value.decode('utf-8'))
        data_=data.drop(['longest_word','sld'], axis=1)
        x=data_.iloc[:,1:-2]
        data["label_pred"],data["confidence_score"]=predict_model.predict_model(x,loaded_model)
        list_data.append(data)
        j=j+1
        if j==100000:
            break
    #save all data in dataframe
    all_data=pd.concat(list_data)
    #save dataframe in csv file
    #all_data.to_csv("D:/cs/Abdallah_medhat_results.csv",index=False)
    all_data.to_csv(output_filepath,index=False)


if __name__ == '__main__':
    # i comment in the next lines becaues of i do not need this lines
    #log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    #logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    #project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    project_dir = Path(__file__).resolve().parents[2]
    main(str(project_dir)+ "\\data\\raw\\training_dataset.csv",str(project_dir)+ "\\data\\processed\\Abdallah_medhat_results.csv")
