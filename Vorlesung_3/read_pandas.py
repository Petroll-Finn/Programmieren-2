import pandas as pd
import plotly.express as px
import numpy as np


## zuvor !pip install plotly
## ggf. auch !pip install nbformat
# import plotly.express as px



def load_activity(path="../data/activity.csv"):
    df = pd.read_csv(path)
    return df



#print (load_activity())

df1 = load_activity()

alle_Power_Werte = df1['PowerOriginal']

mittelwert_Leistung = alle_Power_Werte.mean()
#print(mittelwert_Leistung)

max_Leistung = alle_Power_Werte.max()
#print(max_Leistung)

def time():
    point = 1804
    total_seconds = 30 * 60 + 5
    time_points = np.linspace(0, total_seconds, point)
    return (time_points)

print(time())

fig = px.line(df1, x=time(), y=[df1['PowerOriginal'], df1['HeartRate']], title='Leistung und Herzfrequenz über die Zeit')

fig.show()
# def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    # fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    # return fig




#df = read_my_csv()
#fig = make_plot(df)

#fig.show()


