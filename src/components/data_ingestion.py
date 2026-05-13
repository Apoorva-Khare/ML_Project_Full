import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from  dataclasses import dataclass

@dataclass   #data class decorator helpful for initialising data type
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")   #output will be saved in artifacts folder in train.csv
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"raw.csv")