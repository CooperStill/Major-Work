dataF = ('test_data.csv')
import pandas as pd
from indicators import *



def get_indicator_date(indicator):
    bullish_engulfing_array = bullish_engulfing(dataF)

    if bullish_engulfing_array:
        first_bullish_engulfing = bullish_engulfing_array[0]
        print("First bullish engulfing pattern occurred on:", first_bullish_engulfing)


get_indicator_date(bullish_engulfing)