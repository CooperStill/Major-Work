from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("dark-blue")

def create_indicator_list(parent_frame):
    indicators = customtkinter.CTkScrollableFrame(parent_frame, label_text='Indicators')
    indicators.pack(fill='x', expand='True')

    #Single Candle Patterns
    def on_combobox_click(event):
        if singlec_list.get() == placeholder:
            singlec_list.set('')


    placeholder = 'Single Candle Patterns'
    single_patterns = ['Hammer', 'Shooting Star']
    singlec_list = customtkinter.CTkOptionMenu(indicators, values=single_patterns)
    singlec_list.set(placeholder)
    singlec_list.bind("<Button-1>", on_combobox_click)
    singlec_list.pack(fill='x')


    #Double Candle Patterns
    def on_combobox_click(event):
        if doublec_list.get() == placeholder:
            doublec_list.set('')

    placeholder = 'Double Candle Patterns'
    double_patterns = ['Bullish Engulfing', 'Bearish Engulfing']
    doublec_list = customtkinter.CTkOptionMenu(indicators, values=double_patterns)
    doublec_list.set(placeholder)
    doublec_list.bind("<Button-1>", on_combobox_click)
    doublec_list.pack(fill='x')


    #Triple Candle Pattterns
    def on_combobox_click(event):
        if triplec_list.get() == placeholder:
            triplec_list.set('')

    placeholder = 'Triple Candle Patterns'
    triple_patterns = ['Three White Soilders', 'Three Black Crows']
    triplec_list = customtkinter.CTkOptionMenu(indicators, values=triple_patterns)
    triplec_list.set(placeholder)
    triplec_list.bind("<Button-1>", on_combobox_click)
    triplec_list.pack(fill='x')

