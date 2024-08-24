from tkinter import *
import customtkinter
from indicators import *

#set theme and colour
customtkinter.set_appearance_mode("dark")  # default
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"



def display_dates(parent_frame):
    dates = customtkinter.CTkScrollableFrame(parent_frame,
    label_text='Dates of Compliance')
    dates.pack(fill='x')


    bullish_engulfing_data = bullish_engulfing(dataF)
    
    for date in reversed(bullish_engulfing_data):
        date_label = customtkinter.CTkLabel(dates, text=str(date), anchor='w', font=('arail', 20))
        date_label.pack(fill='x')







