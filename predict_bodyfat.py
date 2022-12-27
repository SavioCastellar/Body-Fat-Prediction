import os
import tarfile
from six.moves import urllib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_val_score, cross_val_predict

# Getting data
bodyfat = pd.read_csv("bodyfat.csv")
df = pd.DataFrame(bodyfat)