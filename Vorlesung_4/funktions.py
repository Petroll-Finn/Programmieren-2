import pandas as pd

def load_activity(path="../data/activity.csv"):
    df = pd.read_csv(path)
    return df


def find_best_effort (df, time_window, frequenz = 1):
    df['RollingMean'] = df['PowerOriginal'].rolling(window = time_window).max()

    df_best_effort = df['RollingMean']
    # df_best_effort ["Größe Time Window"] = 
    max_value = df['RollingMean'].max()
    print (max_value)

    return df_best_effort



if __name__ == '__main__':

    df = load_activity()
    # print(df.head())

    df['RollingMean'] = df['PowerOriginal'].rolling(window=3).max()
    # print(df.head())

    print (find_best_effort(df, 2))


