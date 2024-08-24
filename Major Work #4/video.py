import urllib.request
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import matplotlib.animation as animation
from matplotlib import style
import urllib
import json
import pandas as pd
import numpy as np
#WI2LPGB1MB2IVAIQ
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc



LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)
style.use('ggplot')

f = plt.figure()
#a = f.add_subplot(111)

exchange = 'Choice 1'
counter = 9000
programName = 'Program1'
resampleSize = '15Min'
dataPace = '1d'
candleWidth = 0.008
topIndicator = 'none'
mainIndicator = 'none'
bottomIndicator = 'none'
loadChart = True
paneCount = 1
EMAs = []
SMAs = []


def loadChart(run):
    global loadChart

    if run =='start':
        loadChart = True
    elif run == 'stop':
        loadChart = False



def fetch_data():
    dataLink = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=WI2LPGB1MB2IVAIQ'
    data = urllib.request.urlopen(dataLink)
    data = data.read().decode('utf-8')
    data = json.loads(data)
    return data["Time Series (Daily)"]

def prepare_data(data):
    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    volumes = []
    
    for date, values in data.items():
        dates.append(mdates.date2num(pd.to_datetime(date)))
        opens.append(float(values['1. open']))
        highs.append(float(values['2. high']))
        lows.append(float(values['3. low']))
        closes.append(float(values['4. close']))
        volumes.append(int(values['5. volume']))
        
    df = pd.DataFrame({'Date': dates, 'Open': opens, 'High': highs, 'Low': lows, 'Close': closes, 'Volume': volumes})
    df.set_index('Date', inplace=True)
    return df






