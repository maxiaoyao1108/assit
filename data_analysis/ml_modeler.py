from sklearn.linear_model import LinearRegression
import numpy as np


def ml_modeling(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

    