from sklearn.ensemble import RandomForestRegressor
from IPython.display import display
from sklearn import metrics

import pandas as pd
import numpy as np

import math
PATH ="data/bulldozers/"

df = pd.read_csv(f'{PATH}Train.csv', low_memory=False, parse_dates=["saledate"])
df = df.