def addMainIndicator(what):
    global mainIndicator
    global counter


    if what != 'none':
        if mainIndicator == 'none':
            if what == 'sma':
                mainIQ = tk.Tk()
                label = ttk.Label(mainIQ, text='Choose how many periods you want your SMA to be')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(mainIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global mainIndicator
                    global counter

                    mainIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('sma')
                    group.append(int(periods))
                    mainIndicator.append(group)
                    counter = 9000
                    print('main indicator set to:',mainIndicator)
                    mainIQ.destroy()

                b = ttk.Button(mainIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()




            if what == 'ema':
                mainIQ = tk.Tk()
                label = ttk.Label(mainIQ, text='Choose how many periods you want your EMA to be')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(mainIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global mainIndicator
                    global counter

                    mainIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('ema')
                    group.append(int(periods))
                    mainIndicator.append(group)
                    counter = 9000
                    print('main indicator set to:',mainIndicator)
                    mainIQ.destroy()

                b = ttk.Button(mainIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

        else:
            if what == 'sma':
                mainIQ = tk.Tk()
                label = ttk.Label(mainIQ, text='Choose how many periods you want your SMA to be')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(mainIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global mainIndicator
                    global counter

                    periods = (e.get())
                    group = []
                    group.append('sma')
                    group.append(int(periods))
                    mainIndicator.append(group)
                    counter = 9000
                    print('main indicator set to:',mainIndicator)
                    mainIQ.destroy()

                b = ttk.Button(mainIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()


            if what == 'ema':
                mainIQ = tk.Tk()
                label = ttk.Label(mainIQ, text='Choose how many periods you want your EMA to be')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(mainIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global mainIndicator
                    global counter

                    periods = (e.get())
                    group = []
                    group.append('ema')
                    group.append(int(periods))
                    mainIndicator.append(group)
                    counter = 9000
                    print('main indicator set to:',mainIndicator)
                    mainIQ.destroy()

                b = ttk.Button(mainIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()
    else:
        mainIndicator = 'none'


            





def addTopIndicator(what):
    global topIndicator
    global counter

    # if dataPace == 'tick':
    #     popupmsg('Indicaotrs in Tick Data not avalible')
    
    if what == 'none':
        topIndicator = what
        counter = 9000

    elif what == 'rsi':
        rsiQ = tk.Tk()
        rsiQ.wm_title('Periods?')
        label = ttk.Label(rsiQ, text='Choose how many periods you want each RSI calculation to consider')
        label.pack(side='top', fill='x', pady=10)


        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()

        def callback():
            global topIndicator
            global counter

            periods = (e.get())
            group = []
            group.append('rsi')
            group.append(periods)

            topIndicator = group
            counter = 9000
            print('Set top indicator to', group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text='Submit', width=10, command=callback)
        b.pack()
        tk.mainloop
    
    elif what == 'macd':
        topIndicator = 'macd'
        counter = 9000


def addBottomIndicator(what):
    global bottomIndicator
    global counter

    if dataPace == 'tick':
        popupmsg('Indicaotrs in Tick Data not avalible')
    
    elif what == 'none':
        bottomIndicator = what
        counter = 9000

    elif what == 'rsi':
        rsiQ = tk.Tk()
        rsiQ.wm_title('Periods?')
        label = ttk.Label(rsiQ, text='Choose how many periods you want each RSI calculation to consider')
        label.pack(side='top', fill='x', pady=10)


        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()

        def callback():
            global bottomIndicator
            global counter

            periods = (e.get())
            group = []
            group.append('rsi')
            group.append(periods)

            bottomIndicator = group
            counter = 9000
            print('Set bottom indicator to', group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text='Submit', width=10, command=callback)
        b.pack()
        tk.mainloop
    
    elif what == 'macd':
        bottomIndicator = 'macd'
        counter = 9000








def changeTimeFrame(tf):
    global dataPace
    global counter
    if tf == '7d' and resampleSize == '1Min':
        popupmsg('Too much data chosen, choose a smaller time fram or higher OHLC interval')
    else:
        dataPace = tf
        counter = 9000

def changeSampleSize(size, width):
    global resampleSize
    global counter
    global candleWidth
    if dataPace == '7d' and resampleSize == '1Min':
        popupmsg('Too much data chosen, choose a smaller time fram or higher OHLC interval')
    # elif dataPace == 'tick':
    #     popupmsg('Your currently viewing tick data not OLHC')
    else:
        resampleSize = size
        counter = 9000
        candleWidth = width



def changeExchange(toWhat,pn):
    global exchange
    global counter
    global programName

    exchange = toWhat
    programName = pn
    counter = 9000



def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title('!')
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    B1 = ttk.Button(popup, text='Okay', command = popup.destroy)
    B1.pack()
    popup.mainloop




def animate(i):
    global refreshRate
    global counter
    global loadChart

    if loadChart:
        if paneCount == 1:
            # if dataPace == 'tick':
            #     try:
                    
            #         a = plt.subplot2grid((6,4), (0,0), rowspan = 5, colspan=4)
            #         a2 = plt.subplot2grid((6,4), (5,0), rowspan = 1, colspan=4, sharex = a)


            #         dataLink = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=WI2LPGB1MB2IVAIQ'
            #         data = urllib.request.urlopen(dataLink)
            #         data = data.readall().decode('utf-8')
            #         data = json.loads(data)

            #         data = data['Time Series (Daily)']
            #         data = pd.DataFrame(data)

            #         data['datestamp'] = np.array(data['timestamp']).astype('datetime61[s]')
            #         allDates = data['datestamp'].tolist()

            #         buys = data[(data['type']=='bid')]
            #         buyDates = (buys['datestamp']).tolist()

            #         sells = data[(data['type']=='bid')]
            #         sellDates = (sells['datestamp']).tolist()

            #         volume = data['amount']

            #         a.clear()

            #         a.plot_date(buyDates, buys['price'])
            #         a.plot_date(sellDates, sells['price'])

            #         a2.fill_between(allDates, 0, volume, facecolour = 'blue')

            #         a.xaxis.set_major_locator(mticker.MaxNLocator(5))
            #         a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:M:S'))
            #         plt.setp(a.get_xticklabels(), visible = False)


            #         a.legend(bbox_to_anchor=(0, 1.02, 1, 1.02), loc=3,
            #                                 ncol=2, borderaxespad=0)


            #         title = "Chart 1\nLast Price: "+str(data['price'][1999])
            #         a.set_title(title)

            #     except Exception as e:
            #         print('Failed becuase of:',e)
                if counter > 12:
                    try:
                        data = fetch_data()
                        df = prepare_data(data)
                        
                        if topIndicator != 'none' and bottomIndicator != 'none':
                            a = plt.subplot2grid((6,4), (1,0), rowspan=3, colspan=4)
                            a2 = plt.subplot2grid((6,4), (4,0), sharex = a, rowspan=1, colspan=4)
                            a3 = plt.subplot2grid((6,4), (5,0), sharex = a, rowspan=1, colspan=4)
                            a0 = plt.subplot2grid((6,4), (0,0), sharex = a, rowspan=1, colspan=4)
                        
                        elif topIndicator != 'none':
                            a = plt.subplot2grid((6,4), (1,0), rowspan=4, colspan=4)
                            a2 = plt.subplot2grid((6,4), (5,0), sharex = a, rowspan=1, colspan=4)
                            a0 = plt.subplot2grid((6,4), (0,0), sharex = a, rowspan=1, colspan=4)

                        elif bottomIndicator != 'none':
                            a = plt.subplot2grid((6,4), (0,0), rowspan=4, colspan=4)
                            a2 = plt.subplot2grid((6,4), (4,0), sharex = a, rowspan=1, colspan=4)
                            a3 = plt.subplot2grid((6,4), (5,0), sharex = a, rowspan=1, colspan=4)
                        
                        else:
                            a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                            a2 = plt.subplot2grid((6,4), (5,0), sharex = a, rowspan=1, colspan=4)

                        
                        data = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=WI2LPGB1MB2IVAIQ').read()
                        data = data.decode()
                        data = json.loads(data)
                        dateStamp = np.array(data[0]).astype('datetime64[s]')
                        dateStamp = dateStamp.tolist()

                        df['Close'] = data[1]
                        df['Volume'] = data[2]
                        df['Symbol'] = 'IBM'
                        df['Date'] = df['Datetime'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                        df = df.set_index('Datetime')


                        OHLC = df['Close'].resample(resampleSize, how='ohlc')
                        OHLC = OHLC.dropna()

                        volumeData = df['Volume'].resample(resampleSize, how={'Volume':'sum'})

                        OHLC['dateCopy'] = OHLC.index
                        OHLC['Date'] = OHLC['dateCopy'].apply(lambda date: mdates.date2num(date.to_pydatetime()))

                        del OHLC['dateCopy']

                        volumeData['dateCopy'] = volumeData.index
                        volumeData['Date'] = volumeData['dateCopy'].apply(lambda date: mdates.date2num(date.to_pydatetime()))

                        del volumeData['dateCopy']

                        priceData = OHLC['Close'].apply(float).tolist()

                        a.clear()

                        if mainIndicator != 'none':
                            for eachMA in mainIndicator:
                                #ewma = pd.stats.moments.ewma
                                if eachMA[0] == 'sma':
                                    sma = pd.rolling.mean(OHLC['Close'], eachMA[1])
                                    label = str(eachMA[1])+' SMA'
                                    a.plot(OHLC['Date'], sma, label=label)

                                if eachMA[0] == 'ema':
                                    ewma = pd.rolling.mean(OHLC['Close'], eachMA[1])
                                    label = str(eachMA[1])+' EMA'
                                    a.plot(OHLC['Dates'], ewma(OHLC['closed'], eachMA[1]), label=label)

                            a.legend(loc=0)


                        # if topIndicator[0] == 'rsi':
                        #     rsiIndicator(priceData, 'top')
                        # elif topIndicator == 'macd':
                        #     try:
                        #         computeMACD(priceData, location = 'top')

                        #     except Exception as e:
                        #         print(str(e))



                        # if bottomIndicator[0] == 'rsi':
                        #     rsiIndicator(priceData, 'bottom')
                        # elif bottomIndicator == 'macd':
                        #     try:
                        #         computeMACD(priceData, location = 'bottom')

                        #     except Exception as e:
                        #         print(str(e))



                        csticks = candlestick_ohlc(a, OHLC[['Date', 'Open', 'High', 'Low', 'Close']].values, width=candleWidth, colorup='green', colordown='red')
                        a.set_ylabel('Close')
                        a.xaxis.set_major_locator(mticker.MaxNLocator(3))
                        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

                        if topIndicator != 'none':
                            plt.setp(a0.get_xticklabels(), visible=False)

                        if bottomIndicator != 'none':
                            plt.setp(a2.get_xticklabels(), visible=False)

                        x = (len(OHLC['Close']))-1

                        if dataPace == '1d':
                            title = '1 Day Data with'+resampleSize+' Bars\nLast Price: '+str(OHLC['Close'][x])

                        # if dataPace == '3d':
                        #     title = '3 Day Data with'+resampleSize+' Bars\nLast Price: '+str(OHLC['Close'][x])

                        # if dataPace == '7d':
                        #     title = '7 Day Data with'+resampleSize+' Bars\nLast Price: '+str(OHLC['Close'][x])

                        if topIndicator != 'none':
                            a0.set_title(title)

                        else:
                            a.set_title(title)

                        print('New graph')
                        counter = 0


                    except Exception as e:
                        print('failed in the non-tick animate:',str(e))
                        counter = 9000
                else:
                    counter += 1






class MajorWork(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, 'Major Work')

        container = tk.Frame(self)
        container.pack(side='top', fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Save settings', command = lambda: popupmsg('Not supported just yet'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=quit)
        menubar.add_cascade(label='File', menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label='Choice 1', 
                                   command=lambda: changeExchange('Disply1','Program1'))
        exchangeChoice.add_command(label='Choice 2', 
                                   command=lambda: changeExchange('Disply2','Program2')) 
        exchangeChoice.add_command(label='Choice 3', 
                                   command=lambda: changeExchange('Disply3','Program3')) 
        exchangeChoice.add_command(label='Choice 4', 
                                   command=lambda: changeExchange('Disply4','Program4')) 
        
        menubar.add_cascade(label='Exchange', menu=exchangeChoice)

        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label = '1 Day',
                           command=lambda: changeTimeFrame('1d'))
        dataTF.add_command(label = '3 Day',
                           command=lambda: changeTimeFrame('3d'))
        dataTF.add_command(label = '1 Week',
                           command=lambda: changeTimeFrame('7d'))
        menubar.add_cascade(label='Time Frame', menu=dataTF)

        OHLCI = tk.Menu(menubar, tearoff=1)
        OHLCI.add_command(label = 'Daily ',
                        command=lambda: changeSampleSize('3H', 0.096))
        
        menubar.add_cascade(label = 'OHLC Interval', menu=OHLCI)

        
        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label='None',
                            command = lambda: addTopIndicator('none'))
        topIndi.add_command(label='RSI',
                            command = lambda: addTopIndicator('rsi'))
        topIndi.add_command(label='MACD',
                            command = lambda: addTopIndicator('macd'))
        
        menubar.add_cascade(label='Top Indicator', menu=topIndi)


        mainI = tk.Menu(menubar, tearoff=1)
        mainI.add_command(label='None',
                            command = lambda: addMainIndicator('none'))
        mainI.add_command(label='SMA',
                            command = lambda: addMainIndicator('sma'))
        mainI.add_command(label='EMA',
                            command = lambda: addMainIndicator('ema'))
        
        menubar.add_cascade(label='Main Indicaator', menu=mainI)


        bottomI = tk.Menu(menubar, tearoff=1)
        bottomI.add_command(label='None',
                            command = lambda: addBottomIndicator('none'))
        bottomI.add_command(label='RSI',
                            command = lambda: addBottomIndicator('rsi'))
        bottomI.add_command(label='MACD',
                            command = lambda: addBottomIndicator('macd'))
        
        menubar.add_cascade(label='Bottom Indicator', menu=bottomI)






 




        tk.Tk.config(self, menu=menubar)



        self.frames = {}

        for F in (StartPage, PageOne, Home_Page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Trading Reasearch Major Work', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Agree',
                            command=lambda: controller.show_frame(Home_Page))
        button1.pack()
    
        button2 = ttk.Button(self, text='Disagree',
                            command=quit)
        button2.pack()  
        


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Home',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()




class Home_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Graph Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Home',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()     

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)






app = MajorWork()
app.geometry('1280x720')
ani = animation.FuncAnimation(f, animate, interval=2000)
app.mainloop()








