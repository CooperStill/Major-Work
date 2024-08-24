import pandas as pd
from lightweight_charts import Chart
from time import sleep


if __name__ == '__main__':
    chart = Chart()
    df = pd.read_csv('AAPL.csv')


    chart.set(df)


    chart.show(block=True)

    

