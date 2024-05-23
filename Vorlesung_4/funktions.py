import pandas as pd
import plotly_express as px

def load_activity(path = "../data/activity.csv"):
    df = pd.read_csv(path)
    return df



def find_best_effort (df, time_window, frequenz = 1):
    df['RollingMean'] = df['PowerOriginal'].rolling(window = time_window).mean()
    # df_best_effort = df['RollingMean']
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # print (df_best_effort.head(200))

    if frequenz == 1 :
        max_value = df['RollingMean'].max()
        # print (max_value)
    
    # else: 
        
    return max_value



def return_df_for_plotting (df, window_lenghts = list(range(1, 1806))):
    df_BestEffort = pd.DataFrame(columns=['Duration [s]', 'Best Effort[W]'])

    for lenght, i in zip (window_lenghts, range(1, 1806)):
        df_BestEffort.loc[i] = [lenght, find_best_effort(df, lenght)]

    return df_BestEffort

# [1,5,15,30,45,60,90,120,240,300,360,420,480,540,600,720,840,960,1080,1200,1320,1440,1560,1680,1800]
# [1,5,15,30,45,60,90,120,240,300,360,420,480]


def make_plot (df):
    fig = px.line(return_df_for_plotting (df), x='Duration [s]', y='Best Effort[W]', title='Power Curve')
    fig.show()



if __name__ == '__main__':
    print ("hallo von funktions")


    df = load_activity()
    # print(df.head())
    # df['RollingMean'] = df['PowerOriginal'].rolling(window=3).max()
    # print(df.head())

    print (find_best_effort(df, 10))
    # print (return_df_for_plotting (df))

    make_plot (df)

    df2 = pd.DataFrame(columns=['Spalte1', 'Spalte2'])
    # new_row = {'Spalte1111': 3, 'Spalte2': 3 * 10}
    df2.loc[1] = [1, 1 * 10]
    # Neue Zeile zum DataFrame hinzufügen
    # df2 = df2._append(new_row, ignore_index=True)
    # print (df2)

