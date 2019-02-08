import pandas as pd
import numpy as np


def ex_1():
    id = np.load('../data/id.npy')
    heights = np.load('../data/height.npy')
    return pd.DataFrame(data= {'id': id, 'heights': heights})


def ex_2():
    df = pd.read_csv('../data/nom.csv')
    df2 = df.join(ex_1().set_index('id'), on='id')
    df2.dropna(inplace=True)
    df2.to_csv('../output/data.csv')