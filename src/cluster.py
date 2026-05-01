from sklearn.cluster import KMeans

def apply_kmeans(som, data, df):

    weights = som.get_weights().reshape(-1, data.shape[1])

    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
    labels = kmeans.fit_predict(weights)

    cluster_labels = []

    for x in data:
        w = som.winner(x)
        index = w[0]*10 + w[1]
        cluster_labels.append(labels[index])

    df["Cluster"] = cluster_labels

    return df