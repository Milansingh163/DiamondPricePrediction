import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import Custum_exception
from src.components.data_ingestion import DataIngestion
import numpy as np

from src.utils import load_object
from src.utils import save_object
from src.utils import evaluate_model

from dataclasses import dataclass
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.tree import DecisionTreeRegressor

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('splitting target column from train and test array ')

            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            logging.info('Shapes of out put {},{},{},{}'.format(X_train.shape,y_train.shape,X_test.shape,y_test.shape))

            models={
            'LinearRegression':LinearRegression(),
            'Lasso':Lasso(),
            'Ridge':Ridge(),
            'Elasticnet':ElasticNet(),
            'DecisionTree':DecisionTreeRegressor()
                }
            model_report:dict = evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('='*30)
            logging.info('model reaport {}'.format(model_report))

            best_model_score = max(sorted(model_report.values()))
            best_model_name  = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
                ]
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')


            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
        except Exception as e:
            logging.info('model training failed')
            raise Custum_exception(e,sys)
