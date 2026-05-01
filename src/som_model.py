from minisom import MiniSom

def train_som(data):

    som = MiniSom(x=10, y=10, input_len=data.shape[1],
                  sigma=1.0, learning_rate=0.5)

    # initialize weights
    som.random_weights_init(data)

    print("\nTraining SOM...")
    som.train_random(data, 1000)
    print("Training Complete!")

    return som