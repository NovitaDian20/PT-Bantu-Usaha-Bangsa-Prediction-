import os 
import pandas as pd

path1='C:\Pelatihan\KLASA second stage selection'
os.listdir(path1)

data=pd.read_csv(os.path.join(path1, "Dataset"))
data
