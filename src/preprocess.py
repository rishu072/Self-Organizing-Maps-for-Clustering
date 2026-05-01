import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess():

    # load dataset
    df = pd.read_csv("data/data.csv")

    # fill missing values
    df = df.fillna(df.mean(numeric_only=True))

    # drop unnecessary columns
    df = df.drop(columns=["CUST_ID","Channel","Region"], errors='ignore')

    # scaling
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(df)

    return df, data_scaled