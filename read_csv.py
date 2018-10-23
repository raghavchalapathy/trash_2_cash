import pandas as pd
import numpy as np
def readcsv(fileName):
	df = pd.read_csv(fileName)
	return df
