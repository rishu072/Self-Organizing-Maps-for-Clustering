import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src.preprocess import load_and_preprocess
from src.som_model import train_som
from src.visualize import plot_umatrix, plot_heatmap
from src.cluster import apply_kmeans

df = pd.read_csv("data/data.csv")

print("Data Loaded Successfully!")
print(df.head())
print("Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))
df = df.drop(columns=["CUST_ID","Channel","Region"], errors='ignore')
print("\nAfter Cleaning Shape:", df.shape)

scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(df)
print("\nScaled Data Shape:", data_scaled.shape)

# STEP 1: load + preprocess
df, data_scaled = load_and_preprocess()

# STEP 2: SOM train
som = train_som(data_scaled)

# test
print("Sample BMU:", som.winner(data_scaled[0]))

# visualize
plot_heatmap(df)

# SOM visualization
plot_umatrix(som)

# clustering
df = apply_kmeans(som, data_scaled, df)

print("\nCluster Analysis:\n")
print(df.groupby("Cluster").mean())