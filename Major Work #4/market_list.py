from tkinter import *
import customtkinter
from chart import *

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("dark-blue")

def delete_chart(canvas):
    if canvas:
        # Remove the canvas widget from the parent frame
        canvas.get_tk_widget().pack_forget()
        # Clear the figure to release resources
        canvas.figure.clear()
        plt.close(canvas.figure)



def create_market_list(parent_frame, chart1_frame, canvas):
    markets = customtkinter.CTkScrollableFrame(parent_frame, label_text='Markets')
    markets.pack(fill='x', expand='True')

    #Indices
    def on_combobox_click(event):
        if indices_list.get() == placeholder:
            indices_list.set('')


    placeholder = 'Indices'
    indices = ['ASX 200', 'S&P 500']
    indices_list = customtkinter.CTkOptionMenu(markets, values=indices)
    indices_list.set(placeholder)
    indices_list.bind("<Button-1>", on_combobox_click)
    indices_list.pack(fill='x')


    #Forex
    def on_combobox_click(event):
        if forex_list.get() == placeholder:
            forex_list.set('')
        elif forex_list.get() == 'AUD/USD':
            delete_chart(canvas)
            create_chart(chart1_frame, 'AUDUSD.csv')
        elif forex_list.get() == 'USD/JPY':
            delete_chart(canvas)
            create_chart(chart1_frame, 'USDJPY.csv')

    placeholder = 'Forex'
    forex = ['AUD/USD', 'USD/JPY']
    forex_list = customtkinter.CTkOptionMenu(markets, values=forex)
    forex_list.set(placeholder)
    forex_list.bind("<Button-1>", on_combobox_click)
    forex_list.pack(fill='x')


    #Shares
    def on_combobox_click(event):
        if shares_list.get() == placeholder:
            shares_list.set('')

    placeholder = 'Shares'
    shares = ['Tesla Motors Inc', 'NVIDIA Corp']
    shares_list = customtkinter.CTkOptionMenu(markets, values=shares)
    shares_list.set(placeholder)
    shares_list.bind("<Button-1>", on_combobox_click)
    shares_list.pack(fill='x')


    #Commodites
    def on_combobox_click(event):
        if commodites_list.get() == placeholder:
            commodites_list.set('')

    placeholder = 'Commodites'
    commodites = ['Oil-US Crude', 'Gold']
    commodites_list = customtkinter.CTkOptionMenu(markets, values=commodites)
    commodites_list.set(placeholder)
    commodites_list.bind("<Button-1>", on_combobox_click)
    commodites_list.pack(fill='x')

