import pandas as pd
import numpy as np
# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
# import plotly.express as px

def load_data():

    # Specify the file path
    # file_path = 'activity.csv'

    # Use numpy.genfromtxt to read the CSV data from the file into a NumPy array
    data_array = np.genfromtxt("../data/activity.csv", delimiter=',', dtype=None, names=True)

    # Transpose the array to have each column in a separate NumPy array
    column_names = data_array.dtype.names
    column_arrays = {column: data_array[column] for column in column_names}

    # Print each column
    #for column, array in column_arrays.items():
    #    print(f"{column}: {array}")

    return column_arrays

print (load_data())

def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df= pd.read_csv("../data/activity.csv", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Duration"] 
    # ,"Distance","OriginalPace","HeartRate","Cadence","PowerOriginal","CalculatedPace","CalculatedStrideLength","CalculatedAerobicEfficiencyPace","CalculatedAerobicEfficiencyPower","CalculatedEfficiencyIndex"]
    
    # Gibt den geladen Dataframe zurück
    return df

# print (read_my_csv())

array = load_data()

df = pd.DataFrame(array)
# print (df)

power_original = df['PowerOriginal']
print(power_original)









def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig




#df = read_my_csv()
#fig = make_plot(df)

#fig.show()


