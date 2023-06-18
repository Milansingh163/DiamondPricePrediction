import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import Custum_exception

from src.components.data_ingestion import DataIngestion
from src.components.data_tranformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__=='__main__':
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    print('Train data path : ',train_data_path)
    print('Test data path : ',test_data_path)


    #  data transformation 
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_tranformation(train_data_path,test_data_path)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr,test_arr)
