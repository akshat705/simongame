import pandas as pd
import numpy as np


def is_sorted(a):
    for i in range(len(a)-1):
        if int(a[i+1][0]) < int(a[i][0]):
            return False
    return True

folderName="2022-03-15/"
fileBaseName="VBASS_AR_LEVEL3_03152022_"
for i in range(1, 55):
    fileName = fileBaseName+str(i)+".csv"
    df = pd.read_csv(folderName+fileName,
                     usecols=['BinRangeMinNum', 'BinRangeMaxNum'])
    vals = df.values
    # print(vals)
    print(fileName)
    print(is_sorted(vals), len(vals))
