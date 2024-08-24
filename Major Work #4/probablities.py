dataF = ('test_data.csv')
import pandas as pd
from indicators import *



def day_performance(csv):
    data = pd.read_csv(csv)
    outcomes = {"Up Days": 0, "Down Days": 0, "Neutral Days": 0}
    
    for i in range(10):
        open = data.iloc[-i, 1]
        close = data.iloc[-i, 4]

        if open > close:
            outcomes["Down Days"] += 1
        elif close > open:
            outcomes["Up Days"] += 1
        else:
             outcomes["Neutral Days"] += 1

    print("Up Days:", outcomes["Up Days"])
    print("Down Days:", outcomes["Down Days"])
    print("Neutral Days:", outcomes["Neutral Days"])


