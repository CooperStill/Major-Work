from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("dark-blue")

def create_recently_visited(parent_frame):
    def on_combobox_click(event):
        if recentlyVisited.get() == placeholder:
            recentlyVisited.set('')


    placeholder = 'Recently Visited'
    recentMarkets = ['ASX 200', 'S&P 500']
    recentlyVisited = customtkinter.CTkOptionMenu(parent_frame, values=recentMarkets)
    recentlyVisited.set(placeholder)
    recentlyVisited.bind("<Button-1>", on_combobox_click)
    recentlyVisited.pack(pady=20, side='left', expand='True')
