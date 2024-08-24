dataF = ('test_data.csv')
import pandas as pd
import numpy as np



def bullish_engulfing(csv):
    data = pd.read_csv(csv)
    outcomes = []

    for i in range(len(data)):
        open = data.iloc[-i, 1]
        close = data.iloc[-i, 4]
        date = data.iloc[-i, 0]
        previous_open = data.iloc[-i-1, 1]
        previous_close = data.iloc[-i-1, 4]

    # #Bullish Engulfing
        if (open < close and 
            previous_open > previous_close and
            close > previous_open and
            open <= previous_close):
            outcomes.append(date)
    
    return(outcomes)



def bearish_engulfing(csv):
    data = pd.read_csv(csv)
    outcomes = []

    for i in range(len(data)):
        open = data.iloc[-i, 1]
        close = data.iloc[-i, 4]
        date = data.iloc[-i, 0]
        previous_open = data.iloc[-i-1, 1]
        previous_close = data.iloc[-i-1, 4]

        #Bearish Engulfing
        if (open > close and 
            previous_open < previous_close and
            close < previous_open and
            open >= previous_close):
            outcomes.append(date)

    return(outcomes)


