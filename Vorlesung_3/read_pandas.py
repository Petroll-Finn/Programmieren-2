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


def make_plot_EKG (df):
    fig = px.line(df, x=time(), y=[df['PowerOriginal'], df['HeartRate']], title='Leistung und Herzfrequenz über die Zeit', labels={'x': 'Zeit [s]', 'value': 'Leistung[w] / Heart Rate[Bpm]'})
    # fig.show()
    return fig


if __name__ == '__main__':
    print ("nochmal Hallo")
    df = load_activity()
    print_hallo()
    print (mittelwert(df))
    print (max_Leistung (df))
    make_plot_EKG(df)





