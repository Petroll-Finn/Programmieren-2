import pandas as pd
import plotly.express as px
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go

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

def calc_Zones (max_HR):
    list_Zones = [0.5*max_HR, 0.6*max_HR, 0.7*max_HR, 0.8*max_HR, 0.9*max_HR, 1*max_HR]
    print (list_Zones)

    return list_Zones




def make_plot_EKG (df, max_HR):
    
    liste_mit_zonen = calc_Zones (max_HR)

    fig = go.Figure()

    # Erstellen der Subplots mit zwei y-Achsen
    fig = make_subplots(specs=[[{"secondary_y": True}]])


    fig.add_trace(go.Scatter(x=time(), y= df['HeartRate'], name="EKG-Daten", line=dict(color='red')), secondary_y=False,)
    
    fig.add_trace(go.Scatter(x=time(), y= df['PowerOriginal'], name="Power-Daten", line=dict(color='blue')), secondary_y=True,)
    
    
    
    fig.update_layout(
    title_text="EKG und Power ",
    xaxis_title="time [s]",
    yaxis_title="Heart Rate [BPM]",
    yaxis2_title="Power [w]"
    )

    # fig = px.line(df, x=time(), y=[df['PowerOriginal'], df['HeartRate']], title='Leistung und Herzfrequenz über die Zeit', labels={'x': 'Zeit [s]', 'value': 'Leistung[w] / Heart Rate[Bpm]'})
    
    fig.add_shape(
    type="rect",
    x0=0, x1=1805,  # Zeit in Sekunden
    y0=liste_mit_zonen[0], y1=liste_mit_zonen[1],  # Y-Achsenbereich, um den gesamten Diagramm zu überdecken
    xref='x', yref='y',
    fillcolor="grey",
    opacity=1,
    layer="below",
    line_width=1,
    showlegend=True,
    name='Zone 1 (50-60 %)'
    )

    fig.add_shape(
    type="rect",
    x0=0, x1=1805,  # Zeit in Sekunden
    y0=liste_mit_zonen[1], y1=liste_mit_zonen[2],  # Y-Achsenbereich, um den gesamten Diagramm zu überdecken
    xref='x', yref='y',
    fillcolor="lightgreen",
    opacity=1,
    layer="below",
    line_width=1,
    showlegend=True,
    name='Zone 2 (60-70 %)'
    )

    fig.add_shape(
    type="rect",
    x0=0, x1=1805,  # Zeit in Sekunden
    y0=liste_mit_zonen[2], y1=liste_mit_zonen[3],  # Y-Achsenbereich, um den gesamten Diagramm zu überdecken
    xref='x', yref='y',
    fillcolor="green",
    opacity=0.5,
    layer="below",
    line_width=1,
    showlegend=True,
    name='Zone 3 (70-80 %)'
    )

    fig.add_shape(
    type="rect",
    x0=0, x1=1805,  # Zeit in Sekunden
    y0=liste_mit_zonen[3], y1=liste_mit_zonen[4],  # Y-Achsenbereich, um den gesamten Diagramm zu überdecken
    xref='x', yref='y',
    fillcolor="yellow",
    opacity=0.5,
    layer="below",
    line_width=1,
    showlegend=True,
    name='Zone 4 (80-90 %)'
    )

    fig.add_shape(
    type="rect",
    x0=0, x1=1805,  # Zeit in Sekunden
    y0=liste_mit_zonen[4], y1=liste_mit_zonen[5],  # Y-Achsenbereich, um den gesamten Diagramm zu überdecken
    xref='x', yref='y',
    fillcolor="red",
    opacity=0.3,
    layer="below",
    line_width=1,
    showlegend=True,
    name='Zone 5 (90-100 %)'
    )

    
    # fig.show()
    return fig





if __name__ == '__main__':
    
    df = load_activity()
    print (max_Herzfrequenz(df))

    calc_Zones(100)
    print (mittelwert(df))
    print (max_Leistung (df))
    make_plot_EKG(df, 210)





