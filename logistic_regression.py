import math

class LogisticRegression:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = []

    def sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def fit(self, X, y):
        self.weights = [0] * len(X[0])

        for _ in range(self.epochs):
            for i in range(len(X)):
                z = sum(self.weights[j] * X[i][j] for j in range(len(X[0])))
                pred = self.sigmoid(z)
                error = y[i] - pred
                for j in range(len(self.weights)):
                    self.weights[j] += self.lr * error * X[i][j]

    def predict(self, X):
        preds = []
        for x in X:
            z = sum(self.weights[j] * x[j] for j in range(len(x)))
            preds.append(1 if self.sigmoid(z) >= 0.5 else 0)
        return preds
