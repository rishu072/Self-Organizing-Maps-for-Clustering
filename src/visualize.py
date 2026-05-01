import matplotlib.pyplot as plt
import seaborn as sns
from pylab import bone, pcolor, colorbar, show

# 🔹 U-Matrix
def plot_umatrix(som):
    bone()
    pcolor(som.distance_map().T)
    colorbar()
    plt.title("U-Matrix")
    show()

# 🔹 Heatmap
def plot_heatmap(df):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()