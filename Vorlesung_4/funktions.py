import pandas as pd
import numpy as np


def load_data():

    # Use numpy.genfromtxt to read the CSV data from the file into a NumPy array
    data_array = np.genfromtxt("../data/activity.csv", delimiter=',', dtype=None, names=True)

    # Transpose the array to have each column in a separate NumPy array
    column_names = data_array.dtype.names
    column_arrays = {column: data_array[column] for column in column_names}


    return column_arrays


def load_activity(path="../data/activity.csv"):
    df = pd.read_csv(path)
    return df


if __name__ == '__main__':

    # print (load_data())
    # print (read_my_csv())

    # array = load_data()

    df = load_activity()
    print(df.head())

    power_original = df['PowerOriginal']
    # print(power_original)