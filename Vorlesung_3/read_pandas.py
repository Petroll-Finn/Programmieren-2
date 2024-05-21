import pandas as pd



## zuvor !pip install plotly
## ggf. auch !pip install nbformat
# import plotly.express as px



def load_activity(path="../data/activity.csv"):
    df = pd.read_csv(path)
    return df



print (load_activity())













# def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    # fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    # return fig




#df = read_my_csv()
#fig = make_plot(df)

#fig.show()


