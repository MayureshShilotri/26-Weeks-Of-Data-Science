__author__ = "Prakash"

import numpy as np

def simple_mv(price_train, price_valid, n = 12):
    """ Moving Average Function
    Input:
    ------
    Price_train: the train data on which you want to run moving average
    Price_valid: mainly to know the length of predictions you need to make. use validation data while validating and test_Data dataframe while Predicting.
    alpha: weight parameter
    n: the number of previous datapoints to consider.
    Function:
    --------
    F(t+1) =  (F(t)  + F(t-1) + F(t-2) + .....F(t-n))/n
    Returns:
    -------
    A list with predictions.
    """
    if price_valid is None:
        total_length = len(price_train)
    else:
        total_length = len(price_train)+len(price_valid)

    pred =[]
    for i in range(total_length):
        if i < n:
            pred.append(0)
        elif i <= len(price_train):
            x = price_train[i-n:i]
            pred.append(np.mean(x))
        else:
            x = pred[-n:]
            pred.append(np.mean(x))
    return pred


def ses(price_train, price_valid, alpha =0.2, n = 27):
    """ Moving Average Function
    Input:
    ------
    Price_train: the train data on which you want to run moving average
    Price_valid: mainly to know the length of predictions you need to make. use validation data while validating and test_Data dataframe while Predicting.
    alpha: weight parameter
    n: the number of previous datapoints to consider.
    Function:
    --------
    F(t+1) = alpha * F(t)  + alpha * (1 - aplha) * F(t-1) + alpha * (1 - alpha)^2 * F(t-2) + .....N
    Returns:
    -------
    A list with predictions.
    """
    if price_valid is None:
        total_length = len(price_train)
    else:
        total_length = len(price_train)+len(price_valid)

    pred =[]
    for i in range(total_length):
        if i < n:
            pred.append(0)
        elif i <= len(price_train):
            x = price_train[i-n:i]
            val = []
            for i in range(len(x)):
                m = (alpha)*((1-alpha)**i)*(x[-i])
                val.append(m)
            pred.append(np.sum(val))
        else:
            x = pred[-n:]
            val = []
            for i in range(len(x)):
                m = (alpha)*((1-alpha)**i)*(x[-i])
                val.append(m)
            pred.append(np.sum(val))
    return pred
