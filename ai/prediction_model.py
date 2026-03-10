import numpy as np
from sklearn.linear_model import LinearRegression

def simple_price_prediction(prices):

    X = np.arange(len(prices)).reshape(-1,1)
    y = np.array(prices)

    model = LinearRegression()
    model.fit(X,y)

    next_day = np.array([[len(prices)]])
    prediction = model.predict(next_day)

    return prediction[0]
