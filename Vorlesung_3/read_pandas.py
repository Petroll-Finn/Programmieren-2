import pandas as pd
import plotly.express as px
import numpy as np

def print_hallo ():
    print ("hallo von read pandas")



def load_activity(path="data/activity.csv"):
    df = pd.read_csv(path)
    return df


def mittelwert (df):
    mittelwert_Leistung = df['PowerOriginal'].mean()
    #print(mittelwert_Leistung)

    return mittelwert_Leistung


def max_Leistung (df):
    max_Leistung = df['PowerOriginal'].max()
    #print(max_Leistung)
    return max_Leistung

def time():
    points = 1804
    total_seconds = 30 * 60 + 5
    time_points = np.linspace(0, total_seconds, points)
    return (time_points)

def max_Herzfrequenz (df):
    max_Herzfrequenz = df["HeartRate"].max()
    # print(max_Herzfrequenz)
    return max_Herzfrequenz




def make_plot_EKG (df):
    
    
    fig = px.line(df, x=time(), y=[df['PowerOriginal'], df['HeartRate']], title='Leistung und Herzfrequenz über die Zeit', labels={'x': 'Zeit [s]', 'value': 'Leistung[w] / Heart Rate[Bpm]'})
    
    fig.add_shape(
    type="rect",
    x0=0, x1=1805,  # Zeit in Sekunden
    y0=0, y1=1,  # Y-Achsenbereich, um den gesamten Diagramm zu überdecken
    xref='x', yref='paper',
    fillcolor="Brown",
    opacity=1,
    layer="below",
    line_width=0,
    )

    fig.add_shape(
    type="rect",
    x0=0, x1=1805,  # Zeit in Sekunden
    y0=0.1, y1=0.3,  # Y-Achsenbereich, um den gesamten Diagramm zu überdecken
    xref='x', yref='paper',
    fillcolor="aqua",
    opacity=1,
    layer="below",
    line_width=0,
    )
    
    fig.show()
    return fig





if __name__ == '__main__':
    
    df = load_activity()
    print (max_Herzfrequenz(df))

    print (mittelwert(df))
    print (max_Leistung (df))
    make_plot_EKG(df)





